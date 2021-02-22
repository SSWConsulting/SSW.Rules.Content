---
type: rule
archivedreason: 
title: Do you apply CRM 2015 update rollup 1 before upgrading to 2016
guid: e9aaf0ef-09ef-404b-b54a-50c57b5747c9
uri: do-you-apply-crm-2015-update-rollup-1-before-upgrading-to-2016
created: 2016-01-28T04:15:58.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects: []

---

Make sure CRM 2015 update rollup 1 has been applied before upgrading to CRM 2016.

<!--endintro-->
![](updaterollup1.png)**Figure:   version after applying CRM 2015 update rollup 1**   <strong>Note:</strong> You might come accross the error below while applying CRM 2015 update rollup 1<table cellspacing="0" width="100%" class="ssw15-rteTable-default"><tbody><tr><td class="ssw15-rteTable-default" style="width:100%;"><div>Database update install failed for orgId = 011d5962-3475-4df9-a123-c3ecaf88b048.  Continuing with other orgs.  Exception: System.Reflection.TargetInvocationException: Exception has been thrown by the target of an invocation. ---&gt; System.Data.SqlClient.SqlException: The current transaction cannot be committed and cannot support operations that write to the log file. Roll back the transaction.</div><div>Uncommittable transaction is detected at the end of the batch. The transaction is rolled back.</div></td></tr></tbody></table>  <strong>Solution:</strong> <dl class="ssw15-rteElement-ImageArea"><ol><li> 
                  <span style="background-color:initial;"> Make a backup of the file MetadataDiffs.xml from “C:\Program Files\Microsoft Dynamics               CRM\Setup\Serviceability\Latest\Actions_Org\Install”</span>
</li><li> 
                  <span style="background-color:initial;"> Open the file MetadataDiffs.xml from “C:\Program Files\Microsoft Dynamics CRM\Setup\Serviceability\Latest\Actions_Org\Install”</span></li><li> 
                  <span style="background-color:initial;"></span> <span style="background-color:initial;"> Rem</span><span style="line-height:20px;background-color:initial;">ove the entry about the index “cndx_BusinessDataLocalizedLabel”. This is found at the very end of the file:</span> 
                  <table cellspacing="0" width="100%" class="ssw15-rteTable-default"><tbody><tr><td class="ssw15-rteTable-default" style="width:100%;">   &lt;index Name="cndx_BusinessDataLocalizedLabel"&gt;
     &lt;EntityId&gt;4ba1569e-3c9c-4d9f-99ea-b61fb08d7f97&lt;/EntityId&gt;
     &lt;IsClustered&gt;1&lt;/IsClustered&gt;
     &lt;IsUnique&gt;1&lt;/IsUnique&gt;
     &lt;IndexType&gt;6&lt;/IndexType&gt;
    &lt;IsPrimaryKey&gt;0&lt;/IsPrimaryKey&gt;
     &lt;attributes&gt;
       &lt;attribute AttributeId="d88e1df3-b5b3-42f3-9ffa-007f22951dd4" IsSystemManaged="1" order="0" /&gt;
       &lt;attribute AttributeId="bb23d3c8-8d18-40d3-9519-66101a8cae34" IsSystemManaged="1" order="1" /&gt;
       &lt;attribute AttributeId="976e1053-5faa-4c3f-be6e-669acfec9d5a" IsSystemManaged="1" order="2" /&gt;
       &lt;attribute AttributeId="e81341c4-4d4a-4977-98eb-6597fcde2cc4" IsSystemManaged="1" order="3" /&gt;
     &lt;/attributes&gt;
   &lt;/index&gt;</td></tr></tbody></table></li><li> 
                  <span style="line-height:20px;background-color:initial;">Close Deployment Manager</span>
</li><li> 
                  <span style="background-color:initial;"> Start Deployment Manager</span></li><li> 
                  <span style="background-color:initial;"></span> <span style="background-color:initial;"> Start the organization update from Deployment manager.</span></li><li> 
                  <span style="background-color:initial;">Run the following query on the organization DB to manually recreate the index
</span> 
                  <table cellspacing="0" width="100%" class="ssw15-rteTable-default"><tbody><tr><td class="ssw15-rteTable-default" style="width:100%;">IF EXISTS (SELECT * FROM sys.indexes WHERE name = 'cndx_BusinessDataLocalizedLabel' AND OBJECT_NAME(object_id) = 'BusinessDataLocalizedLabelBase') DROP INDEX [cndx_BusinessDataLocalizedLabel] ON [BusinessDataLocalizedLabelBase];
IF NOT EXISTS (SELECT * FROM sys.indexes WHERE NAME = 'cndx_BusinessDataLocalizedLabel' AND OBJECT_NAME(object_id) = 'BusinessDataLocalizedLabelBase')
BEGIN TRY
 CREATE UNIQUE CLUSTERED INDEX [cndx_BusinessDataLocalizedLabel] ON [BusinessDataLocalizedLabelBase]([ObjectId] ASC, [ObjectIdTypeCode] ASC, [ObjectColumnNumber] ASC, [LanguageId] ASC) WITH (FILLFACTOR = 80, MAXDOP = 4, SORT_IN_TEMPDB = ON, ONLINE = ON)
END TRY
BEGIN CATCH
 CREATE UNIQUE CLUSTERED INDEX [cndx_BusinessDataLocalizedLabel] ON [BusinessDataLocalizedLabelBase]([ObjectId] ASC, [ObjectIdTypeCode] ASC, [ObjectColumnNumber] ASC, [LanguageId] ASC) WITH (FILLFACTOR = 80, MAXDOP = 4, SORT_IN_TEMPDB = ON)
END CATCH</td></tr></tbody></table></li><li> 
                  <span style="background-color:initial;"> Restore the file MetadataDiffs.xml to its original state using the backup taken at step 1.</span></li></ol></dl> Source from: [Error updating Microsoft Dynamics CRM 2015 0.1](https://www.remotingcoders.com/Blogsite/Lists/Posts/Post.aspx?ID=83)
