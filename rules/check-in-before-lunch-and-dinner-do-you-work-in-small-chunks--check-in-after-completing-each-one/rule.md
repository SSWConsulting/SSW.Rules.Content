---
type: rule
archivedreason: 
title: (Check-in before lunch and dinner) Do you work in small chunks & check in after completing each one?
guid: a9f4bf75-4ea9-4e79-944e-fb3a4693076c
uri: check-in-before-lunch-and-dinner-do-you-work-in-small-chunks--check-in-after-completing-each-one
created: 2011-11-18T03:52:27.0000000Z
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


Frequently developers work on long or difficult features/bugs and leave code checked out for days or worse still, weeks. <br>
<ol>
    <li>What happens if your laptop hard drive dies? </li>
    <li>What happens if you call in sick? </li>
    <li>How can you pair program if not sharing your changesets? </li>
</ol>

<br><excerpt class='endintro'></excerpt><br>

  <img alt="" class="ms-rteCustom-ImageArea" src="/TFS/RulesToBetterVersionControlwithTFS(AKASourceControl)/PublishingImages/Check-InRegularly.jpg" />&#160;<font class="ms-rteCustom-FigureNormal" size="+0">Figure&#58; Eating one big meal every three days gives you a bellyache... (aka check in small portions regularly, one large check-in after a few days will give you a headache)</font>
<p>That's why source code should be checked in regularly. We recommend a check-in&#58; </p>
<ul>
    <li>Immediately after completing a piece of functionality, where the <a shape="rect" href="/TFS/RulesToBetterVersionControlwithTFS(AKASourceControl)/Pages/CompilePassed.aspx">code compiles and passes the unit tests </a>Before lunch or dinner </li>
    <li>Before leaving your workstation for an extended period of time </li>
</ul>
If the changes would break the build or are in a state that cannot be put into the main trunk, then this code should be put into a <a shape="rect" href="http&#58;//msdn.microsoft.com/en-us/library/ms181403.aspx">shelveset</a> (sometimes referred to as 'sandbox') in source control. <br>
Another good reason to check-in regularly is that it makes it easier to merge your changes with other developers. If all developers check-in lots of changes in one go, you will spend a lot of your time resolving conflicts instead of doing work. <br>
TIP&#58; How can you enforce regular check-ins? Monitor them using a <a shape="rect" href="http&#58;//www.ssw.com.au/ssw/Standards/Rules/RulesToBetterSourceControlwithTFS.aspx#CheckinReport">report to see who has not checked in</a>. 



