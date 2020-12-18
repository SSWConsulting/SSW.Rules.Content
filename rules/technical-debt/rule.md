---
type: rule
archivedreason: 
title: Do you know the importance of paying back technical debt?
guid: de86d886-3341-43d0-a487-5e8b3cee3938
uri: technical-debt
created: 2020-12-16T23:19:05.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: William Liebenberg
  url: https://ssw.com.au/people/william-liebenberg
- title: Matt Goldman
  url: https://ssw.com.au/people/matt-goldman
related: []
redirects:
- do-you-know-the-importance-of-paying-back-technical-debt

---


<h3 class="ssw15-rteElement-H3">​​What is Technical Debt?​<br></h3><p>Technical Debt is when you take a shortcut to get a feature in to get some feedback.<br></p><div class="ms-rtestate-read ms-rte-embedcode ms-rte-embedil ms-rtestate-notify s4-wpActive"><iframe width="750" height="422" src="https&#58;//www.youtube.com/embed/ASVD4YIOgpU" frameborder="0"></iframe>&#160;</div><p><br></p>
<br><excerpt class='endintro'></excerpt><br>
<p>Code that is hard to understand after reading it multiple times or a single method that spans multiple screens is also considered to be Technical Debt.</p><p>Systems need to have features added to them to&#160;continually&#160;remain useful (or competitive).</p><p>As new features are added to the system, often more Technical Debt will be introduced.&#160;<br></p><p>
   <b>Example&#58;</b> A developer takes a shortcut to get some early feedback on a new feature<br></p><ul><li>$100 - full feature&#160;</li><li>$20 - feature with shortcuts (no tests, dirty code, whatever it takes)</li><li>$80 - IOU via PBI in the backlog e.g. [FeatureName] – Tech Debt - Planned</li></ul><dl class="goodImage"><dt>​​​<img src="/PublishingImages/tech-debt-good-example.png" alt="tech-debt-good-example.png" style="width&#58;750px;" /></dt><dd>Figure&#58; Good example -&#160;Tech Debt is very visible to the Product Owner</dd></dl><h3 class="ssw15-rteElement-H3">What are the consequences of Technical Debt?​​<br></h3><ul><li>Fewer&#160;features overtime for the customers</li><li>More molasses (developer friction) for the developers<br></li></ul><h3 class="ssw15-rteElement-H3">The 2 types of Technical Debt​​<br></h3> 
<br> 
<b></b>
<b>#1 Planned Technical Debt</b>

   <p class="ssw15-rteElement-P">Sometimes you do want to quickly implement a new feature to get it out and receive some feedback.<br></p><p class="ssw15-rteElement-GreyBox">PBI&#58; 
      <b>[FeatureName] – Tech Debt - Planned</b><br></p><div>
      <b>Note&#58;</b> Martin Fowler calls this Deliberate Technical Debt&#160;</div><div><b><br></b></div><div>
         <b>​#2 Discovered Technical Debt</b>
         <p class="ssw15-rteElement-P">During a code review, you or the team notice something as part of the system that is clearly Technical Debt. This code is hindering the ability to add new features or is hard to read/understand.</p><p class="ssw15-rteElement-GreyBox">PBI&#58; 
            <b>[FeatureName] – Tech Debt - Discovered</b></p></div><div>
         <b>Note&#58; </b>Martin Fowler calls this Inadvertent Technical Debt<br> 
         <h3 class="ssw15-rteElement-H3">How to repay Technical Debt​​<br></h3><p class="ssw15-rteElement-P">Just like a business that receives pre-payment from customers, a software team should be reviewing the size of their liabilities (being the list of PBIs with Technical Debt).&#160;</p><p class="ssw15-rteElement-P">At the Sprint Planning&#58;</p><ol><li>Show the Product Owner the list of outstanding Technical Debt PBIs</li><li>The Product Owner should make sure that the developers review the list of Technical Debt list and pick at least 1 PBI to pay back during the upcoming sprint​<br></li></ol><h3 class="ssw15-rteElement-H3">Screenshots<br></h3><dl class="image"><dt><img src="/PublishingImages/techdebt-github.png" alt="techdebt-github.png" style="width&#58;750px;" /></dt><dd>Figure&#58; Screenshot of code with tech debt comment and link to GitHub issue</dd><dd></dd></dl><dl class="image"><dt><img src="/PublishingImages/techdebt-backlog.png" alt="techdebt-backlog.png" style="width&#58;750px;" /></dt><dd>Figure&#58; Screenshot of tech debt on backlog</dd><dd></dd></dl><dl class="image"><dt><img src="/PublishingImages/techdebt-architecture.png" alt="techdebt-architecture.png" style="width&#58;750px;" /></dt><dd>Figure&#58; SugarLearning architecture diagram</dd><dd></dd></dl><h3 class="ssw15-rteElement-H3">Related Rule​<br></h3></div><div><ul><li>
         <a href="/_layouts/15/FIXUPREDIRECT.ASPX?WebId=3dfc0e07-e23a-4cbb-aac2-e778b71166a2&amp;TermSetId=07da3ddf-0924-4cd2-a6d4-a4809ae20160&amp;TermId=21d9fede-f219-4242-8eee-6edd10edc09c">Do you refactor your code and keep methods short?​​</a></li></ul></div>


