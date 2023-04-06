---
type: rule
title: Do you check your "Controlled Lookup Data" (aka Reference Data) is still there?
uri: do-you-check-your-controlled-lookup-data
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
  - title: Matt Wicks
    url: https://www.ssw.com.au/people/matt-wicks
  - title: Jack Pettit
    url: https://www.ssw.com.au/people/jack-pettit
related: []
redirects:
  - do-you-check-your-＂controlled-lookup-data＂-(aka-reference-data)-is-still-there-with-procvalidate
  - do-you-check-your-controlled-lookup-data-(aka-reference-data)-is-still-there-with-procvalidate
created: 2009-10-05T22:35:51.000Z
archivedreason: null
guid: b19ff173-49dc-4504-a549-5f26d3c82b83

---

[Controlled Lookup Data](/do-you-deploy-controlled-lookup-data) is when data is tightly coupled to the application. If the data is not there, you have problems. So how do we check to see if data is still there?

Let's look at an example, of a combo that is populated with Controlled Lookup data (just 4 records)    

<!--endintro-->

### Modern Frameworks (EF) 

With Frameworks like Entity Framework you can write unit tests to catch data issues before it becomes an problem. 

### Legacy Applications

With legacy applications, creating a stored procedure will have the same effect with a bit more effort. 

![Figure: How do I make sure these 4 records never go missing?](TimeProDropDown.png)  

``` sql
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
**Figure: Implement a stored procedure to check the 'Controlled Lookup Data' does not go missing**

::: greybox
**Note**: As this procedure will be [executed many times, it must be Idempotent](/do-you-ignore-idempotency)
:::
