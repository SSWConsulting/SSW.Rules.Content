---
type: rule
title: Do you know how to use Connection String in .NET 2.0?
uri: do-you-know-how-to-use-connection-string-in-net-20
created: 2009-05-08T08:53:04.0000000Z
authors:
- id: 1
  title: Adam Cogan
- id: 17
  title: Ryan Tee

---



<span class='intro'> In .NET 1.1 we used to store our connection string in a configuration file like this&#58; 
 </span>


  <p>&#160;</p>
<dl class="goodCode">
    <dt style="width&#58;92.01%;height&#58;134px;">
    <pre>&lt;configuration&gt;<br>     &lt;appSettings&gt;<br>          &lt;add key=&quot;ConnectionString&quot; value =&quot;integrated security=true;<br>           data source=(local);initial catalog=Northwind&quot;/&gt;<br>     &lt;/appSettings&gt;<br>&lt;/configuration&gt;</pre>
    </dt>
</dl>
<p>and access this connection string in code like this&#58;</p>
<dl class="badCode">
    <dt style="width&#58;92.01%;height&#58;74px;">
    <pre>SqlConnection sqlConn = <br>new SqlConnection(System.Configuration.ConfigurationSettings.<br>AppSettings[&quot;ConnectionString&quot;]);                        </pre>
    </dt>
    <dd>Bad example - old ASP.NET 1.1 way, untyped and prone to error. </dd>
</dl>
<p>In .NET 2.0 you can access it in another way</p>
<p>Step 1&#58; Setup your settings in your common project. E.g. Northwind.Common </p>
<dl class="image">
    <dt><img style="border-bottom&#58;0px solid;border-left&#58;0px solid;border-top&#58;0px solid;border-right&#58;0px solid;" border="0" alt="Settings in Project Properties" src="/Standards/SoftwareDevelopment/RulesToBetterDotNETProjects/PublishingImages/ConnStringNET2_Settings.jpg" /> </dt>
    <dd>Figure&#58; Settings in Project Properties</dd>
</dl>
<p>Step 2&#58; Open up the generated App.config under your common project. E.g. Northwind.Common/App.config </p>
<dl class="image">
    <dt><img style="border-bottom&#58;0px solid;border-left&#58;0px solid;border-top&#58;0px solid;border-right&#58;0px solid;" border="0" alt="Auto generated app.config" src="/Standards/SoftwareDevelopment/RulesToBetterDotNETProjects/PublishingImages/ConnStringNET2_CommonApp.GIF" /> </dt>
    <dd>Figure&#58; Auto generated app.config</dd>
</dl>
<p>Step 3&#58; <s>Copy the content into your entry applications app.config. E.g. Northwind.WindowsUI/App.config</s> The new setting has been updated to app.config automatically in .NET 2.0 </p>
<dl class="badCode">
    <dt style="width&#58;92.31%;height&#58;184px;">
    <pre> &lt;configuration&gt;<br>      &lt;connectionStrings&gt;<br>         &lt;add name=&quot;Common.Properties.Settings.NorthwindConnectionString&quot;<br>              connectionString=&quot;Data Source=(local);Initial Catalog=Northwind;<br>              Integrated Security=True&quot;<br>              providerName=&quot;System.Data.SqlClient&quot; /&gt;<br>        &lt;/connectionStrings&gt;<br> &lt;/configuration&gt;                        </pre>
    </dt>
</dl>
<p>Then you can access the connection string like this in C#</p>
<dl class="goodCode">
    <dt style="width&#58;93.36%;height&#58;59px;">
    <pre>SqlConnection sqlConn =<br> new SqlConnection(Common.Properties.Settings.Default.NorthwindConnectionString);                                </pre>
    </dt>
    <dd>Good example - access our connection string by strongly typed generated settings class. </dd>
</dl>
<div class="greyBox">
<p>Please note these steps does not work for web site model in Visual Studio 2005. However, they work for other projects such as Windows Form, Console application, Class Library and Web Application Project. </p>
<p>This is not an issue in a well designed website, since it's connection string will be defined in the <b>data layer</b> and you can overwrite this connection string in your web.config. </p>
</div>



