---
type: rule
archivedreason: Deprecated
title: Do you add the necessary code so you can always sync the web.config file?
guid: b497a0ee-eccc-4817-9033-a0338bee0542
uri: do-you-add-the-necessary-code-so-you-can-always-sync-the-web-config-file
created: 2009-04-28T02:05:28.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: Ryan Tee
  url: https://ssw.com.au/people/ryan-tee
  noimage: true
related: []
redirects: []

---

The Web.config file should be your main source where you store your application settings. These change, depending on which system you are working on, e.g. your local machine or the website. That's why you have to keep two versions of the Web.config file, one for your local machine and one for the website. 
 That's annoying, not really efficient and often the cause of problems. 
 
<!--endintro-->

In the following extract of a sample Web.config file you can see the problem. The local machine "HIPPO" has, of course, another WebServiceURL than the Webserver "SEAL". So you have to keep two versions of the Web.config file, one when working on "HIPPO" and one when working on "SEAL".


```xml
<add key="SEAL_WebServiceURL"
    value="http://host.something.com:80/SomeDirectory/Filename.asmx"/> 
<add key="HIPPO_WebServiceURL"
    value="http://name:80/SomeDirectory/Filename.asmx"/>
```
**Figure: Sample Web.config file**

There is a better solution:


```vb
Public Shared Function GetWebConfigString(ByVal StringName As String) As String
Dim strReturn As String = ""
Dim strComputerName As String = System.Net.Dns.GetHostName
Try
strReturn = ConfigurationSettings.AppSettings( strComputerName.ToUpper _
+ "_"+ StringName)
Catch
strReturn = ConfigurationSettings.AppSettings(StringName)
End Try
Return strReturn
End Function
```
**Figure: Sample Get WebConfigString Class**

This class simply adds the name of the Computer on which it is running on to the WebConfigString. In the former example, this would be "HIPPO\_" or "SEAL\_".

Instead of using the WebConfigString directly you can now transform it using this function. With the help of this code, you always get the right value for the WebConfigString, no matter on which machine the application runs and you don't have to care about synchronizing the Web.config file any more.
