---
type: rule
title: Do you use version control with Power BI?
uri: do-you-use-version-control-with-power-bi
created: 2017-03-29T06:06:12.0000000Z
authors:
- id: 32
  title: Mehmet Ozdemir
- id: 84
  title: Patricia Barros
- id: 85
  title: Chris Beaver

---



<span class='intro'> <div style="text-align&#58;left;">​​​​Developers in 2018 have better control history than before.<br><br>Prior to the April 2016 update, storing a Power BI Report in version control could be prohibitive, as pbix files contain the dataset and report definition, which in some cases can be gigabytes in size.<br></div><div><br></div><div>The April 2016 update features the ability to export a Power BI Report template (pbit) file, which contains the report definition minus the dataset.</div><div><br></div><div>If the pbix file size is not too large, you may choose to store it directly in source control. When a pbix file is very large, then it may be more economical to store the template (pbit file) only in source control. &#160;<br><br></div><div>Here’s the pros and cons we’ve found for each file type&#58;<br></div> </span>

<p>
   <strong>Template pbit files</strong> are small, but when you open a template in Power BI Desktop, the dataset needs to reload. &#160;If the changes you need to make to a report are small, waiting for a dataset reload can be frustrating (e.g. waiting 10 minutes for the reload to do a one-minute change).&#160;The Power BI pbix file will still be required to publish to Power BI Online.<br></p><p>
   <strong>Power BI pbix files</strong> can get very large, but when you open them, the data is there and you can immediately make changes to the report. However, if your workplace is geographically dispersed, then upload and download times to/from source control will be a consideration.<br></p><p>Having a mixed set of rules for storing different file types based on their size will quickly get messy if you have a number of reports, so make a decision to go one way or the other based on your environment.​<br></p><dl class="badImage"><dt>
      <img src="/PublishingImages/PowerBI-SourceControl-BadExample.png" alt="" style="width&#58;760px;height&#58;325px;" />
   </dt><dd>Figure&#58; Bad Example – Mixed Template and Power BI Files in Source Control</dd></dl><dl class="goodImage"><dt>
      <img src="/PublishingImages/PowerBI-SourceControl-GoodExample.png" alt="" style="width&#58;760px;height&#58;247px;" />
   </dt><dd>Figure&#58; Good Example – Single File Type in Source Control</dd></dl><p>To export a template from Power BI Desktop, select File | Export | Power BI template from the menu, enter a description, file name and click save, as per the below figures.</p><dl class="image"><dt>
      <img src="/PublishingImages/PowerBI-SourceControl-1-3.jpg" unselectable="on" alt="" />
   </dt>&#160;​​<span style="color&#58;#555555;font-weight&#58;bold;">Figure&#58; Exporting a Power BI Template from Power BI Desktop</span></dl><p>Add comments describing the changes made to the report and append to these, in descending order, each time a change is made. This way the history will be at hand each time the template is opened.​</p><dl class="image"><dt>
      <img src="/PublishingImages/PowerBI-SourceControl-2-3.jpg" alt="" />
   </dt>​<span style="color&#58;#555555;font-weight&#58;bold;">Figure&#58; Enter a Description for the Template</span></dl><dl class="image"><dt>
      <img src="/PublishingImages/PowerBI-SourceControl-3-3.jpg" alt="" />
   </dt><dd>Figure&#58; Enter a File Name and Save</dd></dl><p>Save your pbix file to the same folder as the template above, you’ll need these if you want to publish your report to Power BI Online.</p><p>If you’ve decided to store template pbit files in source control, ensure you’ve set your source control application to ignore *.pbix files.<br></p>


