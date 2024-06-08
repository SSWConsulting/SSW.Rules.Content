---
type: rule
title: Do you use Bundling to package script and css files?
uri: do-you-use-bundling-to-package-script-and-css-files
authors:
  - title: Damian Brady
    url: https://ssw.com.au/people/damian-brady
related: []
redirects: []
created: 2013-03-08T14:33:01.000Z
archivedreason: null
guid: d37d8c4d-b868-4124-93f7-a212d11ed390
---

ASP.NET provides a great way to compress and package multiple script files or multiple css files. Bundling multiple files together results in fewer requests from the client and smaller payloads which leads to much faster render times.

<!--endintro-->

Rather than link to each script or css file individually, use bundling to group many together and get the advantages of minification and versioning out of the box.

```html
<link rel="stylesheet" href="~/Content/themes/base/jquery.ui.core.css" />
<link rel="stylesheet" href="~/Content/themes/base/jquery.ui.resizable.css" />
<link rel="stylesheet" href="~/Content/themes/base/jquery.ui.selectable.css" />
<link rel="stylesheet" href="~/Content/themes/base/jquery.ui.accordion.css" />
<link rel="stylesheet" href="~/Content/themes/base/jquery.ui.autocomplete.css" />
<link rel="stylesheet" href="~/Content/themes/base/jquery.ui.button.css" />
<link rel="stylesheet" href="~/Content/themes/base/jquery.ui.dialog.css" />
<link rel="stylesheet" href="~/Content/themes/base/jquery.ui.slider.css" />
<link rel="stylesheet" href="~/Content/themes/base/jquery.ui.tabs.css" />
<link rel="stylesheet" href="~/Content/themes/base/jquery.ui.datepicker.css" />
<link rel="stylesheet" href="~/Content/themes/base/jquery.ui.progressbar.css" />
<link rel="stylesheet" href="~/Content/themes/base/jquery.ui.theme.css" />
```
::: bad
Figure: Bad example – each reference will be downloaded separately and won’t be compressed
:::

```cs
Configuration:
public static void RegisterBundles(BundleCollection bundles)
{
        bundles.Add(new StyleBundle("~/Content/themes/base/css").Include(
                "~/Content/themes/base/jquery.ui.core.css",
                "~/Content/themes/base/jquery.ui.resizable.css",
                "~/Content/themes/base/jquery.ui.selectable.css",
                "~/Content/themes/base/jquery.ui.accordion.css",
                "~/Content/themes/base/jquery.ui.autocomplete.css",
                "~/Content/themes/base/jquery.ui.button.css",
                "~/Content/themes/base/jquery.ui.dialog.css",
                "~/Content/themes/base/jquery.ui.slider.css",
                "~/Content/themes/base/jquery.ui.tabs.css",
                "~/Content/themes/base/jquery.ui.datepicker.css",
                "~/Content/themes/base/jquery.ui.progressbar.css",
                "~/Content/themes/base/jquery.ui.theme.css"));
}

View:
@Styles.Render("~/Content/themes/base/css")
```
::: good
Figure: Good example – Define a bundle and render it in the view for maximum performance
:::
