---
type: rule
title: Do you add the necessary code so you can always sync the web.config file?
uri: do-you-add-the-necessary-code-so-you-can-always-sync-the-webconfig-file
created: 2009-04-28T02:05:28.0000000Z
authors:
- id: 1
  title: Adam Cogan
- id: 17
  title: Ryan Tee

---



<span class='intro'> The Web.config file should be your main source where you store your application settings. These change, depending on which system you are working on, e.g. your local machine or the website. That's why you have to keep two versions of the Web.config file, one for your local machine and one for the website. <br>
That's annoying, not really efficient and often the cause of problems. 
 </span>


  <p>In the following extract of a sample Web.config file you can see the problem. The local machine &quot;HIPPO&quot; has, of course, another WebServiceURL than the Webserver &quot;SEAL&quot;. So you have to keep two versions of the Web.config file, one when working on &quot;HIPPO&quot; and one when working on &quot;SEAL&quot;. </p>
<pre class="brush&#58;c-sharp">&lt;add key=&quot;SEAL_WebServiceURL&quot;
    value=&quot;http&#58;//host.something.com&#58;80/SomeDirectory/Filename.asmx&quot;/&gt; 
    &lt;add key=&quot;HIPPO_WebServiceURL&quot;
    value=&quot;http&#58;//name&#58;80/SomeDirectory/Filename.asmx&quot;/&gt;</pre>
<span class="ms-rteCustom-FigureGood">Figure&#58; Sample Web.config file</span>
<p>There is a better solution&#58; </p>
<pre class="brush&#58;c-sharp">Public Shared Function GetWebConfigString(ByVal StringName As String) As String
Dim strReturn As String = &quot;&quot;
Dim strComputerName As String = System.Net.Dns.GetHostName
Try
strReturn = ConfigurationSettings.AppSettings( strComputerName.ToUpper _
+ &quot;_&quot;+ StringName)
Catch
strReturn = ConfigurationSettings.AppSettings(StringName)
End Try
Return strReturn
End Function</pre>
<span class="ms-rteCustom-FigureGood">Figure&#58; Sample Get WebConfigString Class</span>
<p>This class simply adds the name of the Computer on which it is running on to the WebConfigString. In the former example, this would be &quot;HIPPO_&quot; or &quot;SEAL_&quot;.</p>
<p>Instead of using the WebConfigString directly you can now transform it using this function. With the help of this code, you always get the right value for the WebConfigString, no matter on which machine the application runs and you don't have to care about synchronizing the Web.config file any more.</p>



