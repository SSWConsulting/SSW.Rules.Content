const fs = require("fs");
const path = require("path");
const yaml = require("js-yaml");

const repoRoot = path.resolve(__dirname, "..", "..");

function extractFrontMatter(fileContents) {
  if (!fileContents) return undefined;
  const match = /^---([\s\S]*?)---/.exec(fileContents);
  if (!match) return undefined;
  return match[1];
}

function parseFrontmatter(frontmatterString) {
  if (!frontmatterString) return undefined;
  try {
    return yaml.load(frontmatterString, { schema: yaml.JSON_SCHEMA });
  } catch {
    return undefined;
  }
}

function readFrontmatter(filePath) {
  const fullPath = path.resolve(repoRoot, filePath);
  if (!fs.existsSync(fullPath)) return undefined;
  const contents = fs.readFileSync(fullPath, "utf8");
  const raw = extractFrontMatter(contents);
  return parseFrontmatter(raw);
}

function getRulePathFromFile(filePath) {
  return filePath
    .replace(/\\/g, "/")
    .replace(/^\.\.\/\.\.\//, "")
    .replace(/^\//, "");
}

function getCategoriesFromRule(frontmatter) {
  if (!frontmatter || !frontmatter.categories) return [];
  return frontmatter.categories
    .map((entry) => {
      if (typeof entry === "string") return entry;
      if (entry && entry.category) return entry.category;
      return null;
    })
    .filter(Boolean);
}

function getIndexFromCategory(frontmatter) {
  if (!frontmatter || !frontmatter.index) return [];
  return frontmatter.index
    .map((entry) => {
      if (typeof entry === "string") return entry;
      if (entry && entry.rule) return entry.rule;
      return null;
    })
    .filter(Boolean);
}

function appendRuleToCategoryFile(categoryPath, rulePath) {
  const fullPath = path.resolve(repoRoot, categoryPath);
  const contents = fs.readFileSync(fullPath, "utf8");
  const newEntry = `  - rule: ${rulePath}`;

  // Find the last "- rule:" line in the index section and insert after it
  const lines = contents.split("\n");
  let lastRuleIndex = -1;
  for (let i = 0; i < lines.length; i++) {
    if (/^\s+-\s+rule:\s/.test(lines[i])) {
      lastRuleIndex = i;
    }
  }

  if (lastRuleIndex !== -1) {
    lines.splice(lastRuleIndex + 1, 0, newEntry);
  } else {
    // No existing rule entries — append after "index:" line
    for (let i = 0; i < lines.length; i++) {
      if (/^index:\s*$/.test(lines[i])) {
        lines.splice(i + 1, 0, newEntry);
        break;
      }
    }
  }

  fs.writeFileSync(fullPath, lines.join("\n"), "utf8");
}

function fixCategorySync(changedFiles) {
  const errors = [];
  const fixed = [];

  const ruleFiles = changedFiles.filter(
    (f) =>
      f.startsWith("public/uploads/rules/") &&
      f.endsWith("/rule.mdx") &&
      fs.existsSync(path.resolve(repoRoot, f))
  );

  for (const ruleFile of ruleFiles) {
    const ruleFrontmatter = readFrontmatter(ruleFile);
    if (!ruleFrontmatter) continue;

    const categories = getCategoriesFromRule(ruleFrontmatter);
    if (categories.length === 0) continue;

    const rulePath = getRulePathFromFile(ruleFile);

    for (const categoryPath of categories) {
      const categoryFullPath = path.resolve(repoRoot, categoryPath);

      if (!fs.existsSync(categoryFullPath)) {
        errors.push(
          `Category file '${categoryPath}' referenced by rule '${rulePath}' does not exist.`
        );
        continue;
      }

      const categoryFrontmatter = readFrontmatter(categoryPath);
      if (!categoryFrontmatter) {
        errors.push(
          `Category file '${categoryPath}' referenced by rule '${rulePath}' could not be parsed.`
        );
        continue;
      }

      const indexEntries = getIndexFromCategory(categoryFrontmatter);
      const isRuleInIndex = indexEntries.some(
        (entry) => getRulePathFromFile(entry) === rulePath
      );

      if (!isRuleInIndex) {
        appendRuleToCategoryFile(categoryPath, rulePath);
        fixed.push({ rulePath, categoryPath });
      }
    }
  }

  return { errors, fixed };
}

function main() {
  const args = process.argv.slice(2);
  const filesArg = args[0];

  if (!filesArg) {
    console.log(
      "No files provided. Usage: node category-sync-validator.js '<comma-separated-files>'"
    );
    return;
  }

  const changedFiles = filesArg
    .split(",")
    .map((f) => f.trim())
    .filter((f) => f.length > 0);

  const { errors, fixed } = fixCategorySync(changedFiles);

  if (fixed.length > 0) {
    console.log("Auto-fixed category index entries:");
    for (const { rulePath, categoryPath } of fixed) {
      console.log(`  - Added '${rulePath}' to '${categoryPath}'`);
    }
  }

  if (errors.length > 0) {
    console.log("\nCategory sync errors (cannot auto-fix):\n");
    for (const error of errors) {
      console.log(`- **${error}**`);
    }
    process.exit(1);
  }

  if (fixed.length === 0) {
    console.log("No category sync issues found.");
  }
}

main();
