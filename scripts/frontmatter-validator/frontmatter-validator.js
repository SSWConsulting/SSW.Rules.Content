const fs = require('fs');
const ajv = require('ajv');
const yaml = require('js-yaml');

const schema = JSON.parse(fs.readFileSync('schema.json', 'utf8'));

// const validator = new ajv({ allErrors: true });
const validator = new ajv();
const validate = validator.compile(schema);

const filePath = './rules/3-steps-to-a-pbi/rule.md';
// const filePath = './rules/do-you-know-the-best-project-version-conventions/rule.md';
// const filePath = process.argv[2];
if (filePath) {
    validateFrontmatter(filePath.replace('./', '../../'));
}

function validateFrontmatter(filePath) {
  const fileContents = fs.readFileSync(filePath, 'utf8');
  const frontmatter = parseFrontmatter(fileContents);

  const isValid = validate(frontmatter);

  if (!isValid) {
    console.error(`Invalid Frontmatter in ${filePath}`);
    console.error(validate.errors);
    process.exit(1);
  }
}

function parseFrontmatter(fileContents) {
  const frontmatterMatch = /^---([\s\S]*?)---/.exec(fileContents);
  const frontmatterString = frontmatterMatch[1];
  const frontmatter = yaml.load(frontmatterString);
  return frontmatter
}
