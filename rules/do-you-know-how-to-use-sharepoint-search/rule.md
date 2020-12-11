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


<p class="ssw15-rteElement-P">​​SharePoint search is a powerful tool for discovering information. Here are some tips to make sure you are getting the most from it. There are two things to consider regarding SharePoint search; firstly, how you save information to SharePoint to be more easily discoverable; secondly, how to perform searches within SharePoint.<br></p><div><div><p class="ssw15-rteElement-P">​Here are some tips for performing searches:​​​<br></p><div>
   <div><h3>Know how to navigate SharePoint search – watch this video</h3><div class="ms-rtestate-read ms-rte-embedcode ms-rte-embedil ms-rtestate-notify" unselectable="on"> 
         <iframe width="750" height="422" src="https://www.youtube.com/embed/Vh64ZEC0wcw" frameborder="0"></iframe> </div>
      <br>
   </div></div></div></div>
<br><excerpt class='endintro'></excerpt><br>
<ul class="ssw15-rteElement-P"><li>Use the categories (top)</li><li>Use the filters (right navigation / faceted search)</li><li>Use the scope to go wider</li><li>Use the specific properties (see below)</li><li>People - Use Delve indexed properties (i.e. Skills)<br></li></ul><h3 class="ssw15-rteElement-H3">Search a specific property <br></h3><p>if you are familiar with the structure of the metadata in the content you're searching, you​ can restrict your searches to a property with the syntax <property>:<search term>. E.g. to search the filename field for the term "report", you would use "filename:report".<br></p><p>Example of properties you can use (common ones);<br></p><ul><li>Filetype:</li><li>CreatedBy:</li><li>ModifiedBy:<br></li><li>Title:<br></li></ul><p><b>More:</b> <a href="https://docs.microsoft.com/en-us/office365/securitycompliance/keyword-queries-and-search-conditions">https://docs.microsoft.com/en-us/office365/securitycompliance/keyword-queries-and-search-conditions</a></p><dl class="image"><dt><img src="filter-sharepoint-example.png" alt="filter-sharepoint-example.png" style="width:750px;" /></dt><dd>Figure: Example of using Filetype: filter</dd></dl>
<span style="color:#cc4141;font-family:"segoe ui", "trebuchet ms", tahoma, arial, verdana, sans-serif;font-size:18px;">Use Boolean OR and AND operators</span><p>Similar to Google and Bing, you can use OR and AND Boolean operators. E.g. "sharepoint AND search".</p><p class="ssw15-rteElement-GreyBox">Note: OR and AND must be capitalized, however, the case is irrelevant for actual search terms.<br></p><h3 class="ssw15-rteElement-H3">Use an 
   <a href="http://en.wikipedia.org/wiki/Asterisk"> asterisk (*)</a> wildcard for partial matches</h3><p>This can be useful if you know that certain words are used together, e.g. Fire* will return results for FireBootCamp.</p><p class="ssw15-rteElement-GreyBox">Note: Because of word stemming which is enabled by default in ​SharePoint 2019, 2016, and 2013, you do not need to use wildcards to find variations on words. For example, searching for "computer" will return results that contain "computers", so you do not need to search for "computer*". <br></p><h3 class="ssw15-rteElement-H3">Use double quotes to find specific phrases</h3><p>E.g. search for "social media" to make sure you get results for social media, as opposed to results that simply contain the words "social" and "media" in the same document.<br></p><div><h3 class="ssw15-rteElement-H3">Related Rules​<br></h3><ul class="ssw15-rteElement-P"><li>
         <a href="/_layouts/15/FIXUPREDIRECT.ASPX?WebId=3dfc0e07-e23a-4cbb-aac2-e778b71166a2&TermSetId=07da3ddf-0924-4cd2-a6d4-a4809ae20160&TermId=1f58c5ab-10d5-40f7-8a24-7f88570ad5ef">Do you know how to use Teams Search?​</a><br></li><li> 
         <a href="/_layouts/15/FIXUPREDIRECT.ASPX?WebId=3dfc0e07-e23a-4cbb-aac2-e778b71166a2&TermSetId=07da3ddf-0924-4cd2-a6d4-a4809ae20160&TermId=281372de-6277-4797-8454-e285cfe02bdf">Do you know how to name ShareP​oint documents?</a>​<br></li></ul></div>


