---
type: rule
archivedreason: 
title: Do you know how you deal with impediments in Scrum?
guid: 9cad1080-3451-47e5-b721-22fd88762c0f
uri: do-you-know-how-you-deal-with-impediments-in-scrum
created: 2011-08-11T17:54:33.0000000Z
authors:
- id: 1
  title: Adam Cogan
- id: 13
  title: Paul Neumeyer
related: []

---



  <p>Exercise – Click Click Scrum</p>
<p>This exercise uses the VS2010 planning poker deck of cards &amp; TFS</p>
​​
<br><excerpt class='endintro'></excerpt><br>

  <h1>Separate out the cards
</h1>
<p>Separate out these as Chance Cards</p>
<img class="ms-rteCustom-ImageArea" alt="Chance Cards" src="/PublishingImages/chance-cards.jpg" /> <span class="ms-rteCustom-FigureNormal">Figure&#58; Chance cards</span>
<p>Separate out these as Point Cards</p>
<img class="ms-rteCustom-ImageArea" alt="Point Cards" src="/PublishingImages/point-cards.jpg" /> <span class="ms-rteCustom-FigureNormal">Figure&#58; Point cards</span>
<h1>Set Timeboxes</h1>
<p><strong>Sprint Planning (What)&#58; </strong> 20 minutes<br>
<strong>Sprint Planning (How)&#58;</strong> 20 minutes<br>
<strong>Each Day&#58; </strong> 10 minutes ( x 9 days = 90 minutes)<br>
<strong>Review&#58; </strong> 20 minutes<br>
<strong>Retro&#58;</strong> 20 minutes</p>
<p><strong>Total for 1 complete Sprint&#58;</strong> 170 minutes (~3 hours)</p>
<h1>Sprint Planning Meeting (What)</h1>
<ol>
    <li>The trainer acts as PO and gives User Stories &amp; prioritises them </li>
    <li>Students clarify the requirements of the User Stories (Details, Acceptance Criteria)</li>
    <li>Students do Planning Poker to Estimate</li>
</ol>
<h1>The Sprint Planning Meeting (How)</h1>
<ol>
    <li>Students break User Stories into tasks</li>
    <li>Students put estimates on each task (typical times for work in a day e.g 4 hours, 8 hours)</li>
</ol>
<h1>Each Day in the sprint</h1>
<ol>
    <li>Get the students “Click-Click” their fingers instead of doing actual coding</li>
    <li>The trainer deals one or two cards from the Chance Cards</li>
    <li>The trainer looks up the meaning of the cards (see table below) and the trainer makes up a suitable story that fits the card and the work the students are doing </li>
    <li>The students add or change work items based on the scenario of the Chance cards</li>
    <li>The team reduces the remaining hours on their assigned tasks, with the assumption that each student works 8 hours</li>
    <li>Do the Daily Scrum (describing their day based on the work they just updated in TFS)</li>
