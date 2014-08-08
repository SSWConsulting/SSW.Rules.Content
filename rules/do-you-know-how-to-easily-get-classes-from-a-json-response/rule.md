---
type: rule
archivedreason: 
title: Do you know how to easily get classes from a JSON response?
guid: 05fa3ae4-72b0-411b-90bd-3c0c191737f0
uri: do-you-know-how-to-easily-get-classes-from-a-json-response
created: 2014-08-08T05:26:43.0000000Z
authors:
- title: Drew Robson
  url: https://ssw.com.au/people/drew-robson
related: []
redirects: []

---


​When integrating with external&#160;Web APIs which return a JSON response, there is a quick and easy way to generate classes to handle that response.
<br><excerpt class='endintro'></excerpt><br>
<p>Execute the request, and copy the text of the JSON response.</p><p><img src="/SoftwareDevelopment/RulesToBetterWebAPI/PublishingImages/Pages/Do-you-know-how-to-easily-get-classes-from-a-JSON-response/8-08-2014-3-41-23-PM-compressor.png" alt="8-08-2014-3-41-23-PM-compressor.png" style="margin&#58;5px;width&#58;650px;" /><br></p><p>Create a new class in Visual Studio, and&#160;<span style="line-height&#58;1.6;">Click Edit | Paste Special | Past As JSON Classes and classes will be generated from the JSON in the clipboard.</span></p><p><span style="line-height&#58;1.6;"><img src="/SoftwareDevelopment/RulesToBetterWebAPI/PublishingImages/Pages/Do-you-know-how-to-easily-get-classes-from-a-JSON-response/8-08-2014-3-53-17-PM-compressor.png" alt="8-08-2014-3-53-17-PM-compressor.png" style="margin&#58;5px;" /><br><strong>Figure&#58; Edit | Paste Special | Paste JSON As Classes</strong></span></p><p><span style="line-height&#58;1.6;"><img src="/SoftwareDevelopment/RulesToBetterWebAPI/PublishingImages/Pages/Do-you-know-how-to-easily-get-classes-from-a-JSON-response/8-08-2014-3-56-34-PM-compressor.png" alt="8-08-2014-3-56-34-PM-compressor.png" style="margin&#58;5px;" /><br><strong>Figure&#58; Classes generated from the JSON</strong></span></p><p><span style="line-height&#58;1.6;">The results may need cleaning up a little bit, but it</span><span style="line-height&#58;1.6;">s much easier than trying to write them manually.</span><br></p><p><br></p>


