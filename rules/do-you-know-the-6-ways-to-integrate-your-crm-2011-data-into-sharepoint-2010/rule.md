---
type: rule
archivedreason: 
title: Do you know the 6 ways to integrate your CRM 2011 data into SharePoint 2010?
guid: c41308f6-7e9f-444a-85f4-20747adc0884
uri: do-you-know-the-6-ways-to-integrate-your-crm-2011-data-into-sharepoint-2010
created: 2011-08-24T03:52:23.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: Adam Stephensen
  url: https://ssw.com.au/people/adam-stephensen
- title: William Yin
  url: https://ssw.com.au/people/william-yin
related: []
redirects: []

---

You have data in CRM 2011, so how do you see it in SharePoint? The data that is stored in CRM entities should be available in SharePoint so users can find and use the data in areas such as:

* SharePoint search
* SharePoint reporting (if you are using SQL Reporting Services in integrated mode)


There are many ways to get to this data, let's go through them:

<!--endintro-->

### Option 1: SharePoint BCS Adapter (provided by the CRM Team) RECOMMENDED

This BCS Adapter for CRM 2011 is from the CRM team (It does all of the BCS work for you by interrogating the CRM metadata service).

Summary: SharePoint BCS -&gt; Pre-built Adapter (.NET Assembly) -&gt; CRM web services - &gt; CRM database


| Pros | Cons |
| --- | --- |
| ![clip_image002\[8\]](correct.gif "clip_image002[8]")Read/Write

![clip_image002\[9\]](correct.gif "clip_image002[9]")Minimal coding

![clip_image002\[10\]](correct.gif "clip_image002[10]")Easiest to implement

![clip_image002\[11\]](correct.gif "clip_image002[11]")The likely way forward (Best Practice as Microsoft) | ![clip_image004\[13\]](wrong.gif "clip_image004[13]")Needs to be deployed and published to the web server.

![clip_image004\[14\]](wrong.gif "clip_image004[14]")Less performance than SQL filter views directly

![clip_image004\[15\]](wrong.gif "clip_image004[15]")Only recently released. |


![](figure5.jpg)  

**More information:**    
    Download from Microsoft
    Read "*Connecting to CRM Online 2011 with SharePoint 2010 Business Connectivity Services*"
    Run tool to generate the XML mapping (.BDCM)
    This solution uses a BCS Connector – a .NET Assembly responsible for mapping external data into a form usable by SharePoint. This component is loaded and hosted within SharePoint 2010 and communicates with CRM via the CRM Proxy Service.

### Option 2: SQL Server Filtered Views

    CRM recommends that you \*don't\* read from the Tables, so they provide SQL Views for this purpose.
    Summary: SharePoint BCS -&gt; CRM database


| Pros | Cons |
| --- | --- |
| ![clip_image002\[2\]](correct.gif "clip_image002[2]")Best performance

![clip_image002\[2\]](correct.gif "clip_image002[2]")Codeless | ![clip_image004](wrong.gif "clip_image004")Read-only

![clip_image004\[1\]](wrong.gif "clip_image004[1]")Not available for hosted CRM

![clip_image004\[2\]](wrong.gif "clip_image004[2]") Security issues as you are exposing the view. |

    Filtered Views in Microsoft CRM provide access to the data available that supports providing picklist name and id values (lookup tables).
    **More information:**
    If you only want read-only for CRM on-premises data for SharePoint users, this solution is fine. You create the External Content Type directly against the Filtered Views in the CRM database.
    http://msdn.microsoft.com/en-us/library/gg328467.aspx

![Figure: The result of "SELECT * FROM FilteredCtx_Project". Use Office SharePoint Designer to hook this up](figure1.jpg)  

### Option 3: Web Services
    CRM provides web services.
    Summary: SharePoint BCS -&gt; Code calling CRM web services - &gt; CRM database


| Pros | Cons |
| --- | --- |
| ![clip_image002\[3\]](correct.gif "clip_image002[3]")Read/Write | ![clip_image004\[3\]](wrong.gif "clip_image004[3]")Needs lots of code and test work.

![clip_image004\[4\]](wrong.gif "clip_image004[4]")Needs to be deployed and published to the web server.

