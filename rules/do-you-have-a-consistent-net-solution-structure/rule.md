---
type: rule
title: Do you have a consistent .NET Solution Structure?
uri: do-you-have-a-consistent-net-solution-structure
created: 2009-04-24T03:31:54.0000000Z
authors:
- id: 1
  title: Adam Cogan
- id: 24
  title: Adam Stephensen

---



<span class='intro'> When developing a n-tiered software solution, we follow a standard solution structure. We have incorporated unit testing components, which is an integral part of the Extreme Programming development methodology, into our solution structure&#58; 
 </span>


  <table class="clsSSWTable">
    <tbody>
        <tr>
            <th height="36">Project Type </th>
            <th height="36" width="80">Project Name </th>
            <th height="36" width="250"></th>
            <th height="36">Note </th>
        </tr>
        <tr valign="top">
            <td>Application </td>
            <td width="80">Northwind </td>
            <td width="250">
            <table style="border-collapse&#58;collapse;" id="table25" border="0" cellspacing="0" cellpadding="0" width="100%">
                <tbody>
                    <tr>
                        <td height="18" width="100"><b>Namespace&#58;</b> </td>
                        <td height="18" width="250">SSW.Northwind </td>
                    </tr>
                    <tr>
                        <td><b>Folder&#58;</b> </td>
                        <td width="250">SSW\Northwind\Northwind\ </td>
                    </tr>
                    <tr>
                        <td><b>Output&#58;</b> </td>
                        <td width="250">Northwind.exe </td>
                    </tr>
                </tbody>
            </table>
            </td>
            <td></td>
        </tr>
        <tr valign="top">
            <td>Class Library </td>
            <td width="80">WindowsUI </td>
            <td width="250">
            <table style="border-collapse&#58;collapse;" id="table9" border="0" cellspacing="0" cellpadding="0" width="100%">
                <tbody>
                    <tr>
                        <td width="100"><b>Namespace&#58;</b> </td>
                        <td>SSW.Northwind.WindowsUI </td>
                    </tr>
                    <tr>
                        <td><b>Folder&#58;</b> </td>
                        <td>SSW\Northwind\WindowsUI\ </td>
                    </tr>
                    <tr>
                        <td><b>Folder&#58;</b> </td>
                        <td>SSW\Northwind\WindowsUI.Tests </td>
                    </tr>
                    <tr>
                        <td><b>Output&#58;</b> </td>
                        <td>WindowsUI.dll </td>
                    </tr>
                </tbody>
            </table>
            </td>
            <td>We put all the forms in a separate project so we can run Unit Tests on the UI using reflection.Note if you have two projects you will give them different names (e.g. ProductSilverlightUI and AdminWebUI) </td>
        </tr>
        <tr valign="top">
            <td>Application </td>
            <td width="80">ConsoleUI </td>
            <td width="250">
            <table style="border-collapse&#58;collapse;" id="table22" border="0" cellspacing="0" cellpadding="0" width="100%">
                <tbody>
                    <tr>
                        <td width="100"><b>Namespace&#58;</b> </td>
                        <td>SSW.Northwind.ConsoleUI </td>
                    </tr>
                    <tr>
                        <td><b>Folder&#58;</b> </td>
                        <td>SSW\Northwind\ConsoleUI\ </td>
                    </tr>
                    <tr>
                        <td><b>Folder&#58;</b> </td>
                        <td>SSW\Northwind\ConsoleUI.Tests </td>
                    </tr>
                    <tr>
                        <td><b>Output&#58;</b> </td>
                        <td>NorthwindConsole.exe </td>
                    </tr>
                </tbody>
            </table>
            </td>
            <td></td>
        </tr>
        <tr valign="top">
            <td>Application </td>
            <td width="80">SilverlightUI </td>
            <td width="250">
            <table style="border-collapse&#58;collapse;" id="table22" border="0" cellspacing="0" cellpadding="0" width="100%">
                <tbody>
                    <tr>
                        <td width="100"><b>Namespace&#58;</b> </td>
                        <td>SSW.Northwind.SilverlightUI </td>
                    </tr>
                    <tr>
                        <td><b>Folder&#58;</b> </td>
                        <td>SSW\Northwind\SilverlightUI\ </td>
                    </tr>
                    <tr>
                        <td><b>Folder&#58;</b> </td>
                        <td>SSW\Northwind\SilverlightUI.Tests </td>
                    </tr>
                    <tr>
                        <td><b>Output&#58;</b> </td>
                        <td>SSW.Northwind.SilverlightUI.dll </td>
                    </tr>
                </tbody>
            </table>
            </td>
            <td></td>
        </tr>
        <tr valign="top">
            <td height="90">Application </td>
            <td height="90" width="80">WebUI </td>
            <td height="90" width="250">
            <table style="border-collapse&#58;collapse;" id="table9" border="0" cellspacing="0" cellpadding="0" width="100%">
                <tbody>
                    <tr>
                        <td width="100"><b>Namespace&#58;</b> </td>
                        <td>SSW.Northwind.WebUI </td>
                    </tr>
                    <tr>
                        <td><b>Folder&#58;</b> </td>
                        <td>SSW\Northwind\WebUI\ </td>
                    </tr>
                    <tr>
                        <td><b>Folder&#58;</b> </td>
                        <td>SSW\Northwind\WebUI\UnitTests </td>
                    </tr>
                    <tr>
                        <td><b>Output&#58;</b> </td>
                        <td>SSW.Northwind.WebUI.dll </td>
                    </tr>
                </tbody>
            </table>
            </td>
            <td height="90"></td>
        </tr>
        <tr valign="top">
            <td></td>
            <td width="80"></td>
            <td width="250">
            <table style="border-collapse&#58;collapse;" id="table10" border="0" cellspacing="0" cellpadding="0" width="100%">
                <tbody>
                    <tr>
                        <td width="100"><b>Namespace&#58;</b> </td>
                        <td>SSW.Northwind.WebUI.Reports </td>
                    </tr>
                    <tr>
                        <td><b>Folder&#58;</b> </td>
                        <td>SSW\Northwind\WebUI\Reports\ </td>
                    </tr>
                </tbody>
            </table>
            </td>
            <td>
            <p>Manually-based reports - e.g. using the DataGrid .</p>
            <p><span style="font-family&#58;'times new roman','serif';font-size&#58;12pt;">Part of WebUI. For .css and .ascx user controls </span></p>
            </td>
        </tr>
        <tr>
            <td>Windows Service </td>
            <td width="80">WindowsService </td>
            <td width="250">
            <table style="border-collapse&#58;collapse;" id="table20" border="0" cellspacing="0" cellpadding="0" width="100%">
                <tbody>
                    <tr>
                        <td width="100"><b>Folder&#58;</b> </td>
                        <td>SSW\Northwind\WindowsService\Components </td>
                    </tr>
                    <tr>
                        <td width="100"><b>Folder&#58;</b> </td>
                        <td>SSW\Northwind\WindowsService.Tests </td>
                    </tr>
                    <tr>
                        <td width="100"><b>Output&#58;</b> </td>
                        <td>SSW.Northwind.WindowsService.dll </td>
                    </tr>
                </tbody>
            </table>
            </td>
            <td></td>
        </tr>
        <tr valign="top">
            <td>RS Reports </td>
            <td width="80">Reports </td>
            <td width="250">
            <table style="border-collapse&#58;collapse;" id="table21" border="0" cellspacing="0" cellpadding="0" width="100%">
                <tbody>
                    <tr>
                        <td width="100"><b>Namespace&#58;</b> </td>
                        <td>N/A </td>
                    </tr>
                    <tr>
                        <td><b>Folder&#58;</b> </td>
                        <td>SSW\Northwind\Reports </td>
                    </tr>
                    <tr>
                        <td><b>Output&#58;</b> </td>
                        <td>N/A </td>
                    </tr>
                </tbody>
            </table>
            </td>
            <td>
            <p>Reporting Services </p>
            <p>Note&#58; We don't use Reports2005 or Reports2008 indicating the version number of reporting services because renaming in version control is a process intensive operation</p>
            </td>
        </tr>
        <tr valign="top">
            <td>Class Library </td>
            <td width="80">IServices </td>
            <td width="250">
            <table style="border-collapse&#58;collapse;" id="table1" border="0" cellspacing="0" cellpadding="0" width="100%">
                <tbody>
                    <tr>
                        <td><b>Namespace&#58;</b> </td>
                        <td>SSW.Northwind.IServices </td>
                    </tr>
                    <tr>
                        <td><b>Folder&#58;</b> </td>
                        <td>SSW\Northwind\IServices </td>
                    </tr>
                    <tr>
                        <td><b>Folder&#58;</b> </td>
                        <td>SSW\Northwind\IServices.Tests </td>
                    </tr>
                    <tr>
                        <td><b>Output&#58;</b> </td>
                        <td>SSW.Northwind.IServices.dll </td>
                    </tr>
                </tbody>
            </table>
            </td>
            <td>
            <p>WCF Services Interfaces </p>
            <p>Note&#58; only use if you are not hosting WCF in IIS</p>
            </td>
        </tr>
        <tr valign="top">
            <td>Class Library </td>
            <td width="80">Services </td>
            <td width="250">
            <table style="border-collapse&#58;collapse;" id="table2" border="0" cellspacing="0" cellpadding="0" width="100%">
                <tbody>
                    <tr>
                        <td><b>Namespace&#58;</b> </td>
                        <td>SSW.Northwind.Services </td>
                    </tr>
                    <tr>
                        <td><b>Folder&#58;</b> </td>
                        <td>SSW\Northwind\Services </td>
                    </tr>
                    <tr>
                        <td><b>Folder&#58;</b> </td>
                        <td>SSW\Northwind\Services.Tests </td>
                    </tr>
                    <tr>
                        <td><b>Output&#58;</b> </td>
                        <td>SSW.Northwind.Services.dll </td>
                    </tr>
                </tbody>
            </table>
            </td>
            <td>
            <p>WCF Services Implementations </p>
            <p>Note&#58; If you use WCF IIS Activation then you can put these under WebUI/Services to make deployment easier</p>
            </td>
        </tr>
        <tr>
            <td><s>Class Library </s></td>
            <td width="80"><s>Business </s></td>
            <td width="250">
            <table style="border-collapse&#58;collapse;" id="table20" border="0" cellspacing="0" cellpadding="0" width="100%">
                <tbody>
                    <tr>
                        <td width="100"><b><s>Namespace&#58;</s></b> </td>
                        <td><s>SSW.Northwind.Business </s></td>
                    </tr>
                    <tr>
                        <td><b><s>Folder&#58;</s></b> </td>
                        <td><s>SSW\Northwind\Business\ </s></td>
                    </tr>
                    <tr>
                        <td><b><s>Folder&#58;</s></b> </td>
                        <td><s>SSW\Northwind\Business\Components </s></td>
                    </tr>
                    <tr>
                        <td><b><s>Folder&#58;</s></b> </td>
                        <td><s>SSW\Northwind\Business\UnitTests </s></td>
                    </tr>
                    <tr>
                        <td><b><s>Output&#58;</s></b> </td>
                        <td><s>SSW.Northwind.Business.dll </s></td>
                    </tr>
                </tbody>
            </table>
            </td>
            <td>
            <p><s>This can be code-generated </s></p>
            <p>(REPLACED BY SERVICES)<s></s></p>
            </td>
        </tr>
        <tr valign="top">
            <td>Class Library </td>
            <td width="80">Domain </td>
            <td width="250">
            <table style="border-collapse&#58;collapse;" id="table3" border="0" cellspacing="0" cellpadding="0" width="100%">
                <tbody>
                    <tr>
                        <td><b>Namespace&#58;</b> </td>
                        <td>SSW.Northwind.Domain </td>
                    </tr>
                    <tr>
                        <td><b>Folder&#58;</b> </td>
                        <td>SSW\Northwind\Domain </td>
                    </tr>
                    <tr>
                        <td><b>Folder&#58;</b> </td>
                        <td>SSW\Northwind\Domain.Tests </td>
                    </tr>
                    <tr>
                        <td><b>Output&#58;</b> </td>
                        <td>SSW.Northwind.Domain.dll </td>
                    </tr>
                </tbody>
            </table>
            </td>
            <td>
            <p>LINQ .EDMX AND .DBML sit here - this can be generated using SQL Metal (Replaces DataAccess and DataSets)</p>
            <p>Note&#58; LINQ to Entities is preferred over LINQ to SQL</p>
            </td>
        </tr>
        <tr valign="top">
            <td><s>Class Library </s></td>
            <td width="80"><s>DataSets </s></td>
            <td width="250">
            <table style="border-collapse&#58;collapse;" id="table19" border="0" cellspacing="0" cellpadding="0" width="100%">
                <tbody>
                    <tr>
                        <td width="100"><b><s>Namespace&#58;</s></b> </td>
                        <td><s>SSW.Northwind.DataSets </s></td>
                    </tr>
                    <tr>
                        <td><b><s>Folder&#58;</s></b> </td>
                        <td><s>SSW\Northwind\DataSets\ </s></td>
                    </tr>
                    <tr>
                        <td><b><s>Folder&#58; </s></b></td>
                        <td><s>SSW\Northwind\DataSets\UnitTests </s></td>
                    </tr>
                    <tr>
                        <td><b><s>Output&#58;&gt;</s></b> </td>
                        <td><s>SSW.Northwind.DataSets.dll </s></td>
                    </tr>
                </tbody>
            </table>
            </td>
            <td>
            <p><s>Strongly typed datasets - this can be code-generated </s></p>
            <p>(REPLACED BY DOMAIN)</p>
            </td>
        </tr>
        <tr valign="top">
            <td><s>Class Library </s></td>
            <td width="80"><s>DataAccess </s></td>
            <td width="250">
            <table style="border-collapse&#58;collapse;" id="table13" border="0" cellspacing="0" cellpadding="0" width="100%">
                <tbody>
                    <tr>
                        <td width="100"><b><s>Namespace&#58;</s></b> </td>
                        <td><s>SSW.Northwind.DataAccess </s></td>
                    </tr>
                    <tr>
                        <td><b><s>Folder&#58;</s></b> </td>
                        <td><s>SSW\Northwind\DataAccess\ </s></td>
                    </tr>
                    <tr>
                        <td><b><s>Folder&#58;</s></b> </td>
                        <td><s>SSW\Northwind\DataAccess\Components </s></td>
                    </tr>
                    <tr>
                        <td><s><b>Folder&#58;</b></s> </td>
                        <td><s>SSW\Northwind\DataAccess\UnitTests </s></td>
                    </tr>
                    <tr>
                        <td><b><s>Output&#58;</s></b> </td>
                        <td><s>SSW.Northwind.DataAccess.dll </s></td>
                    </tr>
                </tbody>
            </table>
            </td>
            <td>
            <p><s>This project should contain all the code and SQL statements used to access data from your backend. This project can be code-generated </s></p>
            <p>(REPLACE BY DOMAIN)<s></s></p>
            </td>
        </tr>
        <tr valign="top">
            <td>Class Library </td>
            <td width="80">Tests </td>
            <td width="250">
            <table style="border-collapse&#58;collapse;" id="table14" border="0" cellspacing="0" cellpadding="0" width="100%">
                <tbody>
                    <tr>
                        <td width="100"><b>Namespace&#58;</b> </td>
                        <td>SSW.Northwind.Domain.Tests </td>
                    </tr>
                    <tr>
                        <td><b>Folder&#58;</b> </td>
                        <td>SSW\Northwind.Domain.Tests\ </td>
                    </tr>
                    <tr>
                        <td><b>Output&#58;</b> </td>
                        <td>SSW.Northwind.Domain.Tests.dll </td>
                    </tr>
                </tbody>
            </table>
            </td>
            <td>
            <p>Only need this project if you are not using reusable components and then you do not need Tests folders above </p>
            <p>For more information on <a href="http&#58;//www.ssw.com.au/SSW/Standards/rules/RulesToBetterUnitTests.aspx#OutsideProject" id="naming unit tests">naming unit tests</a></p>
            </td>
        </tr>
        <tr valign="top">
            <td>Wise Setup </td>
            <td width="80">Northwind </td>
            <td width="250">
            <table style="border-collapse&#58;collapse;" id="table15" border="0" cellspacing="0" cellpadding="0" width="100%">
                <tbody>
                    <tr>
                        <td width="100"><b>Folder&#58;</b> </td>
                        <td>SSW\Northwind\Setup\ </td>
                    </tr>
                    <tr>
                        <td><b>Output&#58;</b> </td>
                        <td>SSWNorthwind_v1-11.exe </td>
                    </tr>
                </tbody>
            </table>
            </td>
            <td>
            <p>For Windows&#58; Make an EXE in Wise instead of an MSI because it allows the application to be upgraded </p>
            <p>For Web&#58; Can be manual via an _Instructions.doc or a Setup.bat file</p>
            </td>
        </tr>
    </tbody>
