---
type: rule
title: Do you check your "Controlled Lookup Data" (aka Reference Data) is still there with procValidate?
uri: do-you-check-your-controlled-lookup-data-aka-reference-data-is-still-there-with-procvalidate
created: 2009-10-05T22:35:51.0000000Z
authors:
- id: 1
  title: Adam Cogan

---



<span class='intro'> This field should not be null (Remove me when you edit this field). </span>


  <dl class="image">
    <dt><img alt="" src="/Standards/SoftwareDevelopment/RulesToBetterSQLServerSchemaDeployment/PublishingImages/TimeProDropDown.png" /> </dt>
    <dd>Figure&#58; How do I make sure these 4 records never go missing? </dd>
</dl>
<dl class="image">
    <dt><font class="ms-rteCustom-CodeArea" size="+0">
    <pre>CREATE PROCEDURE procValidate_Region 
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
</pre>
    </font></dt>
    <dd>Figure&#58; Implement a stored procedure to check the 'Controlled Lookup Data' does not go missing </dd>
</dl>
Note&#58; As this procedure will be <a href="/Standards/SoftwareDevelopment/RulesToBetterSQLServerSchemaDeployment/Pages/DoYouIgnoreIdempotency.aspx">executed many times, it must be Idempotent </a>



