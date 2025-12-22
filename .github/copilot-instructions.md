# SSW Rules Content - Copilot Instructions

This repository contains SSW's technical rules and best practices. When working with markdown files in this repository, you have access to several custom markdown extensions and features beyond standard markdown.

## Concepts for Writing Rules

When writing SSW Rules, follow these core principles to create effective, practical documentation:

1. **Show the pain** - Usually in the intro, explain the problem and context around why that rule exists. Help readers understand the motivation before presenting the solution.

2. **Give good and bad examples** - Include practical examples for people to better understand the concepts. [Using images is usually the best way to go](/use-images-to-replace-words). Show what NOT to do (bad example) versus what TO do (good example).

3. **Explain the why, not the how** - A rule isn't a place to document how to use a 3rd party product. Focus on the reasons **why** we do something, then link to external documentation on **how** to do something.

### Examples of Well-Structured Rules

See these examples that follow the structure of good/bad examples and link to external documentation:

* [GitHub Issues - Do you use Issue Templates?](/github-issue-templates)
* [Bicep - Do you use User-defined Data Types?](/bicep-user-defined-data-types)
* [Do you know how to backup data on SQL Azure?](/do-you-know-how-to-backup-data-on-sql-azure)

## Custom Markdown Extensions

### Box Components (boxEmbed)

The SSW Rules platform uses MDX `<boxEmbed>` components to create styled boxes for different types of content.

#### Basic Syntax

```md
<boxEmbed
  style="greybox"
  body={<>
    Content here
  </>}
  figurePrefix="none"
  figure="Optional caption text"
/>
```

#### Available Box Styles

**Good/Bad/OK Examples:**

```md
<boxEmbed
  style="greybox"
  body={<>
    This shows what not to do
  </>}
  figurePrefix="bad"
  figure="Bad example - Description"
/>

<boxEmbed
  style="greybox"
  body={<>
    This shows the recommended approach
  </>}
  figurePrefix="good"
  figure="Good example - Description"
/>

<boxEmbed
  style="greybox"
  body={<>
    This is acceptable but not ideal
  </>}
  figurePrefix="ok"
  figure="OK example - Description"
/>
```

**Information Boxes:**

```md
<boxEmbed
  style="greybox"
  body={<>
    This is a greybox - typically used for code examples or quotes
  </>}
  figurePrefix="none"
  figure=""
/>

<boxEmbed
  style="info"
  body={<>
    This is an information box. Use for additional context or tips.
  </>}
  figurePrefix="none"
  figure=""
/>

<boxEmbed
  style="highlight"
  body={<>
    This is a highlight box - use to draw attention to important content
  </>}
  figurePrefix="none"
  figure=""
/>
```

**Special Purpose Boxes:**

```md
<boxEmbed
  style="china"
  body={<>
    China-specific content or variations
  </>}
  figurePrefix="none"
  figure=""
/>

<boxEmbed
  style="codeauditor"
  body={<>
    SSW Code Auditor related content
  </>}
  figurePrefix="none"
  figure=""
/>

<boxEmbed
  style="todo"
  body={<>
    Content that needs to be completed or updated
  </>}
  figurePrefix="none"
  figure=""
/>
```

**Parameters:**
- `style`: Box type (greybox, info, highlight, china, codeauditor, todo)
- `body`: Content wrapped in `{<> ... </>}`
- `figurePrefix`: Caption prefix (bad, ok, good, none)
- `figure`: Caption text

### Image Components (imageEmbed)

Use MDX `<imageEmbed>` components for all images in rules.

#### Basic Syntax

```md
<imageEmbed
  alt="Descriptive alt text"
  size="large"
  showBorder={true}
  figurePrefix="none"
  figure="Caption text describing the image"
  src="/uploads/rules/rule-name/image-file.jpg"
/>
```

#### Size Options

- `small` - Small images (400px width, full screen on mobile)
- `medium` - Medium images
- `large` - Large images (default, full width)

#### Figure Prefix Options

Use `figurePrefix` to add visual indicators:

