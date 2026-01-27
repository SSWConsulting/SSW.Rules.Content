#!/usr/bin/env node

/**
 * Script to fix duplicate figure prefixes in MDX files.
 *
 * When figurePrefix="bad" or "good", the component automatically adds
 * "Bad example" or "Good example" prefix. This script removes redundant
 * prefixes from the figure text when they would be duplicated.
 *
 * Patterns fixed:
 * - figurePrefix="bad" + figure="Bad Example - ..." → figure="..."
 * - figurePrefix="good" + figure="Good Example - ..." → figure="..."
 * - Also handles variations with different separators (: , – —)
 *
 * Usage: node scripts/fix-duplicate-figure-prefixes.js [--dry-run]
 */

const fs = require('fs');
const path = require('path');

const RULES_DIR = path.join(__dirname, '..', 'public', 'uploads', 'rules');
const DRY_RUN = process.argv.includes('--dry-run');

/**
 * Find all MDX files recursively in a directory
 */
function findMdxFiles(dir) {
  const files = [];

  function walk(currentDir) {
    const entries = fs.readdirSync(currentDir, { withFileTypes: true });

    for (const entry of entries) {
      const fullPath = path.join(currentDir, entry.name);

      if (entry.isDirectory()) {
        walk(fullPath);
      } else if (entry.isFile() && entry.name.endsWith('.mdx')) {
        files.push(fullPath);
      }
    }
  }

  walk(dir);
  return files;
}

/**
 * Extract all JSX-like component blocks from content
 * Returns array of { start, end, content }
 */
function extractComponents(content) {
  const components = [];
  // Match opening tags of custom components (lowercase starting letter = JSX component)
  const tagRegex = /<([a-z][a-zA-Z]*)\s/g;
  let match;

  while ((match = tagRegex.exec(content)) !== null) {
    const tagName = match[1];
    const startPos = match.index;

    // Find the end of this component (self-closing /> or closing tag)
    // We need to handle:
    // 1. JSX expressions like body={<>...</>} which contain > characters
    // 2. Quoted strings that may contain > characters

    let endPos = -1;

    // Search character by character, tracking brace depth and quote state
    let i = startPos + match[0].length;
    let braceDepth = 0;
    let inSingleQuote = false;
    let inDoubleQuote = false;

    while (i < content.length) {
      const char = content[i];
      const prevChar = i > 0 ? content[i - 1] : '';

      // Handle quote state (ignore escaped quotes)
      if (char === "'" && prevChar !== '\\' && !inDoubleQuote) {
        inSingleQuote = !inSingleQuote;
      } else if (char === '"' && prevChar !== '\\' && !inSingleQuote) {
        inDoubleQuote = !inDoubleQuote;
      }

      // Only process braces and angle brackets when not inside quotes
      if (!inSingleQuote && !inDoubleQuote) {
        if (char === '{') {
          braceDepth++;
        } else if (char === '}') {
          braceDepth--;
        } else if (braceDepth === 0) {
          // Only look for /> or > when we're not inside a JSX expression
          if (content.slice(i, i + 2) === '/>') {
            // Self-closing tag
            endPos = i + 2;
            break;
          } else if (char === '>') {
            // Has closing tag - find it
            const closingTag = `</${tagName}>`;
            const closePos = content.indexOf(closingTag, i);
            if (closePos !== -1) {
              endPos = closePos + closingTag.length;
            }
            break;
          }
        }
      }

      i++;
    }

    if (endPos !== -1) {
      components.push({
        start: startPos,
        end: endPos,
        content: content.slice(startPos, endPos)
      });
    }
  }

  return components;
}

/**
 * Check if a component has figurePrefix and matching redundant figure text
 * Returns { needsFix: boolean, figurePrefix: string, oldFigure: string, newFigure: string, quoteChar: string, oldFigurePrefix: string, newFigurePrefix: string }
 */
function checkComponent(componentContent) {
  // Extract figurePrefix value (can use single or double quotes)
  const prefixMatch = componentContent.match(/figurePrefix\s*=\s*["'](bad|good|ok|none)["']/i);
  if (!prefixMatch) {
    return { needsFix: false };
  }

  const figurePrefix = prefixMatch[1].toLowerCase();

  // Extract figure value - try double quotes first, then single quotes
  let figureMatch = componentContent.match(/figure\s*=\s*"([^"]*)"/);
  let quoteChar = '"';

  if (!figureMatch) {
    // Try single quotes
    figureMatch = componentContent.match(/figure\s*=\s*'([^']*)'/);
    quoteChar = "'";
  }

  if (!figureMatch) {
    return { needsFix: false };
  }

  const figure = figureMatch[1];

  // Check if figure starts with a prefix that should be handled
  // Patterns to match:
  // - "Bad example - ..."
  // - "Good example - ..."
  // - "OK example - ..."
  // With separators: " - ", " – ", " — ", ": ", ", "
  const prefixMap = { bad: 'Bad', good: 'Good', ok: 'OK' };

  if (figurePrefix === 'none') {
    // Check if figure starts with any example prefix - if so, we need to fix it
    for (const [key, value] of Object.entries(prefixMap)) {
      const regex = new RegExp(`^${value}\\s+[Ee]xample\\s*[-–—:,]\\s*`, 'i');
      const match = figure.match(regex);
      if (match) {
        // Found a prefix in the figure text - need to change figurePrefix from "none" to the correct value
        let newFigure = figure.slice(match[0].length);
        if (newFigure.length > 0) {
          newFigure = newFigure.charAt(0).toUpperCase() + newFigure.slice(1);
        }
        return {
          needsFix: true,
          figurePrefix: key,
          oldFigure: figure,
          newFigure,
          quoteChar,
          oldFigurePrefix: 'none',
          newFigurePrefix: key
        };
      }
    }
    return { needsFix: false };
  }

  // For bad/good/ok, check if figure has redundant prefix
  const expectedPrefix = prefixMap[figurePrefix];
  const redundantPrefixRegex = new RegExp(
    `^${expectedPrefix}\\s+[Ee]xample\\s*[-–—:,]\\s*`,
    'i'
  );

  const redundantMatch = figure.match(redundantPrefixRegex);
  if (!redundantMatch) {
    return { needsFix: false };
  }

  // Calculate new figure value
  let newFigure = figure.slice(redundantMatch[0].length);

  // Capitalize the first letter if there's content remaining
  if (newFigure.length > 0) {
    newFigure = newFigure.charAt(0).toUpperCase() + newFigure.slice(1);
  }

  return {
    needsFix: true,
    figurePrefix,
    oldFigure: figure,
    newFigure,
    oldFigurePrefix: figurePrefix,
    newFigurePrefix: figurePrefix,
    quoteChar
  };
}

