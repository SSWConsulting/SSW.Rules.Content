---
type: rule
title: Do you add an exception for Hosts file on Windows Defender?
uri: do-you-add-an-exception-for-hosts-file-on-windows-defender
created: 2012-09-19T18:15:45.0000000Z
authors:
- id: 47
  title: Stanley Sidik

---



<span class='intro'> <p>​If you sometimes add entries into your Hosts file (C&#58;\Windows\System32\Drivers\etc\Hosts) you will need to add an exception in Windows Defender as it assumes that malicious code has added an erroneous entry. Malware will in fact often create such erroneous entries in the HOSTS file in order to divert users to alternative servers when they attempt to access sites such as facebook.com. These servers may play host to phishing sites that send user data entered on them to internet fraudsters. The removal of entries for ad servers, which many users utilise as a simple but effective ad blocker, may be down to the fact that malware also makes use of the HOSTS file to divert queries from legitimate advertising servers to their own servers. This enables fraudsters to display their own malicious ads on third-party web sites.
</p> </span>

<p>The relevant setting can be found under &quot;Settings, Excluded files and locations&quot;. Of course this also mean that the anti-virus program will no longer detect any malicious modifications to the HOSTS file.</p>

<img src="/PublishingImages/Windows-Defender-settings.jpg" alt="Figure&#58; Window defender Settings" class="ms-rteCustom-ImageArea" style="width&#58;600px;" />
<span class="ms-rteCustom-FigureNormal">Figure&#58; Window defender Settings</span>


