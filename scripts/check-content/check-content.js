// Warning-only content style checks for SSW Rules. Never exits non-zero.
// Usage: node check-content.js [--base <git-ref>] <file.mdx>[,<file.mdx>...]

import fs from "node:fs";
import path from "node:path";
import { execFileSync } from "node:child_process";
import matter from "gray-matter";

const RULES = "https://www.ssw.com.au/rules";
const CHECKS = {
  title: { label: "Title format", rule: "rule", ruleTitle: "Do you know all the cool stuff you can do on SSW Rules?" },
  listFullStop: { label: "Full stop on list item", rule: "avoid-full-stops", ruleTitle: "Do you avoid full stops in lists, captions, and immediately after a URL?" },
  captionFullStop: { label: "Full stop on caption", rule: "avoid-full-stops", ruleTitle: "Do you avoid full stops in lists, captions, and immediately after a URL?" },
  urlEnding: { label: "URL ends with / or .", rule: "no-full-stop-or-slash-at-the-end-of-urls", ruleTitle: "Do you avoid including full stop or slash at the end of URLs?" },
  longNumber: { label: "Long number without separators", rule: "make-numbers-more-readable", ruleTitle: "Do you use separators to improve numbers' readability?" },
  linkText: { label: "Non-descriptive link text", rule: "descriptive-links", ruleTitle: "Do you make your links descriptive?" },
  language: { label: "Common language pitfall", rule: "avoid-common-mistakes#common-language-pitfalls", ruleTitle: "Do you avoid common spelling and syntax mistakes?" },
};

const TITLE_RE = /^(?:.+ [-–—] )?Do you .+\?$/;
const ABBREVIATION_END = /(\.\.\.|…|\betc\.|\be\.g\.|\bi\.e\.|\bvs?\.|\bInc\.|\bLtd\.)$/;
const GENERIC_LINK_TEXT = new Set([
  "click here", "click this", "here", "this", "link", "this link", "read this",
  "more", "read more", "click", "this page", "go here",
]);
const PITFALLS = [
  [/\be-mails?\b/gi, '"email" not "e-mail"'],
  [/\bEMails?\b/g, '"email" not "EMail"'],
  [/\bcan not\b/gi, '"cannot" not "can not"'],
  [/\bweb sites?\b/gi, '"website" not "web site"'],
  [/\buser names?\b/gi, '"username" not "user name"'],
  [/\btask bars?\b/gi, '"taskbar" not "task bar"'],
  [/\bOk\b/g, '"OK" not "Ok"'],
  [/\bokay\b/gi, '"OK" not "okay"'],
  [/\bAKA\b/g, '"aka" not "AKA"'],
  [/\ba\.k\.a\b\.?/gi, '"aka" not "a.k.a"'],
];

/* --------------------------------- helpers -------------------------------- */

function parseArgs(argv) {
  const args = argv.slice(2);
  let base = null;
  const files = [];
  for (let i = 0; i < args.length; i++) {
    if (args[i] === "--base") base = args[++i];
    else files.push(...args[i].split(",").map((s) => s.trim()).filter(Boolean));
  }
  return { base, files: [...new Set(files)].filter((f) => f.endsWith("rule.mdx")) };
}

function changedLines(base, file) {
  if (!base) return null;
  try {
    const diff = execFileSync("git", ["diff", "-U0", "--no-color", `${base}...HEAD`, "--", file], { encoding: "utf8" });
    const lines = new Set();
    for (const m of diff.matchAll(/^@@ -\S+ \+(\d+)(?:,(\d+))? @@/gm)) {
      const start = Number(m[1]);
      const count = m[2] === undefined ? 1 : Number(m[2]);
      for (let i = 0; i < count; i++) lines.add(start + i);
    }
    return lines;
  } catch {
    return null;
  }
}

