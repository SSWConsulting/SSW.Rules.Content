---
type: rule
archivedreason: 
title: Do you know how to write a good pull request?
guid: d35b49bf-bdd1-48eb-bc1d-944cdc5be4dc
uri: do-you-know-how-to-write-a-good-pull-request
created: 2020-07-17T01:21:08.0000000Z
authors:
- title: Chris Clement
  url: https://ssw.com.au/people/chris-clement
- title: Matt Goldman
  url: https://ssw.com.au/people/matt-goldman
related: []
redirects: []

---


<div>As a software developer, it is very common to see a pull request. The quality of a pull request can be vary - sometimes we have to deal with&#160;a cryptic pull request and sometimes we find a very well written pull request.<br><br></div>​Having a great pull request message can help your peers to understand your pull request quickly so&#160;they can review your pull request faster and also give you better suggestions.<br><div><br></div>
<br><excerpt class='endintro'></excerpt><br>
<p>While the pull request itself is valid and may offer a high value, you need to spend a bit of time to understand what is the context of this pull request and what does it change. Doing this step can take your time easily from 1 minute (if you just recently touched the&#160;code) to more than&#160;10 minutes (if it has been a long time since you worked on it - or even if&#160;you have never touched the code).<br></p><p>Writing a great pull request can help your peers to understand your code better and therefore, they can give you better insights (or faster review turnaround time, that's&#160;great!).<br></p><p>There are a couple of things that you can do to improve your pull request&#58;<br></p><ol><li>Write a concise and self-explanatory title<br></li><li>Write a concise and descriptive body<br></li><li>Link the pull request to the associated issues / PBIs<br></li></ol><h3 class="ssw15-rteElement-H3">​​​​​Write a concise and self-explanatory title<br></h3><p>The key of writing a concise pull request is to base the pull request itself on a PBI / issue.<br></p><p>Example PBI title&#58; Product Backlog Item 100359&#58; &quot;Desktop App | Exporting occasionally failed&quot;<br></p><p class="ssw15-rteElement-GreyBox">​Pull request title&#58; &quot;Fix exporting&quot;<br></p><dd class="ssw15-rteElement-FigureBad">​Bad example - Pull request title does not tell what issues has been fixed and how<br></dd><p class="ssw15-rteElement-GreyBox">​​​Pull request title&#58; &quot;Fix desktop app exporting -&#160;prevent database concurrent access while exporting&quot;<br></p><dd class="ssw15-rteElement-FigureGood">Good example - ​Pull request title briefly describe the&#160;fix that it has<br></dd><p>The important information in the title are&#58;<br></p><p></p><ol><li>What the PR will do<br></li><li>How the PR achieve&#160;it<br></li></ol><p></p><p>Having the &quot;What&quot; information allows the reviewers to quickly understand what this is about, while having the &quot;How&quot; can help the reviewer to briefly understand how did you do it. Sometimes we might want to put&#160;the &quot;How&quot; in the pull request body if it is&#160;too long or complex.<br></p><p> 
   <br> 
</p><h3 class="ssw15-rteElement-H3">​​​Write a concise and descriptive body<br></h3><p>Pull request body is a media for the developer to tell the reviewers what the pull request is about. Things that need to be keep in mind before writing a pull request body&#58;</p><p></p><ol><li>What the pull request is about<br></li><li>How did the pull request achieve the feature/fix the bug/other goal it may have<br></li><li>(Optional) Put a screenshot if it will help the reviewer to understand the end results (e.g. front-end cosmetic change)<br></li><li>(Optional)&#160;What do you want the reviewers to do - this can be approvals (most of the case) or looking&#160;to get more feedback on a piece of code in the pull request.<br></li></ol><dl class="badImage"><dt>​<img src="/SiteAssets/do-you-know-how-to-write-a-good-pull-request/better-pr-bad-pr.png" alt="better-pr-bad-pr.png" style="margin&#58;5px;width&#58;730px;" /></dt><dd class="ssw15-rteElement-FigureBad">​Bad example - Pull request with vague&#160;title and&#160;no description</dd>​​<br></dl><dl class="goodImage"><dt>
      <img src="/SiteAssets/do-you-know-how-to-write-a-good-pull-request/better-pr-good-pr.png" alt="better-pr-good-pr.png" style="margin&#58;5px;width&#58;730px;height&#58;503px;" /> 
   </dt><dd class="ssw15-rteElement-FigureGood">​Good ​example - Pull request with good&#160;title and descriptive body​​​<br></dd>​​<br></dl> ​There is also a well-known pull request&#160;semantic like&#160;<a href="https&#58;//www.conventionalcommits.org/en/v1.0.0-beta.2/">Conventional Commits</a>&#160;on how to write a pull request body but we can still have a great pull request without using a semantic.<br> 
<p></p><p> 
   <br> 
</p><h3 class="ssw15-rteElement-H3">​Link the pull request to the associated issues / PBIs<br></h3><p></p><p>Since we already have a great title and body, the last thing to do is to associate this pull request to the related PBIs or issues.<br></p><p>Linking an issue to a pull request can serve as a documentation on which development work that was done on a specific PBI/issue. It may help the team in the future to debug when and which changes were introduced and what was the original specification of that piece of work.<br></p><dl class="image"><dt>
      <img src="/SiteAssets/do-you-know-how-to-write-a-good-pull-request/better-pr-link-issues.png" alt="better-pr-link-issues.png" style="margin&#58;5px;width&#58;730px;height&#58;504px;" /> 
   </dt><dd>​Figure&#58; Linking a pull request to the related issue</dd>​​<br></dl><dl class="image"><dt>
      <img src="/SiteAssets/do-you-know-how-to-write-a-good-pull-request/better-pr-link-issues-linked.png" alt="better-pr-link-issues-linked.png" style="margin&#58;5px;width&#58;730px;height&#58;504px;" /> 
   </dt><dd>​Figure&#58; A pull request is now associated to the related ​issue</dd>​​<br></dl><dl class="image"><dt>​<br></dt></dl>