```md
<imageEmbed
  alt="Bad example screenshot"
  size="large"
  showBorder={true}
  figurePrefix="bad"
  figure="Bad example - Description of why this is wrong"
  src="/uploads/rules/rule-name/bad-example.jpg"
/>

<imageEmbed
  alt="OK example screenshot"
  size="large"
  showBorder={true}
  figurePrefix="ok"
  figure="OK example - This is acceptable but not ideal"
  src="/uploads/rules/rule-name/ok-example.jpg"
/>

<imageEmbed
  alt="Good example screenshot"
  size="large"
  showBorder={true}
  figurePrefix="good"
  figure="Good example - This shows the recommended approach"
  src="/uploads/rules/rule-name/good-example.jpg"
/>

<imageEmbed
  alt="Regular image"
  size="large"
  showBorder={true}
  figurePrefix="none"
  figure="Regular caption without prefix"
  src="/uploads/rules/rule-name/image.jpg"
/>
```

#### Border Option

Set `showBorder={false}` for images that don't need borders (e.g., screenshots with their own borders):

```md
<imageEmbed
  alt="Screenshot"
  size="large"
  showBorder={false}
  figurePrefix="none"
  figure="Screenshot without border"
  src="/uploads/rules/rule-name/screenshot.jpg"
/>
```

**Parameters:**
- `alt`: Descriptive alt text (required for accessibility)
- `size`: small, medium, or large
- `showBorder`: true or false
- `figurePrefix`: bad, ok, good, or none
- `figure`: Caption text
- `src`: Image path (relative to public folder)

### Code Blocks

Use language-specific syntax highlighting for all code blocks. Always specify the language after the opening backticks for proper syntax highlighting.

**Important:** See [Markdown – Do you set the language on code blocks?](/set-language-on-code-blocks) for more details.

#### Basic Syntax

````markdown
```javascript
// JavaScript code example
let iceCream = "chocolate";
if (iceCream === "chocolate") {
  alert("Yay, I love chocolate ice cream!");
}
```

```csharp
// C# code example
public class Example
{
    public void Method() { }
}
```

```powershell
# PowerShell example
Get-Process | Where-Object { $_.Name -eq "chrome" }
```

```sql
-- SQL example
SELECT * FROM Users WHERE IsActive = 1
```
````

**Figure: Always specify the language for syntax highlighting**

#### Inline Code

For inline code, wrap text with single backticks:

```markdown
Use the `getElementById()` method to select elements.
```

#### Supported Languages

