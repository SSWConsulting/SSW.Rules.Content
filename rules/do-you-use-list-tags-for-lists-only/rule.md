---
type: rule
archivedreason: 
title: Do you use "list" tags for lists only?
guid: 8775ec15-6a54-4e29-9c2a-43aa1b85e1f5
uri: do-you-use-list-tags-for-lists-only
created: 2012-07-02T15:02:44.0000000Z
authors:
- title: Tiago Araujo
  url: https://ssw.com.au/people/tiago-araujo
related: []
redirects:
- do-you-use-＂list＂-tags-for-lists-only

---


<p>The HTML list tags {ltHTMLChar}ul{gtHTMLChar} and {ltHTMLChar}ol{gtHTMLChar} should be used for unordered and ordered lists <strong>only</strong>.</p>
<br><excerpt class='endintro'></excerpt><br>
<p><strong>Tip&#58; </strong>If your list tag ({ltHTMLChar}ul{gtHTMLChar} or {ltHTMLChar}ol{gtHTMLChar}) doesn't have a list item ({ltHTMLChar}li{gtHTMLChar}) inside it, then it's not a list. Consider using another HTML tag (E.g. {ltHTMLChar}p{gtHTMLChar}).
</p>
<div class="ms-rteCustom-GreyBox">
{ltHTMLChar}ul{gtHTMLChar}
A normal text
{ltHTMLChar}/ul{gtHTMLChar}
</div>
<span class="ms-rteCustom-FigureBad">Figure&#58; Bad Example - Using the {ltHTMLChar}ul{gtHTMLChar} for a text</span>
<div class="ms-rteCustom-GreyBox">
<p>{gtHTMLChar}{ltHTMLChar}li{gtHTMLChar}A list item{ltHTMLChar}/li{gtHTMLChar}{ltHTMLChar}/ul{gtHTMLChar}</p>
<p>{ltHTMLChar}ol{gtHTMLChar}{ltHTMLChar}li{gtHTMLChar}A list item{ltHTMLChar}/li{gtHTMLChar}{ltHTMLChar}/ol{gtHTMLChar}</p>
</div>
<span class="ms-rteCustom-FigureGood">Figure&#58; Good Example - Using the {ltHTMLChar}ul{gtHTMLChar} and {ltHTMLChar}ol{gtHTMLChar} for lists</span>


