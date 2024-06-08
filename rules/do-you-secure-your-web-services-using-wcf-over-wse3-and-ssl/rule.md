---
type: rule
title: Do you secure your web services using WCF over WSE3 and SSL?
uri: do-you-secure-your-web-services-using-wcf-over-wse3-and-ssl
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
  - title: Ryan Tee
    url: https://ssw.com.au/people/ryan-tee
    noimage: true
related: []
redirects: []
created: 2009-04-29T06:47:17.000Z
archivedreason: null
guid: 63388838-ff65-414b-83db-69691db56d69
---

Windows Communication Foundation (WCF) extends .NET Framework to enable building secure, reliable & interoperable Web Services.

WCF demonstrated interoperability with using the Web Services Security (WSS) including UsernameToken over SSL, UsernameToken for X509 Certificate and X509 Mutual Certificate profiles.   
<!--endintro-->

WSE has been outdated and replaced by WCF and has provided its own set of attributes that can be plugged into any Web Service application.

1. **Security** 
Implementation of security at the message layer security has several policies that can suite any environment including:
    1. Windows Token
    2. UserName Token
    3. Kerbose Token
    4. X.509 Certificate Token

    It is recommended to implement UserName Token using the standard login screen that prompts for a Username and a Password, which then gets passed into the SOAP header (at message level) for authorization.

    This requires SSL which provides a secure tunnel from client to server.

    However, message layer securtiy does not provide authentication security, so it does not stop the ability for a determined hacker to try username / password attempts forever. Custom Policies setup at Application Level can to prevent brute force.
   
3. **Performance** 

    Indigo has got the smarts to negotiate to the most performant serialization and transport protocol that either side of the WS conversation can accommodate, so it will have the best performance having "all-things-being-equal". You can configure the web services SSL session simply in the web.config file.

    After having Configure an SSL certificate (in the LocalMachine store of the server), the following lines are required in the web.config:

```xml
<configuration xmlns="http://schemas.microsoft.com/.NetConfiguration/v2.0">
<system.serviceModel>
    <services>
        <service 
            type="WCFService" 
            name="WCFService"
            behaviorConfiguration="ServiceBehaviour"
        >
            <endpoint 
                contract="IWCFService" 
                binding="wsHttpBinding"
                bindingConfiguration="WSHttpBinding_IWCFServiceBinding"
            />
        </service>
    </services>

    <bindings>
        <wsHttpBinding>
            <binding name="WSHttpBinding_IWCFServiceBinding">
                <security mode="Message">
                    <message clientCredentialType="UserName" />
                </security>
             </binding>
        </wsHttpBinding>
    </bindings>

    <behaviors>
        <behavior name="ServiceBehaviour" returnUnknownExceptionsAsFaults="true">
            <serviceCredentials>
                <serviceCertificate 
                    findValue="CN=SSW" 
                    storeLocation="LocalMachine"             
                    storeName="My"
                    x509FindType="FindBySubjectDistinguishedName"
                />
            </serviceCredentials>
        </behavior>
    </behaviors>
</system.serviceModel>
</configuration>
```

**Figure: Setting the SSL to Web Service for Message Layer Security**
