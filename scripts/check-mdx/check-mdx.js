import fs from "node:fs/promises";
import path from "node:path";
import process from "node:process";

import { compile } from "@mdx-js/mdx";
import { visit } from "unist-util-visit";

import remarkFrontmatter from "remark-frontmatter";
import matter from "gray-matter";


/**
 * Custom remark plugin:
 * - Fail on mdxTextExpression in prose (likely accidental { ... })
 * - Fail on lists inside blockquotes (often from "> * item")
 */
function remarkCustomMdxRules() {
  return (tree, file) => {
    visit(tree, "mdxTextExpression", (node) => {
      const expr = (node.value || "").trim();

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

function toGhAnnotation(err, fallbackFile) {
  const file = err.file || fallbackFile || "";
  const line = err.position?.start?.line ?? err.line ?? 1;
  const col = err.position?.start?.column ?? err.column ?? 1;
  const msg = (err.reason || err.message || String(err)).replace(/\r?\n/g, " ");
  return `::error file=${file},line=${line},col=${col}::${msg}`;
}

function toRepoRelative(p) {
  const cwd = process.cwd();
  const abs = path.isAbsolute(p) ? p : path.resolve(cwd, p);
  return path.relative(cwd, abs).replaceAll("\\", "/");
}

async function main() {
  let files = process.argv.slice(2).filter(Boolean);

  if (files.length === 1 && files[0].includes(",")) {
    files = files[0].split(",").map((s) => s.trim()).filter(Boolean);
  }

  files = files.filter((f) => f.toLowerCase().endsWith(".mdx"));

  if (files.length === 0) {
    console.log("No .mdx files to check.");
    return;
  }

  files = files.map(toRepoRelative);

  const badFiles = new Set();
  let failed = false;

  for (const f of files) {
    const filePath = path.resolve(process.cwd(), f);
    try {
      const source = await fs.readFile(filePath, "utf8");

      matter(source);

      await compile(source, {
        filepath: f,
        development: true,
        remarkPlugins: [
          [remarkFrontmatter, ["yaml", "toml"]],
          remarkCustomMdxRules,
        ],
      });

      console.log(`OK: ${f}`);
    } catch (err) {
      failed = true;
      badFiles.add(f);
      console.error(toGhAnnotation(err, f));
    }
  }

  if (badFiles.size > 0) {
    const outPath = path.resolve(process.cwd(), "mdx-check-bad-files.txt");
    const content = Array.from(badFiles).sort().join("\n") + "\n";
    await fs.writeFile(outPath, content, "utf8");
    console.log(`\nBad MDX files written to: ${toRepoRelative(outPath)}`);
  }

  if (failed) process.exit(1);
}


main().catch((e) => {
  console.error(toGhAnnotation(e, ""));
  process.exit(1);
});
