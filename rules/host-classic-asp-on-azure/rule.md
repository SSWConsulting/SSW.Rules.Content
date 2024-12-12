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
Migrating a website can be a challenging undertaking, especially when dealing with legacy technologies like Classic ASP. Many organizations with Classic ASP applications are looking to move to a cloud platform like **Azure** due to issues with their current hosting providers, such as outages and downtime that result in unacceptable levels of downtime for end users. 

Moving to Azure offers numerous advantages, including enhanced scalability, reliability, and security. This rule provides a comprehensive guide to migrating your Classic ASP website to Azure, outlining the best options, considerations, and best practices.
<!--endintro-->

**Azure Services for Hosting Classic ASP Websites**

Azure doesn't natively support Classic ASP as it does for newer .NET applications. With the introduction of virtual machine roles, Azure opened up possibilities for hosting Classic ASP applications. Here are the most suitable options for hosting your website:

**Option 1: [Azure App Service with Docker](https://learn.microsoft.com/en-us/azure/migrate/tutorial-app-containerization-aspnet-app-service)(Recommended)** 

This is generally the preferred approach for migrating Classic ASP websites. Containerizing your application with Docker allows for seamless deployment to Azure App Service and enables you to leverage its key features, including scalability, load balancing, and automated deployments.

**✅ Pros:**
- Scalability and load balancing
- Automated deployments
- Managed platform with built-in features
- Cost-effective for most scenarios
- Offers a "longer shelf life" for legacy applications

**❌ Cons:**
- Requires Docker knowledge 
- May require code changes for compatibility

**Option 2: [Azure Virtual Machines](https://azure.microsoft.com/en-us/products/virtual-machines/windows)**

If you need greater control over the underlying infrastructure or have specific dependencies that aren't compatible with App Service, you can create a Windows Virtual Machine in Azure and install the necessary components to host your Classic ASP application.

**✅ Pros:**
- Full control over the environment
- Can accommodate complex dependencies
- Suitable for applications that require specific configurations

**❌ Cons:**
- More management overhead  
- Higher cost compared to App Service

**Migration with Docker**

If you choose to migrate your Classic ASP application to Azure App Service using Docker, here's a step-by-step guide to help you through the process:

1. **Setup Classic ASP Application:** Ensure your application is properly configured and ready for containerization.
2. **Create [Dockerfile](https://docs.docker.com/reference/dockerfile/):** In your application folder, create a Dockerfile that defines the environment and dependencies for your application.
3. **Create local [Docker image](https://docs.docker.com/get-started/docker-concepts/building-images/):** Build a Docker image locally based on your Dockerfile.
4. **Push the Image to [Azure Container Registry](https://learn.microsoft.com/en-us/azure/container-registry/container-registry-get-started-portal?tabs=azure-cli):** Create an Azure Container Registry and push your Docker image to it.
5. **Create [Azure Web App using Docker image](https://learn.microsoft.com/en-us/azure/app-service/tutorial-custom-container?pivots=container-linux&tabs=azure-cli):** Create an Azure Web App and configure it to use your Docker image from the Azure Container Registry.


**Considerations and Challenges**

Migrating a Classic ASP website to Azure can present some challenges that require careful consideration:

- **[COM/COM+ Components](https://imranarshad.com/containerize-and-migrate-legacy-classic-asp-to-azure-app-service/)**: Azure App Service does not allow the registration of COM/COM+ components. If your application relies on these, you'll need to rewrite them in managed code or explore alternative solutions. This might involve significant code modifications and refactoring

- **[Windows Authentication](https://imranarshad.com/containerize-and-migrate-legacy-classic-asp-to-azure-app-service/):** If your application uses Windows Authentication, you might need to replace it with Azure AD. This could require code changes and potential adjustments to your application logic to ensure compatibility with Azure AD

- **Database Connectivity:** Ensure that your database can be migrated to Azure or accessed from Azure. You might need to adjust connection strings and configure network settings to establish proper connectivity between your application and the database. For example, if you're migrating to Azure SQL Database, you'll need to update your connection strings with the appropriate credentials and server address. You might also need to configure firewall rules to allow access from your Azure App Service or Virtual Machine.
- **Third-party Dependencies:** Evaluate any third-party dependencies your application uses and ensure they are compatible with the chosen Azure service. Some older libraries or components might not be compatible with the Azure environment, requiring you to find alternatives or update them to newer versions
