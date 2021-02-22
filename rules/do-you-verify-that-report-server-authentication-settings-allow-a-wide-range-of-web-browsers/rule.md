---
type: rule
archivedreason: 
title: Do you verify that Report Server authentication settings allow a wide range of web browsers?
guid: 9a16aad2-92d9-49f0-85e4-cc7746778d06
uri: do-you-verify-that-report-server-authentication-settings-allow-a-wide-range-of-web-browsers
created: 2017-11-16T22:04:23.0000000Z
authors:
- title: Greg Harris
  url: https://ssw.com.au/people/greg-harris
related: []
redirects: []

---

The default configuration for Report Server isn't accessible by most mobile browsers and some desktop browsers too. You can adjust the authentication types allowed to increase the range.





<!--endintro-->

The configuration file for the Report Server is named RSReportServer.config and the default location is C:\Program Files\Microsoft SQL Server\MSRS13.MSSQLSERVER\Reporting Services\ReportServer\

You should make a backup of the configuration before editing it so you can rollback if you make a mistake.

We normally change the AuthenticationTypes node from:

&lt;AuthenticationTypes&gt;
                            &lt;RSWindowsNegotiate /&gt;  
              &lt;/AuthenticationTypes&gt;
 
to:
 
              &lt;AuthenticationTypes&gt;
                            &lt;RSWindowsNegotiate /&gt;  
                            &lt;RSWindowsKerberos /&gt;  
                            &lt;RSWindowsNTLM /&gt;  
              &lt;/AuthenticationTypes&gt;

Check out the different [Authentication Types in the Report Server documentation](https&#58;//technet.microsoft.com/en-us/library/cc281310%28v=sql.105%29.aspx) and select the types that suit your needs.

More details on configuring windows authentication on the report server can be found [here](https&#58;//docs.microsoft.com/en-us/sql/reporting-services/security/configure-windows-authentication-on-the-report-server).