</ol>
<p>NOTE&#58; It is OK to really code rather than use “Click-Click” development as long as TFS is updated.</p>
<h1>The Review Meeting</h1>
<p>The PO reviews the work of the team (Note&#58; if all the work was “Click-Click” then review the TFS work items to check that they are entered OK).</p>
<h1>The Retro</h1>
<p>Students and PO do a standard Scrum retro for the exercise.</p>
<h1>Meaning of the Chance Cards</h1>
<table border="1" class="ms-rteCustom-SSWTable">
    <tbody>
        <tr>
            <td rowspan="2">
            <p align="center"><strong>∞</strong><strong> </strong></p>
            </td>
            <td valign="top">
            <p>Impediment </p>
            </td>
        </tr>
        <tr>
            <td valign="top">
            <p>&#160;</p>
            <ul>
                <li>Draw a point card </li>
                <li>Add the value to the remaining hours of a task</li>
                <li>Record the impediment</li>
            </ul>
            <p>e.g.&#160; DBA will not give access to the database.<br>
            &#160;&#160;&#160;&#160; </p>
            </td>
        </tr>
        <tr>
            <td rowspan="2">
            <p align="center"><strong>?</strong></p>
            </td>
            <td valign="top">
            <p>Clarification </p>
            </td>
        </tr>
        <tr>
            <td valign="top">
            <p>&#160;</p>
            <ul>
                <li>Draw a point card </li>
                <li>Add a new task</li>
                <li>Set the remaining hours of a task to the value</li>
            </ul>
            <p>e.g.&#160; The error message should change from “User Error” to “The process could not be completed, please check the Url value provided for the webservice and try    again”.</p>
            </td>
        </tr>
        <tr>
            <td rowspan="2">
            <p align="center"><strong>0</strong></p>
            </td>
            <td valign="top">
            <p>Bug </p>
            </td>
        </tr>
        <tr>
            <td valign="top">
            <p>&#160;</p>
            <ul>
                <li>Draw a point card </li>
                <li>Create a bug</li>
                <li>Add a task to the bug</li>
                <li>Set the remaining hours on the task to the value</li>
            </ul>
            <p>e.g. One of the build scripts fails on the build server, but works on a local dev machine.</p>
            </td>
        </tr>
        <tr>
            <td rowspan="2">
            <p align="center"><strong>20</strong></p>
            </td>
            <td valign="top">
            <p>Bubble </p>
            </td>
        </tr>
        <tr>
            <td valign="top">
            <p>&#160;</p>
            <ul>
                <li>Halve the remaining hours on a task </li>
            </ul>
            <p>e.g. The data access layer supports the validation framework so as that was already implemented the effort expected has decreased.</p>
            </td>
        </tr>
        <tr>
            <td rowspan="2">
            <p align="center"><strong>40</strong></p>
            </td>
            <td valign="top">
            <p>Spike </p>
            </td>
        </tr>
        <tr>
            <td valign="top">
            <p>&#160;</p>
            <ul>
                <li>Draw a point card </li>
                <li>Create a new User Story</li>
                <li>Set the User Story points to the value</li>
            </ul>
            <p>e.g. The current implementation may not support real-time display of information with the    performance expected by users – investigate</p>
            <p>&#160;</p>
            </td>
        </tr>
        <tr>
            <td rowspan="2">
            <p align="center"><strong>100</strong></p>
            </td>
            <td valign="top">
            <p>Task blowout </p>
            </td>
        </tr>
        <tr>
            <td valign="top">
            <p>&#160;</p>
            <ul>
                <li>Double the remaining hours on a task </li>
            </ul>
            <p>e.g. Multiple field data validation was supported in the application but when it was implemented for this work it failed all validations calls and it took ages to find the    settings in web.config were wrong.</p>
            </td>
        </tr>
        <tr>
            <td rowspan="2">
            <p align="center"><strong>Cancelled Sprint</strong></p>
            </td>
            <td valign="top">
            <p>The PO cancels the sprint </p>
            </td>
        </tr>
        <tr>
            <td valign="top">
            <p>&#160;</p>
            <ul>
                <li>Cancel all tasks</li>
                <li>Recycle the User Stories to the Product Backlog </li>
            </ul>
            </td>
        </tr>
        <tr>
            <td rowspan="2">
            <p align="center"><strong>Team Member <br>
            Leaves</strong><strong> </strong></p>
            </td>
            <td valign="top">
            <p>The Team is missing a Team Member </p>
            </td>
        </tr>
        <tr>
            <td valign="top">
            <p>&#160;</p>
            <ul>
                <li>Reduce the hours the team works by 8 hours </li>
            </ul>
            </td>
        </tr>
        <tr>
            <td rowspan="2">
            <p align="center"><strong>Scrum Master <br>
            Leaves</strong><strong> </strong></p>
            </td>
            <td valign="top">
            <p>The Team is missing the  Scrum Master </p>
            </td>
        </tr>
        <tr>
            <td valign="top">
            <p>&#160;</p>
            <ul>
                <li>The team handles the missing SM</li>
            </ul>
            </td>
        </tr>
        <tr>
            <td rowspan="2">
            <p align="center"><strong>Product Owner <br>
            Leaves</strong><strong> </strong></p>
            </td>
            <td valign="top">
            <p>The Product Owner is missing </p>
            </td>
        </tr>
        <tr>
            <td valign="top">
            <p>&#160;</p>
            <ul>
                <li>The team handles the missing PO</li>
            </ul>
            </td>
        </tr>
        <tr>
            <td rowspan="2">
            <p align="center"><strong>Stakeholder Interferes</strong><strong> </strong></p>
            </td>
            <td valign="top">
            <p>Stakeholders are contacting the Team to change priorities and requirements </p>
            </td>
        </tr>
        <tr>
            <td valign="top">
            <p>&#160;</p>
            <ul>
                <li>The team handles the Stakeholders </li>
            </ul>
            </td>
        </tr>
    </tbody>
</table>



