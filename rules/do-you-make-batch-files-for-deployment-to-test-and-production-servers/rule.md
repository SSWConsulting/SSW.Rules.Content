---
type: rule
title: Do you make batch files for deployment to Test and Production servers?
  (CRM 4 Only)
uri: do-you-make-batch-files-for-deployment-to-test-and-production-servers
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
  - do-you-make-batch-files-for-deployment-to-test-and-production-servers-crm-4-only
  - do-you-make-batch-files-for-deployment-to-test-and-production-servers-(crm-4-only)
created: 2012-12-10T19:51:27.000Z
archivedreason: null
guid: 571086a1-3626-4cda-b0e6-0de835b2eda2
---
The goal is that CRM developers  **to not ** move from Dev to Test and to Production manually. Basically, we don't want a developer to touch Test or Production servers. The testers can run the .bat file. [See SSW rules to setup packages](http&#58;//www.ssw.com.au/ssw/Standards/Rules/RulesToBetterSetups.aspx).

<!--endintro-->

How should developers work?

* All development done in a Virtual Server
* Use TFS and VS.NET 2003 (since working with VS.NET 2003 you need to TFS adapter for 2003)
* Backup your customizations.xml
* Put into TFS (see rule: [Do you put your exported customizations and your plug-in customization under source-control during deployment?](/do-you-put-your-exported-customizations-and-your-plug-in-customization-under-source-control-during-deployment)) - check it in and replace the file (avoid it customizing workflow in 3.0 because it deploys better in 4.0 - but if you do then you need to backup your workflow changes also)

Create a Deployment.bat like this

```bat
REM (deploy the callouts - Part 1)

REM (restart IIS of CRM TEST Server - BASILISK)
iisreset BASILISK

REM (copy callouts dlls onto CRM TEST Server - BASILISK)
copy Microsoft.Crm.Platform.Callout.Base.dll "\\BASILISK\C$\Program Files\Microsoft CRM\Server\bin\assembly"            
copy SSW.TimeProIntegrationCallouts.dll "\\BASILISK\C$\Program Files\Microsoft CRM\Server\bin\assembly"            
copy callout.config.xml "\\BASILISK\C$\Program Files\Microsoft CRM\Server\bin\assembly" 
            
REM (deploy the callouts - part 2)
REM Stop the WorkFlow Service (as we need to remove the lock on the .dlls)
REM Start it 
REM (avoid workflow in v3 - see comment above C but if you do you need to)
REM Manual - use Import wizard
REM (avoid server side validation logic in v3)
REM  Deploy a 1.1 web service
```

Deploy to Test Server
* Import the customizations.xml
* Run .bat file

Deploy to Production Server
* Import the customizations.xml
* Run .bat file