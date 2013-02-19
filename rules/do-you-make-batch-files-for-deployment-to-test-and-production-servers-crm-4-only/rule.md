---
type: rule
title: Do you make batch files for deployment to Test and Production servers? (CRM 4 Only)
uri: do-you-make-batch-files-for-deployment-to-test-and-production-servers-crm-4-only
created: 2012-12-10T19:51:27.0000000Z
authors:
- id: 1
  title: Adam Cogan

---



<span class='intro'> <p>The goal is that I don't want CRM developers to move from Dev to Test and to Production manually. Basically I don't want a developer to touch Test or Production servers. The testers can run the .bat file. <a href="http&#58;//www.ssw.com.au/ssw/Standards/Rules/RulesToBetterSetups.aspx">See SSW rules to setup packages</a>.</p> </span>

<p>How developers should work? </p>
<ul><li>All development done in a Virtual Server</li>
<li>Use TFS and VS.NET 2003 (since working with VS.NET 2003 you need to TFS adapter for 2003)</li>
<li>Backup your customizations.xml</li>
<li>Put into TFS (see rule&#58; <a href="/Pages/Put-your-exported-customizations-and-your-plug-in-customization-under-source-control-during-deployment.aspx">Do you put your exported customizations and your plug-in customization under source-control during deployment?</a>) - check it in and replace the file (avoid it customizing workflow in 3.0 because it deploys better in 4.0 - but if you do then you need to backup your workflow changes also)</li></ul>
<p>Create a Deployment.bat like this</p>
<div class="greyBox"><pre style="overflow&#58;auto;width&#58;600px;">         
            REM (deploy the callouts - Part 1)

            REM (restart IIS of CRM TEST Server - BASILISK)
            iisreset BASILISK

            REM (copy callouts dlls onto CRM TEST Server - BASILISK)
            copy Microsoft.Crm.Platform.Callout.Base.dll &quot;\\BASILISK\C$\Program Files\Microsoft CRM\Server\bin\assembly&quot;            
            copy SSW.TimeProIntegrationCallouts.dll &quot;\\BASILISK\C$\Program Files\Microsoft CRM\Server\bin\assembly&quot;            
            copy callout.config.xml &quot;\\BASILISK\C$\Program Files\Microsoft CRM\Server\bin\assembly&quot; 
            
            REM (deploy the callouts - part 2)
            REM Stop the WorkFlow Service (as we need to remove the lock on the .dlls)
            REM Start it 
            REM (avoid workflow in v3 - see comment above C but if you do you need to)
            REM Manual - use Import wizard
            REM (avoid server side validation logic in v3)
            REM  Deploy a 1.1 web service
         </pre></div>
<p>Deploy to Test Server </p>
<ul><li>Import the customizations.xml</li>
<li>Run .bat file</li></ul>
<p>&#160;</p>
<p>Deploy to Production Server </p>
<ul><li>Import the customizations.xml</li>
<li>Run .bat file</li></ul>


