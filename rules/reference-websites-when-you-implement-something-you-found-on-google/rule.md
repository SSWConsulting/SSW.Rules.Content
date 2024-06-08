---
type: rule
title: Do you reference websites when you implement something you found on Google?
uri: reference-websites-when-you-implement-something-you-found-on-google
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
  - do-you-reference-websites-when-you-implement-something-you-found-on-google
created: 2018-04-26T22:18:56.000Z
archivedreason: null
guid: 1f721330-54cd-4d93-93c8-a38ca5874026
---
If you end up using someone else's code, or even idea, that you found online, make sure you add a reference to this in your source code. There is a good chance that you or your team will revisit the website. And of course, it never hurts to tip your hat, to thank other coders.

<!--endintro-->

```csharp
private void HideToSystemTray()
{
       // Hide the windows form in the system tray
       if (FormWindowState.Minimized == WindowState)
       { 
              Hide();
       } 
}
```

::: bad
Bad example - The website where the solution was found IS NOT referenced in the comments
:::

```csharp
private void HideToSystemTray()
{
       // Hide the windows form in the system tray
       // I found this solution at http://www.developer.com/net/csharp/article.php/3336751
       if (FormWindowState.Minimized == WindowState)
       { 
              Hide();
       } 
}
```

::: good
Good example - The website where the solution was found is referenced in the comments
:::
