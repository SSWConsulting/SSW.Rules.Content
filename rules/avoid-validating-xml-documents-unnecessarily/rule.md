---
type: rule
archivedreason: 
title: Do you avoid validating XML documents unnecessarily?
guid: d65b2247-f519-4257-b304-bb81be2581d6
uri: avoid-validating-xml-documents-unnecessarily
created: 2018-04-25T19:38:17.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
- do-you-avoid-validating-xml-documents-unnecessarily

---

Validating an XML document against a schema is expensive, and should not be done where it is not absolutely necessary. Combined with weight the XML document object, validation can cause a significant performance hit:

* Read with XmlValidatingReader: 172203 nodes - 812 ms
* Read with XmlTextReader: 172203 nodes - 320 ms
* Parse using XmlDocument no validation - length 1619608 - 1052 ms
* Parse using XmlDocument with XmlValidatingReader: length 1619608 - 1862 ms


You can disable validation when using the XmlDocument object by passing an XmlTextReader instead of the XmlValidatingTextReader:

<!--endintro-->

``` js
XmlDocument report = new XmlDocument();
 XmlTextReader tr = new XmlTextReader(Configuration.LastReportPath);
 report.Load(tr);
```

To perform validation:

``` js
XmlDocument report = new XmlDocument();
 XmlTextReader tr = new XmlTextReader(Configuration.LastReportPath);
 XmlValidatingReader reader = new XmlValidatingReader(tr);
 report.Load(reader);
```

The XSD should be distributed in the same directory as the XML file and a relative path should be used:

``` xml
<Report> <Report xmlns="LinkAuditorReport.xsd">
 ... </Report>
```
