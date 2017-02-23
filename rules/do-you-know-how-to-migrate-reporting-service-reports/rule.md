---
type: rule
title: Do you know how to migrate reporting service reports
uri: do-you-know-how-to-migrate-reporting-service-reports
created: 2016-10-12T08:35:33.0000000Z
authors:
- id: 61
  title: Moss Gu

---



<span class='intro'> <div class="ms-rtestate-read ms-rte-embedcode ms-rte-embedil ms-rtestate-notify" unselectable="on"> 
   <iframe width="850" height="480" src="https&#58;//www.youtube.com/embed/1knwXRIbVNw" frameborder="0"></iframe>&#160;</div><dd class="ssw15-rteElement-FigureNormal"> 
   ​​​​Figure&#58; How to migrate SSRS reports from an old&#160;server to another<br></dd><p>Let's say you want to migrate SSRS reports​ from an old reporting service server (e.g.,&#160;SQL Server 2008 R2) to a new one (e.g., SQL Server 2016). What involves?<br></p><p class="ssw15-rteElement-P">There are three steps&#58;​<br></p> </span>

<h3 class="ssw15-rteElement-H3"> Step 1&#58; Find the reports that don't need to be migrated</h3><ul><li>You&#160;need to install&#160;<a href="https&#58;//www.ssw.com.au/ssw/SQLReportingServicesAuditor/" target="_blank" title="SSW SQL Reporting Service Auditor">SSW SQL Reporting Service Auditor </a>both on the old and new servers. (You'll also need to run it on 3rd step)</li><li>Find those reports are not-in-use, as per a rule&#58; 
      <a href="/_layouts/15/FIXUPREDIRECT.ASPX?WebId=3dfc0e07-e23a-4cbb-aac2-e778b71166a2&amp;TermSetId=07da3ddf-0924-4cd2-a6d4-a4809ae20160&amp;TermId=ed18874b-3724-4388-8411-45f27f63f909">Do you know which reports are being used?</a></li><li>Find&#160;creators of those reports, by clicking “Detail Views” in reports folder
      <dl class="image"><dt>
            <img src="/SiteAssets/do-you-know-how-to-migrate-reporting-service-reports/detailsview.png" alt="detailsview.png" style="width&#58;750px;" />
         </dt><dd>Figure&#58; Find reports creators by clicking &quot;Details View&quot; inside report folder</dd></dl></li><li>Send an email to report creater&#160;ask for&#160;permission to delete&#160;<br><dl class="image"><dt> 
            <img src="/SiteAssets/do-you-know-how-to-migrate-reporting-service-reports/sent.png" alt="sent.png" style="width&#58;750px;" /> 
         </dt><dd>&#160;Figure&#58;&#160;&#160;Send an email to ask permission</dd></dl><dl class="image"><dt> 
            <img src="/SiteAssets/do-you-know-how-to-migrate-reporting-service-reports/receive.png" alt="receive.png" style="width&#58;750px;height&#58;327px;" /> 
         </dt><dd>Figure&#58;&#160;Email received with permission to delete from creator</dd></dl></li><h3>2. Migrate those in-use reports from old server to new server​</h3><blockquote><p class="ssw15-rteElement-InfoBox">Tip&#58; use the 
         <a href="https&#58;//github.com/dapaxx/reportsync" target="_blank">ReportSync​</a>&#160;tool to save time</p></blockquote><h3>3. Check audit results</h3><ul><li>Run SSW SQL Reporting Service Auditor&#160;on both sides</li><li>Compare audit results. Note that even error and warning messages also need to be the same</li></ul><p>If audit results are exactly the same on old and new servers, it indicates that migration is successful.​</p></ul>


