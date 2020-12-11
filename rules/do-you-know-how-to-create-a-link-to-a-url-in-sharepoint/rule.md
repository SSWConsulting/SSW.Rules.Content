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


<div><span style="color:#ff0000;font-size:14.4px;font-weight:bold;">​TODO TIAGO: ADD IMAGE OF WINDOWS EXPLORER (4 files in it) AND ANOTHER WITH SHAREPOINT DOCUMENTS LIBRARY​</span></div><div><br></div><div>You may need a link in a SharePoint document to help you navigate to a different URL (like shortcut in Windows), there are different ways to implement this.<div><br><div><dd class="ssw15-rteElement-FigureBad">A.  Create a shortcut in windows, then upload the shortcut file (.url) to the document library.</dd><dd class="ssw15-rteElement-FigureGood">B. Use "Link to a document" content type in SharePoint.</dd><br></div></div></div>
<br><excerpt class='endintro'></excerpt><br>
<p class="ssw15-rteElement-P">Details on how you to create a link to a document in a SharePoint library.</p><p class="ssw15-rteElement-P"><strong>A. Create a shortcut in windows, then upload the shortcut file (.url) to the document library. </strong></p><p class="ssw15-rteElement-P">To do this, you need to remove .url file type from your blocked file types in your web application. This will bring some security risk, which is not recommended, and I won't show the step details here.</p><p class="ssw15-rteElement-P"><strong>B. Use "Link to a document" content type in SharePoint.</strong><br></p><p class="ssw15-rteElement-P">1) Enable "Content Type management" in your document library.</p><dl class="ssw15-rteElement-ImageArea"><img alt="EnableContentTypeDocument.png" src="EnableContentTypeDocument.png" style="margin:5px;" /></dl><dd class="ssw15-rteElement-FigureNormal">Figure: Enable Content Type management in library setting</dd><p class="ssw15-rteElement-P">2) Add "Link to a Document" content type into the library.</p><dl class="ssw15-rteElement-ImageArea"><img alt="AddExistContentType.png" src="AddExistContentType.png" style="margin:5px;width:650px;" /></dl><dd class="ssw15-rteElement-FigureNormal">Figure: Add from existing site content type</dd><dl class="ssw15-rteElement-ImageArea"><img alt="SelectLinkToADocumentType.png" src="SelectLinkToADocumentType.png" style="margin:5px;width:650px;" /></dl><dd class="ssw15-rteElement-FigureNormal">Figure: Select "Link to a Document" content type</dd><p>3) Create a "Link to a document" instance<br></p><dl class="ssw15-rteElement-ImageArea"><img alt="CreateLinkToADocumentInstance.png" src="CreateLinkToADocumentInstance.png" style="margin:5px;" /></dl><dd class="ssw15-rteElement-FigureNormal">Figure: select "File | New Document (dropdown) | Link to a document"</dd><dl class="ssw15-rteElement-ImageArea"><img alt="InputLinkUrlAndName.png" src="InputLinkUrlAndName.png" style="margin:5px;" /></dl><dd class="ssw15-rteElement-FigureNormal">Figure: Input "Name" and "URL"</dd><p class="ssw15-rteElement-P">4) Done<br></p><p class="ssw15-rteElement-P">You should be able to see the link type document in your library:</p><dl class="ssw15-rteElement-ImageArea"><img alt="LinksTypeDocumentsWithShortcutIcon.png" src="LinksTypeDocumentsWithShortcutIcon.png" data-pin-nopin="true" style="margin:5px;" /></dl><dd class="ssw15-rteElement-FigureNormal">Figure: Link type documents with the lovely shortcut icon</dd>


