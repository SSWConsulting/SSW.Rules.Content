---
type: rule
title: Fix HTML - Do you implement CSS friendly?
uri: fix-html---do-you-implement-css-friendly
created: 2009-06-16T01:52:11.0000000Z
authors:
- id: 8
  title: John Liu
- id: 18
  title: Jay Lin

---



<span class='intro'> 
  <p>It is extremely important to make your site standards compliant&#58;</p>
<ul>
    <li>It makes styling a lot easier. </li>
    <li>It also means your site is likely to work for all browsers, even if you don’t specifically target/support them. </li>
    <li>It requires accessibility for big public sites can be met easier.</li>
</ul>
 </span>


  <p>When you first run your SharePoint site – you’ll discover that it looks nice on the surface but needs a significant amount of work to fix all the bad HTML. </p>
<p>Implement CSS Friendly – these are the control adapters released by Microsoft to make ASP.NET render better, non-table based controls.&#160; You can implement them for SharePoint sites as well. </p>
<dl class="badCode">
    <dl>
        <dl>
            <dt>&lt;<font style="background-color&#58;#ffff80;">TABLE </font>id=zz1_TopNavigationMenu class=&quot;...&quot; border=0 cellSpacing=0 cellPadding=0&gt;<br>
            &lt;TBODY&gt;<br>
            &#160;&#160;&#160; &lt;TR&gt;<br>
            &#160;&#160;&#160;&#160;&lt;TD id=zz1_TopNavigationMenun0&gt;<br>
            &#160;&#160;&#160;&#160; &#160;&#160;&#160;&lt;<font style="background-color&#58;#ffff80;">TABLE </font>class=&quot;...&quot; border=0 cellSpacing=0 cellPadding=0 width=&quot;100%&quot;&gt;<br>
            &#160;&#160;&#160;&#160;&#160; &#160;&#160;&lt;TBODY&gt;<br>
            &#160;&#160;&#160;&#160;&#160;&#160; &#160;&#160;&#160;&#160; &lt;TR&gt;<br>
            &#160;&#160;&#160;&#160;&#160;&#160;&#160; &#160;&#160;&#160;&#160;&#160;&#160;&#160; &lt;TD style=&quot;WHITE-SPACE&#58; nowrap&quot;&gt;<br>
            &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; &#160;&#160;&#160;&#160;&#160;&#160; &lt;A style=&quot;...&quot; class=&quot;...&quot; href=&quot;...&quot;&gt;Home&lt;/A&gt;<br>
            &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; &#160;&#160;&#160;&#160;&#160; &lt;/TD&gt;<br>
            &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; &#160; &lt;/TR&gt;<br>
            &#160;&#160;&#160;&#160;&#160;&#160;&#160; &lt;/TBODY&gt;<br>
            &#160;&#160;&#160;&#160;&#160;&#160;&#160; &lt;/TABLE&gt;<br>
            &#160;&#160;&#160; &lt;/TD&gt;<br>
            &#160;&#160;&#160;&#160;...&#160;&#160;&#160;<br>
            &#160;&#160;&#160; &lt;TD id=zz1_TopNavigationMenun1&gt;<br>
            &#160;&#160;&#160;&#160; &#160;&#160; &lt;<font style="background-color&#58;#ffff80;">TABLE </font>class=&quot;...&quot; border=0 cellSpacing=0 cellPadding=0 width=&quot;100%&quot;&gt;<br>
            &#160;&#160;&#160;&#160; &#160;&#160; &lt;TBODY&gt;<br>
            &#160;&#160;&#160;&#160;&#160; &#160;&#160;&#160;&#160;&#160; &lt;TR&gt;<br>
            &#160;&#160;&#160;&#160;&#160;&#160; &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; &lt;TD style=&quot;WHITE-SPACE&#58; nowrap&quot;&gt;<br>
            &#160;&#160;&#160;&#160;&#160;&#160;&#160; &#160;&#160;&#160;&#160;&#160;&#160;&#160; &lt;A style=&quot;...&quot; class=&quot;...&quot; href=&quot;...&quot;&gt;Operations&lt;/A&gt;<br>
            &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; &#160;&#160;&#160;&#160;&#160;&#160; &lt;/TD&gt;<br>
            &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; &lt;/TR&gt;<br>
            &#160;&#160;&#160;&#160;&#160;&#160;&#160; &lt;/TBODY&gt;<br>
            &#160;&#160;&#160;&#160;&#160;&#160;&#160; &lt;/TABLE&gt;<br>
            &#160;&#160;&#160; &lt;/TD&gt;<br>
            &#160;&#160;&#160; ...<br>
            &#160;&#160;&#160; &lt;TD id=zz1_TopNavigationMenun2&gt;<br>
            &#160;&#160;&#160;&#160;&#160;&#160;&#160; &lt;<font style="background-color&#58;#ffff80;">TABLE </font>class=&quot;...&quot; border=0 cellSpacing=0 cellPadding=0 width=&quot;100%&quot;&gt;<br>
            &#160;&#160;&#160;&#160;&#160;&#160;&#160; &lt;TBODY&gt;<br>
            &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; &lt;TR&gt;<br>
            &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; &lt;TD style=&quot;WHITE-SPACE&#58; nowrap&quot;&gt;<br>
            &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; &lt;A style=&quot;...&quot; class=&quot;...&quot; href=&quot;...&quot;&gt;Application Management&lt;/A&gt;<br>
            &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; &lt;/TD&gt;<br>
            &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; &lt;/TR&gt;<br>
            &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&lt;/TBODY&gt;<br>
            &#160;&#160;&#160;&#160;&#160;&#160;&#160; &lt;/TABLE&gt;<br>
            &#160;&#160;&#160; &lt;/TD&gt;<br>
            &#160;&#160;&#160; ...<br>
            &#160;&#160;&#160; &lt;/TR&gt;<br>
            &lt;/TBODY&gt;<br>
            &lt;/TABLE&gt;</dt>
        </dl>
    </dl>
    <dd>Bad example - without using CSS Friendly </dd>
