import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';
import { config } from 'dotenv';
import fg from 'fast-glob';
import matter from 'gray-matter';
import { algoliasearch } from 'algoliasearch';

config();

const __filename = fileURLToPath(import.meta.url);
const __dirname  = path.dirname(__filename);

const ROOT_DIR = path.resolve(__dirname, '../../../rules');
const APP_ID     = process.env.NEXT_PUBLIC_ALGOLIA_APP_ID;
const ADMIN_KEY  = process.env.NEXT_PUBLIC_ALGOLIA_ADMIN_KEY;
const INDEX_NAME = process.env.NEXT_PUBLIC_ALGOLIA_INDEX_NAME || 'index-json';

if (!APP_ID || !ADMIN_KEY || !INDEX_NAME) {
  console.error('⛔  Missing .env variable.');
  process.exit(1);
}

const files = await fg('**/*.mdx', { cwd: ROOT_DIR, absolute: true });

// TODO: refine the file sent to Algolia if needed
// Right now, it looks like this:
// {
//  "slug": "getting-started-do-you-know-the-scrum-guide",
//  "title": "Getting Started - Do you know the Scrum guide?",
//  "content": "",
//  "objectID": "getting-started-do-you-know-the-scrum-guide"
// }
const objects = files.map(fp => {
  const { data: frontmatter, content } = matter(fs.readFileSync(fp, 'utf-8'));

  const rawSlug = path.relative(ROOT_DIR, fp).replace(/\\/g, '/').replace(/\.mdx$/, '');
  const slug = rawSlug.replace(/-+/g, '-');

  return { objectID: slug, slug, ...frontmatter, content };
});

console.log(`🔄  Sending ${objects.length} objects to "${INDEX_NAME} index"…`);

const client = algoliasearch(APP_ID, ADMIN_KEY);

await client.saveObjects({
  indexName: INDEX_NAME,
  objects,
  waitForTasks: true,
});

console.log('✅  Index updated successfully!');
