---
type: rule
title: When do you use Silverlight?
uri: when-do-you-use-silverlight
created: 2011-06-22T04:51:27.0000000Z
authors:
- id: 1
  title: Adam Cogan

---



<span class='intro'> There is a place for Silverlight, but it can only be the 'richer' experience.&#160;In some case it is better not to use Silverlight for Data Entry Form and also content publisher should have alternative of Silverlight for Andriod &amp; iOS user. 
 </span>


  <p>
    <strong class="ms-rteThemeFontFace-1 ms-rteFontSize-2">Mobile Device&#58; <br>
<br>
<img alt="Silverlight in iPad doesn't work" src="/PublishingImages/SilverlightInIPad.png" /><br>
&#160;&#160;&#160;&#160;Figure&#58; Silverlight does not work on an iPad, It can't be only experience.&#160;</strong> <strong class="ms-rteThemeFontFace-1 ms-rteFontSize-2"><br>
&#160;&#160;&#160;&#160;</strong> <span class="ms-rteThemeFontFace-1 ms-rteFontSize-2"></span><span class="ms-rteThemeFontFace-1 ms-rteFontSize-2">Further Reading&#58; </span><a href="http&#58;//www.pcworld.com/article/193540/ipad_proves_that_apple_wants_to_kill_flash.html" class="ms-rteThemeFontFace-1 ms-rteFontSize-2" target="_blank">PCWorld</a>.&#160;</p>
<div style="text-align&#58;left;"><strong>Data Entry Forms</strong></div>
<div style="text-align&#58;left;">NO. HTML must be the default experience. Microsoft says for Business Apps, but be careful. Silverlight is *Not* for data entry forms. Tab Index Implement is very hard and end result isn’t consistent among popular browser. Users frequently uses tab to move from Text Box to another Text Box and require consistence experience while entering data using different browser. HTML 5 introduced autofocus, placeholder and validation feature which is useful for creating consistent Data Entry form for various browser.</div>
<div style="text-align&#58;left;">&#160;Useful Links&#58; <a href="http&#58;//www.xoriant.com/blog/software-product-development/html5-series-part-3-html5-form-elements.html" target="_blank">HTML 5 Form Elements</a></div>
<div style="text-align&#58;left;">&#160;</div>
<div style="text-align&#58;left;"><strong>Microphone or Camera </strong></div>
<div style="text-align&#58;left;">YES, You can access camera &amp; microphone from Silverlight. System.Windows. Media.CaptureSource object provides methods and properties used to work with audio and video capture devices. In essence, CaptureSource is like a little media player. After video being captured, We can give ShaderEffect&#160; or manipulate captured still image. </div>
<div style="text-align&#58;left;">Useful links&#58; <a href="http&#58;//www.silverlight.net/learn/videos/silverlight-4-videos/access-web-camera-microphone/" target="_blank">Learning Video</a>&#160; &amp; <a href="http&#58;//www.silverlightshow.net/items/Capturing-the-Webcam-in-Silverlight-4.aspx" target="_blank">Blog from SilverlightsShow</a></div>
<div style="text-align&#58;left;">&#160;</div>
<div style="text-align&#58;left;"><strong>Socket Communication </strong></div>
<div style="text-align&#58;left;">YES. System.Net.Sockets.Socket Class provides a set of methods and properties for network communications. The Socket class allows you to perform asynchronous data transfer using any of the communication protocols listed in the ProtocolType enumeration. Currently, the only supported ProtocolType is the TCP protocol. Supported Version Silverlight 4 &amp; 3 . <a href="http&#58;//msdn.microsoft.com/en-us/library/system.net.sockets.socket%28v=vs.95%29.aspx" class="ms-rteCustom-External" target="_blank">MSDN – Socket Class</a></div>
<div style="text-align&#58;left;"><strong></strong>&#160;</div>
<div style="text-align&#58;left;">
<div><strong>For interactive charts in a BI (</strong><em><strong>Business Intelligence</strong></em><strong>) solution </strong></div>
<div>NO. There are some aftermarket solutions available. Notable are Telerik Silverlight Control ,&#160;<a href="http&#58;//www.infragistics.com/dotnet/netadvantage/silverlight/data-visualization.aspx" target="_blank">Infragistics </a>Silverlight Data Visualization. <a href="http&#58;//www.telerik.com/products/new-silverlight-controls.aspx" target="_blank">Telerik</a> provides BI solution using Advanced GridView, Charts with zooming, scrolling, multi-level resource grouping. Both solutions use shared API across Silverlight and WPF, as a result product user can visualize data in more flexible way. </div>
<div>&#160;</div>
</div>
<div style="text-align&#58;left;"><strong>For Richer TextBox</strong></div>
<div style="text-align&#58;left;">YES. Using Silverlight Rich TextBox user can format Text, insert image, DataGrid, Calendar, display Text right-to-left, print content and can access clipboard. Accessing <a href="http&#58;//msdn.microsoft.com/en-us/library/system.windows.clipboard%28v=vs.95%29.aspx" target="_blank">Clipboard</a> can be implemented by using Clipboard Object. Selected Text context can be implemented using <a href="http&#58;//msdn.microsoft.com/en-us/library/system.windows.controls.primitives.popup%28v=vs.95%29.aspx" target="_blank">Popup</a> Control.&#160; <a href="http&#58;//msdn.microsoft.com/en-us/library/ff426926%28v=vs.95%29.aspx" class="ms-rteCustom-External" target="_blank">Sample in MSDN</a> </div>
<div style="text-align&#58;left;">&#160;</div>
<div style="text-align&#58;left;"><strong>For mapping apps</strong></div>
<div style="text-align&#58;left;">YES. Microsoft.Maps.MapControl provides functionality to access Bing Maps. Using script a site can implement map feature by referencing the Bing Maps Silverlight Control XAP file in an object tag. Here are some sample applications&#58;&#160; <a href="http&#58;//www.microsoft.com/maps/isdk/silverlight/" class="ms-rteCustom-External" target="_blank">Microsoft Bing Map</a>&#160;&amp; <a href="http&#58;//deepearth.codeplex.com/" class="ms-rteCustom-External" target="_blank">DeepEarth Project</a></div>
<div style="text-align&#58;left;">&#160;</div>
<div style="text-align&#58;left;"><strong>Slow Response</strong></div>
<div style="text-align&#58;left;">The initial slow response is due to downloading of the .xap file. This is not an issue since it is a one-time download and the user gets a fast response with later interaction. For later visits, user will not face slow response issue as browser already cached the data. Also check out rules - <a href="/Pages/Do-you-use-dynamic-application-loading-in-Silverlight.aspx" target="_blank">Do you use dynamic application loading in Silverlight</a></div>



