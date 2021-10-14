---
type: rule
title: Do you know what to do with a work around?
uri: what-to-do-with-a-work-around
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
related:
  - use-a-signature-with-a-link-when-commenting-on-a-blog
redirects:
  - do-you-know-what-to-do-with-a-work-around
created: 2018-04-30T21:37:19.000Z
archivedreason: null
guid: 6a868928-3104-4ea6-a849-92be86a6cbf3
---
If you have to use a workaround you should always comment your code.

In your code add comments with: 

<!--endintro-->

1. The pain - In the code add a URL to the existing resource your are following 
   e.g. a blog post
2. The potential solution - Search for a suggestion on the product website. If there isn't one, create a suggestion to the product team that points to the resource.
   e.g. on https://uservoice.com/ or https://bettersoftwaresuggestions.com/

::: greybox
"This is a workaround as per the suggestion \[URL]"
:::
**Figure: Always add a URL to the suggestion that you are compensating for**

### Exercise: Understand commenting

You have just added a grid that auto updates, but you need to disable all the timers when you click the edit button. You have found an article on Code Project (http://www.codeproject.com/Articles/39194/Disable-a-timer-at-every-level-of-your-ASP-NET-con.aspx) and you have added the work around.

Now what do you do?

```cs
protected override void OnPreLoad(EventArgs e)
{
     //Fix for pages that allow edit in grids
     this.Controls.ForEach(c =>
     {   
          if (c is System.Web.UI.Timer)
          {
              c.Enabled = false;
          }
     });
     base.OnPreLoad(e);
}
```

**Figure: Work around code in the Page Render looks good. The code is done, something is missing**