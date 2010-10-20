---
type: rule
archivedreason: 
title: Do you keep the best possible bug database?
guid: 6159eae3-6e8b-4999-8812-0907c53db7fd
uri: do-you-keep-the-best-possible-bug-database
created: 2009-02-28T09:44:02.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects: []

---


There are 101 bug databases on the market at the moment and of course many companies make up their own in-house system.

<br><excerpt class='endintro'></excerpt><br>

  <img alt="" class="ms-rteCustom-ImageArea" style="border&#58;0px solid;" src="/Management/RulesToSuccessfulProjects/PublishingImages/bugs.jpg" align="right" border="0" />
<p>This is a common scenario&#58; Your tester/client finds a bug, they log on to your on-line bug database, and enter the data, they save the error message as a gif and upload the image. As Project Manager, you get notified by email of the bug, you log on to the application, view the image, review the status, assign a priority, and assign it to a developer. The developer receives the email, logs on and sets about fixing the bug. When completed, he logs back on to the application, enters a completed date, and an email is sent to the tester/client. The tester/client logs on, and is told what to test, reviews the work, enters a checked by date, and the final email is sent to the manager who closes the bug. </p>
<p>Phew! That sounds like a lot of steps which is why most people resort to just sending an email. I believe most people send requests for tasks via email, if this is the case, why should developers have a separate &quot;to-do&quot; list, in the form of a bug-database in which they re-enter data? </p>
<p>Exchange Server and Public Folders (made available on the Internet) are an alternative solution. The benefits are&#58; </p>
<ul>
    <li>Developers are working solely from their email which they are familiar with, and don't have to switch applications when working on their &quot;to-do&quot; list </li>
    <li>They don't have to re-enter data </li>
    <li>Managers can see important information like Tasks Completed and Tasks Assigned. The reports are ASPX pages that read from Exchange Server via OLEDB </li>
    <li>Clients can see what developers are working on via a URL to the Public Folder</li>
</ul>
<p>
<table class="clsSSWProductTable">
    <tbody>
        <tr>
            <td>You can build your own solution or use <a href="http&#58;//www.ssw.com.au/ssw/ExtremeEmails/Default.aspx">SSW eXtreme Emails!</a> </td>
        </tr>
    </tbody>
</table>
</p>
SSW now uses TFS to manage bugs rather than eXtreme Emails, but we still allow clients to just send us an email.



