---
type: rule
archivedreason: 
title: Do you know how to use Connection String in .NET 2.0?
guid: 2dec2ea4-3359-4bb0-8f30-c278c8735670
uri: do-you-know-how-to-use-connection-string-in-net-2-0
created: 2009-05-08T08:53:04.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: Ryan Tee
  url: https://ssw.com.au/people/ryan-tee
related: []
redirects: []

---


In .NET 1.1 we used to store our connection string in a configuration file like this: 

<br><excerpt class='endintro'></excerpt><br>

  <p> </p>
<dl class="goodCode">
    <dt style="width:92.01%;height:134px;">
    <pre>&lt;configuration&gt;<br>     &lt;appSettings&gt;<br>          &lt;add key="ConnectionString" value ="integrated security=true;<br>           data source=(local);initial catalog=Northwind"/&gt;<br>     &lt;/appSettings&gt;<br>&lt;/configuration&gt;</pre>
    </dt>
</dl>
<p>and access this connection string in code like this:</p>
<dl class="badCode">
    <dt style="width:92.01%;height:74px;">
    <pre>SqlConnection sqlConn = <br>new SqlConnection(System.Configuration.ConfigurationSettings.<br>AppSettings["ConnectionString"]);                        </pre>
    </dt>
    <dd>Bad example - old ASP.NET 1.1 way, untyped and prone to error. </dd>
</dl>
<p>In .NET 2.0 you can access it in another way</p>
<p>Step 1: Setup your settings in your common project. E.g. Northwind.Common </p>
<dl class="image">
    <dt><img style="border-bottom:0px solid;border-left:0px solid;border-top:0px solid;border-right:0px solid;" border="0" alt="Settings in Project Properties" src="ConnStringNET2_Settings.jpg" /> </dt>
    <dd>Figure: Settings in Project Properties</dd>
</dl>
<p>Step 2: Open up the generated App.config under your common project. E.g. Northwind.Common/App.config </p>
<dl class="image">
    <dt><img style="border-bottom:0px solid;border-left:0px solid;border-top:0px solid;border-right:0px solid;" border="0" alt="Auto generated app.config" src="ConnStringNET2_CommonApp.GIF" /> </dt>
    <dd>Figure: Auto generated app.config</dd>
</dl>
<p>Step 3: <s>Copy the content into your entry applications app.config. E.g. Northwind.WindowsUI/App.config</s> The new setting has been updated to app.config automatically in .NET 2.0 </p>
<dl class="badCode">
    <dt style="width:92.31%;height:184px;">
    <pre> &lt;configuration&gt;<br>      &lt;connectionStrings&gt;<br>         &lt;add name="Common.Properties.Settings.NorthwindConnectionString"<br>              connectionString="Data Source=(local);Initial Catalog=Northwind;<br>              Integrated Security=True"<br>              providerName="System.Data.SqlClient" /&gt;<br>        &lt;/connectionStrings&gt;<br> &lt;/configuration&gt;                        </pre>
    </dt>
</dl>
<p>Then you can access the connection string like this in C#</p>
<dl class="goodCode">
    <dt style="width:93.36%;height:59px;">
    <pre>SqlConnection sqlConn =<br> new SqlConnection(Common.Properties.Settings.Default.NorthwindConnectionString);                                </pre>
    </dt>
    <dd>Good example - access our connection string by strongly typed generated settings class. </dd>
</dl>
<div class="greyBox">
<p>Please note these steps does not work for web site model in Visual Studio 2005. However, they work for other projects such as Windows Form, Console application, Class Library and Web Application Project. </p>
<p>This is not an issue in a well designed website, since it's connection string will be defined in the <b>data layer</b> and you can overwrite this connection string in your web.config. </p>
</div>



