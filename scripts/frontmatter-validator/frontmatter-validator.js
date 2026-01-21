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
  let fullPath = `scripts/frontmatter-validator/${schemaPath}`;
  fullPath = args.includes('--file')
    ? `scripts/frontmatter-validator/${schemaPath}`
    : schemaPath;

  // todo fix for non file input
  const json = JSON.parse(fs.readFileSync(fullPath, 'utf8'));
  return json;
}

function determineCategory(filePath) {
  const isRule = filePath.endsWith('rule.md');
  const isInCategories =
    filePath.includes('/categories') &&
    !filePath.endsWith('/categories/index.md');
  const isIndexFile = filePath.endsWith('index.md');
  if (isRule) {
    return 'rule';
  }
  if (isInCategories) {
    if (!isIndexFile) {
      return 'category';
    } else {
      return 'top_category';
    }
  }
}

function getMissingSpaceErrors(frontmatterContents, schema) {
  const errors = [];
  if (!frontmatterContents) return [];
  for (const field of Object.keys(schema.properties)) {
    const regex = new RegExp(`[\\s^](${field}:)\\S`);
    if (frontmatterContents.match(regex)) {
      errors.push(
        `A space is missing after the ':' in the field '${field}'. Please add a space between the ':' and the '${field}' value`
      );
    }
  }
  return errors;
}

function validateFrontmatter(filePath) {
  if (filePath && filePath.endsWith('/categories/index.md')) return;
  if (!fs.existsSync(filePath) || filePath.indexOf('.github') !== -1) {
    return; // Skip if file does not exist or is in .github directory
  }
  const ruleType = determineCategory(filePath);
  if (!ruleType) {
    return; // Skip files that are not rules or categories
  }
  const fileContents = fs.readFileSync(filePath, 'utf8');
  const frontmatterContents = extractFrontMatter(fileContents);
  if (frontmatterContents === undefined) {
    allErrors.push({
      filePath,
      fileErrors: ["missing '---'"],
    });
    return;
  }
  const missingSpaceErrors = getMissingSpaceErrors(
    frontmatterContents,
    schemas[ruleType]
  );
  const frontmatter = parseFrontmatterToJson(frontmatterContents);
  const validate = validator.getSchema(ruleType);
  const isValid = validate(frontmatter);
  if (!isValid && validate.errors) {
    let fileErrors = validate.errors
      .filter(
        (error) =>
          error.keyword === 'errorMessage' || error.keyword === 'required'
      )
      .map((error) => error.message);
    if (fileErrors.length > 0 || missingSpaceErrors.length) {
      allErrors.push({
        filePath,
        fileErrors: [...fileErrors, ...missingSpaceErrors],
      });
    }
  }
}

function parseFrontmatterToJson(fileContents) {
  if (!fileContents) {
    return {};
  }
  try {
    return yaml.load(fileContents, {
      schema: yaml.JSON_SCHEMA,
    });
  } catch (e) {
    return undefined;
  }
}

function extractFrontMatter(fileContents) {
  if (!fileContents) return undefined;
  let frontmatterString;
  const frontmatterMatch = /^---([\s\S]*?)---/.exec(fileContents);

  if (!frontmatterMatch) return undefined;
  frontmatterString = frontmatterMatch[1];
  return frontmatterString;
}

function validateFiles(fileListPath) {
  const fileContents = fs.readFileSync(fileListPath, 'utf8');
  const filePaths = fileContents.trim().split('\n');

  filePaths.forEach((file) => {
    if (file.endsWith('.md')) {
      validateFrontmatter(file);
    }
  });
}

function main() {
  const args = process.argv.slice(2);

  if (args.includes('--file')) {
    const fileListIndex = args.indexOf('--file') + 1;
    const fileListPath = args[fileListIndex];
    validateFiles(fileListPath);
  } else {
    const filesChanged = args[0];
    if (filesChanged) {
      const filePaths = filesChanged
        .split(',')
        .filter((file) => file.endsWith('.md'))
        .map((file) => `../../${file}`);
      filePaths.forEach(validateFrontmatter);
    }
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