See this [json file](https://unpkg.com/gatsby-remark-vscode@1.0.3/lib/grammars/manifest.json) for all supported languages and their aliases.

Common languages: `javascript`, `typescript`, `csharp` (or `cs`), `python`, `sql`, `powershell`, `bash`, `json`, `yaml`, `markdown`, `html`, `css`, `xml`

### Text Decorations

Use standard Markdown syntax for text formatting:

```markdown
_This text will be italic._

**And this text will be bold.**

~~strikethrough.~~

_You **can** combine them_.

==These words== will be highlighted.
```

**Figure: Markdown text decoration syntax**

**Output:**

_This text will be italic._

**And this text will be bold.**

~~strikethrough.~~

_You **can** combine them_.

==These words== will be highlighted.

**Best practices:**
- Use **bold** for emphasis and important terms
- Use _italic_ for subtle emphasis or when introducing new terms
- Use ~~strikethrough~~ to show deprecated or removed items
- Use ==highlight== sparingly for critical information

### Tables

Use Markdown table syntax with alignment options.

#### Basic Syntax

```markdown
| Tables        |      Are      |   Cool |
| ------------- | :-----------: | -----: |
| col 3 is      | right-aligned | \$1600 |
| col 2 is      |   centered    |   \$12 |
| zebra stripes |   are neat    |    \$1 |
```

**Figure: Markdown table with alignment**

#### Alignment

- Left-aligned: `| ----- |` (default)
- Center-aligned: `| :---: |`
- Right-aligned: `| ----: |`

#### Example Output

| Tables        |      Are      |   Cool |
| ------------- | :-----------: | -----: |
| col 3 is      | right-aligned | \$1600 |
| col 2 is      |   centered    |   \$12 |
| zebra stripes |   are neat    |    \$1 |

#### Tables with Formatting

You can use inline formatting within table cells:

| Markdown | Less      | Pretty     |
| -------- | --------- | ---------- |
| _Still_  | `renders` | **nicely** |
| 1        | 2         | 3          |

### Video Embeds (youtubeEmbed)

Use the MDX `<youtubeEmbed>` component for embedding YouTube videos.

#### Basic Syntax

```md
<youtubeEmbed 
  url="https://www.youtube.com/embed/VIDEO_ID" 
  description={"Video: Title of the video (duration)"} 
/>
```

#### Example

```md
<youtubeEmbed 
  url="https://www.youtube.com/embed/0ugMkda9IBw" 
  description={"Video: Top 5 Reasons Why ASP.NET MVC is Great (3 min)"} 
/>
```

**Note:** Always include the video duration in the description to help users decide if they have time to watch it.

### Email Templates (emailEmbed)

Use the MDX `<emailEmbed>` component to display email templates in rules.

#### Basic Syntax

```md
<emailEmbed
  from=""
  to="XXX"
  cc="YYY"
  bcc="ZZZ"
  subject="{{ EMAIL SUBJECT }}"
  shouldDisplayBody={true}
  body={<>
    ## Hi XXX,

    {{ EMAIL CONTENT }}
  </>}
  figurePrefix="good"
  figure="Good example - Nice email template"
/>
```

#### Parameters

- `from`: Sender email (optional, leave empty if not needed)
- `to`: Recipient(s)
- `cc`: CC recipient(s) (optional)
- `bcc`: BCC recipient(s) (optional)
- `subject`: Email subject line
- `shouldDisplayBody`: true to show body, false to hide
- `body`: Email content wrapped in `{<> ... </>}`, supports Markdown
- `figurePrefix`: bad, ok, good, or none
- `figure`: Caption text

#### Example Use Cases

**Good email example:**
```md
<emailEmbed
  from=""
  to="client@company.com"
  subject="Sprint Review - Ready for your feedback"
  shouldDisplayBody={true}
  body={<>
    Hi John,

    The Sprint Review is ready for your feedback...
  </>}
  figurePrefix="good"
  figure="Good example - Clear subject and concise message"
/>
```

**Bad email example:**
```md
<emailEmbed
  from=""
  to="client@company.com"
  subject="Update"
  shouldDisplayBody={true}
  body={<>
    Here's the update you asked for...
  </>}
  figurePrefix="bad"
  figure="Bad example - Vague subject line"
/>
```

## Rule Structure

Every rule must have frontmatter at the top. After the intro, include `<endIntro />` to signal the end of the introduction section.

### Frontmatter format

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

#### Field Descriptions

**Required fields:**
- `type`: Always "rule"
- `title`: Question format (e.g., "Do you use Cocona for building great command line tools in .NET?")
- `guid`: Unique UUID identifier
- `uri`: Short, kebab-case identifier for the URL
- `created`: Creation timestamp in ISO 8601 format
- `authors`: Array of author objects with title and url

**Optional fields:**
- `archivedreason`: Reason for archiving (null or empty if not archived)
- `seoDescription`: SEO meta description
- `related`: Array of related rule URIs (not full paths)
- `categories`: Array of category objects with full file paths (e.g., "categories/folder/file.mdx")
- `sidebarVideo`: YouTube Shorts URL for sidebar video

**System-managed fields** (auto-updated by the system):
- `createdBy`, `createdByEmail`: Original creator information
- `isArchived`: Boolean archive status
- `lastUpdated`, `lastUpdatedBy`, `lastUpdatedByEmail`: Last update metadata

**Note:** 
- `related` uses rule URIs only (e.g., "rule-name")
- `categories` uses full file paths (e.g., "categories/communication/rules-to-better-technical-documentation.mdx")

## Best Practices for SSW Rules

1. **Use good/bad examples** - Always show what not to do vs. what to do using `figurePrefix="bad"` and `figurePrefix="good"`
2. **Include figure captions** - Every image, code block, and box should have a descriptive caption using the `figure` parameter
3. **Be specific** - Use concrete examples rather than abstract concepts
4. **Reference other rules** - Link to related rules to create a knowledge web
5. **Keep it practical** - Focus on actionable advice developers can implement
6. **Use proper heading hierarchy** - Never use Heading 1 (\<h1\>) in content. The page title already uses \<h1\>, and adding more can harm accessibility. Start with Heading 2 (##) and maintain proper hierarchy. See [MDN guidelines - avoid multiple \<h1\> elements](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/Heading_Elements#avoid_using_multiple_h1_elements_on_one_page)
7. **Emphasize headings** - Use **bold** text in headings to emphasize key concepts (e.g., "## This is a heading with some **emphasized text**")

### Figure Captions Best Practices

Always include descriptive captions on images and boxes using the `figure` parameter:

**For images:**
```md
<imageEmbed
  alt="Screenshot"
  size="large"
  showBorder={true}
  figurePrefix="good"
  figure="Good example - Clear description of why this approach is recommended"
  src="/uploads/rules/rule-name/image.jpg"
/>
```

**For boxes:**
```md
<boxEmbed
  style="greybox"
  body={<>
    Code example here
  </>}
  figurePrefix="none"
  figure="Figure: Descriptive caption explaining what this code does"
/>
```

**Caption prefix options:**
- `figurePrefix="bad"` - Adds ❌ for bad examples
- `figurePrefix="ok"` - Adds 😐 for acceptable but not ideal examples  
- `figurePrefix="good"` - Adds ✅ for recommended examples
- `figurePrefix="none"` - Regular caption without prefix

### Links and References

* Internal rule links: `[Rule title](/rule-uri)` (always use relative links for other rules)
* External links: `[Link text](https://example.com)`
* Always use descriptive link text, never "click here" or "read more"

## Content Guidelines

* Write in present tense
* Use active voice
* Neutral, impersonal (third-person) style (company-agnostic/objective)
* Be concise but comprehensive
* Include practical examples
* Use consistent terminology across rules
* Follow the SSW tone of voice (professional but approachable)
* Rule titles are always questions e.g. "Do you use Cocona for building great command line tools in .NET?"

## File Organization

* Rules go in `/rules/rule-name/rule.md`
* Categories go in `/categories/category-name.md`
* Images go next to the rule markdown file
* Use kebab-case for file and folder names

## Adding Rules to Categories

Every rule should belong to at least one category to help users discover related content. Categories are organized in the `/categories` folder and structured by topic.

### Category Structure

Category files are markdown files with a `type: category` frontmatter. They contain an `index` array that lists the URIs of all rules in that category:

```yaml
---
type: category
title: Rules to Better Technical Documentation
guid: 961f2035-1540-4425-9b29-0d6273ac0726
uri: rules-to-better-technical-documentation
index:
  - rule-uri-1
  - rule-uri-2
  - making-last-edited-clear
---
```

### How to Add a Rule to a Category

1. **Find the right category folder**: Categories are organized in folders like:
   * `/categories/communication/` - Communication, documentation, presentations
   * `/categories/software-engineering/` - Software development practices
   * `/categories/project-delivery/` - Project management, delivery processes
   * `/categories/design/` - Design and UX guidelines
   * `/categories/marketing-and-video/` - Marketing and video content
   * `/categories/artificial-intelligence/` - AI and machine learning
   * `/categories/infrastructure-and-networking/` - Infrastructure and networking
   * `/categories/client-engagement/` - Client relationships and sales
   * `/categories/company-operations/` - Internal operations
   * `/categories/others/` - Miscellaneous rules

2. **Choose the most relevant category file**: Browse the category files in the appropriate folder. For example:
   * Documentation rules → `/categories/communication/rules-to-better-technical-documentation.md`
   * Testing rules → `/categories/software-engineering/rules-to-better-unit-tests.md`
   * Meeting rules → `/categories/communication/rules-to-better-meetings.md`

3. **Add the rule URI to the index**: Open the category file and add the rule's URI (from the rule's frontmatter) to the `index` array. Typically add it at the end of the list.

4. **Validate**: Run the frontmatter validator to ensure the category file is still valid:

   ```bash
   cd scripts/frontmatter-validator
   npm install
   node frontmatter-validator.js ../../categories/[folder]/[category-file].md
   ```

### Quick Reference

When asked to "add this rule to a category":

1. Look at the rule's topic and content
2. Navigate to `/categories/[appropriate-folder]/`
3. Find or choose the best matching category file
4. Add the rule's URI to the `index` array in that category file
5. Validate with the frontmatter validator
