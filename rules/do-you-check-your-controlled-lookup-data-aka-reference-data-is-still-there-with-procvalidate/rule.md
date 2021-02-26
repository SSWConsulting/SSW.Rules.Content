---
type: rule
archivedreason: 
title: Do you check your "Controlled Lookup Data" (aka Reference Data) is still there with procValidate?
guid: b19ff173-49dc-4504-a549-5f26d3c82b83
uri: do-you-check-your-controlled-lookup-data-aka-reference-data-is-still-there-with-procvalidate
created: 2009-10-05T22:35:51.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
- do-you-check-your-＂controlled-lookup-data＂-(aka-reference-data)-is-still-there-with-procvalidate
- do-you-check-your-controlled-lookup-data-(aka-reference-data)-is-still-there-with-procvalidate

---

[Controlled Lookup Data](/do-you-deploy-controlled-lookup-data) is when data is tightly coupled to the application. If the data is not there, you have problems. So how do we check to see if data is still there?

The simplest way is to add a procValidate (Stored Procedure) to check that all the lookup data is still there.

![Figure: procValidates are just like a nagging wife](NaggingWife.gif)  

 Let's look at an example, of a combo that is populated with Controlled Lookup data (just 4 records)    
<!--endintro-->

![Figure: How do I make sure these 4 records never go missing?](TimeProDropDown.png)  



```
CREATE PROCEDURE procValidate_Region 
AS

    IF EXISTS(SELECT TOP 1 * FROM dbo.[Region]
              WHERE RegionDescription = 'Eastern')
        PRINT 'Eastern is there'
    ELSE
        RAISERROR(N'Lack of Eastern', 10, 1)
    IF EXISTS(SELECT TOP 1 * FROM dbo.[Region]
              WHERE RegionDescription = 'Western')
        PRINT Western is there'
    ELSE
        RAISERROR(N'Lack of Western', 10, 1)
    IF EXISTS(SELECT TOP 1 * FROM dbo.[Region]
              WHERE RegionDescription = 'Northern')
        PRINT 'Northern is there'
    ELSE
        RAISERROR(N'Lack of Northern', 10, 1)
    IF EXISTS(SELECT TOP 1 * FROM dbo.[Region]
              WHERE RegionDescription = 'Southern')
        PRINT 'Southern is there'
    ELSE
        RAISERROR(N'Lack of Southern', 10, 1)
```


     Figure: Implement a stored procedure to check the 'Controlled Lookup Data' does not go missing   Note: As this procedure will be [executed many times, it must be Idempotent](/do-you-ignore-idempotency)
