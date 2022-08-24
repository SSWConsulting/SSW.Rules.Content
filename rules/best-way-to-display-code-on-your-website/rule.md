---
type: rule
archivedreason:
title: Do you know the best way to display code on your website?
guid: edf8e58b-33bb-42a9-aa9a-85c1ca6b74d1
uri: best-way-to-display-code-on-your-website
created: 2016-08-05T18:57:08.0000000Z
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
  - do-you-know-the-best-way-to-display-code-on-your-website
---

Any website designer that needs to display code should be aware that there is a very simple method for simply formatting code, and there is a slow and complex method.

The complex method requires formatting each line with HTML tags (such as &lt;br&gt; and &nbsp;) to ensure the code looks nice and pretty.

The simpler method uses &lt;pre&gt; tags. Pre (standing for "preformatted") means that the code is formatted exactly as it is written in the HTML window. This means the page designer can format code in a very simple fashion, without worrying about tags.

<!--endintro-->

**Note:**  &lt;code&gt; tags should not be used because they only provide the font Courier - you still have to manually indent all of your code as in the bad code display example below.

```html
<font face="Courier, Times, Arial, Verdana" size="3">
  public class Configuration
  {
    public static string MySetting { get; }
  }
</font>
```

::: bad
Figure: Bad code display example - using &lt;font&gt;  
:::

```html
<code>
  public class Configuration
  {
    public static string MySetting { get; }
  }

</code>
```

::: bad
Figure: Bad code display example - using &lt;code&gt;  
:::

```html
<pre>
  public class Configuration
  {
    public static string MySetting { get; }
  }
</pre>
```
::: good
Figure: Good code display example - using &lt;pre&gt;
:::

**Tip:**  Do not use auto-format (Ctrl-K, Ctrl-F) in Visual Studio when updating page with &lt;pre&gt; tags, or it will destroy all the code formatting. We have made a suggestion to Microsoft to fix this.


