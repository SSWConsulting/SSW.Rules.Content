---
type: rule
title: Do you use SPF, DKIM and DMARC for email security?
uri: email-security-spf-dkim-dmarc
authors:
  - title: Chris Schultz
    url: https://ssw.com.au/people/chris-schultz
related:
  - do-you-know-how-to-reduce-spam
created: 2023-11-02T04:12:53.453Z
guid: 697d3978-0fb6-4266-bb63-2a6055ab57e4
---
Email is a critical communication tool for businesses and individuals worldwide. However, it’s also a common vector for cyber threats like phishing and spoofing.

Three ways these threats are combatted are **Sender Policy Framework (SPF)**, **DomainKeys Identified Mail (DKIM)**, and **Domain-based Message Authentication, Reporting & Conformance (DMARC)**.

<!--endintro-->

## SPF (Sender Policy Framework)

SPF is an email authentication method designed to prevent spammers from sending emails on behalf of your domain. By creating an SPF record in your Domain Name System (DNS), you can specify which mail servers are authorized to send email from your domain.

### Basic Steps for Implementing SPF:

1. Identify the mail servers that are authorized to send email on behalf of your domain.
2. Create an SPF record in the DNS for your domain. The record might look something like:

```
v=spf1 ip4:192.0.2.0/24 ip4:198.51.100.123 a -all
```

## DKIM (DomainKeys Identified Mail)

DKIM provides an encryption key and digital signature that verifies that an email message was not faked or altered.

### Basic Steps for Implementing DKIM in Exchange Online:

1. Generate a pair of cryptographic keys - one private and one public.
2. The private key is kept secure on your mail server.
3. The public key is added to the DNS records for your domain.
4. When an email is sent, it is signed with the private key.

See [Microsoft's documentation](https://learn.microsoft.com/en-us/microsoft-365/security/office-365-security/email-authentication-dkim-configure?view=o365-worldwide) for more details on how to set this up in Exchange Online.

## DMARC (Domain-based Message Authentication, Reporting & Conformance)

DMARC unifies the SPF and DKIM authentication mechanisms into a common framework and allows domain owners to declare how they would like email from that domain to be handled if it fails authentication tests.

### Basic Steps for Implementing DMARC in Exchange Online:

1. Ensure SPF and DKIM are in place.
2. Create a DMARC policy record, which will look something like:

```
v=DMARC1; p=none; rua=mailto:dmarc@yourdomain.com
```

By implementing these three protocols in Exchange Online, you can significantly enhance the security of your email communications, protect your brand reputation, and increase email deliverability rates.

## Avoid whitelisting domains