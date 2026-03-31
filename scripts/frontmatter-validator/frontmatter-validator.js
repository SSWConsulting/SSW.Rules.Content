const fs = require('fs');
const ajv = require('ajv');
const yaml = require('js-yaml');
const addFormats = require('ajv-formats');
const ajvErrors = require('ajv-errors');

let allErrors = [];

const schemas = {
  rule: loadSchema('schema/rule-schema.json'),
  category: loadSchema('schema/category-schema.json'),
  top_category: loadSchema('schema/top-category-schema.json'),
};

const validator = initializeValidator();

function initializeValidator() {
  const validator = new ajv({ allErrors: true });
  addFormats(validator);
  ajvErrors(validator);

  for (const key in schemas) {
    validator.addSchema(schemas[key], key);
  }

  return validator;
}

function loadSchema(schemaPath) {
  const args = process.argv.slice(2);
  const fullPath = args.includes('--file')
    ? `scripts/frontmatter-validator/${schemaPath}`
    : schemaPath;

  return JSON.parse(fs.readFileSync(fullPath, 'utf8'));
}

// Returns null if the path is valid or not a content file.
// Returns an error string if the file is in a content directory but misplaced.
// Valid patterns:
//   Rule:         public/uploads/rules/<rule-name>/rule.mdx
//   Category:     categories/<top-category-name>/<category-name>.mdx
//   Top Category: categories/<top-category-name>/index.mdx
function getFilePathError(filePath) {
  const normalized = filePath.replace(/\\/g, '/').replace(/^(\.\.\/)+/, '');

  if (/^public\/uploads\/rules\/[^/]+\/rule\.mdx$/.test(normalized)) return null;
  if (/^categories\/index\.mdx$/.test(normalized)) return null;
  if (/^categories\/[^/]+\/[^/]+\.mdx$/.test(normalized)) return null;

  const inPublicUploads = normalized.startsWith('public/');
  const inCategories = normalized.startsWith('categories/');
  const inOldRulesDir = normalized.startsWith('rules/'); // legacy Gatsby location

  if (!inPublicUploads && !inCategories && !inOldRulesDir) return null;

  if (inPublicUploads && normalized.includes('/rules/')) {
    const parts = (normalized.split('/rules/')[1] || '').split('/').filter(Boolean);

    if (parts.length === 1) {
      return (
        `Rule file is missing its named subfolder.\n` +
        `  Expected: \`public/uploads/rules/<rule-name>/rule.mdx\``
      );
    }

    if (parts.length === 2 && parts[1] !== 'rule.mdx') {
      return (
        `Rule file must be named \`rule.mdx\`, not \`${parts[1]}\`.\n` +
        `  Expected: \`public/uploads/rules/${parts[0]}/rule.mdx\``
      );
    }
  }

  if (inCategories) {
    const parts = normalized.slice('categories/'.length).split('/').filter(Boolean);

    if (parts.length === 1 && parts[0] !== 'index.mdx') {
      return (
        `Category file \`${parts[0]}\` is missing the top-category subfolder.\n` +
        `  For a subcategory:  \`categories/<top-category-name>/<category-name>.mdx\`\n` +
        `  For a top category: \`categories/<top-category-name>/index.mdx\``
      );
    }
  }

  if (inOldRulesDir) {
    return (
      `File is in the legacy \`rules/\` directory. Rule files have moved.\n` +
      `  Expected: \`public/uploads/rules/<rule-name>/rule.mdx\``
    );
  }

  return (
    `File does not match any recognized content type.\n` +
    `  Rule:         \`public/uploads/rules/<rule-name>/rule.mdx\`\n` +
    `  Category:     \`categories/<top-category-name>/<category-name>.mdx\`\n` +
    `  Top Category: \`categories/<top-category-name>/index.mdx\``
  );
}

// Returns 'rule', 'category', or 'top_category' based on file path.
function determineCategory(filePath) {
  if (filePath.endsWith('rule.mdx')) return 'rule';

  const isInCategories =
    filePath.includes('/categories') &&
    !filePath.endsWith('/categories/index.mdx');

  if (isInCategories) {
    return filePath.endsWith('index.mdx') ? 'top_category' : 'category';
  }
}

// Checks for missing spaces after ':' in frontmatter fields.
function getMissingSpaceErrors(frontmatterContents, schema) {
  if (!frontmatterContents) return [];

  return Object.keys(schema.properties).reduce((errors, field) => {
    if (frontmatterContents.match(new RegExp(`[\\s^](${field}:)\\S`))) {
      errors.push(
        `A space is missing after the ':' in the field '${field}'. Please add a space between the ':' and the '${field}' value`
      );
    }
    return errors;
  }, []);
}

function validateFrontmatter(filePath) {
  if (filePath && filePath.endsWith('/categories/index.mdx')) return;
  if (!fs.existsSync(filePath) || filePath.indexOf('.github') !== -1) return;

  const pathError = getFilePathError(filePath);
  if (pathError) {
    allErrors.push({ filePath, fileErrors: [pathError] });
    return;
  }

  const ruleType = determineCategory(filePath);
  if (!ruleType) return;

  const fileContents = fs.readFileSync(filePath, 'utf8');
  const frontmatterContents = extractFrontMatter(fileContents);

  if (frontmatterContents === undefined) {
    allErrors.push({ filePath, fileErrors: ["missing '---'"] });
    return;
  }

  const missingSpaceErrors = getMissingSpaceErrors(frontmatterContents, schemas[ruleType]);
  const frontmatter = parseFrontmatterToJson(frontmatterContents);
  const validate = validator.getSchema(ruleType);
  const isValid = validate(frontmatter);

  if (!isValid && validate.errors) {
    const fileErrors = validate.errors
      .filter((error) => error.keyword === 'errorMessage' || error.keyword === 'required')
      .map((error) => error.message);

    if (fileErrors.length > 0 || missingSpaceErrors.length) {
      allErrors.push({ filePath, fileErrors: [...fileErrors, ...missingSpaceErrors] });
    }
  }
}

function parseFrontmatterToJson(fileContents) {
  if (!fileContents) return {};
  try {
    return yaml.load(fileContents, { schema: yaml.JSON_SCHEMA });
  } catch (e) {
    return undefined;
  }
}

function extractFrontMatter(fileContents) {
  if (!fileContents) return undefined;
  const match = /^---([\s\S]*?)---/.exec(fileContents);
  return match ? match[1] : undefined;
}

function validateFiles(fileListPath) {
  const filePaths = fs.readFileSync(fileListPath, 'utf8').trim().split('\n');
  filePaths.forEach((file) => {
    if (file.endsWith('.md') || file.endsWith('.mdx')) {
      validateFrontmatter(file);
    }
  });
}

function main() {
  const args = process.argv.slice(2);

  if (args.includes('--file')) {
    validateFiles(args[args.indexOf('--file') + 1]);
  } else if (args[0]) {
    args[0]
      .split(',')
      .filter((file) => file.endsWith('.md') || file.endsWith('.mdx'))
      .map((file) => `../../${file}`)
      .forEach(validateFrontmatter);
  }

  if (allErrors.length === 0) {
    console.log('No frontmatter validation errors found.');
    return;
  }

  allErrors.forEach(({ filePath, fileErrors }) => {
    console.log(
      `## Rule: [${filePath}](https://github.com/SSWConsulting/SSW.Rules.Content/tree/main/${filePath})\n`
    );
    console.log('Issues Detected:');
    fileErrors.forEach((issue) => console.log(`- **${issue}**`));
    console.log('\n');
    console.log('\n');
  });
  process.exit(1);
}
main();
