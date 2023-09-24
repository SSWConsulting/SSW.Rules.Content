const fs = require('fs');
const ajv = require('ajv');
const yaml = require('js-yaml');
const addFormats = require('ajv-formats');

const schema = JSON.parse(fs.readFileSync('schema.json', 'utf8'));

const validator = new ajv();
addFormats(validator);
const validate = validator.compile(schema);

function main() {
  const eventType = process.env.GITHUB_EVENT_NAME;

  if (eventType === 'pull_request') {
    if (process.argv[2] && process.argv[2].length > 0) {
      console.log('test print process.argv:', process.argv[2]);
      const folders = process.argv[2]
        .split(',')
        .filter((file) => file.endsWith('rule.md'))
        .map((file) => `../../${file}`);

      console.log('test print folders:', folders);
      folders.forEach((file) => validateFrontmatter(file));
    }
  }
}

function validateFrontmatter(filePath) {
  const fileContents = fs.readFileSync(filePath, 'utf8');
  const frontmatter = parseFrontmatter(fileContents);

  const isValid = validate(frontmatter);

  if (!isValid) {
    console.error(`Invalid Frontmatter in ${filePath}`);
    console.error(validate.errors);
    process.exit(1);
  } else {
    console.log('Validation successful');
  }
}

function parseFrontmatter(fileContents) {
  const frontmatterMatch = /^---([\s\S]*?)---/.exec(fileContents);
  const frontmatterString = frontmatterMatch[1];
  const frontmatter = yaml.load(frontmatterString, {
    schema: yaml.JSON_SCHEMA,
  });
  return frontmatter;
}

main();
