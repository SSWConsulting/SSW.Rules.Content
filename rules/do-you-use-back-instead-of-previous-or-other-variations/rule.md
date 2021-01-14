---
type: rule
archivedreason: 
title: Do you use "< Back" instead of "< Previous" or other variations?
guid: cd64ef97-75d9-4158-b732-f319de35069b
uri: do-you-use-back-instead-of-previous-or-other-variations
created: 2009-12-04T09:16:18.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: Tristan Kurniawan
  url: https://ssw.com.au/people/tristan-kurniawan
- title: Jade Mitchell
  url: https://ssw.com.au/people/jade-mitchell
related: []
redirects:
- do-you-use-＂-back＂-instead-of-＂-previous＂-or-other-variations

---

According to http://msdn.microsoft.com/en-us/library/ms997609.aspx, the commands for navigating through a wizard should be "&lt; Back" and "Next &gt;".   
<!--endintro-->

When your site needs a link to iterate backwards through records we recommend that you use "&lt; Back" instead of "&lt; Previous".

There are a few reasons for this:

1. This is the standard used in Microsoft Installation files. MSIs are the most widely used installation package available today.
2. Internet Explorer and several other lesser known browsers use a Back button to iterate back through webpages, so your visitors will automatically know what your "&lt; Back" link does.
3. It is important to keep a consistency on your pages.


Below is an example of a Good "&lt; Back" link versus some Bad variations.
<dl class="goodImage">    <br><br>::: good  <br>![Figure: A Good example of a "&lt; Back" link](textboxeswithshowbutton.gif)  <br>:::<br>
    </dl><dl class="badImage">    <br><br>::: bad  <br>![Figure: This is Bad because it says "Previous" instead of "Back"](badpreviouslink.gif)  <br>:::<br>
    </dl><dl class="goodImage">    <br><br>::: good  <br>![Figure: This is bad because it has too many "&lt;"s or it has no space between the "&lt;" and the "Back"](badbacklink.gif)  <br>:::<br>
    </dl>
We have a program called [SSW Code Auditor](http://www.ssw.com.au/ssw/CodeAuditor) to check for this rule.


We have a program called [SSW Link Auditor](http://www.ssw.com.au/ssw/LinkAuditor) to check for this rule. We offer a [rule sample page](http://www.ssw.com.au/SSW/LinkAuditor/Samples/Rules/ReadingBackLink.aspx) for demo scan.
