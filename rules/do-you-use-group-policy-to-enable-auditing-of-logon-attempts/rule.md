---
type: rule
title: Do you use Group Policy to enable auditing of logon attempts​?
uri: do-you-use-group-policy-to-enable-auditing-of-logon-attempts
created: 2019-07-24T20:57:45.0000000Z
authors:
- id: 71
  title: Steven Andrews

---



<span class='intro'> <p class="ssw15-rteElement-P">It is important as a Network Administrator to know when and where failed login attempts are coming from. Through Group Policy you can enable &quot;Audit logon events&quot;.​<br></p> </span>

<ol><li>​Create a group policy called 'Logon Auditing Policy'</li><li>Right click on 'Logon Auditing Policy'&#160;and click on Edit to bring up Group Policy Management Editor</li><li>Select 'Audit account logon events' from Computer Configuration | Policies |&#160;Windows Settings&#160;|&#160;Local Policies |&#160;Audit Policy&#160;and set to Success, Failure</li><li>Select 'Audit logon events'&#160;from Computer Configuration | Policies |&#160;Windows Settings&#160;|&#160;Local Policies |&#160;Audit Policy&#160;and set to&#160;Success, Failure<br> 
      <dl class="image"><dt>
            <img src="/PublishingImages/failed-login-1.png" alt="failed-login-1.png" />
         </dt><dd>Figure&#58;&#160;Select 'Audit logon events'<br></dd></dl></li><li>Select 'Audit&#58; Force audit policy...' from&#160;Computer Configuration | Policies |&#160;Windows Settings&#160;|&#160;Local Policies |&#160;Security Options&#160;and set to&#160;Enabled<br>
      <dl class="image"><dt>
            <img src="/PublishingImages/failed-login-2.png" alt="failed-login-2.png" />
         </dt><dd>Figure&#58;&#160;Select 'Audit&#58; Force audit policy...'<br></dd></dl></li></ol><dl class="image"><dt><img src="/PublishingImages/failed-login-3.png" alt="failed-login-3.png" /></dt><dd>Figure​&#58; Successful and Failed login attempts will now appear in Event Viewer | Security​</dd></dl>​<span style="color&#58;#333333;">Now when you will have access to seeing success/failed login attempts on user accounts, these can then be captured and audited with your own internal process or a third party application such as Whats Up Gold,&#160;see&#58;&#160;</span><a href="/_layouts/15/FIXUPREDIRECT.ASPX?WebId=3dfc0e07-e23a-4cbb-aac2-e778b71166a2&amp;TermSetId=07da3ddf-0924-4cd2-a6d4-a4809ae20160&amp;TermId=002aec6e-9ac2-4701-ae0c-c5f9d1be2690">Do you monitor failed login attempts?</a>


