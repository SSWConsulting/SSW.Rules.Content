const fs = require("fs");
const ajv = require("ajv");
const yaml = require("js-yaml");
const addFormats = require("ajv-formats");
const ajvErrors = require("ajv-errors");

let allErrors = [];

const schemas = {
  rule: loadSchema("schema/rule-schema.json"),
  category: loadSchema("schema/category-schema.json"),
  top_category: loadSchema("schema/top-category-schema.json"),
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
  fullPath = args.includes("--file")
    ? `scripts/frontmatter-validator/${schemaPath}`
    : schemaPath;

  // todo fix for non file input
  const json = JSON.parse(fs.readFileSync(fullPath, "utf8"));
  return json;
}

function matchSchema(filePath) {
  if (filePath.endsWith("rule.md")) {
    return validator.getSchema("rule");
  } else if (
    filePath.indexOf("/categories") !== -1 &&
    !filePath.endsWith("index.md")
  ) {
    return validator.getSchema("category");
  } else if (
    filePath.indexOf("/categories") !== -1 &&
    filePath.endsWith("index.md")
  ) {
    return validator.getSchema("top_category");
  }
}

function validateFrontmatter(filePath) {
  if (!fs.existsSync(filePath) || filePath.indexOf(".github") !== -1) {
    return; // Skip if file does not exist or is in .github directory
  }

  const fileContents = fs.readFileSync(filePath, "utf8");
  const frontmatter = parseFrontmatter(filePath, fileContents);
  const validate = matchSchema(filePath);
  const isValid = validate(frontmatter);

  if (!isValid && validate.errors) {
    let fileErrors = validate.errors
      .filter(
        (error) =>
          error.keyword === "errorMessage" || error.keyword === "required"
      )
      .map((error) => error.message);

    if (fileErrors.length > 0) {
      allErrors.push({ filePath, fileErrors });
    }
  }
}

function parseFrontmatter(filePath, fileContents) {
  if (!fileContents) return {};

  try {
    const frontmatterMatch = /^---([\s\S]*?)---/.exec(fileContents);
    const frontmatterString = frontmatterMatch[1];
    const frontmatter = yaml.load(frontmatterString, {
      schema: yaml.JSON_SCHEMA,
    });
    return frontmatter;
  } catch (error) {
    allErrors.push({
      filePath,
      fileErrors: ["missing '---'"],
    });
  }
}

function validateFiles(fileListPath) {
  const fileContents = fs.readFileSync(fileListPath, "utf8");
  const filePaths = fileContents.trim().split("\n");

  filePaths.forEach((file) => {
    if (file.endsWith(".md")) {
      validateFrontmatter(file);
    }
  });
}

function main() {
  const args = process.argv.slice(2);

  if (args.includes("--file")) {
    const fileListIndex = args.indexOf("--file") + 1;
    const fileListPath = args[fileListIndex];
    validateFiles(fileListPath);
  } else {
    const filesChanged = args[0];
    if (filesChanged) {
      const filePaths = filesChanged
        .split(",")
        .filter((file) => file.endsWith(".md"))
        .map((file) => `../../${file}`);
      filePaths.forEach(validateFrontmatter);
    }
  }

  if (allErrors.length === 0) {
    console.log("No frontmatter validation errors found.");
    return;
  }


  allErrors.forEach(({ filePath, fileErrors }) => {
    console.log(`## Rule: [${filePath}](https://github.com/SSWConsulting/SSW.Rules.Content/tree/main/${filePath})\n`);
    console.log("Issues:");
    fileErrors.forEach((issue) => console.log(`- **${issue}**`));
    console.log("\n");
    console.log("\n");
  });
  process.exit(1);

  process.exit(1);
}

main();
