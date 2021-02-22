---
type: rule
archivedreason: 
title: Do you use interoperability mechanism for COM object?
guid: c9ef1559-48d1-43fc-b279-2bbc15d21f9d
uri: use-interoperability-mechanism-for-com-object
created: 2018-04-25T22:10:13.0000000Z
authors: []
related: []
redirects:
- do-you-use-interoperability-mechanism-for-com-object

---


VB.NET includes the CreateObject () Method for creating the COM object. This is an old relationship between VB and COM.<br>
<br><excerpt class='endintro'></excerpt><br>
<p class="ssw15-rteElement-CodeArea">Sub CreateADODBConnection()<br>Dim adoApp As Object<br>adoApp = CreateObject("ADODB.Connection")<br>End Sub </p><dd class="ssw15-rteElement-FigureBad">Figure: Bad code. Uses a VB technique - CreateObject() - for creating a COM object</dd><p>Using the CreateObject() method affects the performance of your application. The variable adoApp is of type Object and this results in "late binding" </p><p>which might lead to so much uncertainty. It is more efficient to use the interoperability features of .NET, which allows you to work with existing<br>unmanaged code (code running outside the CLR) in COM components as well as Microsoft Win32 DLLs. The interoperability feature uses run-time<br>callable wrappers for handling all interaction between the .NET client code (managed code) and the COM component (unmanaged code).<br></p><p>To add references to COM objects:<br></p><ul><li>On the Project menu, select Add Reference and then click the COM tab.</li><li>Select the component you want to use from the list of COM objects.<dl class="image"><dt><img src="UserCOM.gif" alt="UserCOM.gif" /><br></dt></dl></li><li>​To access to the interoperability assembly in your application, add an Imports statement to the top of the class or module in which you will<br>use the COM object.<br></li></ul><div>You can also create interoperability assemblies using the Tlbimp command line utility.<br><br></div><div><p class="ssw15-rteElement-YellowBorderBox">We have a program called <a href="https://www.ssw.com.au/ssw/CodeAuditor/Rules.aspx#Interoper">SSW Code Auditor</a> to check for this rule.</p></div>


