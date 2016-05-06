---
type: rule
archivedreason: 
title: Do you know how to create a link to a URL in SharePoint?
guid: f7e772d8-748f-4f21-8890-c25ef13718f9
uri: do-you-know-how-to-create-a-link-to-a-url-in-sharepoint
created: 2013-07-26T00:38:30.0000000Z
authors:
- id: 9
  title: William Yin
- id: 1
  title: Adam Cogan
related: []

---


You may&#160;need a link in a SharePoint document to help you navigate to a different URL (like shortcut in Windows), there are different ways to implement this.<div><br><div><dd class="ssw15-rteElement-FigureBad">A.&#160; Create a shortcut in windows, then upload the&#160;shortcut file (.url) to the document library.</dd><dd class="ssw15-rteElement-FigureGood">B. Use &quot;Link to a document&quot; content type in SharePoint.</dd><br></div></div>
<br><excerpt class='endintro'></excerpt><br>
<p class="ssw15-rteElement-P">Details on how you to create a link to a document in a SharePoint library.</p><p class="ssw15-rteElement-P"><strong>A.&#160;Create a shortcut in windows, then upload the&#160;shortcut file (.url) to the document library. </strong></p><p class="ssw15-rteElement-P">To do this, you need to remove&#160;.url file type from your blocked file types&#160;in your web application. This will bring some security risk, which is not recommended, and I won't show the step details here.</p><p class="ssw15-rteElement-P"><strong>B. Use &quot;Link to a document&quot; content type in SharePoint.</strong><br></p><p class="ssw15-rteElement-P">1) Enable &quot;Content Type&#160;management&quot; in your document library.</p><dl class="ssw15-rteElement-ImageArea"><img alt="EnableContentTypeDocument.png" src="/PublishingImages/EnableContentTypeDocument.png" style="margin&#58;5px;" /></dl><dd class="ssw15-rteElement-FigureNormal">Figure&#58;&#160;Enable Content Type management in library setting</dd><p class="ssw15-rteElement-P">2) Add &quot;Link to a Document&quot; content type into the library.</p><dl class="ssw15-rteElement-ImageArea"><img alt="AddExistContentType.png" src="/PublishingImages/AddExistContentType.png" style="margin&#58;5px;width&#58;650px;" /></dl><dd class="ssw15-rteElement-FigureNormal">Figure&#58; Add from existing site content type</dd><dl class="ssw15-rteElement-ImageArea"><img alt="SelectLinkToADocumentType.png" src="/PublishingImages/SelectLinkToADocumentType.png" style="margin&#58;5px;width&#58;650px;" /></dl><dd class="ssw15-rteElement-FigureNormal">Figure&#58; Select &quot;Link to a Document&quot; content type</dd><p>3) Create a &quot;Link to a document&quot; instance<br></p><dl class="ssw15-rteElement-ImageArea"><img alt="CreateLinkToADocumentInstance.png" src="/PublishingImages/CreateLinkToADocumentInstance.png" style="margin&#58;5px;" /></dl><dd class="ssw15-rteElement-FigureNormal">Figure&#58; select &quot;File | New Document (dropdown) | Link to a document&quot;</dd><dl class="ssw15-rteElement-ImageArea"><img alt="InputLinkUrlAndName.png" src="/PublishingImages/InputLinkUrlAndName.png" style="margin&#58;5px;" /></dl><dd class="ssw15-rteElement-FigureNormal">Figure&#58; Input &quot;Name&quot; and &quot;URL&quot;</dd><p class="ssw15-rteElement-P">4) Done<br></p><p class="ssw15-rteElement-P">You should be able to&#160;see the link type document in your library&#58;</p><dl class="ssw15-rteElement-ImageArea"><img alt="LinksTypeDocumentsWithShortcutIcon.png" src="/PublishingImages/LinksTypeDocumentsWithShortcutIcon.png" data-pin-nopin="true" style="margin&#58;5px;" /></dl><dd class="ssw15-rteElement-FigureNormal">Figure&#58; Link type documents with the lovely shortcut icon</dd><dd class="ssw15-rteElement-FigureNormal"><br></dd><dd class="ssw15-rteElement-FigureNormal"><span style="color&#58;#ff0000;">[TO DO TIAGO&#58; ADD IMAGE OF WINDOWS EXPLORER (4 files in it) AND ANOTHER WITH SHAREPOINT DOCUMENTS LIBRARY​] </span></dd>


