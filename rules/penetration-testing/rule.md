---
type: rule
tips: ""
title: Do you take Penetration Testing seriously?
seoDescription: When testing the security of company systems, it's important to conduct Penetration Testing to get a holistic view of company systems to ensure that vulnerabilities are identified and patched before bad actors get to them. Read what penetration tests are, why it's important to do them, how you can protect yourself, and what tools can be used to assist with penetration testing during development.
uri: penetration-testing
authors:
  - title: Lewis Toh
    url: https://www.ssw.com.au/people/lewis-toh/
  - title: Josh Berman
    url: https://www.ssw.com.au/people/josh-berman/
related:
  - multi-factor-authentication-enabled
  - password-manager
redirects: []
created: 2025-02-05T14:56:00.000Z
guid: e4b4cf20-6ca6-480c-809e-4db55019ed9e
---
Penetration testing is an important part of maintaining secure networks and systems - it provides a simulated and controlled way to test the strength of your security. When all your services and infrastructure are exposed to the world, how can you make sure you're safe?

<!--endintro-->

`youtube: https://www.youtube.com/embed/0mPZ0BomyG8`
**Video: Do you take Penetration Testing seriously? | Rob Thomlinson & Oliver Judson | Rules (8 min)**

## What is Penetration Testing?

Penetration Testing is a **simulated cyberattack performed by security professionals** to evaluate the security of the services, systems, and networks of an individual or company. It helps companies identify vulnerabilities in their security systems, access the potential impact and damages, and steps to fix these vulnerabilities.

![Figure: Penetration Testing is an important part of securing your systems](imagefx.jpg)

## Why do we need penetration testing?

It is important for several reasons:

* By mimicking real attackers, penetration testers can **identify vulnerabilities** and, most importantly, **provide solutions** to fix these vulnerabilities before they can be exploited by bad actors.
* Using an external tester **eliminates implicit biases and assumptions**, avoids conflict of interest, and uncovers security flaws that may be overlooked internally.
* The **cost** to secure yourself from an attack is far cheaper than the consequences of an attack.
* Evaluates the **quality** of existing policies, tools and procedures.
* Evaluates **incident response measures** by measuring how well the security team detects, responds to, and mitigates attacks.
* As attack techniques evolve, penetration tests help companies **adapt and defend** against emerging threats and vulnerabilities.

## How can you improve your security?

Great company security starts with great user security. Here are some of the most valuable ways you can help defend against an attacker:

1. Multi Factor Authentication – **[more than one authentication method](https://www.ssw.com.au/rules/multi-factor-authentication-enabled/)** means more layers of security.
2. Use **[password managers](https://www.ssw.com.au/rules/password-manager/)** to generate unique passwords for every service (and auto-fill them).
3. **[Lock your laptop](https://www.ssw.com.au/rules/lock-your-computer-when-you-leave/)** when you leave your desk. For Windows users, check out [DynamicLock](https://learn.microsoft.com/en-us/windows/security/identity-protection/hello-for-business/hello-feature-dynamic-lock).
4. **[Avoid malware](https://www.ssw.com.au/rules/understand-the-dangers-of-social-engineering/)** by not clicking on suspicious links and making sure the person is who they say they are.
5. **[Report potential breaches to SysAdmins]((https://www.ssw.com.au/rules/security-compromised-password/))**, whether it's your personal account or a company account.

## Tools

### For SysAdmins

* **[BloodHound](https://bloodhound.readthedocs.io/en/latest/index.html)** and **[Pingcastle](https://www.pingcastle.com/)** can be used to analyse domain security.
* **[Kali Linux](https://www.kali.org/)** is an Open Source **Linux** distribution that focuses on penetration testing and network security assessments.

### For Developers

* **[Burp Suite](https://portswigger.net/burp)** is used for Web-application security testing
* **[Insomnia](https://insomnia.rest/)** is used for API management and testing
