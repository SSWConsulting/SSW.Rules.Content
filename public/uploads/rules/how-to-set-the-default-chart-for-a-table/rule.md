---
seoDescription: Setting a default chart for a table in Dynamics 365 requires some additional work beyond creating multiple charts. Learn how to set a system-wide default chart using XRMToolBox and Advanced Chart Editor plugins.
type: rule
archivedreason:
title: Do you know how to set the default chart for a table (previously known as an entity)?
guid: a7a94278-db58-47f4-a809-9df55a4788c5
uri: how-to-set-the-default-chart-for-a-table
created: 2021-02-08T15:59:38.0000000Z
authors:
  - title: Mehmet Ozdemir
    url: https://ssw.com.au/people/mehmet-ozdemir
related: []
redirects:
  - do-you-know-how-to-set-the-default-chart-for-a-table-previously-known-as-an-entity
  - do-you-know-how-to-set-the-default-chart-for-a-table-(previously-known-as-an-entity)
---

Model-driven apps allow you to create multiple charts per table, ordinarily, the first chart is the default chart when opening the charts pane. Setting a system-wide default chart takes a bit more work.

<!--endintro-->

![Figure: The first chart in the list is the default](default-chart-1.png)

In the example above “Leads by Rating" is the be the default system-level chart of the Lead table. Some additional work is required to change the default. The easiest way of doing this is with [XRMToolBox](https://www.xrmtoolbox.com/) and the [Advanced Chart Editor](https://crmchartguy.com/2017/06/10/edit-charts-in-the-xrmtoolbox-for-dynamics-365/) plugin.

1. Open the Advanced Chart Editor, Load Entities, and Navigate to the table

![](default-chart-2.png)

2. If changing the default chart to Leads by Source, select chart and export it

![](default-chart-3.png)

3. Open the exported XML file in the text editor of your choice, and change the **isdefault** element to “true" and save the file

![](default-chart-4.png)

4. Import the modified XML back into the Advanced Chart Editor and publish the changes

![](default-chart-5.png)

5. Refresh the Table view, the updated chart should be the default chart in the list

![](default-chart-6.png)

**Note:** If the chart that was modified to be the new default is not at the top of the list, check the first chart in the list by exporting it and confirming the **isdefault** element is set to false.

Where there are two charts with the **isdefault** element set to true, these default charts will be at the top of the list and sorted alphabetically.

For example, if “Lead by Rating" and “Lead by Source" are both set as default then they would both be at the top and sorted alphabetically. The remaining charts would then be sorted alphabetically.

This can be desirable in some instances.

![Figure: Two sorts, first alphabetical sort for the defaults, second alphabetical sort for the remaining charts](default-chart-7.png)
