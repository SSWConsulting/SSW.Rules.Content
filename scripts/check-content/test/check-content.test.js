import { test } from "node:test";
import assert from "node:assert/strict";
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { checkFile, checkTitle, renderReport } from "../check-content.js";

const fixture = path.join(path.dirname(fileURLToPath(import.meta.url)), "fixture.mdx");
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