</table>
<p>We have separated the unit tests, one for each project, for several reasons&#58;</p>
<ul>
    <li><span style="background&#58;yellow;">It provides a clear separation of concerns and allows each component to be individually tested</span> </li>
    <li><span style="background&#58;yellow;">The different libraries can be used on other projects with confidence as there are a set of tests around them</span> </li>
</ul>
<p>For common library project, project name should include the company prefix and solution name, this is so other internal solution can include the common library's project. This will help debugging and development processes.</p>
<table class="clsSSWTable">
    <tbody>
        <tr>
            <th width="100">Project Type </th>
            <th width="100">Project Name </th>
            <th width="380"></th>
            <th width="180">Note </th>
        </tr>
        <tr valign="top">
            <td>Class Library </td>
            <td>Northwind.Common Business </td>
            <td>
            <table style="border-collapse&#58;collapse;" id="table18" border="0" cellspacing="0" cellpadding="0" width="100%">
                <tbody>
                    <tr>
                        <td width="100"><b>Namespace&#58;</b> </td>
                        <td>Northwind.Common.Business </td>
                    </tr>
                    <tr>
                        <td><b>Folder&#58;</b> </td>
                        <td>..\Northwind\Common\Business\ </td>
                    </tr>
                    <tr>
                        <td><b>Output&#58;</b> </td>
                        <td>Northwind.Common.Business.dll </td>
                    </tr>
                </tbody>
            </table>
            </td>
            <td>No space in the Project Name </td>
        </tr>
    </tbody>
</table>
<p>For project documents, we should also add them into solution for later reference, and different document types will be put in different folder, e.g. Mockup files will be in Northwind\Documents\Mockup\</p>
<table class="clsSSWTable">
    <tbody>
        <tr>
            <th width="100">Project Type </th>
            <th width="100">Project Name </th>
            <th width="380"></th>
            <th width="180">Note </th>
        </tr>
        <tr valign="top">
            <td>Documents </td>
            <td>Documents </td>
            <td>
            <table style="border-collapse&#58;collapse;" id="table18" border="0" cellspacing="0" cellpadding="0" width="100%">
                <tbody>
                    <tr>
                        <td width="100"><b>Folder&#58;</b> </td>
                        <td>Northwind\Documents\ </td>
                    </tr>
                </tbody>
            </table>
            </td>
            <td>This is outside the solution trunk </td>
        </tr>
    </tbody>
</table>



