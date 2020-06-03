---
type: rule
title: Do you know what to do with a work around?
uri: do-you-know-what-to-do-with-a-work-around
created: 2018-04-30T21:37:19.0000000Z
authors:
- id: 1
  title: Adam Cogan

---



<span class='intro'> <p>If you have to use a workaround you should always comment your code and reference. You should also make a Suggestion to [Product] if you think it is something that the product should do.<br></p><ol><li>Comment in the code with URL to an existing or new Suggestion</li><li>Create a Suggestion to .NET 3 that points to blog post<br></li></ol> </span>

<p><br></p><p class="ssw15-rteElement-GreyBox">&quot;This is a&#160;workaround&#160;as per the suggestion&#160;<br>&quot;[URL]</p><dd class="ssw15-rteElement-FigureNormal">Figure&#58; Always add a URL to the suggestion that you are compensating for<br></dd><dd class="ssw15-rteElement-FigureNormal"><br></dd><h3 class="ssw15-rteElement-H3">​Exercise&#58; Understand commenting<br></h3><p>You have just added a grid that auto updates, but you need to disable all the timers when you click the edit button. You have found an article on Code Project (http&#58;//www.codeproject.com/Articles/39194/Disable-a-timer-at-every-level-of-your-ASP-NET-con.aspx) and you have added the work around.<br><br>Now what do you do?<br><br></p><p class="ssw15-rteElement-CodeArea">Sub OnPagePreRender(ByVal sender As Object, ByVal e As EventArgs)<br> ' Fix for pages that allow edit in grids<br> Me.FindControls(Of System.Web.UI.Timer).ForEach(Sub (c) c.Enabled = False)<br>End Sub</p><dd class="ssw15-rteElement-FigureNormal">Figure&#58; Work around code in the Page Render</dd><p>​<br></p><br>


