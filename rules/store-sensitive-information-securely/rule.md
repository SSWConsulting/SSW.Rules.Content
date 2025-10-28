---
seoDescription: Securely store sensitive information such as credit card details and passport data with an enterprise password manager like Keeper to protect against data breaches, non-compliance, and management issues.
type: rule
title: Do you store your sensitive information securely?
uri: store-sensitive-information-securely
authors:
  - title: Warwick Leahy
    url: https://ssw.com.au/people/warwick-leahy/
related:
  - password-sharing-practices
  - choose-an-enterprise-password-manager
created: 2023-10-11T21:27:10.724Z
guid: 75da57d7-3f2c-4e5c-b964-eb656f52dccc
---

Keeping sensitive details like credit card numbers and passport information in unsecured places is risky. It can harm both the individuals involved and the organization’s reputation.

Ideally, avoid storing this information altogether. However, that is not always practical. Managers and CEOs often need to share these details with admin staff to book flights or arrange travel, for example. When that happens, make sure the information is stored and shared securely. Use encrypted files, password managers, or secure portals instead of emails, spreadsheets, or notes.

<!--endintro-->

## Risks of insecure storage

Storing credit card details, passport information, or any sensitive data in unsecured fields exposes the organization to unnecessary risks.

### Data breach

* Credit card information and passport details are highly sought-after by cybercriminals. When this data is stored in an unsecure manner, the likelihood of it being accessed and misused by unauthorized parties increases significantly
* Should a data breach occur, the organization could face severe reputational damage, legal consequences, and financial penalties. <https://www.oaic.gov.au/about-the-OAIC/our-regulatory-approach/guide-to-privacy-regulatory-action/chapter-7-privacy-assessments>

### Non-compliance with data protection regulations

* Global and regional data protection regulations, such as GDPR in Europe, CCPA in California, and the Australian Privacy Principles (APPs) under the Privacy Act 1988 in Australia, mandate strict guidelines on how personal and sensitive data should be stored and protected
* Storing such sensitive information in an insecure manner is a direct violation of these regulations, leading to hefty fines and legal action

### Data integrity and management issues

* Over time, unstructured and unsecured data can become outdated, redundant, or even be altered unintentionally
* Using Dynamics 365's notes field for such data means there's no systematic way to track its accuracy, validity, or history

  ::: bad
  ![Figure: Bad example - Storing sensitive data in Dynamics 365's  | Notes is insecure](bad-example-crm-notesfield.png)
  :::

## How to store details securely

Using **enterprise password managers** ensures that this data is stored securely, complies with data protection regulations such as the Australian Privacy Principles (APPs), and remains easy to manage.

### Keeper

* **End-to-end encryption** - [Keeper](https://www.keepersecurity.com) ensures that sensitive information is encrypted both in transit and at rest, using advanced encryption algorithms

* **Role-based access control** - Only authorized personnel can access and manage sensitive data. This ensures that sensitive information is not accidentally or intentionally accessed by unauthorized parties

   ::: good
   ![Figure: Good example - Role based access to sensitive data](keeper-goodexample-sharing.png)
   :::
  
   Even better, share sensitive details one time only, for a short and specific purpose.
  
   ::: good
   ![Figure: Good example - One-Time Share sensitive data for an hour](keeper-onetime-sharing.png)
   :::

* **Auditing and reporting** - Keeper provides detailed logs and reports, allowing for complete oversight and management of all data stored within

   ::: good
   ![Figure: Good example - Keeper allows full auditing of all access](keeper-good-example-auditreport.png)
   :::

* **Regulatory compliance** - With tools and features designed to aid organizations in complying with data protection regulations, enterprise password managers like Keeper ensure that sensitive information is handled according to global standards, including Australian Privacy Principles (APPs)
  
* **Data Integrity** - With structured data management, sensitive data stored in Keeper remains consistent, accurate, and up-to-date
