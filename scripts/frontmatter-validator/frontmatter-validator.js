const fs = require('fs');
const ajv = require('ajv');
const yaml = require('js-yaml');
const addFormats = require('ajv-formats');
const ajvErrors = require('ajv-errors');

const schemas = {
  rule: loadSchema('rule-schema.json'),
  category: loadSchema('category-schema.json'),
  top_category: loadSchema('top-category-schema.json'),
}

const validator = initializeValidator()

function initializeValidator() {
  const validator = new ajv({ allErrors: true });
  addFormats(validator);
  ajvErrors(validator);

  for (const key in schemas) {
    validator.addSchema(schemas[key], key);
  }

  return validator
}

function loadSchema(schemaPath) {
  return JSON.parse(fs.readFileSync(schemaPath, 'utf8'));
}

function matchSchema(filePath) {
  if (filePath.endsWith('rule.md')) {
    return validator.getSchema('rule')
  } else if (filePath.indexOf('/categories') !== -1 && !filePath.endsWith('index.md')) {
    return validator.getSchema('category')
  } else if (filePath.indexOf('/categories') !== -1 && filePath.endsWith('index.md')) {
    return validator.getSchema('top_category')
  }
}

function validateFrontmatter(filePath) {
  const fileContents = fs.readFileSync(filePath, 'utf8');
  const frontmatter = parseFrontmatter(filePath, fileContents);

  const validate = matchSchema(filePath)
  const isValid = validate(frontmatter);

  if (!isValid) {
    console.log(`Invalid Frontmatter detected in ${filePath.replaceAll('../', '')}, see details:`);
    validate.errors.forEach((item) => {
      if (item.keyword === 'errorMessage' || item.keyword === 'required') {
        console.log(`- ${item.message}`);
      }
    })
    process.exit(1);
  }
}

function parseFrontmatter(filePath, fileContents) {
  if (!fileContents) return {}
  
  try {
    const frontmatterMatch = /^---([\s\S]*?)---/.exec(fileContents);
    const frontmatterString = frontmatterMatch[1];
    const frontmatter = yaml.load(frontmatterString, {
      schema: yaml.JSON_SCHEMA,
    });
    return frontmatter;
  } catch (error) {
    console.log(`Invalid Frontmatter detected in ${filePath.replaceAll('../', '')}: missing '---'`);
    process.exit(1);
  }
}

function main() {
  const eventType = process.env.GITHUB_EVENT_NAME;

  if (eventType === 'pull_request') {

    // process.argv[2] represents the argument provided via command-line input when running the script.
    // In the code below, it is a comma-separated list of changed files.
    if (process.argv[2] && process.argv[2].length > 0) {
      const folders = process.argv[2]
        .split(',')
        .filter((file) => file.endsWith('.md'))
        .map((file) => `../../${file}`);

      folders.forEach((file) => validateFrontmatter(file));
    }
  }
}

main();