---
type: rule
title: Do you use resource file for storing your static script?
uri: do-you-use-resource-file-for-storing-your-static-script
created: 2009-05-06T09:48:28.0000000Z
authors:
- id: 1
  title: Adam Cogan
- id: 17
  title: Ryan Tee

---



<span class='intro'> Write&#160;a Intro pragraph here
 </span>


  <h2>&#160;</h2>
<dl class="badCode">
    <dt style="width&#58;92.31%;height&#58;190px;">
    <pre>     StringBuilder sb = new StringBuilder();<br>     sb.AppendLine(@&quot;&lt;script type=&quot;&quot;text/javascript&quot;&quot;&gt;&quot;);<br>     sb.AppendLine(@&quot;function deleteOwnerRow(rowId)&quot;);<br>     sb.AppendLine(@&quot;&#123;&quot;);<br>     sb.AppendLine(string.Format(@&quot;&#123;0&#125;.Delete(&#123;0&#125;.<br>        GetRowFromClientId(rowId));&quot;, OwnersGrid.ClientID));<br>     sb.AppendLine(@&quot;&#125;&quot;);<br>     sb.AppendLine(@&quot;&lt;/script&gt;&quot;); </pre>
    </dt>
    <dd>Bad example - Hard to read ?the string is surrounded by rubbish + inefficient because you have an object and 6 strings</dd>
</dl>
<p>&#160;</p>
<dl class="goodCode">
    <dt style="width&#58;93.08%;height&#58;100px;">
    <pre>     string.Format(@&quot;&lt;script type=&quot;&quot;text/javascript&quot;&quot;&gt;                  <br>       function deleteOwnerRow(rowId)                    <br>      &#123; &#123;0&#125;.Delete(&#123;0&#125;.GetRowFromClientId(rowId)); &#125; &lt;/script&gt; &quot;, <br>       OwnersGrid.ClientID);                                    </pre>
    </dt>
    <dd>Good example Slightly easier to read ?but it is 1 code statement across 10 lines</dd>
</dl>
<dl class="goodCode">
    <dt style="width&#58;92.33%;height&#58;86px;">
    <pre>     string scriptTemplate = Resources.Scripts.DeleteJavascript;<br>     string script = string.Format(scriptTemplate, OwnersGrid.ClientID); </pre>
    </dt>
</dl>
<dl class="goodCode">
    <dt style="width&#58;91.4%;height&#58;161px;">
    <pre>     &lt;script type=&quot;&quot;text/javascript&quot;&quot;&gt;<br>     function deleteOwnerRow(rowId)<br>     &#123;<br>            &#123;0&#125;.Delete(&#123;0&#125;.GetRowFromClientId(rowId));<br>     &#125;<br>     &lt;/script&gt; </pre>
    </dt>
</dl>
<p><b>Figure&#58; The code in the first box, the string in the resource file in the 2nd box. This is the easiest to read + you can localize it eg. If you need to localize an Alert in the javascript</b></p>
<dl class="image">
    <dt><img style="border-bottom&#58;0px solid;border-left&#58;0px solid;border-top&#58;0px solid;border-right&#58;0px solid;" border="0" alt="Create a Resource file" src="/PublishingImages/CreateResource_small.jpg" /> </dt>
    <dd>Figure&#58; Add a recourse file into your project in VS2005</dd>
</dl>
<dl class="image">
    <dt><img style="border-bottom&#58;0px solid;border-left&#58;0px solid;border-top&#58;0px solid;border-right&#58;0px solid;" border="0" alt="Create a Resource file" src="/PublishingImages/ReadResource_small.jpg" /> </dt>
    <dd>Figure&#58; Read value from the new added resource file</dd>
</dl>



