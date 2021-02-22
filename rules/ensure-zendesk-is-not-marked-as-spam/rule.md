---
type: rule
archivedreason: 
title: Do you ensure Zendesk is not marked as spam?
guid: 5dee363c-efd5-4ec5-b28c-709ae811a352
uri: ensure-zendesk-is-not-marked-as-spam
created: 2019-12-06T22:00:10.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: Kaique Biancatti
  url: https://ssw.com.au/people/kaique-biancatti
related: []
redirects:
- do-you-ensure-zendesk-is-not-marked-as-spam

---


Zendesk is being used everywhere now, and it is good! To ensure you are receiving important internal tickets, you need to whitelist your Zendesk domain in your primary email server.<br>
<br><excerpt class='endintro'></excerpt><br>
<p>​If you are using Exchange, you can do this by doing the following:<br></p><ol><li>Go to your Exchange Admin Center (if Office 365, https://outlook.office365.com/ecp/);</li><li>Mail Flow | + icon | Bypass spam filtering:<br>
   <dl class="image"><dt><img src="bypass-spam-filtering.png" alt="bypass-spam-filtering.png" /></dt><dd>Figure: Bypass spam filtering setting in Exchange</dd></dl></li><li>On the new window that opens, type a good name for the rule | Apply this rule if... | domain is | type your Zendesk domain (in our case, ssw.zendesk.com):<br>
   <dl class="image"><dt><img src="adding-domain-to-bypass-list.png" alt="adding-domain-to-bypass-list.png" /></dt><dd>Figure: Adding domain to bypass list​<br></dd></dl></li><li>The rest should already be correctly configured, hit Save</li></ol>Done! You now allow any Zendesk emails through your server correctly. No more missing important tickets!"<br>
<p></p>


