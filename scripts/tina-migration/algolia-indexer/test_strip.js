import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';
import matter from 'gray-matter';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

function stripMdxToPlainText(rawContent) {
  let text = rawContent;
  text = text.replace(/^import\s+.*?[;\n]/gm, '');
  text = text.replace(/<endIntro\s*\/?>/gi, '');
  text = text.replace(/<(boxEmbed|imageEmbed|emailEmbed|youtubeEmbed)\s[\s\S]*?\/>/gi, '');
  text = text.replace(/<[a-zA-Z][a-zA-Z0-9]*\s[^>]*\/>/g, '');
  text = text.replace(/<(script|style)[\s\S]*?<\/\1>/gi, '');
  text = text.replace(/<\/?[a-zA-Z][a-zA-Z0-9]*[^>]*>/g, '');
  text = text.replace(/\{<>|<\/>\}/g, '');
  text = text.replace(/!\[[^\]]*\]\([^)]*\)/g, '');
  text = text.replace(/\[([^\]]*)\]\([^)]*\)/g, '$1');
  text = text.replace(/^#{1,6}\s+/gm, '');
  text = text.replace(/(\*{1,3}|_{1,3}|~~|==)(.*?)\1/g, '$2');
  text = text.replace(/```[\s\S]*?```/g, '');
  text = text.replace(/`([^`]*)`/g, '$1');
  text = text.replace(/^[-*_]{3,}\s*$/gm, '');
  text = text.replace(/^\s*[\*\-\+]\s+/gm, '');
  text = text.replace(/^\s*\d+\.\s+/gm, '');
  text = text.replace(/\n{2,}/g, '\n');
  text = text.replace(/[ \t]{2,}/g, ' ');
  return text.trim();
}

const ROOT_DIR = path.resolve(__dirname, '../../../public/uploads/rules');
const testFile = path.join(ROOT_DIR, 'ai-assisted-tools-for-prototyping/rule.mdx');
const raw = fs.readFileSync(testFile, 'utf-8');
const { data, content } = matter(raw);
const plain = stripMdxToPlainText(content);

console.log('--- TITLE ---');
console.log(data.title);
console.log('--- CONTENT LENGTH ---');
console.log(plain.length, 'chars');
console.log('--- FIRST 500 CHARS ---');
console.log(plain.substring(0, 500));
console.log('--- LAST 200 CHARS ---');
console.log(plain.substring(plain.length - 200));
