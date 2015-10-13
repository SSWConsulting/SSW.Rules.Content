---
type: rule
title: Do you have a favicon in your webpage?
uri: do-you-have-a-favicon-in-your-webpage
created: 2015-10-13T00:47:56.0000000Z
authors:
- id: 1
  title: Adam Cogan
- id: 16
  title: Tiago Araujo

---



<span class='intro'> <p>A Favicon is a small image file included on professional developed sites. The favicon reflects the look and feel of the web site or the organizations visual identity.</p> </span>

<dl class="badImage"><dt><img src="/PublishingImages/favicon-bad.jpg" alt="" /></dt><dd>Figure&#58; Bad Example - When you don't add a favicon the user sees a generic icon</dd></dl><dl class="goodImage"><dt><img src="/PublishingImages/favicon-good.jpg" alt="" /></dt><dd>Figure&#58; Good Example - Using the favicon gives your website professional look and feel</dd></dl><h4>Which formats to use?</h4><p>The size for the image you will use is 16x16 pixels, using either​ 8-bit or 24-bit colors. The format of the image must be one of PNG (a W3C standard), GIF, or ICO.</p><p><strong>Note&#58;</strong> Some Internet Explorer versions supports ICO only. <a href="https&#58;//www.google.com.br/#hl=en&amp;safe=off&amp;sclient=psy-ab&amp;q=convert+png+to+ico&amp;oq=convert+png+to+ico&amp;gs_l=hp.3..0l4.980.3953.0.4436.18.14.0.3.3.1.441.4073.2-9j3j2.14.0.les%3b..0.0...1c.1.5.psy-ab.8wQKEsg0jbw&amp;pbx=1&amp;bav=on.2%2cor.r_gc.r_pw.r_cp.r_qf.&amp;bvm=bv.43287494%2cd.eWU&amp;fp=548854122be17fbe&amp;biw=1440&amp;bih=756">Search for an image converter in Google</a> to create an ICO file.</p><h4>How to implement the favicon?</h4><ol><li>Copy your company's favicon to the root of the site​</li><li>Add the yellow code below inside the &lt;HEAD&gt; tags in your HTML</li></ol><table class="clsSSWTable"><tbody><tr><td><p>&lt;head&gt;<br>
           &lt;title&gt;Page Title&lt;/title&gt;<br>
           <span class="highlight">&lt;link rel=&quot;shortcut icon&quot; href=&quot;/images/favicon.ico&quot; type=&quot;image/x-icon&quot; /&gt;</span><br>
           &lt;/head&gt;</p></td></tr></tbody></table>
   <strong>Figure&#58; One line of HTML lets you add your company's icon to your web page</strong>
            <p>This works for most websites, including ASPX WebForms, MVC and WordPress.</p><p><span class="productBox">We have a program called <a href="https&#58;//www.ssw.com.au/ssw/CodeAuditor/">SSW Code Auditor</a> to check for this rule.</span></p> 
   <span class="productBox">We have a program called <a href="https&#58;//www.ssw.com.au/ssw/LinkAuditor/">SSW Link Auditor</a> to check for this rule. We offer a <a href="/SSW/LinkAuditor/Samples/Rules/Favicon.aspx">rule sample page</a> for demo scan.</span> 



