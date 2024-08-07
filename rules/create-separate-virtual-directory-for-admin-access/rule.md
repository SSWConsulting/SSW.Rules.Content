---
type: rule
archivedreason:
title: Admin - Do you create a separate virtual directory for Admin access?
guid: eddcd8d4-7378-4d14-95a6-6055daeb9dd9
uri: create-separate-virtual-directory-for-admin-access
created: 2024-08-02T11:41:33.0000000Z
authors: 
  - title: Jeoffrey Fischer
    url: https://ssw.com.au/people/jeoffrey-fischer
related:
- when-to-use-reporting-services
redirects: []

---

To securely manage and provide public access to Reporting Services, configure separate ports for authenticated internal access and anonymous public access, following specific setup steps for both Windows Explorer and IIS Manager.

<!--endintro-->

When going public with Reporting Services, you should have 2 ports:

1. **A public access port.** This allows your public users to access their reports normally on a port which has been configured for anonymous users.

2. **An admin access port on your web site.** This allows authenticated internal users to administer the report server via the Report Manager.

To set this up you need to perform the following:

**In Windows Explorer:**

1. Create a Windows User account for the anonymous reporting services site to run as. e.g. IUSR_ReportViewer

2. Open up the ReportingServices directory (C:\Program Files\Microsoft SQL Server\MSSQL.3\Reporting Services)

3. Duplicate the ReportServer and the ReportManager folders then rename postfix them with _External e.g. ReportServer_External and ReportManager_External

4. Set the file access security on the new folders so that "Everyone" has full permissions.

5. Edit the ReportServer_External/rsreportserver.config file. Update the URL node <UrlRoot><http://xxxx:81/ReportServer></URlRoot>

6. the ReportManager_External/RSWebApplication.config file. Update the URL node <ReportServerUrl>http://xxxx:81/ReportServer</ReportServerUrl>

**In IIS Manager:**

1. Create another website on another port (i.e. port 81)

2. Create Virtual Direcoties for ReportServer and Reports then point them to the new folders we just made. Make sure they are setup as applications.

3. Change the Authentication of these 2 virtual directorys to use the user we have already created "USR_ReportViewer". Ensure that all other Authenticated access is unchecked.

4. In the Reports Virtual Direcotry, make sure that it is running the same version of ASP.NET. Set the Applicaiton to execute Scripts and Executables. Add Home.aspx into the Default Documents.

5. In the ReportServer Virtual Directory, make sure that it is running the same version of ASP.NET. Remove all the Application Mappings in the Application Confguration. Then add a wildcard mapping to the Executable C:\WINDOWS\Microsoft.NET\Framework\v2.0.50727\aspnet_isapi.dll

**In SQL Management Studio:**

Add the user for these folders to have access in SQL

**In Reporting Services:**

1. Go to <http://localhost/reports>

2. Click Properties -> New Role Assignment

3. Enter in IUSR_ReportViewer and click Browser then click OK

**Note #1:** The default website will be used for internal Admin (secure) use, and a website on a different port (in this example we use port 81) will be used for external anonymous access.

**Note #2:** Do these steps again every time you install a Reporting Services service pack

Once complete, you should now have authenticated access available on the standard port (80) and public access available on the new port (81).

We think that we should have the ability to choose how IIS authenticates clients - read our [Reporting Services suggestion](https://www.ssw.com.au/ssw/Standards/BetterSoftwareSuggestions/ReportingServices.aspx#authenticate).

![Figure: Create a separate virtual directory for admin access](RSVirtualDirectory.gif)

The process is a little simpler in SQL 2000:

**In Windows Explorer:**

1. Open up the ReportingServices directory (typically c:\Program Files\Microsoft SQL Server\MSSQL\Reporting Services\)

2. Make a copy of the ReportManager folder and call it ReportManagerPublicAccess

3. Duplicate the file access security settings on ReportManager in ReportManagerPublicAccess

4. Edit the RSWebApplication.config in the ReportManagerPublicAccessfolder to point to <http://server:81/ReportServer>

**In IIS Manager:**

1. Configure the default website's ReportsServer virtual directory to give access to IUSR_ServerName (for public access)

2. Export the Report and ReportServer virtual directory to an XML file

3. Create another website on another port (i.e. port 81)

4. Add the Report and ReportServer virtual directories using the XML files created in step 2

5. Set the Reports virtual directory to point to the ReportsManagerSecure directory instead of just ReportsManager

6. Set the directory security on the ReportServer on port 81 to use windows integrated security
