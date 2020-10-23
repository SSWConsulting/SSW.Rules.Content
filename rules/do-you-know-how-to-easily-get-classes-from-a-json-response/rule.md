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


​​When integrating with external&#160;Web APIs which return a JSON response, there is a quick and easy way to generate classes to handle that response.<br>
<br><excerpt class='endintro'></excerpt><br>
<p><br></p><p>If the API specification is published as per&#160;​our rule&#58;&#160;<a href="/_layouts/15/FIXUPREDIRECT.ASPX?WebId=3dfc0e07-e23a-4cbb-aac2-e778b71166a2&amp;TermSetId=07da3ddf-0924-4cd2-a6d4-a4809ae20160&amp;TermId=479faffd-2049-40c0-bb48-850f594edc79">Do you document your Web API?</a></p><p>You can automatically generate your classes from that specification. See our other rule on how to do this&#58;&#160;<a href="/_layouts/15/FIXUPREDIRECT.ASPX?WebId=3dfc0e07-e23a-4cbb-aac2-e778b71166a2&amp;TermSetId=07da3ddf-0924-4cd2-a6d4-a4809ae20160&amp;TermId=df991c05-7dfa-4a2c-b559-4ea6879c6451">Do you know the best way to generate your classes from swagger?<br>​</a><br>If the specification isn't publised you need to generate your clases from the response you get from calling the API. Here is a trick to do that.<br><br></p><p>​Execute the request, and copy the text of the JSON response.<br></p><p><img src="/PublishingImages/8-08-2014-3-41-23-PM-compressor.png" alt="8-08-2014-3-41-23-PM-compressor.png" style="margin&#58;5px;width&#58;650px;" /><br></p><p>Create a new class in Visual Studio, and&#160;<span style="line-height&#58;1.6;">Click Edit | Paste Special | Past As JSON Classes and classes will be generated from the JSON in the clipboard.</span></p><p><span style="line-height&#58;1.6;"><img src="/PublishingImages/8-08-2014-3-53-17-PM-compressor.png" alt="8-08-2014-3-53-17-PM-compressor.png" style="margin&#58;5px;" /><br><strong>Figure&#58; Edit | Paste Special | Paste JSON As Classes</strong></span></p><p><span style="line-height&#58;1.6;"><img src="/PublishingImages/8-08-2014-3-56-34-PM-compressor.png" alt="8-08-2014-3-56-34-PM-compressor.png" style="margin&#58;5px;" /><br><strong>Figure&#58; Classes generated from the JSON</strong></span></p><p><span style="line-height&#58;1.6;">The results may need cleaning up a little bit, but it</span><span style="line-height&#58;1.6;">s much easier than trying to write them manually.</span><br></p><p><br></p>