/**
 * Process a single MDX file and fix duplicate prefixes
 * Returns { modified: boolean, changes: array of change descriptions }
 */
function processFile(filePath) {
  const content = fs.readFileSync(filePath, 'utf8');
  let newContent = content;
  const changes = [];
  const relativePath = path.relative(RULES_DIR, filePath);

  // Extract all components
  const components = extractComponents(content);

  // Process in reverse order to maintain correct positions when replacing
  const sortedComponents = [...components].sort((a, b) => b.start - a.start);

  for (const component of sortedComponents) {
    const check = checkComponent(component.content);

    if (check.needsFix) {
      let newComponentContent = component.content;

      // Replace the figure value (preserve the original quote style)
      const oldFigureAttr = `figure=${check.quoteChar}${check.oldFigure}${check.quoteChar}`;
      const newFigureAttr = `figure=${check.quoteChar}${check.newFigure}${check.quoteChar}`;
      newComponentContent = newComponentContent.replace(oldFigureAttr, newFigureAttr);

      // If figurePrefix needs to change (e.g., from "none" to "good"), update it too
      if (check.oldFigurePrefix !== check.newFigurePrefix) {
        // Match figurePrefix with either single or double quotes
        const oldPrefixAttr = new RegExp(`figurePrefix\\s*=\\s*["']${check.oldFigurePrefix}["']`, 'i');
        newComponentContent = newComponentContent.replace(oldPrefixAttr, `figurePrefix="${check.newFigurePrefix}"`);
      }

      // Replace in the full content
      newContent =
        newContent.slice(0, component.start) +
        newComponentContent +
        newContent.slice(component.end);

      changes.push({
        file: relativePath,
        prefix: check.figurePrefix,
        from: check.oldFigure,
        to: check.newFigure,
        prefixChange: check.oldFigurePrefix !== check.newFigurePrefix
          ? `${check.oldFigurePrefix} → ${check.newFigurePrefix}`
          : null
      });
    }
  }

  const modified = content !== newContent;

  if (modified && !DRY_RUN) {
    fs.writeFileSync(filePath, newContent, 'utf8');
  }

  return { modified, changes };
}

/**
 * Main function
 */
function main() {
  console.log('='.repeat(60));
  console.log('Fix Duplicate Figure Prefixes in MDX Files');
  console.log('='.repeat(60));

  if (DRY_RUN) {
    console.log('\n🔍 DRY RUN MODE - No files will be modified\n');
  }

  // Find all MDX files
  console.log(`\nSearching for MDX files in: ${RULES_DIR}\n`);

  const mdxFiles = findMdxFiles(RULES_DIR);
  console.log(`Found ${mdxFiles.length} MDX files\n`);

  // Process each file
  let totalModified = 0;
  let totalChanges = 0;
  const allChanges = [];

  for (const file of mdxFiles) {
    const { modified, changes } = processFile(file);

    if (modified) {
      totalModified++;
      totalChanges += changes.length;
      allChanges.push(...changes);
    }
  }

  // Print results
  console.log('-'.repeat(60));
  console.log('RESULTS');
  console.log('-'.repeat(60));

  if (allChanges.length > 0) {
    console.log('\nChanges made:\n');

    // Group by file
    const byFile = {};
    for (const change of allChanges) {
      if (!byFile[change.file]) {
        byFile[change.file] = [];
      }
      byFile[change.file].push(change);
    }

    for (const [file, changes] of Object.entries(byFile)) {
      console.log(`📄 ${file}`);
      for (const change of changes) {
        const prefixInfo = change.prefixChange ? ` (figurePrefix: ${change.prefixChange})` : '';
        console.log(`   [${change.prefix}] "${change.from}"${prefixInfo}`);
        console.log(`        → "${change.to}"`);
      }
      console.log();
    }
  }

  console.log('-'.repeat(60));
  console.log(`Files modified: ${totalModified}`);
  console.log(`Total changes: ${totalChanges}`);

  if (DRY_RUN && totalChanges > 0) {
    console.log('\n💡 Run without --dry-run to apply these changes');
  }

  console.log('='.repeat(60));
}

main();
