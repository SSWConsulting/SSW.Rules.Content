---
type: rule
title: Do you use the right service in SharePoint 2013
uri: do-you-use-the-right-service-in-sharepoint-2013
created: 2013-08-27T06:31:48.0000000Z
authors:
- id: 35
  title: Brian Farnhill
- id: 8
  title: John Liu

---



<span class='intro'> ​​​In SharePoint 2010, you can use SharePoint service&#160;<strong>/_vti_bin/listdata.svc</strong> to access data in SharePoint list, but in SharePoint 2013,&#160;<strong>/_vti_bin/listdata.svc</strong> has been officially deprecated.<div><div><br></div></div> </span>

The new service in SharePoint 2013&#160;is&#160;<strong>http&#58;//server/site/_api/web/lists/getbytitle('listname')​</strong><div><b><br></b><strong></strong><div>Read more about it&#58;&#160;</div><div><span></span><a href="http&#58;//msdn.microsoft.com/en-us/library/office/dn292556.aspx">http&#58;//msdn.microsoft.com/en-us/library/office/dn292556.aspx​​</a></div><div><br></div><div><br></div></div>


