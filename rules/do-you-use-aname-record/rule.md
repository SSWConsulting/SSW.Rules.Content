---
type: rule
title: Do you use ANAME record?
uri: do-you-use-aname-record
created: 2016-10-20T22:51:42.0000000Z
authors:
- id: 47
  title: Stanley Sidik

---



<span class='intro'> <p>What is ANAME record? ANAME record is an alias record that allows you to map the apex record or any other record within your domain to a target host name, essentially a CNAME record for the apex record. ANAME record&#160;is&#160;especially useful&#160;for when you have multiple domain names and&#160;your website is hosted by a provider that&#160;changes it's IP Address, this does happen quite regularly with WPEngine. Many DNS service provider does not support ANAME record, however <a href="http&#58;//dnsmadeeasy.com/">DNSMadeEasy</a> has made this service available.</p> </span>

<p><br>Configuring ANAME is as easy as configuring CNAME. Let's have a look at DNS records for adamcogan.com.au, DNS records contains apex record for adamcogan.com.au and a <a href="http&#58;//www.adamcogan.com.au/">www.adamcogan.com.au</a> . The apex record uses ANAME, while CNAME for <a href="http&#58;//www.adamcogan.au/">www.adamcogan.au</a> - never ever we need to worry about any IP Address updates, it will just follow the DNS records for adamcogan.com. DNSMadeEasy also provides&#160;Real-Time Stats are available showing how frequently your DNS records are requested. Let DNSMadeEasy as your delegated DNS!</p><p><img alt="ANAME_adamcogan.com..au.jpg" src="/SiteAssets/do-you-use-aname-record/ANAME_adamcogan.com..au.jpg" style="margin&#58;5px;width&#58;808px;" />&#160;</p>


