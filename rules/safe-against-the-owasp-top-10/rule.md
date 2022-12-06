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

The Open Web Application Security Project (OWASP) is a non-profit charity organization whose sole purpose is to enable other organizations to develop applications that can be trusted.  Their most prominent piece of literature is the [OWASP Top 10](https://owasp.org/Top10/) – a list of the most critical risks found in software.  It is a “living” list, which means it is updated as vulnerabilities become known and more or less common.

<!--endintro-->

### OWASP Top 10 2021

The current OWASP Top 10 states the following are the top risks for web applications today. Knowing and securing against these will give the biggest bang-for-buck in securing your website.

* **Broken Access Control:** Insufficient controls in place to implement the principle of least privilege, insufficient access control protections
* **Cryptographic Failures:** Data transmitted in clear text, sensitive data not encrypted at rest, using weak or broken cryptography algorithms
* **Injection:** Failure to validate user-supplied data, queries not parameterized
* **Insecure Design:** Security not considered as a baseline principle, security added as an after-thought (essentially, need to "shift-left" security)
* **Security Misconfiguration:** Insecure default configurations, misconfigured HTTP headers and verbose error messages containing sensitive information
* **Vulnerable and Outdated Components:** Packages and dependencies not kept up to date, versions with known vulnerabilities kept in the product
* **Identification and Authentication Failures:** Brute force attacks, credential stuffing, missing MFA, permits weak passwords, simple password recovery
* **Software and Data Integrity Failures:**  Failure of infrastructure configuration to protect against exploits, e.g. supply chain attacks, dependency package spoofing
* **Security Logging and Monitoring Failures:** Not logging security events, not monitoring or auditing logs, not raising alerts for suspicious events
* **Server-Side Request Forgery:**  Arbitrarily fetching data from user supplied URLs

#### Other Resources

Protecting against these is a large topic in their own right. There are plenty of resources with information on protecting against these, linked below:

* [Troy Hunt – Protecting your web apps from the tyranny of evil with OWASP](https://tv.ssw.com/1492/protecting-your-web-apps-from-the-tyranny-of-evil-with-owasp) - 
This video goes through the OWASP Top 10 in more detail, describing each risk, how to exploit it, and how to protect against it
* [OWASP Top 10](https://owasp.org/www-project-top-ten/) - The OWASP home page is a little difficult to navigate but contains fantastic information on the risks and how to protect against them. Use the link above to get details on each of the vulnerabilities, with examples on attacking, “Cheat Sheets” for prevention and risk/impact assessment
