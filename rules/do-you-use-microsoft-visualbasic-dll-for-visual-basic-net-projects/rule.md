---
type: rule
archivedreason: 
title: Do you use Microsoft.VisualBasic.dll for Visual Basic.NET projects?
guid: b4257bbf-0e0b-471c-b0ba-6497fe1f25af
uri: do-you-use-microsoft-visualbasic-dll-for-visual-basic-net-projects
created: 2009-04-28T02:53:36.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: Ryan Tee
  url: https://ssw.com.au/people/ryan-tee
related: []
redirects: []

---


The Microsoft.VisualBasic library is provided to ease the implementation of the VB.NET language itself. For VB.NET, it provides some methods familiar to the VB developers and can be seen as a helper library. It is a core part of the .NET redistribution and maps common VB syntax to framework equivalents, without it some of the code may seem foreign to VB programmers. 

<br><excerpt class='endintro'></excerpt><br>

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



