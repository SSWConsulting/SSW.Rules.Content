---
type: rule
title: Are your customizable and non-customizable settings in different files?
uri: are-your-customizable-and-non-customizable-settings-in-different-files
created: 2009-04-29T06:42:19.0000000Z
authors:
- id: 1
  title: Adam Cogan
- id: 17
  title: Ryan Tee

---



<span class='intro'> There are three types of settings files that we may need to use in .NET &#58; 
 </span>


  <ol>
    <li>App.Config/Web.Config is the default .NET settings file, including any settings for the Microsoft Application Blocks (eg. the Exception Management Block and the Configuration Management Block). These are for settings that dont change from within the application. In addition, System.Configuration classes dont allow writing to this file. </li>
    <li>ToolsOptions.Config (an SSW standard) is the file to hold the users own settings, that are users can change in the Tools - Options. <br>
    Eg. ConnectionString, EmailTo, EmailCC<br>
    Note&#58; We read and write to this using Microsoft Configuration Application Block. If we don't use this Block we would store it as a plain XML file and read and write to it using System.XML classes. The idea is that if something does go wrong when you are writing to this file, at least the App.Config would not be affected. Also, this separates our settings (which are few) from the App.Config (which usually has a lot of stuff that we really dont want a user to stuff around with). </li>
    <li>UserSession.Config (an SSW standard). These are for additional setting files that the user can not change. <br>
    e.g. FormLocation, LastReportSelected<br>
    Note&#58; This file is over writable (say during a re-installation) and it will not affect the user if the file is deleted.&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; </li>
</ol>



