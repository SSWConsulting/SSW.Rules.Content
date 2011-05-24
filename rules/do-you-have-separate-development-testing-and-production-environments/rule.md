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
<p>Read more about setup packages at <a href="http&#58;//www.ssw.com.au/ssw/Standards/wisesetup/WiseStandards.aspx">SSW's Wise Standard for Products.</a></p>
<p><strong>Now make each environment clear.</strong> </p>
<p>Whenever an application has a database, have a visual indicator. I recommend a different background color for each environment </p>
<ul>
    <li><span style="background-color&#58;#ff0000;" class="highlight">Red</span> for the <strong>Development</strong> database </li>
    <li><span style="background-color&#58;#ffff00;" class="highlight">Yellow</span> for the <strong>Test</strong> database </li>
    <li><span style="background-color&#58;#cccccc;" class="highlight">Grey (no colour)</span> for the <strong>Production</strong> database </li>
</ul>
<p>Note&#58; The Yellow might have been Orange (kind of like traffic lights) but the color palette in Word doesn't give Orange. </p>
<img style="border-bottom&#58;0px solid;border-left&#58;0px solid;border-top&#58;0px solid;border-right&#58;0px solid;" class="ms-rteCustom-ImageArea" border="0" alt="colors in Word color pallete" src="/Management/RulesToSuccessfulProjects/PublishingImages/WordColorPallete.GIF" /><span class="ms-rteCustom-FigureNormal">Figure&#58; colors in Word color palette </span>
<p>This prevents testers from accidentally entering test data into the&#160;production version. </p>
<p><strong>Windows Forms Tip&#58;</strong> Implement in the base form in the header <br>
<strong>ASP.NET (at least version 2.0) Tip&#58;</strong> Implement in the master form in the header</p>
<img style="border-bottom&#58;0px solid;border-left&#58;0px solid;border-top&#58;0px solid;border-right&#58;0px solid;" class="ms-rteCustom-ImageArea" border="0" alt=" " src="/Management/RulesToSuccessfulProjects/PublishingImages/dev_test_prod_servers.gif" /> <span class="ms-rteCustom-FigureGood">Figure&#58; Spice up your environments with different colors </span>
<p>An application of this rule is how we identify our CRM servers - see rule <a href="http&#58;//www.ssw.com.au/ssw/Standards/Rules/RulestoBetterMicrosoftCRM.aspx#Environment">Do you identify Development, Test and Production CRM Web Servers by colors?</a></p>



