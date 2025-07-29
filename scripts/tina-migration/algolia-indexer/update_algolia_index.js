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

if (!APP_ID || !ADMIN_KEY || !INDEX_NAME) {
  console.error('⛔ Missing .env variable.');
  process.exit(1);
}

const client = algoliasearch(APP_ID, ADMIN_KEY);

// Get current files
const files = await fg('**/*.mdx', { cwd: ROOT_DIR, absolute: true });

const currentObjects = files.map(fp => {
  const { data: frontmatter, content } = matter(fs.readFileSync(fp, 'utf-8'));
  const rawSlug = path.relative(ROOT_DIR, path.dirname(fp)).replace(/\\/g, '/');
  const slug = rawSlug.replace(/-+/g, '-');

  return {
    objectID: slug,
    slug,
    ...frontmatter,
  };
});
const currentObjectIDs = new Set(currentObjects.map(obj => obj.objectID));

// Get existing objects from Algolia
console.log('🔍 Fetching existing objects from Algolia...');
const existingObjects = [];

// Use searchForHits with empty query to get all objects
let page = 0;
const hitsPerPage = 1000; // Maximum allowed
let hasMore = true;

while (hasMore) {
  try {
    const { results } = await client.search({
      requests: [{
        indexName: INDEX_NAME,
        query: '', // Empty query returns all results
        page,
        hitsPerPage,
        attributesToRetrieve: ['objectID'] // Only need objectID for comparison
      }]
    });
    
    const hits = results[0].hits;
    existingObjects.push(...hits);
    
    hasMore = hits.length === hitsPerPage;
    page++;
    
    console.log(`📄 Fetched page ${page}, total objects: ${existingObjects.length}`);
  } catch (error) {
    console.error('Error fetching existing objects:', error);
    break;
  }
}

const existingObjectIDs = new Set(existingObjects.map(obj => obj.objectID));

// Find objects to delete (exist in Algolia but not in current files)
const objectsToDelete = [...existingObjectIDs].filter(id => !currentObjectIDs.has(id));

console.log(`📊 Current files: ${currentObjects.length}`);
console.log(`📊 Existing in index: ${existingObjects.length}`);
console.log(`🗑️  Objects to delete: ${objectsToDelete.length}`);

// Delete removed objects
if (objectsToDelete.length > 0) {
  console.log(`🗑️  Deleting ${objectsToDelete.length} objects...`);
  await client.deleteObjects({
    indexName: INDEX_NAME,
    objectIDs: objectsToDelete,
    waitForTasks: true,
  });
}

// Update/add current objects
if (currentObjects.length > 0) {
  console.log(`🔄 Updating ${currentObjects.length} objects...`);
  await client.saveObjects({
    indexName: INDEX_NAME,
    objects: currentObjects,
    waitForTasks: true,
  });
}

console.log('✅ Index updated successfully!');