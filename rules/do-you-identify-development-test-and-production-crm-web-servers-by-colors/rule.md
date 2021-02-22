---
type: rule
archivedreason: 
title: Do you identify Development, Test and Production Web Servers by colors?
guid: 9b723127-5c2d-4e40-a2a5-45ccd4840d2b
uri: do-you-identify-development-test-and-production-crm-web-servers-by-colors
created: 2012-12-10T19:42:40.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: Jean Thirion
  url: https://ssw.com.au/people/jean-thirion
related: []
redirects:
- do-you-identify-development-test-and-production-web-servers-by-colors

---


<p>As per rule <a href="/_layouts/15/FIXUPREDIRECT.ASPX?WebId=3dfc0e07-e23a-4cbb-aac2-e778b71166a2&TermSetId=07da3ddf-0924-4cd2-a6d4-a4809ae20160&TermId=ae2ccef9-6cdc-4767-8e5a-e0e3dbf46fe2"> "Do you have separate development, testing, and production environment?"</a>, it's better to use different background colors to identify Development, Test and Production servers.<br></p><h3 class="ssw15-rteElement-H3">CRM <br></h3><dl class="image"><dt><img src="ssw staging 2.png" alt="crm staging.png" style="width:808px;" /></dt><dd>Figure: Staging uses blue background</dd></dl><dl class="image"><dt> <img src="ssw production 2.png" alt="crm production.png" style="width:808px;" /></dt><dd>Figure: Production uses red background </dd></dl><p>The way to change the default background color is to edit the CRM CSS files. These changes aren't supported and may be overwritten when CRM Rollups are applied.<br></p><h3 class="ssw15-rteElement-H3">CRM 2015 and CRM 2016<br></h3><p>Using theme feature to change the environment color.</p><dl class="image"><dt><img src="CRM2015Theme.JPG" alt="CRM2015Theme.JPG" /></dt><dd>Figure: Changing CRM 2016 UI by using theme feature<br></dd></dl><h3 class="ssw15-rteElement-H3">CRM 2013</h3><p>Edit: <strong>&lt;CrmWebsiteRoot&gt;</strong><strong>\_controls\navbar\navbar.css</strong></p><p class="ssw15-rteElement-CodeArea">.navigationControl<br>{<br><span style="background-color:#ffff00;">background-color: #006600;</span><br>margin: 0;<br>z-index: 999;<br>float: left;<br>width: 100%;<br>position: relative;<br>}</p><dd class="ssw15-rteElement-FigureNormal"> Figure: Edit the background color to reflect the environment<br></dd><dl class="image"><dt><img alt="crm2013_greenbar.jpg" src="crm2013_greenbar.jpg" style="width:650px;" /></dt><dd> Figure: CRM 2013 with a green navigation bar</dd></dl> 
<br><excerpt class='endintro'></excerpt><br>
<h3 class="ssw15-rteElement-H3">CRM 2011</h3><p>Edit 
   <strong>&lt;CrmWebsiteRoot&gt;\_static\css\1033\cui.css</strong>, locate and modify the section ms-cui-tabBody so that it reads:</p><p>
   <span class="ssw-rteStyle-CodeArea">background-color : #ffffff;</span></p><p>Change color to a suitable color for the environment:</p><p>
   <span class="ssw-rteStyle-CodeArea">background-color : #bbffaa; </span></p><p> <img src="CRM2011_ColorCodedRibbon.jpg" alt="" style="margin:5px;" /><br></p><p>
   <span class="ssw-rteStyle-FigureNormal">Figure: CRM Ribbon color green to signify production environment</span></p><h3 class="ssw15-rteElement-H3">CRM 4</h3><p>Edit,<strong> &lt;CrmWebsiteRoot&gt;\</strong><strong>_common\styles\global.css.aspx</strong></p><dl class="image"><dt><div class="greyBox"><pre>         body.stage
            {
                &lt;% if (CrmStyles.IsRightToLeft) { %&gt;
                    dir:rtl;
                &lt;%} %&gt;
                border-top:1px solid #6893cf;
​​
            <span style="background-color:#ffff00;">/* background-color: #d6e8ff; */</span>

            <span style="background-color:#ffff00;">background-color: #ffff00;</span>

            <span style="background-color:#ffff00;">padding: 4px;</span>
            
            <span style="background-color:#ffff00;">/* background-repeat: repeat-x;</span>
            
            <span style="background-color:#ffff00;">background-image: url(/_imgs/app_back.gif);
                  */</span>
            }
       </pre></div></dt><dd> Figure: In C:\Inetpub\wwwroot\_common\styles\global.css.aspx comment out and change the reference in yellow so the users know what server they are on</dd></dl><dl class="image"><dt>
      <img alt="Color of CRM Development Server" src="CRM_DevelopmentColor.jpg" />
   </dt><dd>Figure: Color of CRM Development Server - Red</dd></dl><dl class="image"><dt>
      <img alt="Color of CRM Test Server" src="CRM_TestColor.jpg" />
   </dt><dd>Figure: Color of CRM Test Server - Yellow</dd></dl><dl class="image"><dt>
      <img alt="Color of CRM Test Server" src="CRM_ProductionColor.jpg" />
   </dt><dd> Figure: Color of CRM Production Server - Default<br></dd></dl><h3>SharePoint online</h3><p>Regarding the color codes, we use to differentiate Production to Test with SharePoint online.</p><p>Here is what we change:</p><ul><li>Site Settings | Change The Look 
      <ul><li>Test – Orange 
            <dl class="image"><dt> 
                  <img src="sharepoint-orange-theme.jpg" alt="sharepoint-orange-theme.jpg" style="width:750px;" /> 
               </dt><dd>Figure: Selecting Orange theme for test</dd></dl><dl class="image"><dt> 
                  <img src="sharepoint-orange-applied.jpg" alt="sharepoint-orange-applied.jpg" /> 
               </dt><dd>Figure: orange theme applied</dd></dl></li><li>Production - Office 
            <dl class="image"><dt> 
                  <img src="sharepoint-office-theme.jpg" alt="sharepoint-orange-theme.jpg" style="width:750px;" /> 
               </dt><dd>Figure: Selecting Office theme for Production</dd></dl><dl class="image"><dt> 
                  <img src="sharepoint-office-applied.jpg" alt="sharepoint-orange-applied.jpg" /> 
               </dt><dd>Figure: office (blue) theme applied</dd></dl></li></ul></li></ul>


