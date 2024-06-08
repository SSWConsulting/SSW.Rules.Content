---
type: rule
title: Do you ensure your application pool is always running?
uri: do-you-ensure-your-application-pool-is-always-running
authors:
  - title: Stanley Sidik
    url: https://ssw.com.au/people/stanley-sidik
related: []
redirects: []
created: 2014-08-29T18:48:34.000Z
archivedreason: null
guid: 31683f0c-1802-4481-b418-be14f9f1998e
---

Do users complain that at times their web application appears to be slow to run at times. The issue can be related to after IIS application pool recycles/reboots/crashes and the application pools are not automatically loaded back into into memory e.g. The first user in the morning complains about excessive load times for their web application.

<!--endintro-->

As per [What's New in IIS 8?](https://docs.microsoft.com/en-us/iis/get-started/whats-new-in-iis-8/) you can use the Application Initialization feature to alleviate this behaviour. If this setting is not enabled, then IIS has default settings to spin down the application and release it from memory when it has been idle for 20 minutes.

When you set the startMode property of your application pool to AlwaysRunning a worker process is spawned as soon as IIS starts up and does not wait for the first user request. But this does not mean the web application is initialized.

When you set preloadEnabled to true, IIS will simulate a user request to the default page (can be changed with initializationPage metabase setting) of the website/virdir so that the application initializes. The request is not logged in the IIS logs.

### IIS 8 configuration:

The feature is built-in to IIS 8

1. Open Internet Information Services (IIS)
2. Browse to the website in question
3. Open Advanced settings 
      
    ![Figure: IIS](iis8-1.jpg)  

4. Change the “start mode” to “Always running” 
      
    ![Figure: Start mode](iis8-2.jpg)  

5. Change Preload Enabled to True 
      
    ![Figure: Preload setting](iis8-3.jpg)  


### Instructions below for IIS 7.5:

1. On the application server install http://www.iis.net/downloads/microsoft/application-initialization or it can be installed using the Web Platform installer
2. Open **Internet Information Services (IIS)**
3. Select the server
4. Scroll down and select **Configuration Editor** 
  ![Figure: IIS](iis7-1.jpg)  

5. From the **Section** menu select **system.applicationHost / applicationPools** 
  ![Figure: Configuration editor](iis7-2.jpg)  

6. Double click the  **“…”** to the right of **(Collection)**
7. Find the Application Pool CFT is running on (it could be ComplyFirstTime or DefaultAppPool)
8. In the  **Properties** window, scroll down and select **startMode** , choose **AlwaysRunning** 
  ![Figure: Set "start Mode"](iis7-3.jpg)  

9. On the top right select **Apply**

---

### Alternative Instructions for IIS 7.5:

1. There is a setting that has to be enabled in the applicationhost.config file which contains all of the top level configuration settings that IIS uses. This file is called appplocated at c:\windows\system32\inetsvr\config on a standard install of IIS. We recommend making a backup of this file before continuing. You can use any text editor to update this file. Search for and locate the section named &lt;applicationPools&gt;. Within this section, you will see your application listed in this format:

    ```xml
    <add name="”Application" pool="" name”="" managedruntimeversion="”v4.0″"></add>
    ```
2. Add the Always Running mode by adding startMode="AlwaysRunning"
    ```xml
    <add name="”Application" pool="" name”="" managedruntimeversion="”v4.0″" startmode="AlwaysRunning"></add>
    ```
3. Save this file and perform an IISReset so that the change is read into the running memory of the IIS server.
