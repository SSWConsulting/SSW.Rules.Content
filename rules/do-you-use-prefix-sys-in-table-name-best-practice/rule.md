---
type: rule
archivedreason: 
title: Do you use prefix sys in table name (Best Practice)?
guid: fcef3df9-1c7a-4e2c-b8ac-58c23b3b9c22
uri: do-you-use-prefix-sys-in-table-name-best-practice
created: 2010-07-23T02:47:37.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related:
- schema-do-you-always-have-version-tracking-tables
redirects:
- do-you-use-prefix-sys-in-table-name-(best-practice)

---



  <p>Don't use sys as a prefix for Access tables. Some developers use this for system tables etc. SQL Server uses tables with this prefix and it becomes confusing. We recommend system tables start with <b><b style="background-color&#58;#ffff66;color&#58;black;">zs</b></b> eg. zsUsers</p>
<p><a href="http&#58;//www.ssw.com.au/ssw/Standards/Rules/RulesToBetterSQLServerDatabases.aspx#ZSPrefix"></a></p>

<br><excerpt class='endintro'></excerpt><br>

  <table class="clsSSWProductTable" cellspacing="2" summary="Upsizing PRO" cellpadding="2">
    <tbody>
        <tr>
            <td><a href="http&#58;//www.ssw.com.au/ssw/UpsizingPRO">Upsizing PRO</a> will check this rule </td>
        </tr>
    </tbody>
</table>
See our <a href="http&#58;//www.ssw.com.au/ssw/Standards/Rules/RulesToBetterSQLServerDatabases.aspx#ZSPrefix">Rules to Better SQL Server Databases - Do you add zs prefix to table name?</a>



