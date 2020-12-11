---
type: rule
archivedreason: 
title: Do you know the right source control to use?
guid: 0841f388-e428-4f04-b7b0-693eae2ac1e2
uri: do-you-know-the-right-source-control-to-use
created: 2011-11-18T03:52:53.0000000Z
authors:
- id: 22
  title: David Klein
- id: 5
  title: Justin King
- id: 6
  title: Tristan Kurniawan
- id: 17
  title: Ryan Tee
related: []

---

SSW uses and recommends Microsoft Team Foundation Server (TFS) as a source code solution.   
<!--endintro-->

![](TFSTeam.jpg) <font class="ms-rteCustom-FigureNormal">Figure: Microsoft Visual Studio Team System </font>
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

<font class="ms-rteCustom-FigureBad">Figure: Bad Example, Visual SourceSafe (VSS) is a bad choice </font>
::: greybox
Reasons companies choose Subversion (SVN) 
 -It's free 
 -It's easy to use 
 -No Build integration 
 -No Work Item integration
:::

 
<font class="ms-rteCustom-FigureNormal">Figure: Better example, Subversion (SVN) is an OK choice <br></font>

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

<font class="ms-rteCustom-FigureGood">Figure: Better example, Subversion (SVN) is an OK choice </font>
