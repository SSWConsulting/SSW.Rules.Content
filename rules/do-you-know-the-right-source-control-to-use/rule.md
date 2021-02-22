---
type: rule
archivedreason: 
title: Do you know the right source control to use?
guid: 0841f388-e428-4f04-b7b0-693eae2ac1e2
uri: do-you-know-the-right-source-control-to-use
created: 2011-11-18T03:52:53.0000000Z
authors:
- title: David Klein
  url: https://ssw.com.au/people/david-klein
- title: Justin King
  url: https://ssw.com.au/people/justin-king
- title: Tristan Kurniawan
  url: https://ssw.com.au/people/tristan-kurniawan
- title: Ryan Tee
  url: https://ssw.com.au/people/ryan-tee
related: []
redirects: []

---

SSW uses and recommends Microsoft Team Foundation Server (TFS) as a source code solution.   
<!--endintro-->
![](TFSTeam.jpg)**Figure: Microsoft Visual Studio Team System** 
Here are some of the reasons why:

* Checkin policies
* Integrated Work Items and Source control
* Visual Studio IDE integration
* Code Metrics
* HTTP access via webservices
* Integrated Build Server



::: greybox
Reasons companies choose Visual SourceSafe (VSS) 
 - No server required
 - No VPN required 
 - They are ignorant about the potential corruption problems  
:::


::: bad
Figure: Bad Example, Visual SourceSafe (VSS) is a bad choice  
:::

::: greybox
Reasons companies choose Subversion (SVN) 
 -It's free 
 -It's easy to use 
 -No Build integration 
 -No Work Item integration  
:::
 
**Figure: Better example, Subversion (SVN) is an OK choice 
** 

::: greybox
Reasons companies choose Team Foundation Server (TFS)
  -It's free (With MSDN)
  -It's easy to use 
 -It's easy to install 
 -High fidelity SQL data store 
 -No VPN required
 -Does not require a server (basic configuration) 
 -Has Build integration 
 -Has Work Item integration 
 -Has Test suite integration 
 -Has reporting out of the box  
:::


::: good
Figure: Better example, Subversion (SVN) is an OK choice  
:::
