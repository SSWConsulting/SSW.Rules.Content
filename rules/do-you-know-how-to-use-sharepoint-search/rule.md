---
type: rule
archivedreason: 
title: Do you know how to use SharePoint search?
guid: 34637e83-ce1f-46db-896c-0a639ae0c28b
uri: do-you-know-how-to-use-sharepoint-search
created: 2015-01-20T12:18:03.0000000Z
authors:
- id: 36
  title: Daniel Šmon
- id: 1
  title: Adam Cogan
related:
- why-do-we-use-vm-for-sharepoint-development-

---


​SharePoint search is a powerful tool for discovering information. Here are some tips to make sure you are getting the most from it. There are two things to consider regarding SharePoint search; firstly, how you save information to SharePoint to be more easily discoverable; secondly, how to perform searches within SharePoint.&#160;​
<br><excerpt class='endintro'></excerpt><br>
<h3 class="ssw15-rteElement-H3">Tips for saving documents to be more discoverable</h3><p>
   <strong>When naming documents, use hyphens to separate words</strong></p><p class="ssw15-rteElement-CodeArea">MonthlyReport.docx</p><div>Bad Example&#58; File name doesn't contain any separators between words.</div><p class="ssw15-rteElement-P">A file name without spaces&#160;means that the SharePoint doesn't know where one word ends and the other one begins. This means that searching for 'monthly'&#160;or 'report' would <strong>not</strong> find this document.</p><p class="ssw15-rteElement-P">&#160;</p><p class="ssw15-rteElement-CodeArea">Monthly Report.docx&#160;</p><div>Bad Example&#58; File name uses&#160;a&#160;space to separate words.</div><p class="ssw15-rteElement-P">As far as SharePoint search goes, this is actually a usable option. What makes&#160;spaces&#160;less-preferable is the fact that the URL to this document will have those spaces escaped with the sequence %20. E.g. <a href="/Pages/Do-you-know-how-to-use-SharePoint-search.aspx">https&#58;//sharepoint/site/library/Monthly%2 0 Report.docx</a>. URLs with escaped spaces are longer and less human-readable.</p><p>&#160;</p><p class="ssw15-rteElement-CodeArea">Monthly_Report.docx&#160;</p><div>Bad&#160;Example&#58; File name uses an underscore to separate words.</div><p>As far as SharePoint search goes, an underscore is only a valid word separator in SharePoint Standard or Enterprise, from 2010 onwards. Underscores are not valid word separators for search in SharePoint foundation. Also, sometimes&#160;underscores are less visible to users, for example, when a hyperlink is underlined. When reading a hyperlink that is underlined,&#160;it is often possible for the&#160;user to be mistaken by thinking that the URL contains spaces instead of underscores.&#160;For these reasons it is best to avoid their use in file names and titles.</p><p>&#160;</p><p class="ssw15-rteElement-CodeArea">Monthly-Report.docx&#160;</p><div>Good Example&#58; File name uses a hyphen to separate words.</div><p class="ssw15-rteElement-P">A hyphen is the best&#160;choice, because it&#160;is understood both by humans and all versions of SharePoint search.</p><p class="ssw15-rteElement-P">&#160;</p><p class="ssw15-rteElement-P">
   <strong>Add relevant metadata where possible</strong></p><p class="ssw15-rteElement-P">If a document library is configured with metadata fields, add as much relevant information as you can. Metadata is more highly regarded by search than the contents within documents, so by adding relevant terms to a documents metadata, you will almost certainly have a positive effect on the relevance of search results.</p><p class="ssw15-rteElement-P">&#160;</p><p class="ssw15-rteElement-P">
   <strong>Use descriptive file names and titles</strong></p><p class="ssw15-rteElement-P">The file name and title is regarded more highly by search than the content within documents. Also, the title or file name is what is displayed in the search results, so by making it descriptive, you are making it easier for people who perform searches to identify the purpose of your document.</p><h3 class="ssw15-rteElement-H3">Tips for performing searches</h3><p>
   <strong>Use Boolean OR and AND operators</strong></p><p>Similar to Google and Bing, you can use&#160;OR and AND&#160;Boolean operators. E.g. &quot;sharepoint AND search&quot;.</p><p class="ssw15-rteElement-GreyBox">Note&#58; OR and AND must be capitalized, however case is irrelevant for actual search terms.</p><p>&#160;</p><p>
   <strong>Use an </strong> <a href="http&#58;//en.wikipedia.org/wiki/Asterisk"> <strong>asterisk (*)</strong></a> <strong>wildcard for partial matches</strong></p><p>This can&#160;be useful if you know that certain words are used together,&#160;e.g. Fire* will return results for FireBootCamp.</p><p class="ssw15-rteElement-GreyBox">Note&#58;&#160;Because of word stemming&#160;which is enabled by default&#160;in SharePoint 2013, you do not need to&#160;use wildcards to find variations on words. For example, searching for&#160;&quot;computer&quot; will return&#160;results that contain &quot;computers&quot;, so you do not need to search for&#160;&quot;computer*&quot;.&#160;</p><p>
   <strong></strong>&#160;</p><p>
   <strong>Use double quotes to find specific phrases</strong></p><p>E.g. search for &quot;social media&quot; to make sure you get results for social media, as opposed to results that simply contain the words &quot;social&quot; and &quot;media&quot; in the same document.</p><p>&#160;</p><p>
   <strong>Search a specific property if you are familiar with the structure of the metadata in the content you're searching</strong></p><p>You can restrict your searches to a property with the syntax &lt;property&gt;&#58;&lt;search term&gt;. E.g. to search the filename field for the term &quot;report&quot;, you would use &quot;filename&#58;report&quot;.</p><p>&#160;</p>
<div></div> <div>Good&#160;Example&#58;&#160;Search on the SSW Intranet. </div>


