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
  const lines = contents.split("\n");

  // Find frontmatter bounds (--- ... ---)
  const fmStart = lines.findIndex((l) => l.trim() === "---");
  if (fmStart === -1) {
    throw new Error(`No frontmatter start '---' found in '${categoryPath}'.`);
  }
  const fmEnd = lines.findIndex((l, i) => i > fmStart && l.trim() === "---");
  if (fmEnd === -1) {
    throw new Error(`No frontmatter end '---' found in '${categoryPath}'.`);
  }

  // Locate the 'index:' line within frontmatter
  const indexLineNo = lines.findIndex(
    (l, i) => i > fmStart && i < fmEnd && /^\s*index:\s*$/.test(l)
  );
  if (indexLineNo === -1) {
    throw new Error(`No 'index:' field found in frontmatter of '${categoryPath}'.`);
  }

  // Determine list item indent style by looking for existing "- rule:" lines
  // between indexLineNo and fmEnd.
  let itemIndent = ""; // default: no indent (matches your "before" example)
  for (let i = indexLineNo + 1; i < fmEnd; i++) {
    const m = /^(\s*)-\s+rule:\s+/.exec(lines[i]);
    if (m) {
      itemIndent = m[1]; // preserve existing style ("" or "  " etc.)
      break;
    }
    // Stop if we hit another top-level key (e.g., lastUpdated:) before any list items
    if (/^\s*[A-Za-z0-9_]+\s*:/.test(lines[i]) && !/^\s*-\s+/.test(lines[i])) {
      break;
    }
  }

  const newEntryLine = `${itemIndent}- rule: ${rulePath}`;

  // Find the last "- rule:" line that belongs to index list (before next key or fmEnd)
  let insertAt = indexLineNo + 1;

  for (let i = indexLineNo + 1; i < fmEnd; i++) {
    // If we reach another key (not a list item), index list has ended
    if (/^\s*[A-Za-z0-9_]+\s*:/.test(lines[i]) && !/^\s*-\s+/.test(lines[i])) {
      insertAt = i;
      break;
    }
    // Track last list item position
    if (/^\s*-\s+rule:\s+/.test(lines[i])) {
      insertAt = i + 1;
    }
  }

  // If we never hit another key, append before fmEnd
  if (insertAt < indexLineNo + 1) insertAt = indexLineNo + 1;
  if (insertAt > fmEnd) insertAt = fmEnd;

  // Insert at end of index list
  lines.splice(insertAt, 0, newEntryLine);

  fs.writeFileSync(fullPath, lines.join("\n"), "utf8");
}

function listAllCategoryFiles(dir = path.resolve(repoRoot, "categories")) {
  const out = [];
  if (!fs.existsSync(dir)) return out;

  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    const full = path.join(dir, entry.name);
    if (entry.isDirectory()) {
      out.push(...listAllCategoryFiles(full));
    } else if (entry.isFile() && entry.name.endsWith(".mdx")) {
      out.push(path.relative(repoRoot, full).replace(/\\/g, "/"));
    }
  }
  return out;
}

/**
 * Removes any "- rule: <rulePath>" entries that belong to the `index:` block
 * in the category frontmatter.
 *
 * Returns true if the file was modified.
 */
function removeRuleFromCategoryFile(categoryPath, rulePath) {
  const fullPath = path.resolve(repoRoot, categoryPath);
  const contents = fs.readFileSync(fullPath, "utf8");
  const lines = contents.split("\n");

  // Find frontmatter bounds (--- ... ---)
  const fmStart = lines.findIndex((l) => l.trim() === "---");
  if (fmStart === -1) return false;

  const fmEnd = lines.findIndex((l, i) => i > fmStart && l.trim() === "---");
  if (fmEnd === -1) return false;

  // Locate 'index:' within frontmatter
  const indexLineNo = lines.findIndex(
    (l, i) => i > fmStart && i < fmEnd && /^\s*index:\s*$/.test(l)
  );
  if (indexLineNo === -1) return false;

  // Walk index block until next key (e.g., lastUpdated:) or fmEnd
  let changed = false;
  for (let i = indexLineNo + 1; i < fmEnd; i++) {
    const line = lines[i];

    // Index block ends at the next YAML key (not a list item)
    if (/^\s*[A-Za-z0-9_]+\s*:/.test(line) && !/^\s*-\s+/.test(line)) break;

    const m = /^\s*-\s+rule:\s*(.+?)\s*$/.exec(line);
    if (!m) continue;

    const entryRule = getRulePathFromFile(m[1]);
    if (entryRule === rulePath) {
      lines.splice(i, 1);
      i--; // adjust index after removal
      changed = true;
    }
  }

  if (changed) fs.writeFileSync(fullPath, lines.join("\n"), "utf8");
  return changed;
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
        try {
          appendRuleToCategoryFile(categoryPath, rulePath);
          fixed.push({ action: "added", rulePath, categoryPath });
        } catch (e) {
          errors.push(String(e.message || e));
        }
      }
    }

    // Remove stale index entries:
    // If any category index references this rule but the rule no longer lists that category, remove it.
    const desiredCategorySet = new Set(
      categories.map((c) => getRulePathFromFile(c))
    );

    const allCategoryFiles = listAllCategoryFiles();
    for (const catFile of allCategoryFiles) {
      const normalizedCat = getRulePathFromFile(catFile);

      // Only remove from categories that are NOT currently referenced by the rule
      if (desiredCategorySet.has(normalizedCat)) continue;

      const catFrontmatter = readFrontmatter(catFile);
      if (!catFrontmatter) continue;

      const indexEntries = getIndexFromCategory(catFrontmatter);
      const hasRule = indexEntries.some(
        (entry) => getRulePathFromFile(entry) === rulePath
      );

      if (hasRule) {
        try {
          const didRemove = removeRuleFromCategoryFile(catFile, rulePath);
          if (didRemove) fixed.push({ action: "removed", rulePath, categoryPath: catFile });
        } catch (e) {
          errors.push(String(e.message || e));
        }
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
    for (const { action, rulePath, categoryPath } of fixed) {
      if (action === "removed") {
        console.log(`  - Removed '${rulePath}' from '${categoryPath}'`);
      } else {
        // default to "added"
        console.log(`  - Added '${rulePath}' to '${categoryPath}'`);
      }
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
