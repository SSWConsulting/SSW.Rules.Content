---
type: rule
archivedreason: 
title: Do you know when anchor should "run at server"?
guid: 721eda39-8237-40ca-8f6b-f3eb9ba8f0b6
uri: when-anchor-should-run-at-server
created: 2016-08-24T22:33:39.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
- do-you-know-when-anchor-should-run-at-server

---


<p><b>{ltHTMLChar}a{gtHTMLChar}</b> tag should <b>runat=“server&quot;</b> *ONLY* if you need to change the target at runtime.</p><p>If you include<b> runat=“server&quot;</b> for an HTML element that you do not need access to in code behind, you are introducing a whole lot of overhead you do not need.&#160;​<br></p>
<br><excerpt class='endintro'></excerpt><br>
<p class="ssw15-rteElement-YellowBorderBox">​We have a program called&#160;<a href="https&#58;//www.ssw.com.au/ssw/CodeAuditor/">SSW Code Auditor</a>&#160;to check for this rule.​​<br></p><br>


