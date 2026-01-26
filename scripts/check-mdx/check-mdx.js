// scripts/check-mdx/check-mdx.mjs
import fs from "node:fs/promises";
import fsSync from "node:fs";
import path from "node:path";
import process from "node:process";

import { compile } from "@mdx-js/mdx";
import { visit } from "unist-util-visit";
import remarkFrontmatter from "remark-frontmatter";
import matter from "gray-matter";

/**
 * Custom remark plugin rules:
 * - Fail on mdxTextExpression in prose (likely accidental { ... })
 * - Fail on lists inside blockquotes (often from "> * item")
 */
function remarkCustomMdxRules() {
  return (tree, file) => {
    // 1) Disallow inline MDX expressions in prose: { ... }
    visit(tree, "mdxTextExpression", (node) => {
      const expr = (node.value || "").trim();

      // Empty expression: {} or {   }
      if (!expr) {
        file.fail(
          `Empty MDX expression "{}" found in content. If you meant literal braces, escape them (e.g. \\{ \\}) or use code formatting.`,
          node
        );
        return;
      }

      file.fail(
        `MDX inline expression "{${expr}}" found in content. Avoid using { } in prose; escape or rephrase.`,
        node
      );
    });

    // 2) Disallow lists inside blockquotes
    visit(tree, "blockquote", (bq) => {
      let hasList = false;
      visit(bq, "list", () => {
        hasList = true;
      });
      if (hasList) {
        file.fail(
          `Lists inside blockquotes are not allowed (often caused by using "*" bullets inside "> ...").`,
          bq
        );
      }
    });
  };
}

function pickPos(err) {
  const line = err?.position?.start?.line ?? err?.line ?? 1;
  const col = err?.position?.start?.column ?? err?.column ?? 1;
  return { line, col };
}

function cleanMsg(err) {
  return (err?.reason || err?.message || String(err)).replace(/\r?\n/g, " ");
}

function toGhAnnotation(err, fallbackFile) {
  const file = err?.file || fallbackFile || "";
  const { line, col } = pickPos(err);
  const msg = cleanMsg(err);
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
    if (parent === dir) return startDir; // fallback if not found
    dir = parent;
  }
}

function normalizeToRepoRelative(repoRoot, p) {
  const abs = path.isAbsolute(p) ? p : path.resolve(repoRoot, p);
  return path.relative(repoRoot, abs).replaceAll("\\", "/");
}

function parseInputFiles(argv) {
  let files = argv.slice(2).filter(Boolean);

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
  return Array.from(new Set(files));
}

async function main() {
  const repoRoot = await findRepoRoot(process.cwd());
  const inputFiles = parseInputFiles(process.argv);

  if (inputFiles.length === 0) {
    console.log("No .mdx files to check.");
    return;
  }

  const reportPath = process.env.MDX_REPORT_PATH || "";
  const errors = [];
  let failed = false;

  for (const raw of inputFiles) {
    const rel = normalizeToRepoRelative(repoRoot, raw);
    const abs = path.resolve(repoRoot, rel);

    try {
      // Deleted/missing files shouldn't break the run
      if (!fsSync.existsSync(abs)) {
        console.log(`SKIP (missing): ${rel}`);
        continue;
      }

      const source = await fs.readFile(abs, "utf8");

      // Validate frontmatter YAML (throws if invalid)
      // Note: We don't compile matter(content) to avoid line number shifts.
      matter(source);

      await compile(source, {
        filepath: rel, // repo-relative paths make annotations nicer
        development: true,
        remarkPlugins: [
          [remarkFrontmatter, ["yaml", "toml"]],
          remarkCustomMdxRules,
        ],
      });

      console.log(`OK: ${rel}`);
    } catch (err) {
      failed = true;

      // GitHub Actions annotation
      console.error(toGhAnnotation(err, rel));

      const { line, col } = pickPos(err);
      const msg = cleanMsg(err);
      errors.push({ file: rel, line, col, msg });
    }
  }

  // Write a temporary report for PR comments (not committed to repo)
  if (failed && reportPath) {
    const marker = "<!-- mdx-check -->";
    const lines = [
      marker,
      "### ❌ MDX check failed",
      "",
      "Found issues in the following files:",
      "",
      ...errors.map(
        (e) => `- \`${e.file}\` (line ${e.line}, col ${e.col}): ${e.msg}`
      ),
      "",
    ];
    await fs.writeFile(reportPath, lines.join("\n"), "utf8");
  }

  if (failed) process.exit(1);
}

main().catch((e) => {
  console.error(toGhAnnotation(e, ""));
  process.exit(1);
});
