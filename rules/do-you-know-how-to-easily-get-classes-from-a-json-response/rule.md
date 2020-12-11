---
type: rule
archivedreason: 
title: Do you know how to easily get classes from a JSON response?
guid: 05fa3ae4-72b0-411b-90bd-3c0c191737f0
uri: do-you-know-how-to-easily-get-classes-from-a-json-response
created: 2014-08-08T05:26:43.0000000Z
authors:
- id: 38
  title: Drew Robson
related: []

---

When integrating with external Web APIs which return a JSON response, there is a quick and easy way to generate classes to handle that response.

<!--endintro-->



If the API specification is published as per our rule: [Do you document your Web API?](/_layouts/15/FIXUPREDIRECT.ASPX?WebId=3dfc0e07-e23a-4cbb-aac2-e778b71166a2&TermSetId=07da3ddf-0924-4cd2-a6d4-a4809ae20160&TermId=479faffd-2049-40c0-bb48-850f594edc79)

You can automatically generate your classes from that specification. See our other rule on how to do this: [Do you know the best way to generate your classes from swagger?](/_layouts/15/FIXUPREDIRECT.ASPX?WebId=3dfc0e07-e23a-4cbb-aac2-e778b71166a2&TermSetId=07da3ddf-0924-4cd2-a6d4-a4809ae20160&TermId=df991c05-7dfa-4a2c-b559-4ea6879c6451)
If the specification isn't publised you need to generate your clases from the response you get from calling the API. Here is a trick to do that.

Execute the request, and copy the text of the JSON response.


![](8-08-2014-3-41-23-PM-compressor.png)

Create a new class in Visual Studio, and Click Edit | Paste Special | Past As JSON Classes and classes will be generated from the JSON in the clipboard.


![Edit | Paste Special | Paste JSON As Classes](8-08-2014-3-53-17-PM-compressor.png)


![Classes generated from the JSON](8-08-2014-3-56-34-PM-compressor.png)

The results may need cleaning up a little bit, but its much easier than trying to write them manually.
