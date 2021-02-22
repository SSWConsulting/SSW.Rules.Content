---
type: rule
archivedreason: 
title: When do you use Silverlight?
guid: d79f0830-78cc-4713-883e-8d752f7339c7
uri: when-do-you-use-silverlight
created: 2011-06-22T04:51:27.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects: []

---


There is a place for Silverlight, but it can only be the 'richer' experience. In some cases, it is better not to use Silverlight for Data Entry Form and also content publisher should have the alternative to Silverlight for Androi​d & iOS users. 
<br>
<br><excerpt class='endintro'></excerpt><br>
<p class="ssw15-rteElement-P"> <b>Mobile Device​</b><br></p><dl class="image"><dt> 
      <img alt="Silverlight in iPad doesn't work" src="SilverlightInIPad.png" /> 
   </dt><dd>Figure: Silverlight does not work on an iPad, It can't be the only experience</dd></dl><p>Further Reading: 
   <a href="http://www.pcworld.com/article/193540/ipad_proves_that_apple_wants_to_kill_flash.html" target="_blank">PCWorld</a>.</p><div>
   <strong>Data Entry Forms</strong></div><div style="text-align:left;">NO. HTML must be the default experience. Microsoft says for Business Apps, but be careful. Silverlight is *Not* for data entry forms. Tab Index Implement is very hard and end result isn’t consistent among the popular browsers. Users frequently use tab to move from Text Box to another Text Box and require consistent experience while entering data using a different browser. HTML 5 introduced autofocus, placeholder and validation feature which is useful for creating consistent Data Entry form for various browser.<br></div><div style="text-align:left;">Useful Links: 
   <a href="https://www.w3schools.com/html/html_form_elements.asp" target="_blank">HTML 5 Form Elements</a>  </div><div style="text-align:left;"> </div><div style="text-align:left;">
   <strong>Microphone or Camera </strong></div><div style="text-align:left;">YES, You can access the camera & microphone from Silverlight. System.Windows. Media.CaptureSource object provides methods and properties used to work with audio and video capture devices. In essence, CaptureSource is like a little media player. After the video being captured, We can give ShaderEffect or manipulate captured still image.<br></div><div style="text-align:left;">Useful links: 
   <a href="http://www.silverlight.net/learn/videos/silverlight-4-videos/access-web-camera-microphone/" target="_blank">Learning Video</a> </div><div style="text-align:left;"> </div><div style="text-align:left;">
   <strong>Socket Communication </strong></div><div style="text-align:left;">YES. System.Net.Sockets.Socket Class provides a set of methods and properties for network communications. The Socket class allows you to perform asynchronous data transfer using any of the communication protocols listed in the ProtocolType enumeration. Currently, the only supported ProtocolType is the TCP protocol. Supported Version Silverlight 4 & 3. 
   <a href="http://msdn.microsoft.com/en-us/library/system.net.sockets.socket%28v=vs.95%29.aspx">MSDN – Socket Class</a><br><br></div><div style="text-align:left;"><div>
      <strong>For interactive charts in a BI (</strong><em><strong>Business Intelligence</strong></em><strong>) solution </strong></div><div>NO. There are some aftermarket solutions available. Notable are Telerik Silverlight Control, <a href="http://www.infragistics.com/dotnet/netadvantage/silverlight/data-visualization.aspx" target="_blank">Infragistics </a>  Silverlight Data Visualization. 
      <a href="http://www.telerik.com/products/new-silverlight-controls.aspx" target="_blank">Telerik</a> provides BI solution using Advanced GridView, Charts with zooming, scrolling, multi-level resource grouping. Both solutions use shared API across Silverlight and WPF, as a result product users can visualize data in more flexible way. </div><div> </div></div><div style="text-align:left;">
   <strong>For Richer TextBox</strong></div><div style="text-align:left;">YES. Using Silverlight Rich TextBox user can format Text, insert image, DataGrid, Calendar, display Text right-to-left, print content, and can access clipboard. Accessing 
   <a href="http://msdn.microsoft.com/en-us/library/system.windows.clipboard%28v=vs.95%29.aspx" target="_blank">Clipboard</a> can be implemented by using Clipboard Object. Selected Text context can be implemented using 
   <a href="http://msdn.microsoft.com/en-us/library/system.windows.controls.primitives.popup%28v=vs.95%29.aspx" target="_blank">Popup</a>   Control. 
   <a href="http://msdn.microsoft.com/en-us/library/ff426926%28v=vs.95%29.aspx" target="_blank">Sample in MSDN</a>​<br></div><div style="text-align:left;"> </div><div style="text-align:left;">
   <strong>For mapping apps</strong></div><div style="text-align:left;">YES. Microsoft.Maps.MapControl provides functionality to access Bing Maps. Using script a site can implement map feature by referencing the Bing Maps Silverlight Control XAP file in an object tag. Here are some sample applications:  
   <a href="http://www.microsoft.com/maps/isdk/silverlight/" target="_blank">Microsoft Bing Map</a> & 
   <a href="http://deepearth.codeplex.com/" target="_blank">DeepEarth Project</a>  </div><div style="text-align:left;"> </div><div style="text-align:left;">
   <strong>Slow Response</strong></div><div style="text-align:left;">The initial slow response is due to downloading of the .xap file. This is not an issue since it is a one-time download and the user gets a fast response with later interaction. For later visits, the user will not face a slow response issue as the browser already cached the data. Also, check out rules - 
   <a href="/Pages/Do-you-use-dynamic-application-loading-in-Silverlight.aspx" target="_blank">Do you use dynamic application loading in Silverlight</a>?  </div>


