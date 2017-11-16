---
type: rule
title: Do you verify that Report Server authentication settings allow a wide range of web browsers?
uri: do-you-verify-that-report-server-authentication-settings-allow-a-wide-range-of-web-browsers
created: 2017-11-16T22:04:23.0000000Z
authors:
- id: 70
  title: Greg Harris

---



<span class='intro'> The default configuration for Report Server isn't accessable by most mobile browsers and some desktop browsers too. You can adjust the authentication types allowed to increase the range.<br> </span>

<p>​The configuration file for the Report Server is named&#160;RSReportServer.config and the default location is&#160;C&#58;\Program Files\Microsoft SQL Server\MSRS13.MSSQLSERVER\Reporting Services\ReportServer\</p><p>You should make a backup of the configuration before editing it so you can rollback if you make a mistake.</p><p>We normally change the AuthenticationTypes node from&#58;</p><p>&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; &lt;AuthenticationTypes&gt;<br>&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; &lt;RSWindowsNegotiate /&gt;&#160; <br>&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; &lt;/AuthenticationTypes&gt;<br>&#160;<br>to&#58;<br>&#160;<br>&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; &lt;AuthenticationTypes&gt;<br>&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; &lt;RSWindowsNegotiate /&gt;&#160; <br>&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; &lt;RSWindowsKerberos /&gt;&#160; <br>&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; &lt;RSWindowsNTLM /&gt;&#160; <br>&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; &lt;/AuthenticationTypes&gt;</p><p>Check out the different <a href="https&#58;//technet.microsoft.com/en-us/library/cc281310%28v=sql.105%29.aspx">Authentication Types in the Report Server documentation ​</a>and select the types that suit your needs.</p><p>More details on configuring windows authentication on the report server can be found <a href="https&#58;//docs.microsoft.com/en-us/sql/reporting-services/security/configure-windows-authentication-on-the-report-server">here​</a>.<br></p><p><br>&#160;</p><p><br>&#160;</p>


