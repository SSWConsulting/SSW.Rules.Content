---
type: rule
title: Do you know when to use CAML instead of object model?
uri: do-you-know-when-to-use-caml-instead-of-object-model
created: 2009-04-09T06:10:00.0000000Z
authors:
- id: 8
  title: John Liu
- id: 18
  title: Jay Lin

---



<span class='intro'> 
  <p>SharePoint utilizes CAML to do a lot of things - one of these is using CAML to define a query language to select elements from lists within SharePoint.</p>
<p>The development experience with CAML is not good.&#160; CAML is unforgiving when it comes to errors, but it doesn't tell you what's wrong.&#160; Thus earning it a bad name with SharePoint developers.&#160; People don't like CAML.</p>
 </span>


  <p>The SharePoint object model is very comprehensive and lets you select items from lists, select lists from sites, in site-collections within web-applications.</p>
<p>Naturally, using the object model is great for traversing all elements in a list.&#160; Once you have a handle to the item, you can also easily modify that item.</p>
<p>On the other hand, one of the SharePoint class SPSiteDataQuery allows a developer to use CAML to specify a query condition that SharePoint can understand to search and return matching elements from across the entire site collection.</p>
<p>This is the underlying class that the Content Query Web Part relies on.</p>
<p>So, you need to use object model when you want to&#58;</p>
<ul>
    <li>Iterate all elements in a list </li>
    <li>Modify elements in a list</li>
</ul>
<p>And you use CAML, whether in CQWP or in code with SPSiteDataQuery to&#58;</p>
<ul>
    <li>Select, filter elements from SharePoint lists </li>
    <li>Select elements from multiple lists</li>
</ul>



