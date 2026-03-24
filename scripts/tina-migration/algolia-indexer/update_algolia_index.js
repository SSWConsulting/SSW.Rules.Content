import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';
import { config } from 'dotenv';
import fg from 'fast-glob';
import matter from 'gray-matter';
import { algoliasearch } from 'algoliasearch';

config();

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const ROOT_DIR = path.resolve(__dirname, '../../../public/uploads/rules');

const APP_ID = process.env.NEXT_PUBLIC_ALGOLIA_APP_ID;
const ADMIN_KEY = process.env.NEXT_PUBLIC_ALGOLIA_ADMIN_KEY;
const INDEX_NAME = process.env.NEXT_PUBLIC_ALGOLIA_INDEX_NAME || 'index-json';

// Maximum content length to stay within Algolia's 10KB record limit
// Frontmatter typically takes ~1-2KB, so we cap content at 8000 chars
const MAX_CONTENT_LENGTH = 8000;

if (!APP_ID || !ADMIN_KEY || !INDEX_NAME) {
  console.error('⛔ Missing .env variable.');
  process.exit(1);
}

const client = algoliasearch(APP_ID, ADMIN_KEY);

/**
 * Strip MDX/JSX components, HTML tags, import statements, and markdown
 * syntax to produce clean plain text suitable for full-text search indexing.
 */
function stripMdxToPlainText(rawContent) {
  let text = rawContent;

  // Remove import statements
  text = text.replace(/^import\s+.*?[;\n]/gm, '');

  // Remove <endIntro /> self-closing tags
  text = text.replace(/<endIntro\s*\/?>/gi, '');

  // Remove multi-line MDX component blocks (e.g. <boxEmbed ... />, <imageEmbed ... />, etc.)
  // These can span multiple lines with JSX expressions like body={<>...</>}
  text = text.replace(/<(boxEmbed|imageEmbed|emailEmbed|youtubeEmbed)\s[\s\S]*?\/>/gi, '');

  // Remove any remaining self-closing JSX/HTML tags
  text = text.replace(/<[a-zA-Z][a-zA-Z0-9]*\s[^>]*\/>/g, '');

  // Remove paired HTML/JSX tags and their content for non-content tags
  text = text.replace(/<(script|style)[\s\S]*?<\/\1>/gi, '');

  // Remove remaining HTML/JSX opening and closing tags (keep inner content)
  text = text.replace(/<\/?[a-zA-Z][a-zA-Z0-9]*[^>]*>/g, '');

  // Remove JSX expression wrappers {<> ... </>}
  text = text.replace(/\{<>|<\/>\}/g, '');

  // Remove markdown image syntax ![alt](url)
  text = text.replace(/!\[[^\]]*\]\([^)]*\)/g, '');

  // Convert markdown links [text](url) to just text
  text = text.replace(/\[([^\]]*)\]\([^)]*\)/g, '$1');

  // Remove markdown heading markers
  text = text.replace(/^#{1,6}\s+/gm, '');

  // Remove markdown emphasis markers (bold, italic, strikethrough, highlight)
  text = text.replace(/(\*{1,3}|_{1,3}|~~|==)(.*?)\1/g, '$2');

  // Remove markdown code block fences
  text = text.replace(/```[\s\S]*?```/g, '');
  text = text.replace(/`([^`]*)`/g, '$1');

  // Remove horizontal rules
  text = text.replace(/^[-*_]{3,}\s*$/gm, '');

  // Remove markdown list markers
  text = text.replace(/^\s*[\*\-\+]\s+/gm, '');
  text = text.replace(/^\s*\d+\.\s+/gm, '');

  // Collapse multiple newlines and spaces
  text = text.replace(/\n{2,}/g, '\n');
  text = text.replace(/[ \t]{2,}/g, ' ');

  return text.trim();
}

// Get current files
const files = await fg('**/*.mdx', { cwd: ROOT_DIR, absolute: true });

const currentObjects = files.map(fp => {
  const { data: frontmatter, content } = matter(fs.readFileSync(fp, 'utf-8'));
  const rawSlug = path.relative(ROOT_DIR, path.dirname(fp)).replace(/\\/g, '/');
  const slug = rawSlug.replace(/-+/g, '-');

  // Strip MDX to plain text and truncate for Algolia record size limit
  let plainContent = stripMdxToPlainText(content);
  if (plainContent.length > MAX_CONTENT_LENGTH) {
    plainContent = plainContent.substring(0, MAX_CONTENT_LENGTH) + '…';
  }

  // Only patch the content field — preserve all other fields managed by TinaCMS
  return {
    objectID: slug,
    content: plainContent,
  };
});

console.log(`📊 Rules to update: ${currentObjects.length}`);

// Patch content field on existing Algolia records without overwriting other fields
if (currentObjects.length > 0) {
  console.log(`🔄 Patching content field on ${currentObjects.length} records...`);
  await client.partialUpdateObjects({
    indexName: INDEX_NAME,
    objects: currentObjects,
    createIfNotExists: false,
    waitForTasks: true,
  });
}

// Configure searchable attributes and snippet/highlight settings
console.log('⚙️  Configuring index settings...');
await client.setSettings({
  indexName: INDEX_NAME,
  indexSettings: {
    searchableAttributes: [
      'title',
      'uri',
      'seoDescription',
      'content',
    ],
    attributesToSnippet: [
      'content:30',
    ],
    attributesToHighlight: [
      'title',
      'content',
    ],
    highlightPreTag: '<mark>',
    highlightPostTag: '</mark>',
  },
});

console.log('✅ Index updated successfully!');