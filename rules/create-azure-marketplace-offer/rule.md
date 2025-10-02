---
seoDescription: Learn how to create an Azure Marketplace offer, including the required steps, assets, and configurations to successfully publish your solution.
type: rule
archivedreason:
title: Do you know how to create an Azure Marketplace offer?
guid: 56b5a7f1-ddfc-4752-917d-0dbe6db9b954
uri: create-azure-marketplace-offer
created: 2025-09-12T04:20:00.0000000Z
authors:
  - title: Luke Mao
    url: https://ssw.com.au/people/luke-mao
  - title: Jim Zheng
    url: https://ssw.com.au/people/jim-zheng
related:
redirects:
---

Publish your solution to the [Azure Marketplace](https://azuremarketplace.microsoft.com) to reach millions of Microsoft customers and unlock new revenue streams. However, many partners underestimate the preparation required, which leads to rejected offers, costly delays, or poor marketplace visibility.

<!--endintro-->

`youtube: https://www.youtube.com/embed/e7RvBydtmj4`

**Video: Marketplace Mini | Creating a marketplace offer (2 min)**

## Prerequisites

Before you begin creating your Azure Marketplace offer, ensure you have:

1. **Microsoft Partner Center account** - [Register for Partner Center](https://partner.microsoft.com) if you don't have one
2. **Verified publisher profile** - Complete the publisher verification process with legal documents and tax information
3. **Azure subscription** - Required for testing your offer in a real Azure environment
4. **Technical solution ready** - Your application or service must be production-ready and meet Azure's technical requirements
5. **Business documentation** - Terms of use, privacy policy, and support contact information

::: info
**Note:** The publisher verification process can take several days, so plan accordingly.
:::

## The key steps to creating an offer

### 1. Choose your offer type

Select the most appropriate offer type based on your solution:

- **Azure Application (Managed app)** - Solutions with managed resource deployment. See example: [SSW.EagleEye](https://azuremarketplace.microsoft.com/en-us/marketplace/apps/ssw1700450141896.ssweagleeye?tab=Overview)
- **Azure Application (Solution template)** - Multi-resource deployments using ARM templates
- **Azure Container** - Containerized applications for Azure Container Instances/Kubernetes
- **Azure Virtual Machine** - VM-based applications with pre-configured software
- **Software as a Service (SaaS)** - Cloud applications with subscription billing

**Note:** See [Microsoft's offer type guidance](https://learn.microsoft.com/en-us/partner-center/marketplace-offers/determine-your-listing-type) for all available types.

### 2. Follow offer type-specific publishing guide

Different types of offers have different publishing steps. Follow Microsoft's [Publisher Guide by Offer Type](https://learn.microsoft.com/en-us/partner-center/marketplace-offers/publisher-guide-by-offer-type) for detailed steps.

#### Example: Azure Application offer

Publishing an Azure Application offer involves several key phases:

1. **Plan your offer** - Choose between Solution Template or Managed Application based on your management and transaction needs
2. **Prepare technical assets** - Create ARM templates, managed application packages, and configure resource deployment
3. **Configure offer details** - Set up properties, offer listing with descriptions and media, preview audience, and technical configuration
4. **Create plans** - Define pricing models, availability, and plan-specific configurations
5. **Test and validate** - Use preview mode for end-to-end testing before full publication
6. **Market your offer** - Configure co-sell opportunities and CSP program participation

For detailed guidance on each step, see the [Azure Application publishing guide](https://learn.microsoft.com/en-us/partner-center/marketplace-offers/plan-azure-application-offer).

::: good
![Figure: Good example - SSW.EagleEye is published to Azure Marketplace](eagleeye-azure-marketplace.png)
:::
