---
seoDescription: Learn best practices for securely sharing sensitive information, including hosting recommendations.
type: rule
title: Do you securely share sensitive information?
uri: securely-share-sensitive-information
authors:
  - title: Rob Thomlinson
    url: https://ssw.com.au/people/rob-thomlinson
created: 2024-12-11T13:42:55.753
guid: 4612ecc6-00dc-4591-a087-680c57197706
related:
  - change-link-sharing-default-behaviour
  - secure-password-share
  - password-sharing-practices
---

Sharing sensitive information is an essential part of any business, however sharing information securely is equally important, especially when files, videos or images can contain sensitive information. Without proper precautions, sensitive data can inadvertently become accessible to unauthorised parties, creating significant risks.

<!--endintro-->

### Best Practices for Sharing Sensitive Information

When sharing files which may include sensitive content, such as discussions about clients or current security issues for a product, follow these steps to keep them secure:

#### 1. Choose a Secure Hosting Platform

- **Option 1 (Recommended)**: **SharePoint** (for files) and **Microsoft Stream** (for videos)
  - When recording videos via Teams, you can automatically uploaded the recordings to Microsoft Stream, this ensures that the videos remain private within your organisation.
  - SharePoint provides similar controls for document sharing and integrates seamlessly with other Microsoft 365 tools like Microsoft Stream.

- **Option 2**: **Google Drive**
  - When using the Google Suite users can upload files to Google Drive for the organisation and restrict access similarly to the Microsoft 365 suite

- **Option 2**: **YouTube Videos set to Private Visibility**
  - For teams not using Microsoft 365 products, YouTube's "Private" option can be used to share videos securely. Be cautious, as this approach can accidentally expose videos publicly if you are not careful.

#### 2. Restrict Access to Authorised Individuals

Ensure that only the relevant team members or clients can view sensitive information:
- Set file or folder permissions based on specific roles or groups.
- Periodically review permissions to remove access for users who no longer need it.

#### 3. Use Data Security Techniques

For extra protection, particularly when the information might be shared more broadly:
- **Redact information**: Replace or black out sensitive details in documents or screenshots.
- **Generalise context**: Use placeholders (e.g., "Client A" or "Project B") instead of real names and specifics.

#### 4. Securely Share Links

If you need to Securely Share Links, please see these rule:
- [Do you know how to securely share your passwords?](https://www.ssw.com.au/rules/secure-password-share)
- [Do you know the best way to share a password externally?](https://www.ssw.com.au/rules/password-sharing-practices)

#### 5. Regularly Review Privacy Policies on Hosting Services

Platforms like SharePoint and Stream adhere to strict security standards, but regular audits of your privacy settings and hosting policies help ensure continuous compliance with organisational or legal requirements.

---

::: greybox
**Scenario:**
You need to share a sprint summary video with your team, and it contains client-sensitive information.

**Steps:**
1. Upload the video to Microsoft Stream or SharePoint.
2. Set permissions to allow viewing only for specific team members.
3. Use the platform's secure sharing link feature, ensuring it’s time-limited.
:::

:::good
![Figure: Good example - Sensitive sprint summary uploaded to Microsoft Stream with confidential information redacted.](SecureSprintReviews.png)
:::

:::bad
![Figure: Bad Example - Sensitive sprint summary uploaded as a private YouTube video, however confidential information is exposed.](SecureSprintReviewsBad.png)
:::
