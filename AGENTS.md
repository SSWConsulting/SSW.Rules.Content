# SSW.Rules.Content - Agent Guidelines

This document provides essential information for AI coding agents working in the SSW.Rules.Content repository.

## Project Overview

This is a **content-only repository** containing SSW's technical rules and best practices. It has no traditional build process - content is written in MDX (Markdown with JSX) and consumed by the [SSW.Rules engine](https://github.com/SSWConsulting/SSW.Rules) which builds it into a static site.

**Structure:**
- `public/uploads/rules/[rule-name]/rule.mdx` - Individual rules with frontmatter
- Top category - `categories/[top-category-folder]/index.mdx`
- `categories/[top-category-folder]/[category-name].mdx` - Category organization
- `scripts/` - Validation and utility scripts (Node.js, Python, C#)
- `.github/workflows/` - CI/CD automation

## Validation Commands

### Validate Frontmatter

```bash
cd scripts/frontmatter-validator
npm install
node frontmatter-validator.js '<comma-separated-files>'
```

**Example:**
```bash
node frontmatter-validator.js 'public/uploads/rules/my-rule/rule.mdx'
```

### Validate Markdown (Linting)

```bash
npm install -g markdownlint-cli
markdownlint <file-paths> --config .markdownlint/config.json
```

**Auto-fix markdown:**
```bash
markdownlint --fix <file-paths> --config .markdownlint/config.json
```

### Check for Unreferenced Images

```bash
cd scripts/find-unreferenced-images
npm install
node find-unreferenced-images.js
```

### Check for Duplicate Images

```bash
cd scripts/rename-duplicate-images
npm install
node rename-duplicate-images.js
```

## Writing Rules

### Frontmatter Structure (YAML)

**Required fields:**
- `type: rule` (always "rule")
- `title:` Question format (e.g., "Do you use TypeScript?")
- `uri:` Short kebab-case identifier for URL (e.g., "use-typescript")
- `guid:` UUID identifier (generate with `uuidgen` or online tool)
- `seoDescription:` Brief SEO-friendly description
- `authors:` Array with `title` and `url` (SSW people URLs)

**Optional fields:**
- `archivedreason:` Reason for archiving (null if not archived)
- `related:` Array of related rule objects with `rule:` key pointing to full path
- `redirects:` Array of old URIs for redirect handling
- `categories:` Array of category objects with full file paths

**Example:**
```yaml
---
type: rule
archivedreason: #empty if not archived (null or empty string)
title:  # e.g. "Do you ....?" (always in question format)
seoDescription:  # A brief description of the rule for search engines
guid:  # Unique identifier for the rule (UUID format)
uri:  # e.g. "cocona-for-command-line-tools", keep short, ensure no conflicts
created:  # e.g. 2025-01-03T00:00:00.000Z (ISO 8601 format)
authors: 
  - title:  # e.g. "Brady Stroud"
    url:  # e.g. "https://www.ssw.com.au/people/brady-stroud"
related: 
  -  # e.g. "provide-list-of-arguments" (rule URIs only)
  -  # e.g. "dependency-injection"
categories:
  - category:  # e.g. "categories/communication/rules-to-better-technical-documentation.mdx" (full path)
  - category:  # Multiple categories allowed
sidebarVideo:  # Optional: e.g. "https://youtube.com/shorts/ak37CjgT_uM?si=Od8VIFMIHjycrygv"
createdBy:  # System-managed: Original creator name (e.g. "Brady Stroud [SSW]")
createdByEmail:  # System-managed: Creator email
isArchived:  # Boolean: true or false
lastUpdated:  # System-managed: Last update timestamp (e.g. 2025-12-04 00:53:15+00:00)
lastUpdatedBy:  # System-managed: Last editor name
lastUpdatedByEmail:  # System-managed: Last editor email
---

{{Rule Markdown content here}}

<endIntro />

{{Rest of the rule content}}
```

### Content Structure

**For Rules (`public/uploads/rules/[rule-name]/rule.mdx`):**
1. **Intro section** - Explain the problem/context
2. **`<endIntro />`** - Marks end of introduction (REQUIRED for rules)
3. **Main content** - Use good/bad examples with MDX components
4. **Links to related rules** - Cross-reference other rules

**For Categories (`categories/[folder]/[category-name].mdx`):**
- Categories do NOT use `<endIntro />` tags
- Only descriptive content in the body (after frontmatter)
- No special intro/content separation needed

### MDX Components

**Box components:**
```md
<boxEmbed
  style="greybox"
  body={<>
    Code or text content here
  </>}
  figurePrefix="good"
  figure="Good example - Description"
/>
```

**Styles:** `greybox`, `info`, `highlight`, `china`, `codeauditor`, `todo`  
**Prefixes:** `bad`, `ok`, `good`, `none`

**Image components:**
```md
<imageEmbed
  alt="Descriptive alt text"
  size="large"
  showBorder={true}
  figurePrefix="good"
  figure="Good example - Clear descriptive caption"
  src="/uploads/rules/rule-name/image-file.jpg"
/>
```

**Email templates:**
```md
<emailEmbed
  from=""
  to="recipient@example.com"
  subject="Subject line"
  shouldDisplayBody={true}
  body={<>
    Email content here
  </>}
  figurePrefix="good"
  figure="Good example - Clear email"
/>
```

**YouTube videos:**
```md
<youtubeEmbed
  url="https://www.youtube.com/embed/VIDEO_ID"
  description={"Video: Title (duration)"}
/>
```

## Code Style Guidelines

### File Organization

- Rule files: `public/uploads/rules/[uri-name]/rule.mdx`
- Images: Store next to rule file in the same folder
- Use **kebab-case** for folder and file names
- Folder name MUST match the `uri` field in frontmatter

### Markdown Best Practices

1. **Headings:** Never use `#` (H1) - page title uses it. Start with `##` (H2)
2. **Heading emphasis:** Use bold for key concepts (e.g., `## This is a **key concept**`)
3. **Code blocks:** Always specify language (e.g., `` ```typescript ``)
4. **Figure captions:** Every image/box needs a descriptive `figure` parameter
5. **Links:** Use relative links for internal rules: `[Rule title](/rule-uri)`
6. **Line length:** No limit (MD013 disabled)
7. **Inline HTML:** Allowed (MD033 disabled) for MDX components

### Writing Style

- Present tense, active voice
- Neutral/impersonal (third-person perspective)
- Company-agnostic and objective
- Concise but comprehensive
- **Show the pain** - Explain WHY before HOW
- **Good/bad examples** - Use `figurePrefix="bad"` and `figurePrefix="good"`
- Focus on "why" not "how" - Link to external docs for implementation details
- Rule titles are ALWAYS questions (e.g., "Do you...?")

## Common Tasks

### Creating a New Rule

1. Create folder: `public/uploads/rules/[uri-name]/`
2. Create file: `rule.mdx` with proper frontmatter
3. Add images to the same folder
4. Validate frontmatter: Run validator script
5. Add rule to appropriate category file(s) in `categories/`

### Adding Rule to Category

1. Find category file in `categories/[folder]/[category-name].mdx`
2. Open category frontmatter
3. Add rule path to `index:` array
4. Validate with frontmatter validator

**Category folders:**
- `communication/` - Documentation, presentations, meetings
- `software-engineering/` - Development practices, code quality
- `project-delivery/` - Project management, Scrum
- `design/` - UX, UI guidelines
- `marketing-and-video/` - Marketing content
- `artificial-intelligence/` - AI/ML practices
- `infrastructure-and-networking/` - DevOps, infrastructure
- `client-engagement/` - Client relationships
- `company-operations/` - Internal operations
- `others/` - Miscellaneous

**Choose the most relevant category file**: Browse the category files in the appropriate folder. For example:
   * Documentation rules → `/categories/communication/rules-to-better-technical-documentation.md`
   * Testing rules → `/categories/software-engineering/rules-to-better-unit-tests.md`
   * Meeting rules → `/categories/communication/rules-to-better-meetings.md`

### Handling Images

- Images go in the rule folder next to `rule.mdx`
- Use descriptive filenames (kebab-case)
- Extensions must be lowercase (`.jpg`, `.png`, `.gif`, `.svg`)
- Always use `<imageEmbed>` component, never plain markdown images
- Include descriptive `alt` text for accessibility

## Validation Rules

### Frontmatter Schema Requirements

**Rules must have:**
- Valid `type: rule`
- Non-empty `title`, `uri`, `guid`, `seoDescription`
- At least one author with valid `title` and `url`
- Valid UUID format for `guid`
- Valid URI reference format for `uri`
- Valid datetime for `created` field

### Markdown Linting

**Disabled rules:**
- MD046 - Code block style (fenced blocks allowed)
- MD013 - Line length (no limit)
- MD033 - Inline HTML (needed for MDX)
- MD036 - Emphasis instead of heading
- MD055 - Table pipe style
- MD024 - Duplicate headings (allowed)

**Enabled rules:**
- MD003 - Heading style must be ATX (`##`)
- MD004 - List style must use asterisks (`*`)

## CI/CD Automation

**On every PR:**
- Frontmatter validation (changed files only)
- Markdown linting with auto-fix
- Image validation
- Folder name consistency check

**On push to main:**
- Full frontmatter validation (all files)
- Deployment trigger to SSW.Rules engine

**Scheduled (weekly):**
- Duplicate image detection and renaming

## Important Notes

- NO package.json in root - this is a content repo
- NO traditional build/test commands - validation only
- Content is consumed by separate build system (SSW.Rules)
- Always run validation scripts before committing
- Folder names auto-sync with `uri` field via GitHub Actions
- Use TinaCMS for visual editing (optional)
- Read `.github/copilot-instructions.md` for detailed MDX component usage

## Resources

- [SSW.Rules Engine](https://github.com/SSWConsulting/SSW.Rules) - The build system
- [Copilot Instructions](.github/copilot-instructions.md) - Detailed component usage