![clip_image004\[5\]](wrong.gif "clip_image004[5]")Less performance than SQL filter views directly #1 |

    #1 Note: Performance could be improved by making the reads from the views and the writes through the web service
    **More information:**
    1. Use BCS in VS 2010
    2. Write code that calls the CRM web services (that access the CRM data)
    3. Test
    4. Deploy

### Option 4: Expose OData from CRM as RSS
    The CRM 2011 OData Query Designer can be used to build queries to expose the data from CRM as RSS


| Pros | Cons |
| --- | --- |
| ![clip_image002\[4\]](correct.gif "clip_image002[4]")Easy configuration | ![clip_image004\[6\]](wrong.gif "clip_image004[6]")50 records limit. Need to page through the results.

![clip_image004\[7\]](wrong.gif "clip_image004[7]")Possible issues with firewalls and proxies because it uses Integrated Security for authentication.

![clip_image004\[8\]](wrong.gif "clip_image004[8]")Read-Only

![clip_image004\[9\]](wrong.gif "clip_image004[9]")No easy way to consume |

    **
** **Note:** You can really only call the OData endpoint from an application that already has an authentication cookie with the CRM server. 
i.e. you can't impersonate and call it like you can the standard WCF endpoints 
So it is really only suited to calling from Silverlight and JavaScript web resources that are delivered inside CRM (because they have the cookie)
    **More information:**
    The first step is to expose the data:
    1. Install [http://crm2011odatatool.codeplex.com](http://crm2011odatatool.codeplex.com/)
    2. Make a query

![Figure: Designing a query](figure2.jpg)  
    3. See the data

![Figure: See the data - RSS source for xtc_countrySet](figure3.jpg)  
    The second step (and the problem) is consuming the data

![Figure: BCS has no option to consume RSS data. Please Microsoft SharePoint Team, we need a new 'Data Source Type' = OData](figure4.jpg)  
    In summary, CRM 2011 can expose OData, but SharePoint 2010 BCS doesn't consume OData.
    The 3 options to consume the OData/RSS data:
    Consume the OData by SQL Server, via TSQL ???    Then use BCS to call SQL Server. 
Summary: SharePoint BCS -&gt; DataSourceType: SQL Server -&gt; OData- &gt; CRM database
    You would need to be crazy to go down this route [http://www.vishalseth.com/post/2009/12/22/Call-a-webservice-from-TSQL-(Stored-Procedure)-using-MSXML.aspx](http://www.vishalseth.com/post/2009/12/22/Call-a-webservice-from-TSQL-%28Stored-Procedure%29-using-MSXML.aspx)
    · Consume the OData by a BCS adapter + code calling web services (same story as above). 
Summary: SharePoint BCS -&gt; code calling OData- &gt; CRM database
    · Consume the RSS by "SharePoint RSS view web part" directly. 
Summary: SharePoint RSS view web part -&gt; OData- &gt; CRM database 
(not recommended as it could not be used in "SharePoint Search")
    So OData is all things horrible because it is hard to eat :-(

### Option 5: BizTalk

    Biztalk is built for mapping systems together, unfortunately, this solution is only considered for large enterprises.
    Summary: SharePoint BCS -&gt; BizTalk Database - &gt; CRM database


| Pros | Cons |
| --- | --- |
| ![clip_image002\[5\]](correct.gif "clip_image002[5]")Read/Write

![clip_image002\[6\]](correct.gif "clip_image002[6]")The BizTalk data centre can also provide data for any system.

![clip_image002\[7\]](correct.gif "clip_image002[7]")Requires little code if users already have BizTalk | ![clip_image004\[10\]](wrong.gif "clip_image004[10]")BizTalk :-)

![clip_image004\[11\]](wrong.gif "clip_image004[11]")Deployment - Needs external work to deploy BizTalk server.

![clip_image004\[12\]](wrong.gif "clip_image004[12]") Licence Cost |


### Option 6: OData 3rd Party solutions (doesn't exist)

    Today SharePoint 2010 exposes lists and document libraries as OData, but does not natively consume OData.
    What does this mean?
    * CRM 2011 exposes it data as OData, but cannot consume OData
    * SharePoint 2010 exposes it data as OData, but cannot consume OData
    ....and there are no 3rd party solutions to solve this...
