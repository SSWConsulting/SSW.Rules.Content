import fs from "node:fs";
import path from "node:path";
import process from "node:process";

/**
 * Checks rule.mdx files for a missing <endIntro /> tag.
 * If no argument is supplied, it scans all rule.mdx files under public/uploads/rules/.
 *
 * Environment variables:
 *   ENDINTRO_REPORT_PATH - If set, writes a Markdown report to this path (used by CI to post PR comments).
 */

const END_INTRO_RE = /^\s*<endIntro\s*\/?\s*>/m;

/* --------------------------------- helpers -------------------------------- */

function findRepoRoot(startDir) {
  let dir = startDir;
  while (dir !== path.dirname(dir)) {
    if (fs.existsSync(path.join(dir, ".git"))) return dir;
    dir = path.dirname(dir);
  }
  return startDir;
}

function isRuleFile(filePath) {
  return path.basename(filePath) === "rule.mdx";
}

function getAllRuleFiles(rootDir) {
  const rulesDir = path.join(rootDir, "public", "uploads", "rules");
  if (!fs.existsSync(rulesDir)) return [];

  const results = [];
  for (const entry of fs.readdirSync(rulesDir, { withFileTypes: true })) {
    if (!entry.isDirectory()) continue;
    const ruleFile = path.join(rulesDir, entry.name, "rule.mdx");
    if (fs.existsSync(ruleFile)) results.push(ruleFile);
  }
  return results;
}

/* ---------------------------------- main ---------------------------------- */

const repoRoot = findRepoRoot(process.cwd());
const rawArg = process.argv[2] || "";

let filesToCheck;

if (rawArg.trim()) {
  filesToCheck = rawArg
    .split(",")
    .map((f) => f.trim())
    .filter(Boolean)
    .map((f) => (path.isAbsolute(f) ? f : path.resolve(repoRoot, f)))
    .filter(isRuleFile);
} else {
  filesToCheck = getAllRuleFiles(repoRoot);
}

if (filesToCheck.length === 0) {
  console.log("No rule.mdx files to check.");
  process.exit(0);
}

const missing = [];

for (const filePath of filesToCheck) {
  if (!fs.existsSync(filePath)) {
    console.warn(`Warning: file not found, skipping: ${filePath}`);
    continue;
  }

  const content = fs.readFileSync(filePath, "utf8");

  if (!END_INTRO_RE.test(content)) {
    const rel = path.relative(repoRoot, filePath).replace(/\\/g, "/");
    missing.push(rel);
    console.log(`::error file=${rel},line=1::Missing <endIntro /> tag`);
  }
}

/* --------------------------------- report --------------------------------- */

if (missing.length > 0) {
  console.log(`\n❌ ${missing.length} rule(s) missing <endIntro />:\n`);
  for (const f of missing) {
    console.log(`  - ${f}`);
  }

  const reportPath = process.env.ENDINTRO_REPORT_PATH;
  if (reportPath) {
    const lines = [
      "## ❌ Missing `<endIntro />` tag\n",
      `Found **${missing.length}** rule(s) without an \`<endIntro />\` tag.\n`,
      "Every rule must include `<endIntro />` after the introduction paragraph to separate it from the main content.\n",
      "| # | File |",
      "|---|------|",
      ...missing.map((f, i) => `| ${i + 1} | \`${f}\` |`),
      "",
    ];
    fs.writeFileSync(reportPath, lines.join("\n"), "utf8");
    console.log(`\nReport written to ${reportPath}`);
  }

  process.exit(1);
} else {
  console.log(`\n✅ All ${filesToCheck.length} rule(s) contain <endIntro />.`);
  process.exit(0);
}
