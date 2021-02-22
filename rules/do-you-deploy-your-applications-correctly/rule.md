---
type: rule
archivedreason: 
title: Do you deploy your applications correctly?
guid: f355fc30-7a9b-4288-8ef9-2dc8d8366c6b
uri: do-you-deploy-your-applications-correctly
created: 2009-05-05T06:05:52.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: Ryan Tee
  url: https://ssw.com.au/people/ryan-tee
related: []
redirects: []

---


​<p>Many applications end up working perfectly on the developer's machine. However once the application is deployed into a setup package and ready for the public, the application could suddenly give the user the most horrible experience of his life. There are plenty of issues that developers don't take into consideration. Amongst the many issues, three can stand above the rest if the application isn't tested thoroughly:​<br></p>
<br><excerpt class='endintro'></excerpt><br>
<ol><li>The SQL Server Database or the Server machine cannot be accessed by the user, and so developer settings are completely useless to the user.</li><li>The user doesn't install the application in the default location. (i.e. instead of C:\Program Files\ApplicationName, the user could install it on D:\Temp\ApplicationName)</li><li>The developer has assumed that certain application dependencies are installed on the user's machine. (i.e. MDAC; IIS; a particular version of MS Access; or SQL Server runtime components like sqldmo.dll)</li></ol><p>To prevent issues from arising and having to re-deploy continuously which would only result in embarrassing yourself and the company, there are certain procedures to follow to make sure you give the user a smooth experience when installing your application.</p><ol><li>Have scripts that can get the pathname of the .exe that the user has installed the application on<br> 
      <br>Wise has a Dialog that prompts the user for the installation directory: <dl class="goodImage"><dt> <img border="0" src="INSTALLDIR.jpg" alt="" /> </dt><dd>Figure: Wise Prompts the user for the installation directory and sets the path to a property in wise called "INSTALLDIR"</dd></dl><p>An embedded script must be used if the pathname is necessary in the application (i.e. like .reg files that set registry keys in registry)</p><dl class="goodCode"><dt><pre>'The .reg file includes the following hardcoded lines:

 '[HKEY_CLASSES_ROOT\SSWNetToolkit\shell\open\command]​
  
               <a href="mailto:%27@=%22\%22C:\\Program">'@="\"C:\\Program</a> Files\\SSW NetToolKit\\WindowsUI\\bin\\SSW.NetToolkit.exe\" /select \"%1\""

 'This should be replaced with the following lines:<br>
 '[HKEY_CLASSES_ROOT\SSWNetToolkit\shell\open\command]

               <a href="mailto:%27@=%22\%22REPLACE_ME\">'@="\"REPLACE_ME\</a>" /select \"%1\""

  Dim oFSO, oFile, sFile<br>
  Set oFSO = createobject("Scripting.FileSystemObject")
           
  sFile = Property("<span style="background-color:#ffff00;">INSTALLDIR</span>") & "WindowsUI\PartA\UrlAcccess.reg"
                                        
  Set oFile = oFSO.OpenTextFile(sFile)

  regStream = oFile.ReadAll()<br>
  oFile.Close

 string appPath = replace(Property("INSTALLDIR") & "WindowsUI\bin\SSW.NetToolkit.exe", "\", "\\")

 regStream = replace(regStream, "REPLACE_ME", appPath)<br>
 Set oFile = oFSO.OpenTextFile(sFile,2)<br>
 oFile.Write regStream

 oFile.Close
</pre></dt><dd>Figure: The "REPLACE_ME" string is replaced with the value of the INSTALLDIR property in the .reg file</dd></dl></li><li>After setting up the wise file then running the build script, the application must be first tested on the developers' own machine.<br>Many developers forget to test the application outside the development environment completely and don't bother to install the application using the installation package they have just created.<br>Doing this will allow them to fix e.g. pathnames of images that might have been set to a relative path of the running process and not the relative path of the actual executable. <dl class="badCode"><dt><pre>  this.pictureReportSample.Image = Image.FromFile(@"Reports\Images\Blank.jpg");<br></pre></dt><dd>Bad code - FromFile() method (as well as Process.Start()) give the relative path of the running process. This could mean the path relative to the shortcut or the path relative to the .exe itself, and so an exception will be thrown if the image cannot be found when running from the shortcut.</dd></dl><dl class="goodCode"><dt><pre>string appFilePath = System.Reflection.Assembly.GetExecutingAssembly().Location;

string appPath = Path.GetDirectoryName(appFilePath);

this.pictureReportSample.Image = Image.FromFile(appPath + @"\Reports\Images\Blank.jpg");<br></pre></dt><dd>Good code - GetExecutingAssembly().Location will get the pathname of the actual executable and no exception will be thrown.</dd></dl><p>This exception would never have been found if the developer didn't bother to test the actual installation package on his own machine.</p></li><li>Having tested on the developer's machine, the application must be tested on a virtual machine in a pure environment without dependencies installed in GAC, registry or anywhere else in the virtual machine.<br> 
      <p>Users may have MS Access 2000 installed and, the developer's application may behave differently on an older version of MS Access even though it works perfectly on MS Access 2003. The most appropriate way of handling this is to use programs like VM Ware or MS Virtual PC.<br>This will help the developer test the application on all possible environments to ensure that it caters for <b>all</b> users, minimizing the amount of assumptions as possible.</p>
      </li></ol>


