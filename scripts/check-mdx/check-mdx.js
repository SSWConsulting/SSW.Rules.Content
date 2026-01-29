import fs from "node:fs/promises";
import fsSync from "node:fs";
import path from "node:path";
import process from "node:process";

import { compile } from "@mdx-js/mdx";
import { visit } from "unist-util-visit";
import remarkFrontmatter from "remark-frontmatter";
import matter from "gray-matter";

/* ------------------------- error formatting helpers ------------------------ */

function pickPos(err) {
  const line = err?.position?.start?.line ?? err?.line ?? 1;
  const col = err?.position?.start?.column ?? err?.column ?? 1;
  return { line, col };
}

function cleanMsg(err) {
  return (err?.reason || err?.message || String(err)).replace(/\r?\n/g, " ");
}

function humanizeMdxError(err) {
  const raw = cleanMsg(err);

  if (raw.toLowerCase().includes("could not parse expression with acorn")) {
    return (
      "Invalid MDX expression inside curly braces `{ ... }`.\n" +
      "This usually happens when curly braces are used in normal text.\n" +
      "If you meant literal braces, escape them as `\\{` and `\\}`, or wrap them in code (e.g. `` `{test}` ``).\n" +
      "If you meant double braces `{{ ... }}`:\n" +
      "- Outside JSX: use `\\{\\{ ... \\}\\}` or code.\n" +
      "- Inside JSX (e.g. body={<></>}): use `&#123;&#123; ... &#125;&#125;` or `{\"{{ ... }}\"}`."
    );
  }

  if (raw.includes("Expected a closing tag for `<>`")) {
    return (
      'Found `<>` which MDX may treat as a JSX fragment.\n' +
      'Write it as inline code: `` `<>` ``, or escape it.'
    );
  }

  return raw;
}

function toGhAnnotation(err, fallbackFile) {
  const file = err?.file || fallbackFile || "";
  const { line, col } = pickPos(err);
  const msg = humanizeMdxError(err).replace(/\r?\n/g, " ");
  return `::error file=${file},line=${line},col=${col}::${msg}`;
}

/* ------------------------------ repo helpers ------------------------------ */

async function findRepoRoot(startDir) {
  let dir = startDir;
  while (true) {
    try {
      await fs.access(path.join(dir, ".git"));
      return dir;
    } catch {
      // keep going up
    }
    const parent = path.dirname(dir);
    if (parent === dir) return startDir;
    dir = parent;
  }
}

function normalizeToRepoRelative(repoRoot, p) {
  const abs = path.isAbsolute(p) ? p : path.resolve(repoRoot, p);
  return path.relative(repoRoot, abs).replaceAll("\\", "/");
}

function parseArgs(argv) {
  const args = argv.slice(2);
  const fix = args.includes("--fix");
  const filesRaw = args.filter((a) => a !== "--fix");

  let files = filesRaw.filter(Boolean);

  // Support a single comma-separated argument (workflow passes "a,b,c")
  if (files.length === 1 && files[0].includes(",")) {
    files = files[0]
      .split(",")
      .map((s) => s.trim())
      .filter(Boolean);
  }

  // Only check .mdx
  files = files.filter((f) => f.toLowerCase().endsWith(".mdx"));

  // Deduplicate
  files = Array.from(new Set(files));

  return { fix, files };
}

/* ----------------------------- fix utilities ------------------------------ */

/**
 * Convert {{...}} (and \{\{...\}\}) inside JSX attribute expressions (={ ... })
 * into HTML entities, so JSX never tries to parse braces as expressions.
 *
 * Applies within balanced ={ ... } regions only.
 */
