---
type: rule
archivedreason: 
title: Fix HTML - Do you make SharePoint CSS friendly?
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

Implement CSS Friendly – these are the control adapters released by Microsoft to make ASP.NET render better, non-table based controls. You can implement them for SharePoint sites as well:

``` html
<TABLE id=zz1_TopNavigationMenu class="..." border=0 cellSpacing=0 cellPadding=0>
  <TBODY>
    <TR>
      <TD id=zz1_TopNavigationMenun0>
        <TABLE class="..." border=0 cellSpacing=0 cellPadding=0 width="100%">
          <TBODY>
            <TR>
              <TD style="WHITE-SPACE: nowrap">
                <A style="..." class="..." href="...">Home</A>
              </TD>
            </TR>
          </TBODY>
        </TABLE>
      </TD> ... <TD id=zz1_TopNavigationMenun1>
        <TABLE class="..." border=0 cellSpacing=0 cellPadding=0 width="100%">
          <TBODY>
            <TR>
              <TD style="WHITE-SPACE: nowrap">
                <A style="..." class="..." href="...">Operations</A>
              </TD>
            </TR>
          </TBODY>
        </TABLE>
      </TD> ... <TD id=zz1_TopNavigationMenun2>
        <TABLE class="..." border=0 cellSpacing=0 cellPadding=0 width="100%">
          <TBODY>
            <TR>
              <TD style="WHITE-SPACE: nowrap">
                <A style="..." class="..." href="...">Application Management</A>
              </TD>
            </TR>
          </TBODY>
        </TABLE>
      </TD> ...
    </TR>
  </TBODY>
</TABLE> Bad example - without using CSS Friendly <div class="CssFriendly-Menu-Horizontal" id="zz1\_TopNavigationMenu">
  <ul class="CssFriendly-Menu">
    <li class="CssFriendly-Menu-WithChildren">
      <a href="..." class="CssFriendly-Menu-Link TopLevelNavItem">About Us</a>
      <div class="cbb CssFriendly-Menu-Dropdown">
        <div class="CssFriendly-Menu-Dropdown-ItemHost">
          <ul class="first">
            <li class="CssFriendly-Menu-Leaf">
              <a href="..." class="CssFriendly-Menu-Link">Employees</a>
            </li>
          </ul>
        </div>
      </div>
    </li> ...
  </ul>
</div>
```
::: good
Good example - using CSS Friendly in SharePoint
:::
