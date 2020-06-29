---
type: rule
title: Do you know the best Project/Version conventions?
uri: do-you-know-the-best-projectversion-conventions
created: 2011-11-18T03:52:36.0000000Z
authors:
- id: 22
  title: David Klein
- id: 5
  title: Justin King
- id: 17
  title: Ryan Tee
- id: 6
  title: Tristan Kurniawan

---



<span class='intro'> <p>Having a good folder structure in version control allows everyone to know where everything is without even having to look.​</p> </span>

<dl><pre>/northwind
 /trunk
 /branches (or shelvesets)
  /experiemental-feature1
 /releases (or tags)
  /1.0.0.356</pre>
<dd>Figure&#58; Bad example, SVN conventions are a dated and ignore releases, hotfixes and Service Packs </dd></dl>
<p>Trunk is the old way, Main is the new way as per the branching guidance, and it is the way that Microsoft does things.</p>
<dl><dt><img alt="Main branch guidance " src="BranchGuidance.jpg" /></dt>
<dd>Figure&#58; Good example, this makes a lot more sense </dd></dl>
<b>More Information&#58;</b> <dl><dt class="ssw-rteStyle-ImageArea"><img alt="Good format for the information" src="GoodFormatForInfo.jpg" /></dt>
<dd>Figure&#58; A good format for all your Products/Projects makes it easy to know where things are and what they are for </dd></dl>
<p>Read the TFS 2010 Branching Guidance - <a href="http&#58;//tfsbranchingguideiii.codeplex.com/">http&#58;//tfsbranchingguideiii.codeplex.com</a></p>


