---
type: rule
title: Do you know how to refresh the cube?
uri: how-to-refresh-the-cube
authors:
  - title: Adam Cogan
    url: https://www.ssw.com.au/people/adam-cogan
created: 2021-09-20T21:11:46.406Z
archivedreason: "Piers: We don’t use TFS anymore and even if we did, this rule
  looks very outdated. "
guid: b4fe89a4-32bd-4e31-b1f5-bf238dff24e2
---
**Note:** These are instructions for TFS 2010 Beta 2

If you enter data and then look at reports you will see stale data!!!

![Figure: The report footer tells you that the TFS Warehouse is not up to date](refresh1.jpg)

The UI does not provide an easy option. However you have 2 \*hard\* ways of updating the TFS Data Warehouse.

**Option 1** - Open SQL Management Studio and then force re-processing\
**Option 2** - Open the TFS Web Services in IE and then force processing (Recommended - see below)

#### More info on Option 2

Follow these instructions to reprocess the data warehouse using the web services (this took us a long time to work out):

1. Open IIS Manager
2. Go to "Team Foundation Server"
3. Open the feature "Directory browsing"
4. "Enable"
5. Back to "Team Foundation Server"
6. "Browse website"
7. Browse to <http://localhost:8080/tfs/TeamFoundation/Administration/v3.0/WarehouseControlService.asmx>

   ![Figure: You will need to call 2 of these web services](refresh2.jpg)

8. Invoke "ProcessWarehouse" with the parameter "DefaultCollection" (or whatever your collection is called)

   ![Figure: Call "ProcessWarehouse" web service with parameter "DefaultCollection"](refresh3.jpg)

9. Invoke "ProcessAnalysisDatabase" with parameter "Full"

   ![Figure: Call "ProcessAnalysisDatabase" with parameter "Full"](refresh4.jpg)

10. Now once the the reprocess is completed, the reports are up to date

More info see the blog entry from Grant Holliday:[http://ozgrant.com/2006/05/15/forcing-data-warehouse-update-for-tfs/](https://www.ssw.com.au/SSW/Redirect/ForceDataWarehouseforUpdateTFS.htm)

Note: [We have a suggestion to the TFS team for this.](https://www.ssw.com.au/ssw/Standards/BetterSoftwareSuggestions/TeamFoundationServer.aspx%22%20%5Cl%20%22RefreshTFSCube)

[See the suggestion for a VS extension to Refresh Report Data](https://www.ssw.com.au/ssw/Standards/BetterSoftwareSuggestions/TeamFoundationServer.aspx%22%20%5Cl%20%22RefreshData)