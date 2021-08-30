---
type: rule
title: Do you get the work items into Azure DevOps via Excel?
uri: get-work-items-via-excel
authors:
  - title: Ulysses Maclaren
    url: https://www.ssw.com.au/people/uly
created: 2021-08-27T00:22:59.977Z
guid: e90c2504-57a6-499f-ba86-d8820f1dce6d
---
Initializing the Project - See how to get the work items into Azure DevOps via Excel:

<!--endintro-->

* Open SSW Priorities Estimate Template in Excel
  ![Figure: Find SSW Template - 'New | My templates... | SSW_Proposal-Project | SSWPrioritiesEstimateTemplate.xltx''](ExcelSSWTemplate.jpeg)

* Add the tasks and additional tasks into Release_XX sheet
  ![Figure: Copy work items to Release_XX sheet](ExcelReleaseSheet.jpeg)

**Note:** The Project Management tasks will be calculated based on your tasks

* Create a new sheet and go to Team tab
* Click "New List" and choose your project
  ![Figure: Find your project in the list](ExcelFindProject.jpeg)

  ![Figure: Choose 'Input list' to download the empty template](ExcelInputList.jpeg)
  
* Add the other useful columns e.g. Baseline Work, Remaining Work, Completed Work into Excel
  ![Figure: Click 'Choose columns'](ExcelChooseColumnsButton.jpeg)

  ![Figure: Select columns in the left list](ExcelChooseColumnsList.jpeg)
  
* Copy work items (including the Project Management tasks) from Release_XX to the new sheet
  ![Figure: Copy work items from Release_XX](ExcelWorkItems.jpeg)

* Click "Publish" button to upload the work items to TFS