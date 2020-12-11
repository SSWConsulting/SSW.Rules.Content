---
type: rule
archivedreason: 
title: Do you know how to migrate reporting service reports
guid: 684f90fc-01c1-43e5-b864-d4f3efabbf76
uri: do-you-know-how-to-migrate-reporting-service-reports
created: 2016-10-12T08:35:33.0000000Z
authors:
- id: 61
  title: Moss Gu
related: []

---


<div class="ms-rtestate-read ms-rte-embedcode ms-rte-embedil ms-rtestate-notify" unselectable="on"> 
   <iframe width="850" height="480" src="https://www.youtube.com/embed/1knwXRIbVNw" frameborder="0"></iframe> </div><dd class="ssw15-rteElement-FigureNormal"> 
   ​​​​Figure: How to migrate SSRS reports from an old server to another<br></dd><p>Let's say you want to migrate SSRS reports​ from an old reporting service server (e.g., SQL Server 2008 R2) to a new one (e.g., SQL Server 2016). What involves?<br></p><p class="ssw15-rteElement-P">There are three steps:​<br></p>
<br><excerpt class='endintro'></excerpt><br>
<h3 class="ssw15-rteElement-H3"> Step 1: Find the reports that don't need to be migrated</h3><ul><li>You need to install <a href="https://www.ssw.com.au/ssw/SQLReportingServicesAuditor/" target="_blank" title="SSW SQL Reporting Service Auditor">SSW SQL Reporting Service Auditor </a>both on the old and new servers. (You'll also need to run it on 3rd step)</li><li>Find those reports are not-in-use, as per a rule: 
      <a href="/_layouts/15/FIXUPREDIRECT.ASPX?WebId=3dfc0e07-e23a-4cbb-aac2-e778b71166a2&TermSetId=07da3ddf-0924-4cd2-a6d4-a4809ae20160&TermId=ed18874b-3724-4388-8411-45f27f63f909">Do you know which reports are being used?</a></li><li>Find creators of those reports, by clicking “Detail Views” in reports folder
      <dl class="image"><dt>
            <img src="detailsview.png" alt="detailsview.png" style="width:750px;" />
         </dt><dd>Figure: Find reports creators by clicking "Details View" inside report folder</dd></dl></li><li>Send an email to report creater ask for permission to delete <br><dl class="image"><dt> 
            <img src="sent.png" alt="sent.png" style="width:750px;" /> 
         </dt><dd> Figure:  Send an email to ask permission</dd></dl><dl class="image"><dt> 
            <img src="receive.png" alt="receive.png" style="width:750px;height:327px;" /> 
         </dt><dd>Figure: Email received with permission to delete from creator</dd></dl></li><h3>2. Migrate those in-use reports from old server to new server​</h3><blockquote><p class="ssw15-rteElement-InfoBox">Tip: use the 
         <a href="https://github.com/dapaxx/reportsync" target="_blank">ReportSync​</a> tool to save time</p></blockquote><h3>3. Check audit results</h3><ul><li>Run SSW SQL Reporting Service Auditor on both sides</li><li>Compare audit results. Note that even error and warning messages also need to be the same</li></ul><p>If audit results are exactly the same on old and new servers, it indicates that migration is successful.​</p></ul>


