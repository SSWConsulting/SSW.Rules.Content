// scripts/check-mdx/check-mdx.mjs
import fs from "node:fs/promises";
import fsSync from "node:fs";
import path from "node:path";
import process from "node:process";

import { compile } from "@mdx-js/mdx";
import { visit } from "unist-util-visit";
import remarkFrontmatter from "remark-frontmatter";
import matter from "gray-matter";

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
      "If you meant literal braces, escape them as `\\{` and `\\}`, or wrap them in code (e.g. `` `{test}` ``)."
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

/**
 * Conservative auto-fixes (only when --fix):
 * 1) Escape curly braces for mdxTextExpression / mdxFlowExpression by using node offsets.
 * 2) Replace blockquote list markers (> * / > - / > +) with a bullet char (> •) via regex.
 */
function applyFixes({ source, exprFixes }) {
  let out = source;

  // Apply expression fixes by offsets from end to start to avoid shifting.
  const fixes = exprFixes
    .filter((f) => Number.isFinite(f.start) && Number.isFinite(f.end) && f.end > f.start)
    .sort((a, b) => b.start - a.start);

  for (const f of fixes) {
    const original = out.slice(f.start, f.end); // includes { ... }
    // Replace ONLY the outer braces with escaped braces.
    // If original is "{test}", becomes "\{test\}"
    // If original is "{}", becomes "\{\}"
    if (original.startsWith("{") && original.endsWith("}")) {
      const inner = original.slice(1, -1);
      const replacement = `\\{${inner}\\}`;
      out = out.slice(0, f.start) + replacement + out.slice(f.end);
    }
  }

  // Blockquote list markers to plain bullet lines:
  // "> * item" / ">> - item" / "> + item" -> "> • item"
  out = out.replace(
    /^(\s*>+\s*)([*+-])(\s+)/gm,
    (_, prefix, _marker, space) => `${prefix}•${space}`
  );

  return out;
}

/**
 * remark plugin that:
 * - In check mode: fails on mdxTextExpression/mdxFlowExpression and lists in blockquotes
 * - In fix mode: records expression node offsets for auto-fix; still reports issues (so we can comment)
 */
function remarkCustomMdxRules({ fixMode, collected }) {
  return (tree, file) => {
    const recordExpression = (node) => {
      const expr = (node.value || "").trim();

      const start = node?.position?.start?.offset;
      const end = node?.position?.end?.offset;

      // Record for reporting
      collected.issues.push({
        kind: "expression",
        file: file.path || "",
        line: node?.position?.start?.line ?? 1,
        col: node?.position?.start?.column ?? 1,
        message: !expr
          ? 'Empty MDX expression "{}" found in content. If you meant literal braces, escape them as \\{ and \\}, or wrap them in code.'
          : `MDX expression "{${expr}}" found in content. Avoid using { } in prose; escape them as \\{ and \\}, or wrap in code.`,
        // for fixer
        start,
        end,
      });

      if (!fixMode) {
        // Fail hard in check-only mode
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

    // Lists inside blockquotes
    visit(tree, "blockquote", (bq) => {
      let hasList = false;
      visit(bq, "list", () => {
        hasList = true;
      });

      if (hasList) {
        collected.issues.push({
          kind: "blockquote-list",
          file: file.path || "",
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

    try {
      let source = await fs.readFile(abs, "utf8");

      // First pass: collect issues (and in check mode, fail immediately)
      let collected;
      try {
        collected = await compileAndCollect({ source, relPath: rel, fixMode: fix });
      } catch (err) {
        // Hard compile/yaml errors (not our custom rule) always fail
        failed = true;
        anyIssues = true;
        console.error(toGhAnnotation(err, rel));

        const { line, col } = pickPos(err);
        reportLines.push(`- \`${rel}\` (line ${line}, col ${col}): ${humanizeMdxError(err)}`);
        continue;
      }

      if (collected.issues.length > 0) {
        anyIssues = true;

        // Add to report
        for (const it of collected.issues) {
          reportLines.push(`- \`${rel}\` (line ${it.line}, col ${it.col}): ${it.message}`);
        }

        if (fix) {
          // Apply conservative fixes
          const exprFixes = collected.issues
            .filter((i) => i.kind === "expression")
            .map((i) => ({ start: i.start, end: i.end }));

          const fixed = applyFixes({ source, exprFixes });

          if (fixed !== source) {
            await fs.writeFile(abs, fixed, "utf8");
            fixedSomething = true;
            console.log(`FIXED: ${rel}`);
          } else {
            console.log(`NO AUTO-FIX CHANGES: ${rel}`);
          }

          // Re-check after fix: now fail hard if still issues remain
          try {
            await compileAndCollect({ source: fixed, relPath: rel, fixMode: false });
            console.log(`OK AFTER FIX: ${rel}`);
          } catch (err2) {
            failed = true;
            console.error(toGhAnnotation(err2, rel));
            const { line, col } = pickPos(err2);
            reportLines.push(`- \`${rel}\` (line ${line}, col ${col}): ${humanizeMdxError(err2)}`);
          }
        } else {
          // In check-only mode, the plugin would have thrown already if these issues exist.
          // But kept for completeness.
          failed = true;
        }
      } else {
        console.log(`OK: ${rel}`);
      }
    } catch (err) {
      // Unexpected runtime errors
      failed = true;
      anyIssues = true;
      console.error(toGhAnnotation(err, rel));
      const { line, col } = pickPos(err);
      reportLines.push(`- \`${rel}\` (line ${line}, col ${col}): ${humanizeMdxError(err)}`);
    }
  }

  if (!anyIssues) {
    reportLines.push("✅ No MDX issues found.");
  } else if (fix) {
    reportLines.push("");
    reportLines.push(
      fixedSomething
        ? "✅ Auto-fix applied. A commit will be pushed to this PR branch (same-repo PRs only)."
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
