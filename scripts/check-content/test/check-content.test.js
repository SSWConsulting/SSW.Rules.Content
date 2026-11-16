import { test } from "node:test";
import assert from "node:assert/strict";
import fs from "node:fs";
import path from "node:path";
import os from "node:os";
import { execFileSync, spawnSync } from "node:child_process";
import { fileURLToPath } from "node:url";
import { checkFile, checkTitle, renderReport } from "../check-content.js";

const testDir = path.dirname(fileURLToPath(import.meta.url));
const fixture = path.join(testDir, "fixture.mdx");
const script = path.join(testDir, "..", "check-content.js");
const issues = checkFile(fixture);
const noWarnLine = fs.readFileSync(fixture, "utf8").split("\n").indexOf("## Should NOT warn") + 1;
const count = (check) => issues.filter((i) => i.check === check).length;

test("flags every planted problem", () => {
  assert.deepEqual(
    {
      title: count("title"),
      heading: count("heading"),
      listFullStop: count("listFullStop"),
      captionFullStop: count("captionFullStop"),
      urlEnding: count("urlEnding"),
      longNumber: count("longNumber"),
      linkText: count("linkText"),
      language: count("language"),
    },
    { title: 2, heading: 2, listFullStop: 3, captionFullStop: 2, urlEnding: 2, longNumber: 4, linkText: 1, language: 10 },
  );
});

test("skips code, greyboxes, emails, mentions, years and spaced phone numbers", () => {
  const leaked = issues.filter((i) => i.line >= noWarnLine && !(i.check === "captionFullStop"));
  assert.deepEqual(leaked, []);
});

test("checks rule titles", () => {
  // Valid, including names later in the title
  assert.deepEqual(checkTitle("Do you have a war room?"), []);
  assert.deepEqual(checkTitle("Scrum - Do you use Azure Test Plans?"), []);
  // A capitalised word right after "Do you"
  assert.match(checkTitle("Do you Disable AD Users?")[0], /write "disable" not "Disable"/);
  assert.match(checkTitle("Printers - Do you Code-Sign your apps?")[0], /write "code-sign" not "Code-Sign"/);
  // Still checked when the title has other problems
  assert.equal(checkTitle("Do you Configure the build").length, 2);
});

test("a renamed rule only counts its edited lines as changed", () => {
  const dir = fs.mkdtempSync(path.join(os.tmpdir(), "check-content-"));
  const git = (...args) => execFileSync("git", ["-c", "user.name=t", "-c", "user.email=t@t", ...args], { cwd: dir });
  const body = ["---", "title: Do you test?", "---", "", ...Array.from({ length: 20 }, (_, i) => `- Item ${i}.`), ""];
  fs.mkdirSync(path.join(dir, "old-name"));
  fs.writeFileSync(path.join(dir, "old-name/rule.mdx"), body.join("\n"));
  git("init", "-q", "-b", "main");
  git("add", ".");
  git("commit", "-qm", "base");
  git("mv", "old-name", "new-name");
  body[10] = "- Edited item.";
  fs.writeFileSync(path.join(dir, "new-name/rule.mdx"), body.join("\n"));
  git("commit", "-qam", "rename");

  const out = execFileSync("node", [script, "--base", "HEAD~1", "new-name/rule.mdx"], { cwd: dir, encoding: "utf8" });
  assert.match(out, /new-name\/rule\.mdx: 1 in changed lines, 19 existing/);
  fs.rmSync(dir, { recursive: true, force: true });
});

test("reads paths from a file and fails on a crash", () => {
  const dir = fs.mkdtempSync(path.join(os.tmpdir(), "check-content-"));
  const rule = path.join(dir, "rule.mdx");
  fs.copyFileSync(fixture, rule);
  fs.writeFileSync(path.join(dir, "list.txt"), `${rule}\n`);
  const ok = spawnSync("node", [script, "--files-from", path.join(dir, "list.txt")], { encoding: "utf8" });
  assert.equal(ok.status, 0);
  assert.match(ok.stdout, /rule\.mdx: \d+ in changed lines/);
  fs.rmSync(dir, { recursive: true, force: true });

  const crash = spawnSync("node", [script, "--files-from", "/does/not/exist.txt"], { encoding: "utf8" });
  assert.equal(crash.status, 1);
  assert.match(crash.stdout, /Content check crashed/);
});

test("suggests spaces for phone numbers", () => {
  const phones = issues.filter((i) => i.check === "longNumber" && i.msg.includes("spaces"));
  assert.equal(phones.length, 2);
});

test("keeps the report under GitHub's comment limit", () => {
  const old = Array.from({ length: 2000 }, (_, i) => ({ line: i + 1, check: "listFullStop", msg: "List item ends with a full stop" }));
  const report = renderReport([{ file: "public/uploads/rules/x/rule.mdx", mine: old.slice(0, 3), old }]);
  assert.ok(report.length <= 60000, `report is ${report.length} chars`);
  assert.match(report, /…and \d+ more/);
  assert.match(report, /⚠️ 3 warning\(s\)/);
});
