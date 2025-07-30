---
seoDescription: Determine whether ClickOnce or MSI deployment best suits your application's needs by comparing features in this comprehensive table.
type: rule
title: Do you know whether you should use Click Once or MSI?
uri: use-click-once-or-msi
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan/
created: 2014-03-14T02:17:00.000Z
archivedreason: outdated
guid: 97d83855-0de7-4200-a1ca-071efe18fd23
---

1. Check the following table whether ClickOnce is suit for your application.\
   This table compares the features of ClickOnce deployment with Windows Installer deployment. Read [ClickOnce Deployment Overview](https://learn.microsoft.com/en-us/visualstudio/deployment/clickonce-security-and-deployment) for more details

<!--endintro-->

| Feature                                                 | ClickOnce                                                         | Windows Installer                        |
| ------------------------------------------------------- | ----------------------------------------------------------------- | ---------------------------------------- |
| Automatic update<sup>1</sup>                            | Yes                                                               | Yes                                      |
| Post-installation rollback<sup>2</sup>                  | Yes                                                               | No                                       |
| Update from Web                                         | Yes                                                               | No                                       |
| Does not affect shared components or other applications | Yes                                                               | No                                       |
| Security permissions granted                            | Grants only permissions necessary for the application (more safe) | Grants Full Trust by default (less safe) |
| Security permissions required                           | Internet or Intranet Zone (Full Trust for CD-ROM installation)    | Administrator                            |
| Application and deployment manifest signing             | Yes                                                               | No                                       |
| Installation-time user interface                        | Single prompt                                                     | Multipart Wizard                         |
| Installation of assemblies on demand                    | Yes                                                               | No                                       |
| Installation of shared files                            | No                                                                | Yes                                      |
| Installation of drivers                                 | No                                                                | Yes (with custom actions)                |
| Installation to Global Assembly Cache                   | No                                                                | Yes                                      |
| Installation for multiple users                         | No                                                                | Yes                                      |
| Add application to Start menu                           | Yes                                                               | Yes                                      |
| Add application to Startup group                        | No                                                                | Yes                                      |
| Add application to Favorites menu                       | No                                                                | Yes                                      |
| Register file types                                     | No                                                                | Yes                                      |
| Install time registry access<sup>3</sup>                | Limited                                                           | Yes                                      |
| Binary file patching                                    | No                                                                | Yes                                      |
| Application installation location                       | ClickOnce application cache                                       | Program Files folder                     |

Notes

1. With Windows Installer, you must implement programmatic updates in the application code.
2. With ClickOnce, rollback is available in Add or Remove Programs.
3. ClickOnce deployment can access HKEY_LOCAL_MACHINE (HKLM) only with Full Trust permission.

For more information, see [Choosing a Deployment Strategy](https://learn.microsoft.com/en-us/visualstudio/deployment/choosing-a-clickonce-deployment-strategy?view=vs-2022).

2. Customize the Installation of the Application, including: Publish location, installation url, install mode, publish version, Download files on demand, Prerequisites, Updates, Options.

![Figure: Publish tab of the application properties](clickonce_publishtab.gif)

3. Specify the code access security permissions that the application requires in order to run.

![Figure: Security tab of the application properties](clickonce_securitytab.gif)

4. Deploy the COM Components. Read [Deploying COM Components with ClickOnce](https://learn.microsoft.com/en-us/visualstudio/deployment/deploying-com-components-with-clickonce) for more informations.
5. Publish the application using Publish Wizard.

![Figure: ClickOnce Publish Wizard](images/clickonce_publishwizard.gif)
