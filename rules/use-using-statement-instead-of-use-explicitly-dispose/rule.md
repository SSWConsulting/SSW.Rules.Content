---
type: rule
archivedreason: 
title: Do you use "using" declaration instead of use explicitly "dispose"?
guid: 5307acc7-e011-4c7e-905d-ae604f32e5be
uri: use-using-statement-instead-of-use-explicitly-dispose
created: 2018-04-26T20:56:47.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
- do-you-use-using-declaration-instead-of-use-explicitly-dispose

---

Don't explicitly use "dispose" to close objects and dispose of them, the "using" statement will do all of them for you. It is another awesome tool that helps reduce coding effort and possible issues. 

<!--endintro-->

```
static int WriteLinesToFile(IEnumerable<string> lines)
{
  // We must declare the variable outside of the using block
  // so that it is in scope to be returned.
  int skippedLines = 0;
  var file = new System.IO.StreamWriter("WriteLines2.txt")
  foreach (string line in lines)
  {
    if (!line.Contains("Second"))
    {
      file.WriteLine(line);
    }
    else
    {
      skippedLines++;
    }
  }
  file.Dispose();
  return skippedLines;
}
```

::: bad
Figure: Bad example of dispose of resources
:::

```
static int WriteLinesToFile(IEnumerable<string> lines)
{
  // We must declare the variable outside of the using block
  // so that it is in scope to be returned.
  int skippedLines = 0;
  using (var file = new System.IO.StreamWriter("WriteLines2.txt"))
  {
    foreach (string line in lines)
    {
      if (!line.Contains("Second"))
      {
        file.WriteLine(line);
      }
      else
      {
        skippedLines++;
      }
    }
  } // file is disposed here
   return skippedLines;
}
```

::: bad
Figure: Bad example of dispose of resources 
:::

```
static int WriteLinesToFile(IEnumerable<string> lines)
{
  using var file = new System.IO.StreamWriter("WriteLines2.txt");
  // Notice how we declare skippedLines after the using statement.
  int skippedLines = 0;
  foreach (string line in lines)
  {
    if (!line.Contains("Second"))
    {
      file.WriteLine(line);
    }
    else
    {
      skippedLines++;
     }
    }
    // Notice how skippedLines is in scope here.
    return skippedLines;
   // file is disposed here
}
```
::: good
Figure: Good example of dispose of resources, using c# 8.0 using declaration  
:::


::: greybox
**Tip: Did you know it is not recommended to dispose HttpClient?**

One last note is regarding disposing of HttpClient.  Yes, HTTPClient does implement IDisposable, however, I do not recommend creating a HttpClient inside a Using block to make a single request. When HttpClient is disposed it causes the underlying connection to be closed also.  This means the next request has to re-open that connection.  You should try and re-use your HttpClient instances.  If the server really does not want you holding open it’s connection then it will send a header to request the connection be closed.
:::
