---
type: rule
archivedreason: 
title: (Before starting) Do you follow a Test Driven Process?
guid: 786cd996-54da-4864-9362-26893d5acb4d
uri: before-starting-do-you-follow-a-test-driven-process
created: 2011-11-18T03:52:57.0000000Z
authors:
- id: 5
  title: Justin King
- id: 6
  title: Tristan Kurniawan
related: []

---


This field should not be null (Remove me when you edit this field).
<br><excerpt class='endintro'></excerpt><br>

  <ol class="ms-rteCustom-GreyBox" style="width&#58;840px;height&#58;100px;">
    <strong>Bad Process</strong>
    <li>Check out </li>
    <li>Compile </li>
    <li>Develop </li>
    <li>Compile </li>
    <li>Check In </li>
</ol>
<font class="ms-rteCustom-FigureBad" size="+0">A Bad Developer</font> <img alt="" class="ms-rteCustom-ImageArea" src="/TFS/RulesToBetterVersionControlwithTFS(AKASourceControl)/PublishingImages/BeforeCoding.jpg" /> <font class="ms-rteCustom-FigureNormal" size="+0">Figure&#58; Before you start cooking prepare all your ingredients (aka before you start coding, &quot;Get Latest&quot; the right way)</font>
<ol class="ms-rteCustom-GreyBox"><strong>Good Process</strong>
    <li>Get latest </li>
    <li>Compile </li>
    <li>Run Unit Tests </li>
    <li>If Tests pass then start developing </li>
    <li>Check out </li>
    <li>Develop </li>
    <li>Compile </li>
    <li>Run Unit Tests </li>
    <li>Get Latest (Always do a Get Latest before checking in as code you didn't change could break your code) </li>
    <li>Compile </li>
    <li>Run Unit Tests </li>
    <li>Check In if all tests passed </li>
    <li>Wait for gated check-in (GC) to complete </li>
    <li>Reconcile your workspace if it was successful </li>
    <li>Check that Continuous Integration (CI) build was successful(If GC was skipped) </li>
</ol>
<font class="ms-rteCustom-FigureGood" size="+0">A Good Developer</font>Note&#58; You should have both a Gated-Check-in (GC) and a Continuous Integration (CI) build on every branch.



