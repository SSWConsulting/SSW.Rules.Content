# Category Rule Grouping

## Overview

Categories can now organize rules using headings to improve readability and organization. This feature allows you to group related rules under descriptive headings without modifying the rule titles themselves.

## Benefits

- **Improved readability**: Rules are visually organized into logical groups
- **Reduced noise**: No need for prefixes in rule titles
- **Flexibility**: Rules can appear in multiple categories with different groupings
- **Backward compatible**: Existing flat list format still works

## Format

The `index` field in category frontmatter supports two formats:

### 1. Flat List Format (Traditional)

```yaml
index:
  - rule-uri-one
  - rule-uri-two
  - rule-uri-three
```

### 2. Grouped Format (New)

```yaml
index:
  - heading: Group Name
    rules:
      - rule-uri-one
      - rule-uri-two
  - heading: Another Group
    rules:
      - rule-uri-three
      - rule-uri-four
```

### 3. Mixed Format (Flexible)

You can mix both formats in the same category:

```yaml
index:
  - rule-uri-one
  - heading: Communication
    rules:
      - rule-uri-two
      - rule-uri-three
  - rule-uri-four
  - heading: Teamwork
    rules:
      - rule-uri-five
      - rule-uri-six
```

## Example

Here's a practical example showing how to organize a category with grouped rules:

```yaml
---
type: category
title: Rules to Better Software Consultants - Working in a Team
guid: 99fb319c-14d5-482f-bf74-b851a56cebb0
uri: rules-to-better-software-consultants-working-in-a-team
index:
  - wise-men-improve-rules
  
  - heading: Communication
    rules:
      - professional-integrity
      - are-you-candid-in-your-communication
      - do-you-repeat-back-the-specifics-of-a-request
      - send-done-videos
      - how-to-take-feedback-or-criticism
      - understand-the-power-of-empathy
      - handle-passive-aggressive-comments
      - do-you-ask-questions-where-youre-stuck
      
  - heading: Teamwork
    rules:
      - do-you-manage-up
      - do-you-know-the-5-dysfunctions-of-a-team
      - teamwork-pillars
      - work-in-pairs
      - gather-team-opinions
      
  - heading: Mentoring
    rules:
      - standards-watchdog
      - what-is-mentoring
      - mentoring-programs
      
  - heading: Quality
    rules:
      - go-the-extra-mile
      - quality-do-you-get-your-most-experienced-colleagues-to-check-your-work
      - quality-do-you-implement-an-error-logger-that-has-notifications
      
  - heading: Work Management
    rules:
      - work-in-order-of-importance-aka-priorities
      - 4-quadrants-important-and-urgent
      - do-you-timebox-approval-requests
      - do-you-use-timeboxing-to-avoid-wasted-time
---
```

## Guidelines

1. **Use descriptive headings**: Keep headings short but meaningful (e.g., "Communication", "Teamwork", "Best Practices")
2. **Logical grouping**: Group rules by theme, topic, or workflow
3. **Keep it simple**: Don't over-categorize - aim for 3-7 groups per category
4. **Consistency**: Use similar heading styles across categories when appropriate
5. **Standalone rules**: Rules that don't fit a group can remain ungrouped (as shown with `wise-men-improve-rules` in the example)

## Validation

The frontmatter validator automatically validates both formats. Each grouped entry must have:
- A `heading` field (string)
- A `rules` field (array of rule URIs)

Run validation:
```bash
cd scripts/frontmatter-validator
node frontmatter-validator.js ../../categories/your-category/category-file.md
```

## Migration Strategy

When converting from prefix-based organization to heading-based grouping:

1. **Analyze existing prefixes**: Look at rule titles to identify common prefixes (e.g., "Communication -", "Teamwork -")
2. **Create logical groups**: Convert prefixes into headings
3. **Test the changes**: Run the frontmatter validator to ensure correctness
4. **Consider removing prefixes from rule titles**: This should be done separately as needed

**Note**: This feature only affects how rules are displayed in category pages. Rule titles themselves are not modified by this change.

## Website Rendering

The SSW.Rules website will need to be updated to render these headings. The rendering logic should:
- Display headings as subtle section dividers
- Render grouped rules under their respective headings
- Handle mixed format gracefully
- Maintain the visual hierarchy

See the [SSW.Rules repository](https://github.com/SSWConsulting/SSW.Rules) for implementation details.
