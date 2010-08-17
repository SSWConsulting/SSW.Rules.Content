---
type: rule
title: Do you use Microsoft.VisualBasic.dll for Visual Basic.NET projects?
uri: do-you-use-microsoftvisualbasicdll-for-visual-basicnet-projects
created: 2009-04-28T02:53:36.0000000Z
authors:
- id: 1
  title: Adam Cogan
- id: 17
  title: Ryan Tee

---



<span class='intro'> The Microsoft.VisualBasic library is provided to ease the implementation of the VB.NET language itself. For VB.NET, it provides some methods familiar to the VB developers and can be seen as a helper library. It is a core part of the .NET redistribution and maps common VB syntax to framework equivalents, without it some of the code may seem foreign to VB programmers. 
 </span>


  <table style="width&#58;600px;border-collapse&#58;collapse;height&#58;99px;" id="table23" class="clsSSWTable" border="1" cellspacing="0" cellpadding="0" width="600">
    <tbody>
        <tr>
            <th>Microsoft.VisualBasic </th>
            <th>.NET Framework </th>
        </tr>
        <tr>
            <td>CInt, CStr </td>
            <td>Convert.ToInt(...), ToString() </td>
        </tr>
        <tr>
            <td>vbCrLf </td>
            <td>Environment.NewLine, or &quot;\r\n&quot; </td>
        </tr>
        <tr>
            <td>MsgBox </td>
            <td>MessageBox.Show(...) </td>
        </tr>
    </tbody>
</table>



