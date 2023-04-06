---
type: rule
archivedreason: 
title: Do you refer to images the correct way in ASP .NET?
guid: a304e5ec-11c0-442b-9d8f-74a3f87b3593
uri: do-you-refer-to-images-the-correct-way-in-asp-net
created: 2009-04-28T02:35:45.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: Ryan Tee
  url: https://ssw.com.au/people/ryan-tee
  noimage: true
related: []
redirects: []

---

There are many ways to reference images in ASP.NET. There are two different situations commonly encountered by developers when working with images:   
<!--endintro-->

* **Scenario #1:** Images that are part of the content of a specific page eg. a picture used only on one page
* **Scenario #2:** Images that are shared across on user controls which are shared across different pages in a site eg. a shared logo used across the site (commonly in user controls, or master pages)

Each of these situations requires a different referencing method.

### Option #1:Absolute Paths (Root-Relative Paths)
Often developers reference all images by using an absolute path (prefixing the path with a slash, which refers to the root of the site), as shown below.

```
<img src="/Images/spacer.gif" height="1" width="1">
```
::: bad
Bad example - Referencing images with absolute paths
:::

This has the advantage that &lt;img&gt; tags can easily be copied between pages, however it should not be used in either situation, because it requires that the website have its own site IIS and be placed in the root (not just an application), or that the entire site be in a subfolder on the production web server. For example, the following combinations of URLs are possible with this approach:

| Staging Server URL  | Production Server URL  |
| --- | --- |
| bee:81/   | www.ssw&#46;com.au/  |
| bee/ssw/  | www.ssw&#46;com.au/ssw/  |

As shown above, this approach makes the URLs on the staging server hard to remember, or increases the length of URLs on the production web server.

Verdict for Scenario #1: ![](fail.gif)

Verdict for Scenario #2: ![](fail.gif)

### Option #2:Relative Paths

Images that are part of the content of a page should be referenced using relative paths, e.g.

```
<img src="../Images/spacer.gif" height="1" width="1">
```
::: good
Good example - Referencing images with absolute paths
:::

However, this approach is not possible with images on user controls, because the relative paths will map to the wrong location if the user control is in a different folder to the page.

Verdict for Scenario #1: ![](pass.gif)

Verdict for Scenario #2: ![](fail.gif)

### Option #3:Application-Relative Paths

In order to simplify URLs, ASP.NET introduced a new feature, application relative paths. By placing a tilde (~) in front of a path, a URL can refer to the root of a site, not just the root of the web server. However, this only works on Server Controls (controls with a runat="server" attribute).

To use this feature, you need either use ASP.NET Server controls or HTML Server controls, as shown below.

```
<asp:Image ID="spacerImage" ImageUrl="~/Images/spacer.gif" Runat="server" />
<img id="spacerImage" src="~/Images/spacer.gif" originalAttribute="src" originalPath=""~/Images/spacer.gif"" runat="server">
```
::: good
Good example - Application-relative paths with an ASP.NET Server control
:::

Using an HTML Server control creates less overhead than an ASP.NET Server control, but the control does not dynamically adapt its rendering to the user's browser, or provide such a rich set of server-side features.

Verdict for Scenario #1: ![](fail.gif)

Verdict for Scenario #2: ![](pass.gif)


**Note:** A variation on this approach involves calling the Page.ResolveUrl method with inline code to place the correct path in a non-server tag.

```
<img src='<%# originalAttribute="src" originalPath="'<%#" Page.ResolveUrl("~/Images/spacer.gif") %>'>
```
::: bad
Bad example - Page.ResolveUrl method with a non-server tag
:::

This approach is not recommended, because the data binding will create overhead and affect caching of the page. The inline code is also ugly and does not get compiled, making it easy to accidentally introduce syntax errors.
