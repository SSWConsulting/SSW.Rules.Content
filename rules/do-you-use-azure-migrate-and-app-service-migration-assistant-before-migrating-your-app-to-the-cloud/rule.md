---
seoDescription: Learn why you should use Azure Migrate and the App Service Migration Assistant for assessing and migrating on-premise applications to Azure with a fast, clear, and repeatable process.
type: rule
title: Do you use Azure Migrate and App Service Migration Assistant before migrating your app to the cloud?
uri: azure-migrate-before-migration
authors:
  - title: Ben Neoh
    url: https://www.ssw.com.au/people/ben-neoh
  - title: Rick Su
    url: https://www.ssw.com.au/people/rick-su
    
related:
  - azure-do-you-use-the-right-azure-service
  - azure-do-you-use-azure-landing-zones
created: 2025-07-17T13:45:00.000Z
guid: 3d9644e5-1d2d-456f-a7b4-90b8923a1e4b
---

Migrating legacy applications to Azure without first performing a readiness assessment can lead to unexpected failures or hidden blockers. Using Azure’s App Service Migration Assistant, an on-premises web application was assessed and packaged for migration efficiently through Microsoft’s PowerShell scripts.

<!--endintro-->

By following this structured, automated approach, migrations are faster, clearer, and more predictable.

### Why use Azure Migrate + App Service Migration Assistant?

**✅ Pros**

* **Fast process** – Full assessment and packaging completed within 30-60 minutes when paired with SysAdmin who had the knowledge of the application's on-premises server.
* **Clear, actionable reports** – Output is easy to interpret, helping teams resolve migration blockers quickly.
* **Repeatable and scalable** – Scripts are well-documented, ideal for reuse across multiple migrations.

::: greybox
Scripts used:
1. `Get-SiteReadiness.ps1` – Assesses suitability for Azure App Service, checking:
   - Configuration errors
   - Location tag issues
   - HTTPS binding setup
2. `Get-SitePackage.ps1` – Packages the site for migration.
3. `Generate-MigrationSettings.ps1` – Generates deployment configuration files.
:::
::: good
Figure: Good Example – A clear, script-driven process with consistent output.
:::

**⚠️ Cons**

* Requires **local administrator access** – Scripts must be run directly on the server (coordination with SysAdmin required) dev cannot do this by himself.
* **No remote execution** – Assessment cannot be initiated remotely.

---

### Recommendation

Use Azure Migrate and the App Service Migration Assistant before migrating any web application to Azure. This toolset helps identify blockers early and reduces time spent resolving avoidable issues during actual migration.

For web applications, always run the assessment scripts in advance and generate migration packages using Microsoft’s tools. This will help your team feel more confident in the migration process and avoid unnecessary surprises.

### Useful Resources

* [🔗 Official Azure App Service Migration Assistant Documentation](https://learn.microsoft.com/en-us/azure/app-service/app-service-migration-assistant)
* [🔗 App Service Migration Assistant – Official Azure Blog Announcement](https://azure.microsoft.com/en-us/blog/introducing-the-app-service-migration-assistant-for-asp-net-applications/)
* [▶️ Video: Azure App Service Migration Assistant Demo](https://www.youtube.com/watch?v=9LBUmkUhmXU)
