---
type: rule
title: Do you always update the DotNetNuke style sheets to underline a link?
uri: update-the-dotnetnuke-style-sheets-to-underline-a-link
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan/
created: 2014-03-14T03:05:00.000Z
archivedreason: outdated
guid: b26cba54-c155-4418-8766-392d38ea958d
---
As per [rules to underline all links](/underlined-links/) always update the necessary DotNetNuke style sheets to make links perfectly clear, by underlining them.  

<!--endintro-->

To underline links in DotNetNuke you need to change the styles in the style sheet Portals/\_default/default.css 

```css
A:Link
{
    text-decoration: none;
    color: #003366;
}
A:Visited
{
    text-decoration: none;
    color: #003366;                   
}
A:Hover
{
    text-decoration: underline;
    color: #ff0000;
}
A:Active
{
    text-decoration: none;
    color: #003366;
}
```
::: good
Figure: Good example - The style now underline all links
:::
