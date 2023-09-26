const fs = require('fs');
const ajv = require('ajv');
const yaml = require('js-yaml');
const addFormats = require('ajv-formats');
const ajvErrors = require('ajv-errors');

const schema = JSON.parse(fs.readFileSync('schema.json', 'utf8'));

const validator = new ajv({ allErrors: true });
addFormats(validator);
ajvErrors(validator);
const validate = validator.compile(schema);

function main() {
  const eventType = process.env.GITHUB_EVENT_NAME;

  if (eventType === 'pull_request') {
    if (process.argv[2] && process.argv[2].length > 0) {
      const folders = process.argv[2]
        .split(',')
        .filter((file) => file.endsWith('rule.md'))
        .map((file) => `../../${file}`);

      folders.forEach((file) => validateFrontmatter(file));
    }
  }
}

function validateFrontmatter(filePath) {
  const fileContents = fs.readFileSync(filePath, 'utf8');
  const frontmatter = parseFrontmatter(fileContents);

  const isValid = validate(frontmatter);

  if (!isValid) {
    console.log(`Invalid Frontmatter detected in ${filePath.replaceAll('../', '')}, see details:`);
    validate.errors.forEach((item) => {
      if (item.keyword === 'errorMessage' || item.keyword === 'required') {
        console.log(`- ${item.message}`)
      }
    })
    process.exit(1);
  } else {
    console.log('Validation successful');
  }
}

function parseFrontmatter(fileContents) {
  if (!fileContents) return {}
  
  try {
    const frontmatterMatch = /^---([\s\S]*?)---/.exec(fileContents);
    const frontmatterString = frontmatterMatch[1];
    const frontmatter = yaml.load(frontmatterString, {
      schema: yaml.JSON_SCHEMA,
    });
    return frontmatter;
  } catch (error) {
    console.error(`Error parsing frontmatter: missing '---'`);
    process.exit(1);
  }
}

main();