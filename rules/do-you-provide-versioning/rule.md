---
type: rule
title: Do you provide versioning?
uri: do-you-provide-versioning
created: 2014-07-17T21:34:48.0000000Z
authors:
- id: 1
  title: Adam Cogan

---



<span class='intro'> <p>As an API provider, one of your most important tasks is to make sure that breaking changes will never occur in your API. Making breaking changes will make life difficult for the developers who depend on your service and can easily start causing frustration when things start to break.</p> </span>

<p>There are typically three main ways people provide versioning.</p><ol><li> 
      <strong>Change the URL&#58;</strong> Append a version number in the path<br>e.g. 
      <a href="/SoftwareDevelopment/RulesToBetterWebAPI/Pages/">https&#58;//dimensiondataaperture.com/api/v2/account/</a> 
      <ol style="list-style&#58;lower-alpha;"><li>Best choice for anonymous API access (callers may not be authenticated)</li><li>E.g. Github, Twitter​</li></ol></li><li>
      <strong>Based upon caller&#58;</strong> The caller has been authenticated and you determine the version of the API based upon the customer's record. 
      <ol style="list-style&#58;lower-alpha;"><li>Your URL's never change</li><li>Allows you to see the oldest version that customers are using and notifying customers to upgrade</li><li>E.g. Salesforce</li></ol></li><li>
      <strong>Custom request header&#58;</strong> You can use the same URL but add a header such as &quot;api-version&#58; 2&quot; 
      <ol style="list-style&#58;lower-alpha;"><li>Your URL's never change</li></ol></li></ol><p>All of these methods work well. The above list is in order of our recommendations.&#160;​</p><p>
      <strong>Option 2</strong> is a viable solution as you only have a few authenticated users that will consume the web service. It also allows you to notify users if they are using an old version that will be decommissioned.</p><p>If you are working with objects, keep the object id in the URL and leave everything else to the query string.</p>


