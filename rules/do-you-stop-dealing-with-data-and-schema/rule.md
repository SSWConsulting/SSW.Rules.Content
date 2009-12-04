---
type: rule
archivedreason: 
title: Do you stop dealing with Data and Schema?
guid: d8a098fd-b81e-4f70-92ae-c03af30915f5
uri: do-you-stop-dealing-with-data-and-schema
created: 2009-03-10T06:36:56.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects: []

---


This field should not be null (Remove me when you edit this field).
<br><excerpt class='endintro'></excerpt><br>

  <p>Take a version control approach. It doesn't have to be too complicated, but you should keep a history of structure changes in a table. Some developers <a href="http&#58;//www.ssw.com.au/ssw/Standards/Rules/RulesToBetterSQLServerDatabases.aspx#General">use a text file (.sql)</a> or hardcode it in code, that's fine, just don't make changes in the interface (i.e.. Access or Enterprise Manager). Changes should be made programmatically, or in a method that they can be played back.</p>
<p>An assumption to this is you have a front-end and backend table that is used to record the version number. </p>
<img border="0" src="/Standards/Management/RulesToSuccessfulProjects/PublishingImages/imgTableWithCrossThroughIt.gif" alt="Table with cross through it" style="border&#58;0px solid;width&#58;330px;height&#58;282px;" class="ms-rteCustom-ImageArea" /> <span class="ms-rteCustom-FigureBad">Figure&#58; Never make a change manually in Enterprise Manager or Access </span><img border="0" src="/Standards/Management/RulesToSuccessfulProjects/PublishingImages/SaveChangeScript.gif" alt=" " style="border&#58;0px solid;" class="ms-rteCustom-ImageArea" /> <span class="ms-rteCustom-FigureGood">Figure&#58; Always save your changes in script</span> <img border="0" src="/Standards/Management/RulesToSuccessfulProjects/PublishingImages/ChangeScripts.gif" alt=" " style="border&#58;0px solid;" class="ms-rteCustom-ImageArea" /> <span class="ms-rteCustom-FigureGood">Figure&#58; Name them in the order they're executed </span><img border="0" src="/Standards/Management/RulesToSuccessfulProjects/PublishingImages/SampleTable.gif" alt=" " style="border&#58;0px solid;" class="ms-rteCustom-ImageArea" /> <span class="ms-rteCustom-FigureGood">Figure&#58; An example of a backend table recording the version numbers </span>
<p><strong>Tip&#58;</strong> If you’re using Next Gen and you’re changing just one table, then just regenerate for that table</p>
<table cellspacing="2" cellpadding="2" summary="SQL Deploy" class="clsSSWProductTable">
    <tbody>
        <tr>
            <td>We have a program called <a href="http&#58;//www.ssw.com.au/ssw/SQLDeploy/Default.aspx">SSW SQL Deploy</a> to solve this problem and automatically make schema changes.</td>
        </tr>
    </tbody>
</table>



