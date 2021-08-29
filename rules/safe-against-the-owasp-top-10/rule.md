---
type: rule
archivedreason: 
title: Do you stay safe against the OWASP Top 10?
guid: 8e413708-5259-45d0-9352-747d68546bc6
uri: safe-against-the-owasp-top-10
created: 2016-05-13T18:31:21.0000000Z
authors:
- title: Steve Leigh
  url: https://ssw.com.au/people/steve-leigh
related: []
redirects:
- do-you-stay-safe-against-the-owasp-top-10

---

The Open Web Application Security Project (OWASP) is a non-profit charity organization whose sole purpose is to enable other organizations to develop applications that can be trusted.  Their most prominent piece of literature is the [OWASP Top 10](https&#58;//www.owasp.org/index.php/Top_10-2017_Top_10) – a list of the most critical risks found in software.  It is a “living” list, which means it is updated as vulnerabilities become known and more or less common.

<!--endintro-->

### OWASP Top 10 2017

The current OWASP Top 10 states the following are the top risks for web applications today. Knowing and securing against these will give the biggest bang-for-buck in securing your website.

* **Injection:** Being able to execute arbitrary SQL, LDAP or other code via your application
* **Broken authentication and session management:** Exploiting weak login and session management.  See our other [rules to better security](/rules-to-better-security)
* **Sensitive data exposure:** Storing sensitive data in a way that can easily be retrieved and abused
* **XML External Entities (XXE):** Exposing internal files or sensistive information through poorly configured external entity references in XML documents
* **Broken Access Control:** Exploiting poorly enforced authentication rules to access unauthorised data
* **Security Misconfiguration:** Insecure default configurations, misconfigured HTTP headers and verbose error messages containing sensitive information
* **Cross-site scripting (XSS):** Executing arbitrary JavaScript on a web page, often by reflecting unescaped user input
* **Insecure Deserialization:**  Not securing or sanitisng deserialisation can lead to remote code execution or other payload attacks
* **Using components with known vulnerabilities:** Applications and APIs using components with known vulnerabilities may undermine application defenses and enable various attacks
* **Insufficient Logging & Monitoring:**  Most breach studies show time to detect a breach is over 200 days, typically detected by external parties rather than internal processes or monitoring

#### Other Resources

Protecting against these is a large topic in their own right. There are plenty of resources with information on protecting against these, linked below:

* [Troy Hunt – Protecting your web apps from the tyranny of evil with OWASP](https://tv.ssw.com/1492/protecting-your-web-apps-from-the-tyranny-of-evil-with-owasp) - 
This video goes through the OWASP Top 10 in more detail, describing each risk, how to exploit it, and how to protect against it
* [OWASP Top 10](https://www.owasp.org/index.php/Category&#58;OWASP_Top_Ten_2017_Project) - The OWASP home page is a little difficult to navigate but contains fantastic information on the risks and how to protect against them. Use the link above to get details on each of the vulnerabilities, with examples on attacking, “Cheat Sheets” for prevention and risk/impact assessment
