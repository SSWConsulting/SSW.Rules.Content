---
type: rule
archivedreason: 
title: Do you know how to share a touch of code?
guid: e92c844c-fa4d-48e1-bf11-cde61f4dd6ee
uri: do-you-know-how-to-share-a-touch-of-code
created: 2015-12-03T05:44:57.0000000Z
authors:
- title: Chris Briggs
  url: https://ssw.com.au/people/chris-briggs
related: []
redirects: []

---

Any regular blogger who writes about code knows that embedding code snippets into their posts can be a real pain!

Syntax highlighting, special tags and keeping a track of your code snippets can be a nightmare. As a developer, you're sold on the virtues of source control, making changes then rolling back, forking, and cloning code. Wouldn't it be great if there were a simple way to share a touch of code?

<!--endintro-->


::: bad  
![Figure - Using images for code snippets is difficult to maintain.](2014-03-08\_19-49-571.png)  
:::

Introducing Github Gists, which makes sharing, embedding and keeping track of code snippets easy. The standout feature of Github Gists is that every code snippet (often referred to by GitHub as a Gist) is behind the scenes a Git repository, which in turn gives you access to all of the benefits of source control.

Upon editing an already published Gist, the previous versions are preserved. As to be expected with any good source control, you can use the built-in diff engine to highlight clearly the changes between any two versions of a single Gist. This sounds like it can get out of hand quickly, but you can easily view all your Gists by heading to https://gist.github.com/&lt;username&gt;/.


::: good  
![Figure - Easy to review your Gists.](2015-12-03\_15-46-34.png)  
:::

It is very simple to embed your code snippets using Github Gists, as you can embed any Gist in your blog with a single a line of JavaScript. The embedded Gists automatically display the current version of your snippet while still maintaining all the formatting and syntax highlighting. Furthermore, if you're using WordPress, it's even easier. Click here to find out all of the shortcuts for embedding Gists in WordPress! blogs.


::: good  
![Figure - Embeded Gist with JavaScript provided by Github](2015-12-03\_15-50-42.png)  
:::
