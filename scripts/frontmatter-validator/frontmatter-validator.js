const fs = require('fs');
const ajv = require('ajv');
const yaml = require('js-yaml');
const addFormats = require('ajv-formats');
const ajvErrors = require('ajv-errors');

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
  const fullPath = `scripts/frontmatter-validator/${schemaPath}`; // Correct the path
  const json = JSON.parse(fs.readFileSync(fullPath, 'utf8'))
  return json;
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
  if (!fs.existsSync(filePath)) {
    return []; // Return an empty array
  }

  if (filePath.indexOf('.github') !== -1) {
    return []
  }

  const fileContents = fs.readFileSync(filePath, 'utf8');
  const frontmatter = parseFrontmatter(filePath, fileContents);

  const validate = matchSchema(filePath);
  const isValid = validate(frontmatter);
  if (!isValid && validate.errors) {
    const errorList = validate.errors.filter(error => {
      return error.keyword === 'errorMessage' || error.keyword === 'required'
    });

    if (errorList.length >= 1) {
      const errors = [`Invalid Frontmatter detected in ${filePath.replaceAll('../', '')}, please fix the following issues:`];
      errorList.forEach((error, index) => {
        errors.push(`${index + 1}. ${error.message}`);
      });
      return errors; // Return the list of errors
    }
  }

  return []; // Return an empty array if there are no errors
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
  }
}

function validateFiles(fileListPath) {
  const fileContents = fs.readFileSync(fileListPath, 'utf8');
  const filePaths = fileContents.trim().split('\n');
  let allErrors = [];

  filePaths
    .filter(file => file.endsWith('.md'))
    .map(file => `${file}`) // Adjust the path as necessary
    .forEach(filePath => {
      const fileErrors = validateFrontmatter(filePath.trim());
      if (fileErrors.length > 0) {
        allErrors = allErrors.concat(fileErrors);
      }
    });

  return allErrors;
}


function main() {
  const args = process.argv.slice(2);
  let allErrors = [];

  if (args.includes('--file')) {
    const fileListIndex = args.indexOf('--file') + 1;
    const fileListPath = args[fileListIndex];
    allErrors = validateFiles(fileListPath);
  } else {
    const filesChanged = args[0];
    if (filesChanged) {
      const folders = filesChanged
        .split(',')
        .filter(file => file.endsWith('.md'))
        .map(file => `../../${file}`);

      folders.forEach(file => {
        const fileErrors = validateFrontmatter(file);
        if (fileErrors.length > 0) {
          allErrors = allErrors.concat(fileErrors);
        }
      });
    }
  }

  if (allErrors.length > 0) {
    allErrors.forEach(error => console.log(error));
    process.exit(1);
  }
}


main();
