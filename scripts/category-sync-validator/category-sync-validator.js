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
  // Normalize to forward slashes and make relative to repo root
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

function validateCategorySync(changedFiles) {
  const errors = [];

  // Filter for rule .mdx files only
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
        errors.push({
          ruleFile: rulePath,
          categoryFile: categoryPath,
          message: `Category file '${categoryPath}' referenced by rule does not exist.`,
        });
        continue;
      }

      const categoryFrontmatter = readFrontmatter(categoryPath);
      if (!categoryFrontmatter) {
        errors.push({
          ruleFile: rulePath,
          categoryFile: categoryPath,
          message: `Category file '${categoryPath}' could not be parsed.`,
        });
        continue;
      }

      const indexEntries = getIndexFromCategory(categoryFrontmatter);
      const isRuleInIndex = indexEntries.some(
        (entry) => getRulePathFromFile(entry) === rulePath
      );

      if (!isRuleInIndex) {
        errors.push({
          ruleFile: rulePath,
          categoryFile: categoryPath,
          message: `Rule '${rulePath}' lists category '${categoryPath}', but the category's index does not include this rule. Please add '- rule: ${rulePath}' to the index in '${categoryPath}'.`,
        });
      }
    }
  }

  return errors;
}

function main() {
  const args = process.argv.slice(2);
  const filesArg = args[0];

  if (!filesArg) {
    console.log("No files provided. Usage: node category-sync-validator.js '<comma-separated-files>'");
    return;
  }

  const changedFiles = filesArg
    .split(",")
    .map((f) => f.trim())
    .filter((f) => f.length > 0);

  const errors = validateCategorySync(changedFiles);

  if (errors.length === 0) {
    console.log("No category sync issues found.");
    return;
  }

  console.log("## Category Sync Issues\n");
  console.log(
    "The following rules reference categories, but the category index files have not been updated:\n"
  );

  for (const error of errors) {
    console.log(
      `### Rule: [${error.ruleFile}](https://github.com/SSWConsulting/SSW.Rules.Content/tree/main/${error.ruleFile})\n`
    );
    console.log(`- **${error.message}**\n`);
  }

  console.log(
    "\nPlease update the category index files to include the rules listed above."
  );
  process.exit(1);
}

main();
