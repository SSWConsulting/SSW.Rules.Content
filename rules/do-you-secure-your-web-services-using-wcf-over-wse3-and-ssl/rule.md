---
type: rule
title: Do you secure your web services using WCF over WSE3 and SSL?
uri: do-you-secure-your-web-services-using-wcf-over-wse3-and-ssl
created: 2009-04-29T06:47:17.0000000Z
authors:
- id: 1
  title: Adam Cogan
- id: 17
  title: Ryan Tee

---



<span class='intro'> 
  <br>
Windows Communication Foundation (WCF) extends .NET Framework to enable building secure, reliable &amp; interoperable Web Services.<br>
WCF demonstrated interoperability with using the Web Services Security (WSS) including UsernameToken over SSL, UsernameToken for X509 Certificate and X509 Mutual Certificate profiles. 
 </span>


  <p>WSE has been outdated and replaced by WCF and has provided its own set of attributes that can be plugged into any Web Service application. </p>
<ol>
    <li><b>Security</b> <br>
    Implementation of security at the message layer security has several policies that can suite any environment including&#58;
    <ol>
        <li>Windows Token </li>
        <li>UserName Token </li>
        <li>Kerbose Token </li>
        <li>X.509 Certificate Token </li>
    </ol>
    At SSW we implement UserName Token using the standard login screen that prompts for a Username and a Password, which then gets passed into the SOAP header (at message level) for authorization.<br>
    This requires SSL which provides a secure tunnel from client to server.<br>
    However, message layer securtiy does not provide authentication security, so it does not stop the ability for a determined hacker to try user name / password attempts forever. Custom Policies setup at Application Level can to prevent brute force. </li>
    <li><b>Performance</b> <br>
    Indigo has got the smarts to negotiate to the most performant serialization and transport protocol that either side of the WS conversation can accommodate, so it will have the best performance having &quot;all-things-being-equal&quot;. You can configure the web services SSL session simply in the web.config file.<br>
    After having Configure an SSL certificate (in the LocalMachine store of the server), the following lines are required in the web.config&#58; </li>
</ol>
<p>&#160;</p>
<pre class="brush&#58;c-sharp">&lt;configuration xmlns=&quot;http&#58;//schemas.microsoft.com/.NetConfiguration/v2.0&quot;&gt;
&lt;system.serviceModel&gt;
&lt;services&gt;
&lt;service type=&quot;WCFService&quot; name=&quot;WCFService&quot;
behaviorConfiguration=&quot;ServiceBehaviour&quot;&gt;
&lt;endpoint contract=&quot;IWCFService&quot; binding=&quot;wsHttpBinding&quot;
bindingConfiguration=&quot;WSHttpBinding_IWCFServiceBinding&quot;/&gt;
&lt;/service&gt;
&lt;/services&gt;
&lt;bindings&gt;
&lt;wsHttpBinding&gt;
&lt;binding name=&quot;WSHttpBinding_IWCFServiceBinding&quot; &gt;
&lt;security mode=&quot;Message&quot;&gt;
&lt;message clientCredentialType=&quot;UserName&quot; /&gt;
&lt;/security&gt;
&lt;/binding&gt;
&lt;/wsHttpBinding&gt;
&lt;/bindings&gt;
&lt;behaviors&gt;
&lt;behavior name=&quot;ServiceBehaviour&quot; returnUnknownExceptionsAsFaults=&quot;true&quot; &gt;
&lt;serviceCredentials&gt;
&lt;serviceCertificate findValue=&quot;CN=SSW&quot; storeLocation=&quot;LocalMachine&quot;             
storeName=&quot;My&quot; x509FindType=&quot;FindBySubjectDistinguishedName&quot;/&gt;
    &lt;/serviceCredentials&gt;
    &lt;/behavior&gt;
    &lt;/behaviors&gt;
    &lt;/system.serviceModel&gt;
    &lt;/configuration&gt;     </pre>
<span class="ms-rteCustom-FigureGood">Figure&#58; Setting the SSL to Web Service for Message Layer Security.</span>



