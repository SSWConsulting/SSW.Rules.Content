---
type: rule
archivedreason: 
title: Do you apply CRM 2015 update rollup 1 before upgrading to 2016
guid: e9aaf0ef-09ef-404b-b54a-50c57b5747c9
uri: do-you-apply-crm-2015-update-rollup-1-before-upgrading-to-2016
created: 2016-01-28T04:15:58.0000000Z
authors:
- id: 1
  title: Adam Cogan
related: []

---


Make sure CRM 2015 update rollup 1 has been applied before upgrading to CRM 2016.<br>
<br><excerpt class='endintro'></excerpt><br>
<dl class="ssw15-rteElement-ImageArea"> <img src="updaterollup1.png" alt="" style="margin:5px;width:758px;" /> <strong>Figure:   version after applying CRM 2015 update rollup 1</strong> <dl class="ssw15-rteElement-ImageArea"><dl class="ssw15-rteElement-ImageArea"> <strong>Note:</strong> You might come accross the error below while applying CRM 2015 update rollup 1</dl><dl class="ssw15-rteElement-ImageArea"><table cellspacing="0" width="100%" class="ssw15-rteTable-default"><tbody><tr><td class="ssw15-rteTable-default" style="width:100%;"><div>Database update install failed for orgId = 011d5962-3475-4df9-a123-c3ecaf88b048.  Continuing with other orgs.  Exception: System.Reflection.TargetInvocationException: Exception has been thrown by the target of an invocation. ---> System.Data.SqlClient.SqlException: The current transaction cannot be committed and cannot support operations that write to the log file. Roll back the transaction.</div><div>Uncommittable transaction is detected at the end of the batch. The transaction is rolled back.</div></td></tr></tbody></table></dl><dl class="ssw15-rteElement-ImageArea"> <strong>Solution:</strong> <dl class="ssw15-rteElement-ImageArea"><ol><li> 
                  <span style="background-color:initial;"> Make a backup of the file MetadataDiffs.xml from “C:\Program Files\Microsoft Dynamics               CRM\Setup\Serviceability\Latest\Actions_Org\Install”</span><br></li><li> 
                  <span style="background-color:initial;"> Open the file MetadataDiffs.xml from “C:\Program Files\Microsoft Dynamics CRM\Setup\Serviceability\Latest\Actions_Org\Install”</span></li><li> 
                  <span style="background-color:initial;"></span> <span style="background-color:initial;"> Rem</span><span style="line-height:20px;background-color:initial;">ove the entry about the index “cndx_BusinessDataLocalizedLabel”. This is found at the very end of the file:</span> 
                  <table cellspacing="0" width="100%" class="ssw15-rteTable-default"><tbody><tr><td class="ssw15-rteTable-default" style="width:100%;">   <index Name="cndx_BusinessDataLocalizedLabel"><br>     <EntityId>4ba1569e-3c9c-4d9f-99ea-b61fb08d7f97</EntityId><br>     <IsClustered>1</IsClustered><br>     <IsUnique>1</IsUnique><br>     <IndexType>6</IndexType><br>    <IsPrimaryKey>0</IsPrimaryKey><br>     <attributes><br>       <attribute AttributeId="d88e1df3-b5b3-42f3-9ffa-007f22951dd4" IsSystemManaged="1" order="0" /><br>       <attribute AttributeId="bb23d3c8-8d18-40d3-9519-66101a8cae34" IsSystemManaged="1" order="1" /><br>       <attribute AttributeId="976e1053-5faa-4c3f-be6e-669acfec9d5a" IsSystemManaged="1" order="2" /><br>       <attribute AttributeId="e81341c4-4d4a-4977-98eb-6597fcde2cc4" IsSystemManaged="1" order="3" /><br>     </attributes><br>   </index></td></tr></tbody></table></li><li> 
                  <span style="line-height:20px;background-color:initial;">Close Deployment Manager</span><br></li><li> 
                  <span style="background-color:initial;"> Start Deployment Manager</span></li><li> 
                  <span style="background-color:initial;"></span> <span style="background-color:initial;"> Start the organization update from Deployment manager.</span></li><li> 
                  <span style="background-color:initial;">Run the following query on the organization DB to manually recreate the index<br></span> 
                  <table cellspacing="0" width="100%" class="ssw15-rteTable-default"><tbody><tr><td class="ssw15-rteTable-default" style="width:100%;">IF EXISTS (SELECT * FROM sys.indexes WHERE name = 'cndx_BusinessDataLocalizedLabel' AND OBJECT_NAME(object_id) = 'BusinessDataLocalizedLabelBase') DROP INDEX [cndx_BusinessDataLocalizedLabel] ON [BusinessDataLocalizedLabelBase];<br>IF NOT EXISTS (SELECT * FROM sys.indexes WHERE NAME = 'cndx_BusinessDataLocalizedLabel' AND OBJECT_NAME(object_id) = 'BusinessDataLocalizedLabelBase')<br>BEGIN TRY<br> CREATE UNIQUE CLUSTERED INDEX [cndx_BusinessDataLocalizedLabel] ON [BusinessDataLocalizedLabelBase]([ObjectId] ASC, [ObjectIdTypeCode] ASC, [ObjectColumnNumber] ASC, [LanguageId] ASC) WITH (FILLFACTOR = 80, MAXDOP = 4, SORT_IN_TEMPDB = ON, ONLINE = ON)<br>END TRY<br>BEGIN CATCH<br> CREATE UNIQUE CLUSTERED INDEX [cndx_BusinessDataLocalizedLabel] ON [BusinessDataLocalizedLabelBase]([ObjectId] ASC, [ObjectIdTypeCode] ASC, [ObjectColumnNumber] ASC, [LanguageId] ASC) WITH (FILLFACTOR = 80, MAXDOP = 4, SORT_IN_TEMPDB = ON)<br>END CATCH</td></tr></tbody></table></li><li> 
                  <span style="background-color:initial;"> Restore the file MetadataDiffs.xml to its original state using the backup taken at step 1.</span></li></ol></dl></dl></dl></dl> Source from:​ <a href="https://www.remotingcoders.com/Blogsite/Lists/Posts/Post.aspx?ID=83" target="_blank">Error updating Microsoft Dynamics CRM 2015 0.1 </a> 


