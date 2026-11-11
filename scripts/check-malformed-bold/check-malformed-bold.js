import fs from "node:fs";
import path from "node:path";
import process from "node:process";

/**
 * Checks Markdown/MDX content for malformed bold formatting where whitespace
 * has been included immediately inside the `**` markers, e.g.
 *
 *   ** Note:**      -> should be **Note:**
 *   **Note: **      -> should be **Note:**
 *   ** important ** -> should be **important**
 *
 * These are produced when an editor bolds a selection that includes a leading
 * or trailing space. Tina's preview looks fine but the saved Markdown renders
 * incorrectly (the `**` show up as literal characters).
 *
 * If no argument is supplied, all tracked `.md`/`.mdx` files are scanned.
 * A comma-separated list of files can be passed as the first argument (used by CI).
 *
 * Environment variables:
 *   BOLD_REPORT_PATH - If set, writes a Markdown report to this path (used by CI to post PR comments).
 *
 * Detection is deliberately conservative to avoid false positives:
 *   - YAML frontmatter is skipped.
 *   - Fenced code blocks (``` / ~~~) are skipped.
 *   - Inline code (`...`) and escaped characters (`\*`) are masked with a
 *     same-length filler so `**` inside them is never treated as a marker.
 *     This keeps valid bold-wrapping-inline-code such as **`Foo`** from being
 *     flagged.
 */

/* --------------------------------- helpers -------------------------------- */

function findRepoRoot(startDir) {
  let dir = startDir;
  while (dir !== path.dirname(dir)) {
    if (fs.existsSync(path.join(dir, ".git"))) return dir;
    dir = path.dirname(dir);
  }
  return startDir;
}

function walk(dir, acc) {
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    if (entry.name === ".git" || entry.name === "node_modules") continue;
    const full = path.join(dir, entry.name);
    if (entry.isDirectory()) walk(full, acc);
    else if (/\.mdx?$/.test(entry.name)) acc.push(full);
  }
  return acc;
}

/**
 * Return a same-length copy of the line where escaped chars and inline-code
 * spans are replaced by 'X', so `**` inside them is neutralised. Positions are
 * preserved so findings map back to the original line.
 */
function mask(line) {
  const s = [...line];
  const n = s.length;
  // escaped: backslash + next char -> XX
  for (let i = 0; i < n - 1; i++) {
    if (s[i] === "\\") {
      s[i] = "X";
      s[i + 1] = "X";
      i++;
    }
  }
  // inline code: matching backtick runs
  let i = 0;
  while (i < n) {
    if (s[i] === "`") {
      let j = i;
      while (j < n && s[j] === "`") j++;
      const run = j - i;
      let k = j;
      let close = -1;
      while (k < n) {
        if (s[k] === "`") {
          let m = k;
          while (m < n && s[m] === "`") m++;
          if (m - k === run) {
            close = k;
            break;
          }
          k = m;
        } else k++;
      }
      if (close === -1) {
        for (let t = i; t < n; t++) s[t] = "X";
        break;
      }
      for (let t = i; t < close + run; t++) s[t] = "X";
      i = close + run;
    } else i++;
  }
  return s.join("");
}

// A bold span: ** ... ** where the inner text contains no `**`.
const BOLD = /\*\*((?:[^*]|\*(?!\*))+?)\*\*/g;

function findMalformed(line) {
  const masked = mask(line);
  const findings = [];
  let m;
  BOLD.lastIndex = 0;
  while ((m = BOLD.exec(masked)) !== null) {
    const start = m.index;
    const end = start + m[0].length;
    const inner = line.slice(start + 2, end - 2);
    if (inner !== inner.trim()) {
      findings.push({ col: start + 1, text: line.slice(start, end) });
    }
  }
  return findings;
}

function scanFile(file) {
  let text;
  try {
    text = fs.readFileSync(file, "utf8");
  } catch {
    return [];
  }
  const lines = text.split("\n");
  const findings = [];
  let inFence = false;
  let fence = null;
  let inFrontmatter = false;

  for (let idx = 0; idx < lines.length; idx++) {
    const line = lines[idx];
    const trimmedStart = line.replace(/^\s+/, "");

    if (idx === 0 && trimmedStart === "---") {
      inFrontmatter = true;
      continue;
    }
    if (inFrontmatter) {
      if (trimmedStart === "---") inFrontmatter = false;
      continue;
    }

    const fenceMatch = line.match(/^\s*(```+|~~~+)/);
    if (fenceMatch) {
      const marker = fenceMatch[1][0].repeat(3);
      if (!inFence) {
        inFence = true;
        fence = marker;
      } else if (line.trim().startsWith(fence)) {
        inFence = false;
        fence = null;
      }
      continue;
    }
    if (inFence) continue;

    for (const f of findMalformed(line)) {
      findings.push({ line: idx + 1, col: f.col, text: f.text });
    }
  }
  return findings;
}

/* ---------------------------------- main ---------------------------------- */

const repoRoot = findRepoRoot(process.cwd());
const rawArg = process.argv[2] || "";

let files;
if (rawArg.trim()) {
  files = rawArg
    .split(",")
    .map((f) => f.trim())
    .filter(Boolean)
    .filter((f) => /\.mdx?$/.test(f))
    .map((f) => (path.isAbsolute(f) ? f : path.join(repoRoot, f)))
    .filter((f) => fs.existsSync(f));
} else {
  files = walk(repoRoot, []).filter((f) => {
    const rel = path.relative(repoRoot, f);
    return (
      rel.startsWith("public/uploads/rules") ||
      rel.startsWith("categories") ||
      rel.startsWith("homepage") ||
      !rel.includes(path.sep) // top-level .md files (README, etc.)
    );
  });
}

let total = 0;
const report = [];
for (const file of files) {
  const findings = scanFile(file);
  if (findings.length === 0) continue;
  total += findings.length;
  const rel = path.relative(repoRoot, file);
  for (const f of findings) {
    console.log(`${rel}:${f.line}:${f.col}  ${JSON.stringify(f.text)}`);
    report.push(`- \`${rel}:${f.line}\` — \`${f.text}\``);
  }
}

if (process.env.BOLD_REPORT_PATH && report.length) {
  const md = [
    "## :warning: Malformed bold formatting",
    "",
    "Bold markdown must not contain whitespace immediately inside the `**` markers.",
    "",
    "| ❌ Incorrect | ✅ Correct |",
    "| --- | --- |",
    "| `** Note:**` | `**Note:**` |",
    "| `**Note: **` | `**Note:**` |",
    "| `This is ** important **` | `This is **important**` |",
    "",
    "Please fix the following:",
    "",
    ...report,
    "",
  ].join("\n");
  fs.writeFileSync(process.env.BOLD_REPORT_PATH, md);
}

if (total > 0) {
  console.error(
    `\n❌ Found ${total} malformed bold occurrence(s) (whitespace inside ** markers).`
  );
  process.exit(1);
}

console.log("✅ No malformed bold formatting found.");
