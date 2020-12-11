---
type: rule
archivedreason: 
title: Do you configure your TFS to be accessible from outside the network?
guid: c0ecaeb8-a15d-40aa-8617-b62004fe22ac
uri: do-you-configure-your-tfs-to-be-accessible-from-outside-the-network
created: 2011-11-18T03:53:00.0000000Z
authors:
- id: 22
  title: David Klein
- id: 5
  title: Justin King
- id: 17
  title: Ryan Tee
- id: 6
  title: Tristan Kurniawan
related: []

---

* TFS SP1 
This feature called "Extranet Support" was added way back in TFS 2005 SP1 as per [Stuff in the pipe for Team Foundation Server](http://www.ssw.com.au/ssw/Redirect/StandardsRules/MSDNBlog.htm)
* A domain name or IP address forwarded to TFS (eg: tfs.your-domain.com)
* Port 8080 (this is port that TFS uses for source control)
* Firewall/Router rule (ideally)


<!--endintro-->

Tip: You can solve this with TFS Extranet Support:

Yes Port 8080 will work in most cases but not on the strictest networks, where only Port 80 is allowed.     
Then you have to use port forwarding via a firewall/router rule (recommended) to forward port 80 to the TFS port, while in this way, you would lose the TFS SharePoint Portal and Reporting Services.
<dl>&lt;dt&gt;
      <img alt="Rule to forward port 80 to the TFS port" src="tfs-firewall-rule-80.gif" width="681" height="339">
   &lt;/dt&gt;<dd>Figure: Rule to forward port 80 to the TFS port </dd></dl>
