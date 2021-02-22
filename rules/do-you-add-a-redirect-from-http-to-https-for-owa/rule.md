---
type: rule
archivedreason: 
title: Do you add a redirect from http to https for OWA?
guid: df2d7b63-316f-4989-912e-09543657f80c
uri: do-you-add-a-redirect-from-http-to-https-for-owa
created: 2016-05-02T06:48:16.0000000Z
authors:
- title: Stanley Sidik
  url: https://ssw.com.au/people/stanley-sidik
related: []
redirects: []

---


<p>Do you configure redirection from HTTP to https for Outlook Web App (OWA)? To simplify OWA access for your users, you want to configure the Outlook Web App page to automatically redirect users to https. The HTTP redirect procedure in IIS Manager simplifies OWA URL and forces to SSL connection from <b>http://mail.domain.com</b> to h<b>ttps://mail.domain.com/owa</b>.<b></b><br></p>
<br><excerpt class='endintro'></excerpt><br>
<h3 class="ssw15-rteElement-H3">Step 1: Use IIS Manager to simplify OWA URL and force redirection to SSL</h3><ol><li>Start IIS Manager.</li><li>Expand the local computer, expand <strong>Sites</strong>, and then click <strong>Default Web Site</strong>.</li><li>At the bottom of the Default Web Site Home pane, click <strong>Features View</strong> if this option isn't already selected.</li><li>In the <strong>IIS</strong> section, double-click <strong>HTTP Redirect</strong></li><li>Select the <strong>Redirect requests to this destination</strong> check box.</li><li>Type the absolute path of the /owa virtual directory. For example, type <strong>https://mail.domain.com/owa​.</strong></li><li>Under <strong>Redirect Behavior</strong>, select the <strong>Only redirect requests to content in this directory (not subdirectories)</strong> check box.<br></li><li>In the <strong>Status code</strong> list, click <strong>Found (302)</strong>.</li><li>In the Actions pane, click <strong>Apply</strong>. <dl class="image"><dt> <img alt="OWARedirect.jpg" src="OWARedirect.jpg" style="width:800px;" /> </dt></dl></li><li>Click <strong>Default Web Site</strong>.</li><li>In the Default Web Site Home pane, double-click <strong>SSL Settings</strong>.</li><li>In <strong>SSL Settings</strong>, clear <strong>Require SSL</strong>. <dl class="image"><dt> <img alt="OWARedirect2.jpg" src="OWARedirect2.jpg" /> </dt></dl></li></ol><h3 class="ssw15-rteElement-H3">Step 2: Remove redirection from virtual directories</h3><ol><li>Open a Command Prompt window.<br></li><li>Navigate to:<p class="ssw15-rteElement-CodeArea">&lt;Window directory&gt;\System32\Inetsrv.<br></p></li><li>Run the following commands:<p class="ssw15-rteElement-CodeArea">appcmd set config "Default Web Site/autodiscover" /section:httpredirect /enabled:false -commit:apphost <br>appcmd set config "Default Web Site/ecp" /section:httpredirect /enabled:false -commit:apphost<br>appcmd set config "Default Web Site/ews" /section:httpredirect /enabled:false -commit:apphost<br>appcmd set config "Default Web Site/owa" /section:httpredirect /enabled:false -commit:apphost<br>appcmd set config "Default Web Site/oab" /section:httpredirect /enabled:false -commit:apphost<br>appcmd set config "Default Web Site/powershell" /section:httpredirect /enabled:false -commit:apphost<br>appcmd set config "Default Web Site/rpc" /section:httpredirect /enabled:false -commit:apphost<br>appcmd set config "Default Web Site/rpcwithcert" /section:httpredirect /enabled:false -commit:apphost<br>appcmd set config "Default Web Site/Microsoft-Server ActiveSync" /section:httpredirect /enabled:false -commit:apphost</p>​<br></li><li>Finish by running the command:<p class="ssw15-rteElement-CodeArea">
         <code>​​iisreset/noforce</code>.<br></p></li></ol><h3 class="ssw15-rteElement-H3">Step 3: Test that HTTP to HTTPS redirect is working</h3><ol><li>Open Internet Explorer and type in <b>http://mail.domain.com</b></li><li>DONE - You are then redirected to <b>https://mail.domain.com/owa</b>  <br></li></ol><dl class="image"><dt> <img src="iisnoredirect.jpg" alt="iisnoredirect.jpg" style="width:808px;" /> </dt><dd> Figure: Bad Example, no redirect in place for OWA<br></dd></dl><dl class="image"><dt> <img src="iisredirect.jpg" alt="iisredirect.jpg" style="width:808px;" /> </dt><dd>Figure: Good Example, redirect from HTTP to https for OWA </dd></dl>