function convertDoubleBracesInJsxAttributeExpressions(source) {
  let out = source;
  let i = 0;

  while (i < out.length) {
    const start = out.indexOf("={", i);
    if (start === -1) break;

    const braceStart = start + 1; // points to '{'
    let j = braceStart + 1;
    let depth = 1;

    // simple brace matcher w/ string awareness
    let inSingle = false,
      inDouble = false,
      inTemplate = false,
      escaped = false;

    for (; j < out.length; j++) {
      const ch = out[j];

      if (escaped) {
        escaped = false;
        continue;
      }
      if (ch === "\\") {
        escaped = true;
        continue;
      }

      if (!inDouble && !inTemplate && ch === "'") inSingle = !inSingle;
      else if (!inSingle && !inTemplate && ch === '"') inDouble = !inDouble;
      else if (!inSingle && !inDouble && ch === "`") inTemplate = !inTemplate;

      if (inSingle || inDouble || inTemplate) continue;

      if (ch === "{") depth++;
      else if (ch === "}") depth--;

      if (depth === 0) {
        const region = out.slice(braceStart, j + 1);

        const fixedRegion = region
          // raw
          .replace(/\{\{/g, "&#123;&#123;")
          .replace(/\}\}/g, "&#125;&#125;")
          // escaped
          .replace(/\\\{\\\{/g, "&#123;&#123;")
          .replace(/\\\}\\\}/g, "&#125;&#125;");

        if (fixedRegion !== region) {
          out = out.slice(0, braceStart) + fixedRegion + out.slice(j + 1);
          i = braceStart + fixedRegion.length;
        } else {
          i = j + 1;
        }
        break;
      }
    }

    if (depth !== 0) break;
  }

  return out;
}

/**
 * Replace raw {{...}} -> \{\{...\}\} BUT
 * - skip fenced code blocks ```...``` or ~~~...~~~
 * - assumes {{...}} does not intentionally span huge ranges in prose (typical placeholders)
 */