const stripInlineCode = (s) => s.replace(/`[^`]*`/g, (m) => " ".repeat(m.length));
const stripUrls = (s) =>
  s.replace(/\]\([^)]*\)/g, "]()").replace(/https?:\/\/[^\s)\]>"'`]+/g, " ").replace(/&#?\w+;/g, " ");

/**
 * Split the body into lines tagged with how they should be checked:
 * - "code": fenced code, skipped
 * - "example": greybox / bad example / email body, skipped (examples may break the rules on purpose)
 * - "attr": component attribute lines, skipped except captions
 * - "content": normal prose
 * Captions from figure="..." are collected separately for every component.
 */
function classify(lines, firstLine) {
  const out = [];
  const captions = [];
  let fence = null;

  for (let i = 0; i < lines.length; i++) {
    const line = lines[i];
    const lineNo = firstLine + i;

    const f = line.match(/^\s*(```|~~~)/);
    if (fence || f) {
      if (f && !fence) fence = f[1];
      else if (f && f[1] === fence) fence = null;
      out.push({ lineNo, text: line, kind: "code" });
      continue;
    }

    const open = line.match(/^\s*<(\w+Embed)\b/);
    if (!open) {
      out.push({ lineNo, text: line, kind: /^\s*<!--/.test(line) ? "code" : "content" });
      continue;
    }

    let end = i;
    if (!/\/>\s*$/.test(line)) {
      while (end + 1 < lines.length && lines[end].trim() !== "/>") end++;
    }
    const block = lines.slice(i, end + 1);
    const text = block.join("\n");
    const style = text.match(/\bstyle="(\w+)"/)?.[1];
    const prefix = text.match(/\bfigurePrefix="(\w+)"/)?.[1];
    const isExample = open[1] === "emailEmbed" || style === "greybox" || prefix === "bad";

    let inBody = false;
    block.forEach((b, k) => {
      const n = lineNo + k;
      const cap = b.match(/\bfigure="([^"]*)"/);
      if (cap) captions.push({ lineNo: n, caption: cap[1] });
      if (/body=\{<>/.test(b)) { inBody = true; out.push({ lineNo: n, text: b, kind: "attr" }); return; }
      if (/<\/>\s*\}/.test(b)) { inBody = false; out.push({ lineNo: n, text: b, kind: "attr" }); return; }
      out.push({ lineNo: n, text: b, kind: inBody ? (isExample ? "example" : "content") : "attr" });
    });
    i = end;
  }
  return { out, captions };
}

/* --------------------------------- checks --------------------------------- */

function checkTitle(title) {
  const t = String(title ?? "").replace(/[​-‍﻿]/g, "").trim();
  if (TITLE_RE.test(t)) return [];
  const msgs = [];
  if (t.includes("?") && !t.endsWith("?")) {
    msgs.push(`Text after the "?" - put brackets or other info before the question mark, e.g. "Do you have a war room (summary)?"`);
  } else if (!t.endsWith("?")) {
    msgs.push('Title should end with a question mark');
  }
  if (!/(^| [-–—] )Do you /.test(t)) {
    msgs.push(/(^| [-–—] )do you /i.test(t)
      ? 'Write "Do you" with a capital D and lowercase "you"'
      : 'Title should start with "Do you" (a prefix like "Category - Do you..." is OK)');
  }
  return msgs.map((m) => `${m}: "${t}"`);
}

function checkLine(raw) {
  const issues = [];
  const code = stripInlineCode(raw);

  const item = code.match(/^\s*(?:[*+-]|\d+[.)])\s+(.*\S)\s*$/);
  if (item && item[1].endsWith(".") && !ABBREVIATION_END.test(item[1])) {
    issues.push(["listFullStop", "List item ends with a full stop"]);
  }

  if (/^\s*\*\*(?:[✅❌]\s*)?Figure:.*[^.]\.\*\*\s*$/.test(code)) {
    issues.push(["captionFullStop", "Caption ends with a full stop"]);
  }

  for (const m of code.matchAll(/https?:\/\/[^\s)\]>"'`*]+/g)) {
    const url = m[0].replace(/[,;:!?]+$/, "");
    if (url.endsWith(".")) issues.push(["urlEnding", `URL followed by a full stop (may get copied into the link): ${url}`]);
    else if (url.endsWith("/")) issues.push(["urlEnding", `URL ends with a slash: ${url}`]);
  }

  for (const m of code.matchAll(/\[([^\]]+)\]\(/g)) {
    const text = m[1].replace(/[*_]/g, "").trim().toLowerCase();
    if (GENERIC_LINK_TEXT.has(text)) issues.push(["linkText", `Link text "${m[1]}" doesn't describe the destination`]);
  }
  if (/\bclick (here|this)\b/i.test(code) && !issues.some(([k]) => k === "linkText")) {
    issues.push(["linkText", 'Avoid "click here" / "click this" - describe the destination instead']);
  }

  const prose = stripUrls(code);
  for (const m of prose.matchAll(/(?<![\w#.,:/-])\d{4,}(?!\w)/g)) {
    const n = m[0];
    const before = prose.slice(Math.max(0, m.index - 2), m.index);
    const after = prose.slice(m.index + n.length, m.index + n.length + 2);
    if (n.length === 4 && /^(19|20)\d\d$/.test(n)) continue;
    if (n.length === 4 && (/\d\s$/.test(before) || /^\s\d/.test(after))) continue;
    issues.push(["longNumber", `"${n}" - add separators, e.g. ${Number(n).toLocaleString("en-US")}`]);
  }

  const usedWords = prose.replace(/^\s*(?:[*+-]|\d+[.)])\s+/, " ").replace(/"[^"]*"|“[^”]*”|‘[^’]*’|(?<!\w)'[^'\n]+'(?!\w)|(?<!\*)\*(?!\*)[^*]+\*(?!\*)/g, " ");
  for (const [re, msg] of PITFALLS) {
    if (usedWords.match(re)) issues.push(["language", `Use ${msg}`]);
  }

  return issues;
}

function checkFile(file) {
  const source = fs.readFileSync(file, "utf8");
  const parsed = matter(source);
  const issues = [];

  const fmEnd = source.length - parsed.content.length;
  const firstBodyLine = source.slice(0, fmEnd).split("\n").length;
  const titleLine = source.split("\n").findIndex((l) => /^title:/.test(l)) + 1 || 1;

  if (parsed.data.isArchived !== true) {
    for (const msg of checkTitle(parsed.data.title)) issues.push({ line: titleLine, check: "title", msg });
  }

  const { out, captions } = classify(parsed.content.split("\n"), firstBodyLine);
  for (const { lineNo, text, kind } of out) {
    if (kind !== "content") continue;
    for (const [check, msg] of checkLine(text)) issues.push({ line: lineNo, check, msg });
  }
  for (const { lineNo, caption } of captions) {
    if (/[^.]\.$/.test(caption.trim())) issues.push({ line: lineNo, check: "captionFullStop", msg: "Caption ends with a full stop" });
  }

  return issues.sort((a, b) => a.line - b.line);
}

/* --------------------------------- report --------------------------------- */

function formatIssue(i) {
  const c = CHECKS[i.check];
  return `- Line ${i.line}: **${c.label}** - ${i.msg} (as per [${c.ruleTitle}](${RULES}/${c.rule}))`;
}

function main() {
  const { base, files } = parseArgs(process.argv);
  const reportPath = process.env.CONTENT_REPORT_PATH;
  const sections = [];

  for (const file of files) {
    if (!fs.existsSync(file)) continue;
    const issues = checkFile(file);
    const changed = changedLines(base, file);
    const isNew = (i) => !changed || changed.has(i.line);
    const mine = issues.filter(isNew);
    const old = issues.filter((i) => !isNew(i));

    for (const i of mine) {
      console.log(`::warning file=${file},line=${i.line},title=${CHECKS[i.check].label}::${i.msg}`);
    }
    console.log(`${file}: ${mine.length} in changed lines, ${old.length} existing`);
    if (!mine.length && !old.length) continue;

    const section = [`**\`${file}\`**`, ""];
    if (mine.length) section.push(`⚠️ ${mine.length} warning(s) in lines changed by this PR:`, "", ...mine.map(formatIssue), "");
    else section.push("✅ No warnings in lines changed by this PR.", "");
    if (old.length) section.push(`${old.length} existing warning(s), not introduced by this PR:`, "", ...old.map(formatIssue), "");
    sections.push(section.join("\n"));
  }

  if (!reportPath) return;
  if (!sections.length) {
    fs.rmSync(reportPath, { force: true });
    return;
  }

  const lines = [
    "<!-- content-check -->",
    "### ✍️ Content style check",
    "",
    "_Warnings only - this check never blocks the PR._",
    "",
    sections.join("\n"),
  ];
  fs.writeFileSync(reportPath, lines.join("\n"), "utf8");
}

try {
  main();
} catch (err) {
  console.log(`::warning::Content check crashed: ${err.message}`);
}
