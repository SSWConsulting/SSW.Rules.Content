---
type: rule
archivedreason: 
title: Do you avoid using ReportViewer local processing mode?
guid: d18272f4-c4b7-4d7b-be6a-b9729503615d
uri: avoid-using-reportviewer-local-processing-mode
created: 2016-11-11T18:00:54.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
- do-you-avoid-using-reportviewer-local-processing-mode

---

[ReportViewer control](https&#58;//www.ssw.com.au/ssw/redirect/msdn/ReportViewerControl.htm) is a powerful control designed for Windows application and Web application to process and display reports. This control can be configured to run in local processing mode and remote processing mode.

<!--endintro-->

* Local Processing Mode
This mode uses [client report definition (.rdlc) files](https&#58;//www.ssw.com.au/ssw/redirect/msdn/CreatingClientReportDefinition.htm), all report processing is performed on the computer that hosts the application. All data used by the report must be retrieved from data that the client application provides, so you have to configure the ReportViewer control's Data sources, Report parameters.
See [Configuring ReportViewer for Local Processing](https&#58;//www.ssw.com.au/ssw/redirect/msdn/ConfiguringReportViewer.htm) for more information.
* Remote Processing Mode
This mode needs the Microsoft SQL Server 2005 Reporting Services report server, The report server processes the data and renders the report into an output format. The ReportViewer control retrieves the finished report from the report server and displays it on the screen, so you have to configure the ReportViewer control's report server information. 
See [Configuring ReportViewer for Remote Processing](https&#58;//www.ssw.com.au/ssw/redirect/msdn/ConfiguringReportViewerforRemotProcessing.htm) for more information.


If you use local processing mode in your Web application, there are more configuration to do for the ReportViewer control, report processing will also slow down the web server.