</dl>
<dl class="goodCode">
    <dt>&lt;div class=&quot;CssFriendly-Menu-Horizontal&quot; id=&quot;zz1_TopNavigationMenu&quot;&gt;<br>
    &#160;&#160;&#160; &lt;<font style="background-color&#58;#ffff80;">ul</font> class=&quot;CssFriendly-Menu&quot;&gt;<br>
    &#160;&#160;&#160;&#160;&#160;&#160;&#160; &lt;<font style="background-color&#58;#ffff80;">li</font> class=&quot;CssFriendly-Menu-WithChildren&quot;&gt;<br>
    &#160;&#160;&#160;&#160;&#160;&#160;&#160; &lt;a href=&quot;...&quot; class=&quot;CssFriendly-Menu-Link TopLevelNavItem&quot;&gt;About Us&lt;/a&gt;<br>
    &#160;&#160;&#160;&#160;&#160;&#160;&#160; &lt;div class=&quot;cbb CssFriendly-Menu-Dropdown&quot;&gt;<br>
    &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; &lt;div class=&quot;CssFriendly-Menu-Dropdown-ItemHost&quot;&gt;<br>
    &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; &lt;<font style="background-color&#58;#ffff80;">ul</font> class=&quot;first&quot;&gt;<br>
    &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; &lt;<font style="background-color&#58;#ffff80;">li</font> class=&quot;CssFriendly-Menu-Leaf&quot;&gt;<br>
    &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; &lt;a href=&quot;...&quot; class=&quot;CssFriendly-Menu-Link&quot;&gt;Employees&lt;/a&gt;<br>
    &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; &lt;/li&gt;<br>
    &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; &lt;/ul&gt;<br>
    &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; &lt;/div&gt;<br>
    &#160;&#160;&#160;&#160;&#160;&#160;&#160; &lt;/div&gt;<br>
    &#160;&#160;&#160;&#160;&#160;&#160;&#160; &lt;/li&gt;<br>
    &#160;&#160;&#160;&#160;&#160;&#160;&#160; ...<br>
    &#160;&#160;&#160; &lt;/ul&gt;<br>
    &lt;/div&gt; </dt>
    <dd>Good example - using CSS Friendly</dd>
</dl>
<p>&#160;</p>



