---
type: rule
title: Customization - Do you check custom JavaScript with the CRM Custom Code Validation Tool?
uri: customization---do-you-check-custom-javascript-with-the-crm-custom-code-validation-tool
created: 2013-06-28T05:11:16.0000000Z
authors:
- id: 32
  title: Mehmet Ozdemir

---



<span class='intro'> ​As of the December 2012 Service Update (online) and Rollup 12 (on-prem) CRM HTML Components (HTC) are disabled by default. This means any JavaScript that references the V4&#160;API will fail. Using the CRM Custom Code Validation Tool will help you to track down this legacy code and update it. It is not recommend to  re-enable the HTC controls as it will just create more problems down the track. </span>

<p>​</p><p>To use the CRM 2011&#160;Custom Code Validation Tool, download the zip file from Microsoft and install the solution into CRM2011. Once installed in CRM you will be able to run the validation tool over the custom JavaScript. Issues in red highlight deprecated functions and should be fixed immediately, issues in blue are uses of undocumented functions, while not as important they should also be checked.</p><p><img class="ssw-rteStyle-ImageArea" alt="CRM-2011-Custom-Code-Validation-Tool.png" src="/PublishingImages/CRM-2011-Custom-Code-Validation-Tool.png" style="margin&#58;5px;" />&#160;</p><p><span class="ssw-rteStyle-FigureNormal">Figure&#58; Using Custom Code Verification Tool</span></p><p>Download the CRM 2011 Custom Code Validation Tool from&#58; <a href="http&#58;//www.microsoft.com/en-us/download/details.aspx?id=30151"><span style="text-decoration&#58;underline;"><font color="#0066cc">http&#58;//www.microsoft.com/en-us/download/details.aspx?id=30151</font></span></a></p><p>&#160;</p>


