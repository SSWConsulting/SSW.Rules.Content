---
type: rule
tips: ""
title: Do you know how to host classic ASP on Azure?
seoDescription: This rule outlines the steps, considerations, and best practices
  for migrating your Classic ASP website to Azure, including using Azure App
  Service with Docker and Azure Virtual Machines
uri: host-classic-asp-on-azure
authors:
  - title: ""
guid: 8f04a3f4-01c8-4ecb-8bb7-281b80576ed9
---
Migrating a website can be a challenging undertaking, especially when dealing with legacy technologies like Classic ASP. Many organizations with Classic ASP applications are looking to move to a cloud platform like **Azure** due to issues with their current hosting providers, such as outages and downtime that result in unacceptable levels of downtime for end users. Moving to Azure offers numerous advantages, including enhanced scalability, reliability, and security. This rule provides a comprehensive guide to migrating your Classic ASP website to Azure, outlining the best options, considerations, and best practices.
<!--endintro-->
**Azure Services for Hosting Classic ASP Websites**

Azure doesn't natively support Classic ASP as it does for newer **.NET applications**. With the introduction of virtual machine roles, Azure opened up possibilities for hosting Classic ASP applications. Here are the most suitable options for hosting your website:

- **[Azure App Service with Docker](https://learn.microsoft.com/en-us/azure/migrate/tutorial-app-containerization-aspnet-app-service)(Recommended):** This is generally the preferred approach for migrating Classic ASP websites. Containerizing your application with Docker allows for seamless deployment to Azure App Service and enables you to leverage its key features, including scalability, load balancing, and automated deployments.
- **[Azure Virtual Machines](https://azure.microsoft.com/en-us/products/virtual-machines/windows)**: If you need greater control over the underlying infrastructure or have specific dependencies that aren't compatible with App Service, you can create a Windows Virtual Machine in Azure and install the necessary components to host your Classic ASP application


2. Place your content here. Markdown is your friend. See this [example rule](https://www.ssw.com.au/rules/rule) for all the things you can do with Rules.
3. Submit your rule for review.
4. Add your rule to a category. See [How to Add and Edit Categories and Top Categories](https://github.com/SSWConsulting/SSW.Rules.Content/wiki/How-to-Add-and-Edit-Categories-and-Top-Categories).
