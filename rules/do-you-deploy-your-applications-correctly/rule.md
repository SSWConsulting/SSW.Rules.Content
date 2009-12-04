---
type: rule
title: Do you deploy your applications correctly?
uri: do-you-deploy-your-applications-correctly
created: 2009-05-05T06:05:52.0000000Z
authors:
- id: 1
  title: Adam Cogan
- id: 17
  title: Ryan Tee

---



<span class='intro'> This field should not be null (Remove me when you edit this field). </span>

<ol>
<li>The SQL Server Database or the Server machine cannot be accessed by the user, and so developer settings are completely useless to the user. 
<li>The user doesn't install the application in the default location. (i.e. instead of C&#58;\Program Files\ApplicationName, the user could install it on D&#58;\Temp\ApplicationName) 
<li>The developer has assumed that certain application dependencies are installed on the user's machine. (i.e. MDAC; IIS; a particular version of MS Access; or SQL Server runtime components like sqldmo.dll) </li></ol>
<p>To prevent issues from arising and having to re-deploy continuously which would only result in embarrassing yourself and the company, there are certain procedures to follow to make sure you give the user a smooth experience when installing your application.</p>
<ol>
<li>Have scripts that can get the pathname of the .exe that the user has installed the application on<br><br>Wise has a Dialog that prompts the user for the installation directory&#58; 
<dl class="goodImage">
<dt><img style="border-bottom&#58;0px solid;border-left&#58;0px solid;border-top&#58;0px solid;border-right&#58;0px solid;" border="0" src="/Standards/SoftwareDevelopment/RulesToBetterDotNETProjects/PublishingImages/INSTALLDIR.jpg" /></dt></dl><b>&#160;&#160;&#160;&#160; Figure&#58; Wise Prompts the user for the installation directory and sets the path to a property in wise called &quot;INSTALLDIR&quot;</b> 
<p>&#160;&#160;&#160;&#160; An embedded script must be used if the pathname is necessary in the application (i.e. like .reg files that set registry keys in registry)</p>
<dl class="goodCode">
<dt style="width&#58;92.6%;height&#58;710px;"><pre>   'The .reg file includes the following hardcoded lines&#58;
<br>
 '[HKEY_CLASSES_ROOT\SSWNetToolkit\shell\open\command]
<br>
  <a href="mailto&#58;'@=&quot;\&quot;C&#58;\\Program">'@=&quot;\&quot;C&#58;\\Program</a> Files\\SSW NetToolKit\\WindowsUI\\bin\\SSW.NetToolkit.exe\&quot; /select \&quot;%1\&quot;&quot;
<br>
 'This should be replaced with the following lines&#58;
<br>
 '[HKEY_CLASSES_ROOT\SSWNetToolkit\shell\open\command]
<br>
 <a href="mailto&#58;'@=&quot;\&quot;REPLACE_ME\">'@=&quot;\&quot;REPLACE_ME\</a>&quot; /select \&quot;%1\&quot;&quot;
<br>
                                        
  Dim oFSO, oFile, sFile
<br>
  Set oFSO = createobject(&quot;Scripting.FileSystemObject&quot;)
<br>
                                        
  sFile = Property(&quot;<span style="background-color&#58;#ffff00;">INSTALLDIR</span>&quot;) &amp; &quot;WindowsUI\PartA\UrlAcccess.reg&quot;<br>
                                        
  Set oFile = oFSO.OpenTextFile(sFile)
<br>
  regStream = oFile.ReadAll()
<br>
  oFile.Close
<br>
 string appPath = replace(Property(&quot;INSTALLDIR&quot;) &amp; &quot;WindowsUI\bin\SSW.NetToolkit.exe&quot;, &quot;\&quot;, &quot;\\&quot;)
<br>
 regStream = replace(regStream, &quot;REPLACE_ME&quot;, appPath)
<br>
 Set oFile = oFSO.OpenTextFile(sFile,2)
<br>
 oFile.Write regStream
<br>
 oFile.Close
<br>
                                            </pre></dt></dl>
<p><b>&#160;&#160;&#160;&#160; Figure&#58; The &quot;REPLACE_ME&quot; string is replaced with the value of the INSTALLDIR property in the .reg file</b></p>
<li>After setting up the wise file then running the build script, the application must be first tested on the developers own machine.<br>Many developers forget to test the application outside the development environment completely, and don't bother to install the application using the installation package they have just created.<br>Doing this will allow them to fix e.g. pathnames of images that might have been set to a relative path of the running process and not the relative path of the actual executable. 
<dl class="badCode">
<dt style="width&#58;92.76%;height&#58;51px;"><pre>  this.pictureReportSample.Image = Image.FromFile(@&quot;Reports\Images\Blank.jpg&quot;);
                                            </pre>
<dd>&#160;&#160;&#160;&#160; Bad code - FromFile() method (as well as Process.Start()) give the relative path of the running process. This could mean the path relative to the shortcut or the path relative to the .exe itself, and so an exception will be thrown if the image cannot be found when running from the shortcut.</dd></dl>
<dl class="goodCode">
<dt style="width&#58;92.77%;height&#58;152px;"><pre>   string appFilePath = System.Reflection.Assembly.GetExecutingAssembly().Location;
<br>
string appPath = Path.GetDirectoryName(appFilePath);
<br>
this.pictureReportSample.Image = Image.FromFile(appPath + @&quot;\Reports\Images\Blank.jpg&quot;);
                                            </pre>
<dd>&#160;&#160;&#160;&#160; Good code - GetExecutingAssembly().Location will get the pathname of the actual excecutable and no exception will be thrown.</dd></dl>
<p>This exception would never have been found if the developer didn't bother to test the actual installation package on his own machine.<br>&#160;</p>
<li>Having tested on the developer's machine, the application must be tested on a virtual machine in a pure environment without dependencies installed in GAC, registry or anywhere else in the virtual machine.<br><br>Users may have MS Access 2000 installed and, the developer's application may behave differently on an older version of MS Access even though it works perfectly on MS Access 2003. The most appropriate way of handling this is to use programs like VM Ware or MS Virtual PC.<br>This will help the developer test the application on all possible environments to ensure that it caters for <b>all</b> users, minimizing the amount of assumptions as possible.</li></ol>


