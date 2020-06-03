---
type: rule
title: Do you share code using packages? (Binary and source sharing)
uri: do-you-share-code-using-packages-binary-and-source-sharing
created: 2017-05-19T16:58:36.0000000Z
authors:
- id: 1
  title: Adam Cogan
- id: 46
  title: Danijel Malik

---



<span class='intro'> <p>Devs need a way of sharing and consuming the source code or binaries.&#160;<br></p><p>VSTS is the best home to put it and share it across their organization because&#58;&#160; <br></p> </span>

<p></p><ul><li>it&#160;caches&#160;your packages<br></li><li>it's a&#160;centralized&#160;place for your packages<br></li><li>it's constantly evolving (some really cool features are coming...check the video below)<br></li></ul><p class="ssw15-rteElement-GreyBox">Sharing source or binaries via File Shares or Version Control</p><dd class="ssw15-rteElement-FigureBad">Bad example<br></dd><p class="ssw15-rteElement-GreyBox">​Sharing source or binaries via&#160;3rd party tools like ProGet, MyGet</p>​<br>
<dd class="ssw15-rteElement-FigureNormal">OK example​​<br></dd><p class="ssw15-rteElement-GreyBox">Sharing source or binaries via&#160;packages created using VSTS Team Build</p><dd class="ssw15-rteElement-FigureGood">Good example</dd><dl class="image"><dt>
      <img src="/PublishingImages/package-management-site.png" alt="package-management-site.png" />
   </dt><dd>Figure&#58; Start from 
      <a href="https&#58;//marketplace.visualstudio.com/items?itemName=ms.feed" target="_blank">https&#58;//marketplace.visualstudio.com/items?itemName=ms.feed </a>
      <br></dd></dl><div>VSTS is about to add benefits like Component Governance, which allows policies to be set over who can and cannot use the source or binaries E.g. Licensing (MIT might be ok and GPL not ok), security - in development</div><div><dd class="ssw15-rteElement-FigureGood"> 
      <br>Good example&#58;&#160;Sharing source or binaries via&#160;packages created using Sonatype Nexus.<br>Already supports Component Governance</dd><h3 class="ssw15-rteElement-H3">Additional info 
      <br></h3> ​ 
   <div class="ms-rtestate-read ms-rte-embedcode ms-rte-embedil ms-rtestate-notify"> 
      <iframe width="780" height="440" src="https&#58;//www.youtube.com/embed/r-nVWDq1QBg" frameborder="0"></iframe>&#160;</div><ul><li>At 2&#58;50 Mario Rodriguez talks about the bad ways customers share code</li><li>At 6&#58;30 Mario explains to Danijel Malik how VSTS helps with the nasty problem of Diamond Dependencies (aka Binary Consumption Hell) &#160; (E.g. That's when devs are trying to get the new version of say Newtonsoft v1.9 in all projects, but one at a time)<br></li></ul><p></p></div>


