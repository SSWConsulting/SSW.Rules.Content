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

SharePoint search is a powerful tool for discovering information. Here are some tips to make sure you are getting the most from it. There are two things to consider regarding SharePoint search; firstly, how you save information to SharePoint to be more easily discoverable; secondly, how to perform searches within SharePoint.


Here are some tips for performing searches:



### Know how to navigate SharePoint search – watch this video


`youtube: https://www.youtube.com/embed/Vh64ZEC0wcw`
 





<!--endintro-->

* Use the categories (top)
* Use the filters (right navigation / faceted search)
* Use the scope to go wider
* Use the specific properties (see below)
* People - Use Delve indexed properties (i.e. Skills)


### Search a specific property 


if you are familiar with the structure of the metadata in the content you're searching, you can restrict your searches to a property with the syntax <property>:<search term="">. E.g. to search the filename field for the term "report", you would use "filename:report".<br></search></property>

Example of properties you can use (common ones);

* Filetype:
* CreatedBy:
* ModifiedBy:
* Title:


**More:** https://docs.microsoft.com/en-us/office365/securitycompliance/keyword-queries-and-search-conditions
<dl class="image">&lt;dt&gt;<img src="filter-sharepoint-example.png" alt="filter-sharepoint-example.png" style="width:750px;">&lt;/dt&gt;<dd>Figure: Example of using Filetype: filter</dd></dl>Use Boolean OR and AND operators
Similar to Google and Bing, you can use OR and AND Boolean operators. E.g. "sharepoint AND search".


::: greybox
Note: OR and AND must be capitalized, however, the case is irrelevant for actual search terms.

:::


### Use an <br>   [asterisk (\*)](http://en.wikipedia.org/wiki/Asterisk) wildcard for partial matches

This can be useful if you know that certain words are used together, e.g. Fire\* will return results for FireBootCamp.


::: greybox
Note: Because of word stemming which is enabled by default in SharePoint 2019, 2016, and 2013, you do not need to use wildcards to find variations on words. For example, searching for "computer" will return results that contain "computers", so you do not need to search for "computer\*". 

:::


### Use double quotes to find specific phrases

E.g. search for "social media" to make sure you get results for social media, as opposed to results that simply contain the words "social" and "media" in the same document.


### Related Rules


* [Do you know how to use Teams Search?](/_layouts/15/FIXUPREDIRECT.ASPX?WebId=3dfc0e07-e23a-4cbb-aac2-e778b71166a2&TermSetId=07da3ddf-0924-4cd2-a6d4-a4809ae20160&TermId=1f58c5ab-10d5-40f7-8a24-7f88570ad5ef)
* [Do you know how to name SharePoint documents?](/_layouts/15/FIXUPREDIRECT.ASPX?WebId=3dfc0e07-e23a-4cbb-aac2-e778b71166a2&TermSetId=07da3ddf-0924-4cd2-a6d4-a4809ae20160&TermId=281372de-6277-4797-8454-e285cfe02bdf)
