---
type: rule
title: Do you know how to name documents?
uri: do-you-know-how-to-name-documents
created: 2019-02-26T01:04:10.0000000Z
authors:
- id: 1
  title: Adam Cogan
- id: 9
  title: William Yin

---



<span class='intro'> <p class="ssw15-rteElement-P">When naming documents, use hyphens to separate words to make your files&#160;more easily discoverable.<br></p> </span>

<p class="ssw15-rteElement-CodeArea" style="width&#58;781.188px;">MonthlyReport.docx<br></p><dd class="ssw15-rteElement-FigureBad">Bad Example&#58; File name doesn't contain any separators between words.<br></dd>A file name without spaces&#160;means that the SharePoint doesn't know where one word ends and the other one begins. This means that searching for 'monthly'&#160;or 'report' would&#160;<strong>not</strong>&#160;find this document.<br> 
<p class="ssw15-rteElement-CodeArea" style="width&#58;781.188px;">Monthly Report.docx&#160;<br></p><dd class="ssw15-rteElement-FigureBad">Bad Example&#58; File name uses&#160;a&#160;space to separate words.</dd><p class="ssw15-rteElement-P">As far as SharePoint search goes, this is actually a usable option. What makes&#160;spaces&#160;less-preferable is the fact that the URL to this document will have those spaces escaped with the sequence %20. E.g.&#160;<a href="/Pages/Do-you-know-how-to-use-SharePoint-search.aspx">https&#58;//sharepoint/site/library/Monthly%2 0 Report.docx</a>. URLs with escaped spaces are longer and less human-readable.<br></p><p class="ssw15-rteElement-CodeArea" style="width&#58;781.188px;">Monthly_Report.docx&#160;</p><dd class="ssw15-rteElement-FigureBad">Bad&#160;Example&#58; File name uses an underscore to separate words.</dd><p>As far as SharePoint search goes, an underscore is only a valid word separator in SharePoint Standard or Enterprise, from 2010 onwards. Underscores are not valid word separators for search in SharePoint foundation. Also, sometimes&#160;underscores are less visible to users, for example, when a hyperlink is underlined. When reading a hyperlink that is underlined,&#160;it is oft​en possible for the&#160;user to be mistaken by thinking that the URL contains spaces instead of underscores.&#160;For these reasons it is best to avoid their use in file names and titles.<br></p><p class="ssw15-rteElement-CodeArea" style="width&#58;781.188px;">Monthly-Report.docx&#160;<br></p><dd class="ssw15-rteElement-FigureGood">Good Example&#58; File name uses a hyphen to separate words.</dd><p class="ssw15-rteElement-P">A hyphen is the best&#160;choice, because it&#160;is understood both by humans and all versions of SharePoint search.<br></p><h3 class="ssw15-rteElement-H3">Add relevant metadata where possible</h3><p class="ssw15-rteElement-P">If a document library is configured with metadata fields, add as much relevant information as you can. Metadata is more highly regarded by search than the contents within documents, so by adding relevant terms to a documents metadata, you will almost certainly have a positive effect on the relevance of search results.​<br></p><h3 class="ssw15-rteElement-H3">Use descriptive file names and titles</h3><p class="ssw15-rteElement-P">The file name and title is regarded more highly by search than the content within documents. Also, the title or file name is what is displayed in the search results, so by making it descriptive, you are making it easier for people who perform searches to identify the purpose of your document.​<br></p><h3 class="ssw15-rteElement-H3">Related Rule<br></h3><ul class="ssw15-rteElement-P"><li>
      <a href="/_layouts/15/FIXUPREDIRECT.ASPX?WebId=3dfc0e07-e23a-4cbb-aac2-e778b71166a2&amp;TermSetId=07da3ddf-0924-4cd2-a6d4-a4809ae20160&amp;TermId=154cc595-9579-45c9-8e23-79948dd3e084">Do you know how to use SharePoint search?</a><br></li></ul>


