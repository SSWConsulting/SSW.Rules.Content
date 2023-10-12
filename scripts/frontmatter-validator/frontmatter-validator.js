const fs = require('fs');
const ajv = require('ajv');
const yaml = require('js-yaml');
const addFormats = require('ajv-formats');
const ajvErrors = require('ajv-errors');

const schemas = {
  rule: loadSchema('./schema/rule-schema.json'),
  category: loadSchema('./schema/category-schema.json'),
  top_category: loadSchema('./schema/top-category-schema.json'),
}

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
  return JSON.parse(fs.readFileSync(schemaPath, 'utf8'));
}

function matchSchema(filePath) {
  if (filePath.endsWith('rule.md')) {
    return validator.getSchema('rule');
  } else if (filePath.indexOf('/categories') !== -1 && !filePath.endsWith('index.md')) {
    return validator.getSchema('category');
  } else if (filePath.indexOf('/categories') !== -1 && filePath.endsWith('index.md')) {
    return validator.getSchema('top_category');
  }
}

function validateFrontmatter(filePath) {
  if (filePath.indexOf('.github') !== -1) {
    return
  }
  
  if (!fs.existsSync(filePath)) {
    console.error(`File ${filePath} does not exist.`);
    return
  }

  const fileContents = fs.readFileSync(filePath, 'utf8');
  const frontmatter = parseFrontmatter(filePath, fileContents);

  const validate = matchSchema(filePath);
  const isValid = validate(frontmatter);

  if (!isValid && validate.errors) {
    const errorList = validate.errors.filter(error => {
      return error.keyword === 'errorMessage' || error.keyword === 'required'
    })

    if (errorList.length >= 1) {
      console.log(`Invalid Frontmatter detected in ${filePath.replaceAll('../', '')}, please fix the following issues:`);
      errorList.forEach((error, index) => {
        console.log(`${index + 1}. ${error.message}`);
      })
      process.exit(1);
    }
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
    const filesChanged  = process.argv[2];

    if (filesChanged) {
      const folders = filesChanged
        .split(',')
        .filter((file) => file.endsWith('.md'))
        .map((file) => `../../${file}`);

      folders.forEach((file) => validateFrontmatter(file));
    }
  }
}

main();
