# SSW Rules custom MDX

Read this reference before adding or modifying custom MDX in a rule or category. These components and conventions are specific to the SSW.Rules engine.

## Introduction marker

Every rule requires exactly one `<endIntro />` between its introduction and main content:

```md
Explain the pain or context.

<endIntro />

Explain the recommended practice.
```

Category files do not use `<endIntro />`.

## Figures

`boxEmbed`, `imageEmbed`, and `emailEmbed` share these figure fields:

* `figurePrefix="bad"` for a bad example
* `figurePrefix="ok"` for an acceptable but imperfect example
* `figurePrefix="good"` for a recommended example
* `figurePrefix="none"` for a neutral figure
* `figure` for a concise, descriptive caption

Use a meaningful `figure` caption for every image and example box.

## Boxes

```md
<boxEmbed
  style="greybox"
  body={<>
    Content can include **Markdown** and other supported embeds.
  </>}
  figurePrefix="good"
  figure="Good example - The recommendation is easy to identify"
/>
```

Supported `style` values:

* `greybox`
* `info`
* `warning`
* `tips`
* `highlight`
* `china`
* `codeauditor`
* `yakshaver`
* `todo`

## Images

Store an image beside its rule and reference it from the public root:

```md
<imageEmbed
  src="/uploads/rules/rule-uri/descriptive-image-name.png"
  alt="Describe the meaningful content of the image"
  size="large"
  showBorder={true}
  figurePrefix="good"
  figure="Good example - The important result is visible"
/>
```

Supported `size` values are `small`, `medium`, and `large`. Use lowercase file extensions and descriptive alternative text. Use `<imageEmbed>` rather than Markdown image syntax.

## Email examples

```md
<emailEmbed
  from="sender@example.com"
  to="recipient@example.com"
  cc=""
  bcc=""
  subject="Descriptive subject"
  shouldDisplayBody={true}
  body={<>
    Hi {{ NAME }},

    Keep the message concise and actionable.
  </>}
  figurePrefix="good"
  figure="Good example - The email has a clear purpose"
/>
```

`cc` and `bcc` are optional. Keep literal placeholders such as `{{ NAME }}` inside fenced code when possible; otherwise the MDX checker converts them to safe entities. Literal angle-bracketed text inside an email body must use `&lt;` and `&gt;` so MDX does not interpret it as JSX.

## YouTube videos

```md
<youtubeEmbed
  url="https://www.youtube.com/watch?v=VIDEO_ID"
  description={"Video: Descriptive title (5 min)"}
/>
```

`url` accepts a standard YouTube URL, embed URL, Shorts URL, `youtu.be` URL, or 11-character video ID. Include the title and duration in `description`.

## Highlights

SSW.Rules supports:

```md
==Highlighted text==

==red:Critical highlighted text==
```

Yellow is the default. `red` is the other supported named color.

## MDX pitfalls

* Wrap rich component content in `body={<> ... </>}`.
* Raw braces in prose are parsed as MDX expressions. Escape them or put the text in inline/fenced code.
* Do not place Markdown lists inside blockquotes; use plain text bullets if the quoted material requires them.
* Specify a language on fenced code blocks.
* Run `scripts/check-mdx/check-mdx.js` after editing custom MDX.
