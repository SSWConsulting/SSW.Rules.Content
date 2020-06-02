

---
uri: do-you-ensure-zendesk-is-not-marked-as-spam
title: Do you ensure Zendesk is not marked as spam?
created: YYYY-12-DD 22:00:10
authors:
  - id: 1
    title: Adam Cogan
  - id: 73
    title: Kaique Biancatti
---




<span class='intro'> Zendesk is being used everywhere now, and it is good! To ensure you are receiving important internal tickets, you need to whitelist your Zendesk domain in your primary email server.<br> </span>

<p>​If you are using Exchange, you can do this by doing the following&#58;<br></p><ol><li>Go to your Exchange Admin Center (if Office 365, https&#58;//outlook.office365.com/ecp/);</li><li>Mail Flow | + icon | Bypass spam filtering&#58;<br>
   <dl class="image"><dt><img src="/PublishingImages/bypass-spam-filtering.png" alt="bypass-spam-filtering.png" /></dt><dd>Figure&#58; Bypass spam filtering setting in Exchange</dd></dl></li><li>On the new window that opens, type a good name for the rule | Apply this rule if... | domain is | type your Zendesk domain (in our case, ssw.zendesk.com)&#58;<br>
   <dl class="image"><dt><img src="/PublishingImages/adding-domain-to-bypass-list.png" alt="adding-domain-to-bypass-list.png" /></dt><dd>Figure&#58; Adding domain to bypass list​<br></dd></dl></li><li>The rest should already be correctly configured, hit Save</li></ol>Done! You now allow any Zendesk emails through your server correctly. No more missing important tickets!&quot;<br>
<p></p>


