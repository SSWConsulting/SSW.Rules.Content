---
type: rule
archivedreason: 
title: Customization - Do you check custom JavaScript with the CRM Custom Code Validation Tool?
guid: 48302773-5fa3-440a-a9d1-e92c4c33bc21
uri: customization-do-you-check-custom-javascript-with-the-crm-custom-code-validation-tool
created: 2013-06-28T05:11:16.0000000Z
authors:
- title: Mehmet Ozdemir
  url: https://ssw.com.au/people/mehmet-ozdemir
related: []
redirects: []

---


​As of the December 2012 Service Update (online) and Rollup 12 (on-prem) CRM HTML Components (HTC) are disabled by default. This means any JavaScript that references the V4 API will fail. Using the CRM Custom Code Validation Tool will help you to track down this legacy code and update it. It is not recommend to  re-enable the HTC controls as it will just create more problems down the track.
<br><excerpt class='endintro'></excerpt><br>
<p>​</p><p>To use the CRM 2011 Custom Code Validation Tool, download the zip file from Microsoft and install the solution into CRM2011. Once installed in CRM you will be able to run the validation tool over the custom JavaScript. Issues in red highlight deprecated functions and should be fixed immediately, issues in blue are uses of undocumented functions, while not as important they should also be checked.</p><p><img class="ssw-rteStyle-ImageArea" alt="CRM-2011-Custom-Code-Validation-Tool.png" src="CRM-2011-Custom-Code-Validation-Tool.png" style="margin:5px;" /> </p><p><span class="ssw-rteStyle-FigureNormal">Figure: Using Custom Code Verification Tool</span></p><p>Download the CRM 2011 Custom Code Validation Tool from: <a href="http://www.microsoft.com/en-us/download/details.aspx?id=30151"><span style="text-decoration:underline;"><font color="#0066cc">http://www.microsoft.com/en-us/download/details.aspx?id=30151</font></span></a></p><p> </p>