function convertDoubleBracesOutsideJsxSkippingFences(source) {
  // Split into alternating: [nonFenceChunk, fenceChunk, nonFenceChunk, ...]
  // Fence chunk includes its fence lines and content.
  const parts = [];
  let buf = "";

  let inFence = false;
  let fenceMarker = null; // "```" or "~~~"

  const lines = source.split(/\r?\n/);
  for (let idx = 0; idx < lines.length; idx++) {
    const line = lines[idx];
    const fullLine = line + (idx < lines.length - 1 ? "\n" : "");

    const m = line.match(/^\s*(```|~~~)/);
    if (m) {
      const marker = m[1];

      if (!inFence) {
        // entering fence: flush buf as non-fence
        if (buf) {
          parts.push({ type: "text", value: buf });
          buf = "";
        }
        inFence = true;
        fenceMarker = marker;
        parts.push({ type: "fence", value: fullLine });
        continue;
      }

      // if already in fence, only close when marker matches the opener
      if (inFence && fenceMarker === marker) {
        parts.push({ type: "fence", value: fullLine });
        inFence = false;
        fenceMarker = null;
        continue;
      }
    }

    if (inFence) {
      parts.push({ type: "fence", value: fullLine });
    } else {
      buf += fullLine;
    }
  }

  if (buf) parts.push({ type: "text", value: buf });

  // Apply replacement only to non-fence text chunks.
  // NOTE: This runs after we convert JSX attribute regions, so raw {{...}} inside ={...} is already gone.
  const replaced = parts
    .map((p) => {
      if (p.type !== "text") return p.value;
      return p.value.replace(/\{\{([\s\S]*?)\}\}/g, (_m, inner) => `\\{\\{${inner}\\}\\}`);
    })
    .join("");

  return replaced;
}

/**
 * Conservative fixes based on AST offsets:
 * 1) Replace mdxTextExpression/mdxFlowExpression outer braces:
 *    "{test}" -> "\{test\}"
 * 2) Replace blockquote list markers (> * / > - / > +) -> (> •)
 */
function applyFixes({ source, exprFixes }) {
  let out = source;

  // Apply expression fixes from end to start to avoid offset shifts.
  const fixes = exprFixes
    .filter((f) => Number.isFinite(f.start) && Number.isFinite(f.end) && f.end > f.start)
    .sort((a, b) => b.start - a.start);

  for (const f of fixes) {
    const original = out.slice(f.start, f.end); // includes { ... }
    if (original.startsWith("{") && original.endsWith("}")) {
      const inner = original.slice(1, -1);
      const replacement = `\\{${inner}\\}`;
      out = out.slice(0, f.start) + replacement + out.slice(f.end);
    }
  }

  // Blockquote list markers -> plain bullets
  out = out.replace(
    /^(\s*>+\s*)([*+-])(\s+)/gm,
    (_m, prefix, _marker, space) => `${prefix}•${space}`
  );

  return out;
}

/* ----------------------------- remark plugin ------------------------------ */

/**
 * remark plugin that:
 * - In check mode: fails on mdxTextExpression/mdxFlowExpression and lists in blockquotes
 * - In fix mode: collects offsets for auto-fix and records issues for report
 */
function remarkCustomMdxRules(_opts = {}) {
  // When passed as [plugin, options] in remarkPlugins, remark calls it with options.
  const { fixMode, collected } = _opts;

  return (tree, file) => {
    const recordExpression = (node) => {
      const expr = (node.value || "").trim();
      const start = node?.position?.start?.offset;
      const end = node?.position?.end?.offset;

      collected.issues.push({
        kind: "expression",
        line: node?.position?.start?.line ?? 1,
        col: node?.position?.start?.column ?? 1,
        message: !expr
          ? 'Empty MDX expression "{}" found in content. If you meant literal braces, escape them as \\{ and \\}, or wrap them in code.'
          : `MDX expression "{${expr}}" found in content. Avoid using { } in prose; escape them as \\{ and \\}, or wrap in code.`,
        start,
        end,
      });

      if (!fixMode) {
        if (!expr) {
          file.fail(
            'Empty MDX expression "{}" found in content. If you meant literal braces, escape them (e.g. \\{ \\}) or use code formatting.',
            node
          );
        } else {
          file.fail(
            `MDX expression "{${expr}}" found in content. Avoid using { } in prose; escape them as \\{ and \\}, or wrap in code.`,
            node
          );
        }
      }
    };

    visit(tree, "mdxTextExpression", recordExpression);
    visit(tree, "mdxFlowExpression", recordExpression);

    visit(tree, "blockquote", (bq) => {
      let hasList = false;
      visit(bq, "list", () => {
        hasList = true;
      });

      if (hasList) {
        collected.issues.push({
          kind: "blockquote-list",
          line: bq?.position?.start?.line ?? 1,
          col: bq?.position?.start?.column ?? 1,
          message:
            'Lists inside blockquotes are not allowed (often caused by using "*" bullets inside "> ..."). Consider using plain text bullets (e.g. "•") instead.',
        });

        if (!fixMode) {
          file.fail(
            'Lists inside blockquotes are not allowed (often caused by using "*" bullets inside "> ...").',
            bq
          );
        }
      }
    });
  };
}

async function compileAndCollect({ source, relPath, fixMode }) {
  const collected = { issues: [] };

  // Validate frontmatter YAML (throws if invalid)
  matter(source);

  await compile(source, {
    filepath: relPath,
    development: true,
    remarkPlugins: [
      [remarkFrontmatter, ["yaml", "toml"]],
      [remarkCustomMdxRules, { fixMode, collected }],
    ],
  });

  return collected;
}

/* ---------------------------------- main ---------------------------------- */

async function main() {
  const repoRoot = await findRepoRoot(process.cwd());
  const { fix, files } = parseArgs(process.argv);

  if (files.length === 0) {
    console.log("No .mdx files to check.");
    return;
  }

  const reportPath = process.env.MDX_REPORT_PATH || "";
  const reportMarker = "<!-- mdx-check -->";
  const reportLines = [
    reportMarker,
    fix ? "### 🛠️ MDX check (auto-fix enabled)" : "### ❌ MDX check failed",
    "",
  ];

  let anyIssues = false;
  let failed = false;
  let fixedSomething = false;

  for (const raw of files) {
    const rel = normalizeToRepoRelative(repoRoot, raw);
    const abs = path.resolve(repoRoot, rel);

    if (!fsSync.existsSync(abs)) {
      console.log(`SKIP (missing): ${rel}`);
      continue;
    }

    let source = await fs.readFile(abs, "utf8");

    let collected;
    try {
      collected = await compileAndCollect({ source, relPath: rel, fixMode: fix });
    } catch (err) {
      anyIssues = true;

      const rawMsg = cleanMsg(err).toLowerCase();

      // If --fix and MDX parsing failed early, try a fallback fixer for {{...}} patterns
      if (fix && rawMsg.includes("could not parse expression with acorn")) {
        let fixed = source;

        // 1) Convert any {{...}} within JSX attribute expressions into entities
        fixed = convertDoubleBracesInJsxAttributeExpressions(fixed);

        // 2) Convert remaining {{...}} outside JSX attribute expressions into escaped braces,
        //    while skipping fenced code blocks
        fixed = convertDoubleBracesOutsideJsxSkippingFences(fixed);

        if (fixed !== source) {
          await fs.writeFile(abs, fixed, "utf8");
          fixedSomething = true;
          console.log(`FIXED (fallback {{...}}): ${rel}`);

          // Re-check after fallback fix
          try {
            await compileAndCollect({ source: fixed, relPath: rel, fixMode: false });
            console.log(`OK AFTER FALLBACK FIX: ${rel}`);
            reportLines.push(`- \`${rel}\`: Auto-fixed double braces \`{{...}}\` (JSX -> entities, prose -> escaped).`);
            continue;
          } catch (err2) {
            failed = true;
            console.error(toGhAnnotation(err2, rel));
            const { line, col } = pickPos(err2);
            reportLines.push(`- \`${rel}\` (line ${line}, col ${col}): ${humanizeMdxError(err2)}`);
            continue;
          }
        }
      }

      // No fallback fix applied
      failed = true;
      console.error(toGhAnnotation(err, rel));
      const { line, col } = pickPos(err);
      reportLines.push(`- \`${rel}\` (line ${line}, col ${col}): ${humanizeMdxError(err)}`);
      continue;
    }

    // If we reach here, compile succeeded (in fix mode, the plugin did not throw)
    if (collected.issues.length === 0) {
      console.log(`OK: ${rel}`);
      continue;
    }

    anyIssues = true;

    // Add collected issues to report
    for (const it of collected.issues) {
      reportLines.push(`- \`${rel}\` (line ${it.line}, col ${it.col}): ${it.message}`);
    }

    if (!fix) {
      // In check-only mode, collected issues should have thrown; but keep this for safety.
      failed = true;
      continue;
    }

    // Apply fixes:
    const exprFixes = collected.issues
      .filter((i) => i.kind === "expression")
      .map((i) => ({ start: i.start, end: i.end }));

    let fixed = applyFixes({ source, exprFixes });

    // Convert double braces in JSX attribute expressions into entities
    fixed = convertDoubleBracesInJsxAttributeExpressions(fixed);

    // Convert remaining double braces in prose (skip fenced code blocks)
    fixed = convertDoubleBracesOutsideJsxSkippingFences(fixed);

    if (fixed !== source) {
      await fs.writeFile(abs, fixed, "utf8");
      fixedSomething = true;
      console.log(`FIXED: ${rel}`);
    } else {
      console.log(`NO AUTO-FIX CHANGES: ${rel}`);
    }

    // Re-check after fix
    try {
      await compileAndCollect({ source: fixed, relPath: rel, fixMode: false });
      console.log(`OK AFTER FIX: ${rel}`);
    } catch (err2) {
      failed = true;
      console.error(toGhAnnotation(err2, rel));
      const { line, col } = pickPos(err2);
      reportLines.push(`- \`${rel}\` (line ${line}, col ${col}): ${humanizeMdxError(err2)}`);
    }
  }

  if (!anyIssues) {
    reportLines.push("✅ No MDX issues found.");
  } else if (fix) {
    reportLines.push("");
    reportLines.push(
      fixedSomething
        ? "✅ Auto-fix applied. A commit may be pushed to this PR branch (same-repo PRs only)."
        : "ℹ️ Issues found, but no auto-fix changes were applied."
    );
  }

  if (reportPath) {
    await fs.writeFile(reportPath, reportLines.join("\n") + "\n", "utf8");
  }

  if (failed) process.exit(1);
}

main().catch((e) => {
  console.error(toGhAnnotation(e, ""));
  process.exit(1);
});
