---
type: rule
title: Do you use resource file for storing your static script?
uri: do-you-use-resource-file-for-storing-your-static-script
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
  - title: Ryan Tee
    url: https://ssw.com.au/people/ryan-tee
    noimage: true
related: []
redirects: []
created: 2009-05-06T09:48:28.000Z
archivedreason: null
guid: 826a38d4-86e2-4e68-9809-643454ed2f48
---

Resource files provide a structured and centralized approach to storing and retrieving static scripts, eliminating the need for scattered code snippets and enhancing your development workflow. 

<!--endintro-->

```cs
StringBuilder sb = new StringBuilder();
sb.AppendLine(@"<script type=""text/javascript"">");
sb.AppendLine(@"function deleteOwnerRow(rowId)");
sb.AppendLine(@"{");
sb.AppendLine(string.Format(@"{0}.Delete({0}.GetRowFromClientId(rowId));", OwnersGrid.ClientID));
sb.AppendLine(@"}");
sb.AppendLine(@"</script>");
```
::: bad
Bad example - Hard to read, the string is surrounded by rubbish + inefficient because you have an object and 6 strings  
:::


```cs
string.Format(@"
<script type=""text/javascript"">
    function deleteOwnerRow(rowId)
    { 
        {0}.Delete({0}.GetRowFromClientId(rowId)); 
    } 
</script>
", OwnersGrid.ClientID);
```
::: good
Good example Slightly easier to read ?but it is 1 code statement across 10 lines
:::

```cs
string scriptTemplate = Resources.Scripts.DeleteJavascript;
string script = string.Format(scriptTemplate, OwnersGrid.ClientID);
```

```cs
<script type=""text/javascript"">
     function deleteOwnerRow(rowId)
     {
         {0}.Delete({0}.GetRowFromClientId(rowId));
     }
</script>
```

**Figure: The code in the first box, the string in the resource file in the 2nd box. This is the easiest to read + you can localize it eg. If you need to localize an Alert in the javascript**

![Figure: Add a recourse file into your project in VS2005](CreateResource\_small.jpg)  

![Figure: Read value from the new added resource file](ReadResource\_small.jpg)
