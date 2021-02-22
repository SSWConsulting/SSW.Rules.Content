---
type: rule
archivedreason: 
title: Do you have separate development, testing and production environments?
guid: 616246d0-1675-4c1c-b4b0-d4352fe818e1
uri: do-you-have-separate-development-testing-and-production-environments
created: 2009-03-10T07:02:13.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects: []

---


It is important to maintain three separate environments for development, testing and production. Some companies skip the testing server because it can be a hassle to copy new files, register DLLs and deploy backend changes. This will usually result in higher support costs and unhappy users due to simple bugs that could have being found in testing.

<br><excerpt class='endintro'></excerpt><br>

  <p>The best solution is to use build scripts (.bat and .vbs files) to automatically create a setup package that can be used to deploy to testing and production environments. For backend changes, you can either include the change scripts with the setup package (if it's a localised database), or run those scripts as part of your deployment process.</p>
<p>Read more about setup packages at <a href="http://www.ssw.com.au/ssw/Standards/wisesetup/WiseStandards.aspx">SSW's Wise Standard for Products.</a></p>
<p><strong>Now make each environment clear.</strong> </p>
<p>Whenever an application has a database, have a visual indicator. I recommend a different background color for each environment </p>
<ul>
    <li><span class="highlight" style="background-color:rgb(255, 0, 0);">Red</span> for the <strong>Development</strong> database </li>
    <li><span class="highlight" style="background-color:rgb(255, 255, 0);">Yellow</span> for the <strong>Test</strong> database </li>
    <li><span class="highlight" style="background-color:rgb(204, 204, 204);">Grey (no colour)</span> for the <strong>Production</strong> database </li>
</ul>
<p>Note: The Yellow might have been Orange (kind of like traffic lights) but the color palette in Word doesn't give Orange. </p>
<img border="0" class="ms-rteCustom-ImageArea" alt="colors in Word color pallete" src="WordColorPallete.GIF" style="border-width:0px;border-style:solid;border-color:-moz-use-text-color;" /><span class="ms-rteCustom-FigureNormal">Figure: colors in Word color palette </span>
<p>This prevents testers from accidentally entering test data into the production version. </p>
<p><strong>Windows Forms Tip:</strong> Implement in the base form in the header <br>
<strong>ASP.NET (at least version 2.0) Tip:</strong> Implement in the master form in the header</p>
<img border="0" class="ms-rteCustom-ImageArea" alt=" " src="dev_test_prod_servers.gif" style="border-width:0px;border-style:solid;border-color:-moz-use-text-color;" /> <span class="ms-rteCustom-FigureGood">Figure: Spice up your environments with different colors </span>
<p>An application of this rule is how we identify our CRM servers - see rule <a href="/do-you-identify-development-test-and-production-crm-web-servers-by-colors">Do you identify Development, Test and Production CRM Web Servers by colors?</a></p>



