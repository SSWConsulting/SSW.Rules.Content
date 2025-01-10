---
type: rule
tips: ""
title: Do you know how to host Classic ASP on Azure?
seoDescription: How to migrate your Classic ASP website to Azure, using Azure
  App Service with Docker or Azure Virtual Machines including considerations and
  best practices
uri: host-classic-asp-on-azure
authors:
  - title: Gordon Beeming
    url: https://www.ssw.com.au/people/gordon-beeming/
  - title: Matt Wicks
    url: https://www.ssw.com.au/people/matt-wicks/
created: 2024-12-12T16:44:00.000Z
guid: 8f04a3f4-01c8-4ecb-8bb7-281b80576ed9
---
Migrating a website can be a challenging undertaking, especially when dealing with legacy technologies like Classic ASP. Many organizations with Classic ASP applications are looking to move to a cloud platform like **Azure** due to issues with their current hosting providers, such as outages and downtime that result in unacceptable levels of downtime for end users. 

Moving to Azure offers numerous advantages, including enhanced scalability, reliability, and security. This rule provides a comprehensive guide to migrating your Classic ASP website to Azure, outlining the best options, considerations, and best practices.
<!--endintro-->

## Azure service options for hosting classic ASP websites

Azure doesn't natively support Classic ASP as it does for newer .NET applications. However, there are two primary options for hosting your Classic ASP website on Azure:

### Option 1: Azure App Service with Docker (Recommended)

This is generally the preferred approach for migrating Classic ASP websites. Containerizing your application with Docker allows for seamless deployment to Azure App Service and enables you to leverage its key features, including scalability, load balancing, and automated deployments. 

See:
https://learn.microsoft.com/en-us/azure/migrate/tutorial-app-containerization-aspnet-app-service

**✅ Pros:**
- Scalability and load balancing
- Automated deployments
- Managed platform with built-in features
- Cost-effective for most scenarios
- Offers a "longer shelf life" for legacy applications

**❌ Cons:**
- Requires Docker knowledge 
- May require code changes for compatibility

### Option 2: Azure Virtual Machines

If you need greater control over the underlying infrastructure or have specific dependencies that aren't compatible with App Service, you can create a Windows Virtual Machine in Azure and install the necessary components to host your Classic ASP application.

See:
https://azure.microsoft.com/en-us/products/virtual-machines/windows

**✅ Pros:**
- Full control over the environment
- Can accommodate complex dependencies
- Suitable for applications that require specific configurations

**❌ Cons:**
- More management overhead  
- Higher cost compared to App Service

## Migration with Docker

If you choose to migrate your Classic ASP application to Azure App Service using Docker, here's a step-by-step guide to help you through the process:

1. **Setup Classic ASP Application:** Ensure your application is properly configured and ready for containerization.
2. **Create [Dockerfile](https://docs.docker.com/reference/dockerfile/):** In your application folder, create a Dockerfile that defines the environment and dependencies for your application.
3. **Create local [Docker image](https://docs.docker.com/get-started/docker-concepts/building-images/):** Build a Docker image locally based on your Dockerfile.
4. **Push the Image to [Azure Container Registry](https://learn.microsoft.com/en-us/azure/container-registry/container-registry-get-started-portal?tabs=azure-cli):** Create an Azure Container Registry and push your Docker image to it.
5. **Create [Azure Web App using Docker image](https://learn.microsoft.com/en-us/azure/app-service/tutorial-custom-container?pivots=container-linux&tabs=azure-cli):** Create an Azure Web App and configure it to use your Docker image from the Azure Container Registry.


## Considerations and Challenges

Migrating a Classic ASP website to Azure can present some challenges that require careful consideration:

- **COM/COM+ Components**: Azure App Service does not allow the registration of COM/COM+ components. If your application relies on these, you'll need to rewrite them in managed code or explore alternative solutions. This might involve significant code modifications and refactoring

- **Windows Authentication:** If your application uses Windows Authentication, you might need to replace it with Azure Entra ID. This could require code changes and potential adjustments to your application logic to ensure compatibility with Azure Entra ID

- **Database Connectivity:** Ensure that your database can be migrated to Azure or accessed from Azure. You might need to adjust connection strings and configure network settings to establish proper connectivity between your application and the database. For example, if you're migrating to Azure SQL Database, you'll need to update your connection strings with the appropriate credentials and server address. You might also need to configure firewall rules to allow access from your Azure App Service or Virtual Machine.
- **Third-party Dependencies:** Evaluate any third-party dependencies your application uses and ensure they are compatible with the chosen Azure service. Some older libraries or components might not be compatible with the Azure environment, requiring you to find alternatives or update them to newer versions.

## Best practices for migrating classic ASP websites to Azure
- **Assess Your Application:** Thoroughly evaluate your application's dependencies, codebase, and configuration to identify potential challenges and plan accordingly.
- **Containerize with Docker:** If using Azure App Service, containerize your application with Docker to simplify deployment and improve portability.
- **Modernize Your Code:** Update outdated libraries, refactor code, and address security vulnerabilities to improve security, performance, and maintainability.
- **Test Thoroughly:** Before switching over to Azure, rigorously test your application in the new environment to ensure everything functions as expected.
- **Use Migration Tools:** Leverage Azure Migrate and other migration tools to streamline the process and reduce manual effort.
- **Understand File Structure:** When hosting on self-hosted IIS, the default location of the sites is `C:\inetpub\wwwroot`, Azure App Services stores the root content for a site in a fixed home directory `D:\home\site\wwwroot`. Double-check your code and application configuration for any references to this path.

## Conclusion
Migrating a Classic ASP website to Azure can be a complex process, but with careful planning and execution, it can bring significant benefits. By understanding the available options, considering the challenges, and following best practices, you can successfully move your website to the cloud and enjoy improved performance, scalability, and reliability.

Key takeaways from the research include:

- **Containerization with Docker:** Using Docker to containerize your Classic ASP application simplifies the deployment process and enhances portability when using Azure App Service.
- **Legacy Dependencies:** Migrating legacy dependencies like COM/COM+ components and Windows Authentication can be challenging and may require code modifications.
- **Database Migration:** Ensure your database is compatible with Azure or can be accessed from Azure. Plan for potential adjustments to connection strings and network settings.
- **Thorough Assessment and Testing:** Before migrating, thoroughly assess your application and conduct rigorous testing in the Azure environment to ensure a smooth transition.

By carefully considering these factors and leveraging the resources and best practices outlined in this article, you can confidently migrate your Classic ASP website to Azure and take advantage of the cloud's capabilities.




