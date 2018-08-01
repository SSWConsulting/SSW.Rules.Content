---
type: rule
title: Do you use ANAME record?
uri: do-you-use-aname-record
created: 2016-10-20T22:51:42.0000000Z
authors:
- id: 47
  title: Stanley Sidik

---



<span class='intro'> <p> What is ANAME record? ANAME record (also known as A record) is an alias record that allows you to map the apex record or any other record within your domain to a target host name, essentially a CNAME record for the apex record. ANAME record&#160;is&#160;especially useful&#160;for when you have multiple domain names and&#160;your website is hosted by a provider that&#160;changes it's IP Address, this does happen quite regularly with WPEngine. Many DNS service provider does not support ANAME record, however, <a href="http&#58;//dnsmadeeasy.com/">DNSMadeEasy</a>&#160;has made this service available.</p> </span>

<p>Configuring ANAME is as easy as configuring CNAME. Let's have a look at DNS records for adamcogan.com.au, DNS records contains apex record for adamcogan.com.au and a <b>www.adamcogan.com.au</b>. The apex record uses ANAME, while CNAME for <b>www.adamcogan.</b><b>au</b>&#160;- now we will never have to worry about updating these records,&#160;they will follow the DNS records&#160;of <b>adamcogan.com</b>. ​<img src="/PublishingImages/2018-08-01_14-41-32.jpg" alt="2018-08-01_14-41-32.jpg" style="margin&#58;5px;width&#58;808px;" /></p><dl class="image"><dd>Figure&#58; Example DNS entry from Azure DNS<br>​​​​<br>​<br></dd></dl>


