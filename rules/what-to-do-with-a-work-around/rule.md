---
type: rule
archivedreason: 
title: Do you know what to do with a work around?
guid: 6a868928-3104-4ea6-a849-92be86a6cbf3
uri: what-to-do-with-a-work-around
created: 2018-04-30T21:37:19.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
- do-you-know-what-to-do-with-a-work-around

---

If you have to use a workaround you should always comment your code and reference. You should also make a Suggestion to [Product] if you think it is something that the product should do.

1. Comment in the code with URL to an existing or new Suggestion
2. Create a Suggestion to [Product] that points to blog post


<!--endintro-->




::: greybox
"This is a workaround as per the suggestion [URL]  
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


 **Figure: Work around code in the Page Render**
