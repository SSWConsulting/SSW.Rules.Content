---
type: rule
archivedreason: 
title: Do you know how to name documents?
guid: fd6b589b-9f74-4d95-bc4f-b90b4c349c31
uri: how-to-name-sharepoint-documents
created: 2019-02-26T01:04:10.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: William Yin
  url: https://ssw.com.au/people/william-yin
related: []
redirects:
- do-you-know-how-to-name-documents

---


<p class="ssw15-rteElement-P">When naming documents, use kebab-case&#160;to separate words to make your files&#160;more easily discoverable.<br></p>
<br><excerpt class='endintro'></excerpt><br>
<p>A file name without spaces&#160;means that the search engine doesn't know where one word ends and the other one begins. This means that searching for 'monthly'&#160;or 'report' might&#160;<strong>not</strong>&#160;find this document.</p>
<p class="ssw15-rteElement-CodeArea" style="width&#58;781.188px;">MonthlyReport.docx<br></p><dd class="ssw15-rteElement-FigureBad">Bad Example&#58; File name doesn't contain any separators between words<br><br></dd>As far as&#160;search goes, using spaces&#160;is actually a usable option. What makes&#160;spaces&#160;less-preferable is the fact that the URL to this document will have those spaces escaped with the sequence %20. E.g.&#160;https&#58;//sharepoint/site/library/Monthly%20​Report.docx. URLs with escaped spaces are longer and less human-readable.<br>
<p class="ssw15-rteElement-CodeArea" style="width&#58;781.188px;">Monthly Report.docx&#160;<br></p><dd class="ssw15-rteElement-FigureBad">Bad Example&#58; File name uses&#160;a&#160;space to separate words<br></dd><p class="ssw15-rteElement-P"><br>Underscores are not valid word separators for search in SharePoint,&#160;and not recommended by others. Also, sometimes&#160;underscores are less visible to users, for example, when a hyperlink is underlined. When reading a hyperlink that is underlined,&#160;it is oft​en possible for the&#160;user to be mistaken by thinking that the URL contains spaces instead of underscores.&#160;For these reasons it is best to avoid their use in file names and titles.<br></p><p class="ssw15-rteElement-CodeArea" style="width&#58;781.188px;">Monthly_Report.docx&#160;</p><dd class="ssw15-rteElement-FigureBad">Bad&#160;Example&#58; File name uses an underscore (snake_case) to separate words<br><br></dd><p>A hyphen is the best&#160;choice, because it&#160;is understood both by humans and all versions of SharePoint search.<br></p><p class="ssw15-rteElement-CodeArea" style="width&#58;781.188px;">Monthly-Report.docx&#160;<br></p><dd class="ssw15-rteElement-FigureGood">Good Example&#58; File name uses a kebab-case​ to separate words<br><br></dd><h3 class="ssw15-rteElement-H3">Add relevant metadata where possible</h3><p class="ssw15-rteElement-P">If a document library is configured with metadata fields, add as much relevant information as you can. Metadata is more highly regarded by search than the contents within documents, so by adding relevant terms to a documents metadata, you will almost certainly have a positive effect on the relevance of search results.​<br></p><h3 class="ssw15-rteElement-H3">Use descriptive file names and titles</h3><p class="ssw15-rteElement-P">The file name and title is regarded more highly by search than the content within documents. Also, the title or file name is what is displayed in the search results, so by making it descriptive, you are making it easier for people who perform searches to identify the purpose of your document.​<br></p><h3 class="ssw15-rteElement-H3">Related Rule<br></h3><ul class="ssw15-rteElement-P"><li> 
      <a href=/do-you-know-how-to-use-sharepoint-search>Do you know how to use SharePoint search?</a><br></li><li><a href=/use-dashes-in-urls>Do you use dashes in your URLs?</a><br></li></ul>


