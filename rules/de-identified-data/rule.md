---
seoDescription: Only transfer de-identified data to ensure the privacy and security of client information.
type: rule
archivedreason:
title: Do you only transfer de-identified data?
guid: 276fe534-48e1-4ddc-81cb-d1452b84ce66
uri: de-identified-data
created: 2023-02-13T05:44:24+0000
authors:
  - title: Kaique Biancatti
    url: https://ssw.com.au/people/kaique-biancatti
related:
---

Ensuring the privacy and security of client data is a critical responsibility in today's digital age. With increasing data breaches and the rise of cyber-attacks, it is imperative to take proactive measures to protect client information. De-identifying data is a key step in reducing the risk of data breaches and safeguarding the privacy and confidentiality of client information.

<!--endintro-->

When working with client data, you should do the following:

1. Avoid copying client data to local servers in the first place. If it is unavoidable to copy the data, it is crucial to ensure that the data is de-identified before it is transferred. This helps to reduce the risk of unauthorized access to client information and protects against data breaches.
2. If copying data is not avoidable, only copy de-identified data. There are several tools available for de-identifying data, including:

   - Data masking software - Data masking software, such as Informatica MDM, K2View and IRI FieldShield, helps to protect client information by obscuring sensitive data with randomized characters, making it unreadable to unauthorized users.
   - Redaction tools - Redaction tools, like Adobe Acrobat Pro, Ibjective Redact and Egress Respond, allow you to remove sensitive information from documents by blacking out or obscuring the data.
   - Pseudonymization tools - Pseudonymization tools, such as Talend, replace sensitive data, such as personal identification, with generic identifiers, helping to protect the privacy and confidentiality of client information.
   - All-in-one de-identification software - For a complete solution, consider using all-in-one de-identification software, such as Anonymize, brighter AI, the Informatica suite, and Privacy1, which provides a range of tools and features for de-identifying data, including data masking, redaction, pseudonymization, and more.

3. If you must work with live data, it is recommended to use Azure. Azure is a secure and compliant cloud computing platform that provides a safe and secure environment for processing and storing client data. With Azure, you can ensure that client information is protected against unauthorized access and data breaches, while also meeting regulatory requirements and industry standards.

The [Future of Privacy Forum](https://fpf.org/blog/a-visual-guide-to-practical-data-de-identification/) has an easy guide to practical da de-identification:

::: good
![Figure: Good Example - It's crucial to understand what de-identification is, and how to protect the identity of others](deidentify.jpg)
:::
