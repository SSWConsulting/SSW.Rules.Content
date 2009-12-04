---
type: rule
archivedreason: 
title: Do you secure your web services using WCF over WSE3 and SSL?
guid: 63388838-ff65-414b-83db-69691db56d69
uri: do-you-secure-your-web-services-using-wcf-over-wse3-and-ssl
created: 2009-04-29T06:47:17.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: Ryan Tee
  url: https://ssw.com.au/people/ryan-tee
related: []
redirects: []

---


This field should not be null (Remove me when you edit this field).
<br><excerpt class='endintro'></excerpt><br>
    <p>
        WSE has been outdated and replaced by WCF and has provided its own set of attributes
        that can be plugged into any Web Service application.
    </p>
    <ol>
        <li><b>Security</b>
            <br>
            Implementation of security at the message layer security has several policies that
            can suite any environment including&#58;
            <ol>
                <li>Windows Token </li>
                <li>UserName Token </li>
                <li>Kerbose Token </li>
                <li>X.509 Certificate Token </li>
            </ol>
            At SSW we implement UserName Token using the standard login screen that prompts
            for a Username and a Password, which then gets passed into the SOAP header (at message
            level) for authorization.<br>
            This requires SSL which provides a secure tunnel from client to server.<br>
            However, message layer securtiy does not provide authentication security, so it
            does not stop the ability for a determined hacker to try user name / password attempts
            forever. Custom Policies setup at Application Level can to prevent brute force.
        </li>
        <li><b>Performance</b>
            <br>
            Indigo has got the smarts to negotiate to the most performant serialization and
            transport protocol that either side of the WS conversation can accommodate, so it
            will have the best performance having &quot;all-things-being-equal&quot;. You can configure
            the web services SSL session simply in the web.config file.<br>
            After having Configure an SSL certificate (in the LocalMachine store of the server),
            the following lines are required in the web.config&#58; </li>
    </ol>
    <p>
        &#160;</p>
<pre class="brush&#58;c-sharp">
{ltHTMLChar}configuration xmlns=&quot;http&#58;//schemas.microsoft.com/.NetConfiguration/v2.0&quot;{gtHTMLChar}
{ltHTMLChar}system.serviceModel{gtHTMLChar}
{ltHTMLChar}services{gtHTMLChar}
{ltHTMLChar}service type=&quot;WCFService&quot; name=&quot;WCFService&quot;
behaviorConfiguration=&quot;ServiceBehaviour&quot;{gtHTMLChar}
{ltHTMLChar}endpoint contract=&quot;IWCFService&quot; binding=&quot;wsHttpBinding&quot;
bindingConfiguration=&quot;WSHttpBinding_IWCFServiceBinding&quot;/{gtHTMLChar}
{ltHTMLChar}/service{gtHTMLChar}
{ltHTMLChar}/services{gtHTMLChar}
{ltHTMLChar}bindings{gtHTMLChar}
{ltHTMLChar}wsHttpBinding{gtHTMLChar}
{ltHTMLChar}binding name=&quot;WSHttpBinding_IWCFServiceBinding&quot; {gtHTMLChar}
{ltHTMLChar}security mode=&quot;Message&quot;{gtHTMLChar}
{ltHTMLChar}message clientCredentialType=&quot;UserName&quot; /{gtHTMLChar}
{ltHTMLChar}/security{gtHTMLChar}
{ltHTMLChar}/binding{gtHTMLChar}
{ltHTMLChar}/wsHttpBinding{gtHTMLChar}
{ltHTMLChar}/bindings{gtHTMLChar}
{ltHTMLChar}behaviors{gtHTMLChar}
{ltHTMLChar}behavior name=&quot;ServiceBehaviour&quot; returnUnknownExceptionsAsFaults=&quot;true&quot; {gtHTMLChar}
{ltHTMLChar}serviceCredentials{gtHTMLChar}
{ltHTMLChar}serviceCertificate findValue=&quot;CN=SSW&quot; storeLocation=&quot;LocalMachine&quot;             
storeName=&quot;My&quot; x509FindType=&quot;FindBySubjectDistinguishedName&quot;/{gtHTMLChar}
    {ltHTMLChar}/serviceCredentials{gtHTMLChar}
    {ltHTMLChar}/behavior{gtHTMLChar}
    {ltHTMLChar}/behaviors{gtHTMLChar}
    {ltHTMLChar}/system.serviceModel{gtHTMLChar}
    {ltHTMLChar}/configuration{gtHTMLChar}     </pre>
    <span class="ms-rteCustom-FigureGood">Figure&#58; Setting the SSL to Web Service for Message Layer Security.</span>


