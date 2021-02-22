---
type: rule
archivedreason: 
title: Fix HTML - Do you implement CSS friendly?
guid: d19badb1-94f3-48c9-8409-d562a857b407
uri: fix-html-do-you-implement-css-friendly
created: 2009-06-16T01:52:11.0000000Z
authors:
- title: John Liu
  url: https://ssw.com.au/people/john-liu
- title: Jay Lin
  url: https://ssw.com.au/people/jay-lin
related: []
redirects: []

---

It is extremely important to make your site standards compliant:

* It makes styling a lot easier.
* It also means your site is likely to work for all browsers, even if you don’t specifically target/support them.
* It requires accessibility for big public sites can be met easier.


<!--endintro-->

When you first run your SharePoint site – you’ll discover that it looks nice on the surface but needs a significant amount of work to fix all the bad HTML.

Implement CSS Friendly – these are the control adapters released by Microsoft to make ASP.NET render better, non-table based controls.  You can implement them for SharePoint sites as well.
            &lt;<font style="background-color&#58;rgb(255, 255, 128);">TABLE </font>id=zz1_TopNavigationMenu class=&quot;...&quot; border=0 cellSpacing=0 cellPadding=0&gt;

            &lt;TBODY&gt;

            &#160;&#160;&#160; &lt;TR&gt;

            &#160;&#160;&#160;&#160;&lt;TD id=zz1_TopNavigationMenun0&gt;

            &#160;&#160;&#160;&#160; &#160;&#160;&#160;&lt;<font style="background-color&#58;rgb(255, 255, 128);">TABLE </font>class=&quot;...&quot; border=0 cellSpacing=0 cellPadding=0 width=&quot;100%&quot;&gt;

            &#160;&#160;&#160;&#160;&#160; &#160;&#160;&lt;TBODY&gt;

            &#160;&#160;&#160;&#160;&#160;&#160; &#160;&#160;&#160;&#160; &lt;TR&gt;

            &#160;&#160;&#160;&#160;&#160;&#160;&#160; &#160;&#160;&#160;&#160;&#160;&#160;&#160; &lt;TD style=&quot;WHITE-SPACE&#58; nowrap&quot;&gt;

            &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; &#160;&#160;&#160;&#160;&#160;&#160; &lt;A style=&quot;...&quot; class=&quot;...&quot; href=&quot;...&quot;&gt;Home&lt;/A&gt;

            &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; &#160;&#160;&#160;&#160;&#160; &lt;/TD&gt;

            &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; &#160; &lt;/TR&gt;

            &#160;&#160;&#160;&#160;&#160;&#160;&#160; &lt;/TBODY&gt;

            &#160;&#160;&#160;&#160;&#160;&#160;&#160; &lt;/TABLE&gt;

            &#160;&#160;&#160; &lt;/TD&gt;

            &#160;&#160;&#160;&#160;...&#160;&#160;&#160;

            &#160;&#160;&#160; &lt;TD id=zz1_TopNavigationMenun1&gt;

            &#160;&#160;&#160;&#160; &#160;&#160; &lt;<font style="background-color&#58;rgb(255, 255, 128);">TABLE </font>class=&quot;...&quot; border=0 cellSpacing=0 cellPadding=0 width=&quot;100%&quot;&gt;

            &#160;&#160;&#160;&#160; &#160;&#160; &lt;TBODY&gt;

            &#160;&#160;&#160;&#160;&#160; &#160;&#160;&#160;&#160;&#160; &lt;TR&gt;

            &#160;&#160;&#160;&#160;&#160;&#160; &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; &lt;TD style=&quot;WHITE-SPACE&#58; nowrap&quot;&gt;

            &#160;&#160;&#160;&#160;&#160;&#160;&#160; &#160;&#160;&#160;&#160;&#160;&#160;&#160; &lt;A style=&quot;...&quot; class=&quot;...&quot; href=&quot;...&quot;&gt;Operations&lt;/A&gt;

            &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; &#160;&#160;&#160;&#160;&#160;&#160; &lt;/TD&gt;

            &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; &lt;/TR&gt;

            &#160;&#160;&#160;&#160;&#160;&#160;&#160; &lt;/TBODY&gt;

            &#160;&#160;&#160;&#160;&#160;&#160;&#160; &lt;/TABLE&gt;

            &#160;&#160;&#160; &lt;/TD&gt;

            &#160;&#160;&#160; ...

            &#160;&#160;&#160; &lt;TD id=zz1_TopNavigationMenun2&gt;

            &#160;&#160;&#160;&#160;&#160;&#160;&#160; &lt;<font style="background-color&#58;rgb(255, 255, 128);">TABLE </font>class=&quot;...&quot; border=0 cellSpacing=0 cellPadding=0 width=&quot;100%&quot;&gt;

            &#160;&#160;&#160;&#160;&#160;&#160;&#160; &lt;TBODY&gt;

            &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; &lt;TR&gt;

            &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; &lt;TD style=&quot;WHITE-SPACE&#58; nowrap&quot;&gt;

            &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; &lt;A style=&quot;...&quot; class=&quot;...&quot; href=&quot;...&quot;&gt;Application Management&lt;/A&gt;

            &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; &lt;/TD&gt;

            &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; &lt;/TR&gt;

            &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&lt;/TBODY&gt;

            &#160;&#160;&#160;&#160;&#160;&#160;&#160; &lt;/TABLE&gt;

            &#160;&#160;&#160; &lt;/TD&gt;

            &#160;&#160;&#160; ...

            &#160;&#160;&#160; &lt;/TR&gt;

            &lt;/TBODY&gt;

            &lt;/TABLE&gt;
                  Bad example - without using CSS Friendly        &lt;div class="CssFriendly-Menu-Horizontal" id="zz1\_TopNavigationMenu"&gt;
         &lt;<font style="background-color&#58;rgb(255, 255, 128);">ul</font> class="CssFriendly-Menu"&gt;
             &lt;<font style="background-color&#58;rgb(255, 255, 128);">li</font> class="CssFriendly-Menu-WithChildren"&gt;
             &lt;a href="..." class="CssFriendly-Menu-Link TopLevelNavItem"&gt;About Us&lt;/a&gt;
             &lt;div class="cbb CssFriendly-Menu-Dropdown"&gt;
                 &lt;div class="CssFriendly-Menu-Dropdown-ItemHost"&gt;
                     &lt;<font style="background-color&#58;rgb(255, 255, 128);">ul</font> class="first"&gt;
                         &lt;<font style="background-color&#58;rgb(255, 255, 128);">li</font> class="CssFriendly-Menu-Leaf"&gt;
                         &lt;a href="..." class="CssFriendly-Menu-Link"&gt;Employees&lt;/a&gt;
                         &lt;/li&gt;
                     &lt;/ul&gt;
                 &lt;/div&gt;
             &lt;/div&gt;
             &lt;/li&gt;
             ...
         &lt;/ul&gt;
     &lt;/div&gt;      Good example - using CSS Friendly
