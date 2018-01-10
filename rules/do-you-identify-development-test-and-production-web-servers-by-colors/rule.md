---
type: rule
title: Do you identify Development, Test and Production Web Servers by colors?
uri: do-you-identify-development-test-and-production-web-servers-by-colors
created: 2012-12-10T19:42:40.0000000Z
authors:
- id: 1
  title: Adam Cogan
- id: 69
  title: Jean Thirion

---



<span class='intro'> <p>As per rule 
   <a href="/_layouts/15/FIXUPREDIRECT.ASPX?WebId=3dfc0e07-e23a-4cbb-aac2-e778b71166a2&amp;TermSetId=07da3ddf-0924-4cd2-a6d4-a4809ae20160&amp;TermId=ae2ccef9-6cdc-4767-8e5a-e0e3dbf46fe2"> &quot;Do you have separate development, testing, and production environment?&quot;</a>, it's better to use different background colors to identify Development, Test and Production servers.<br></p><h3 class="ssw15-rteElement-H3">CRM​​<br></h3><dl class="image"><dt><img src="/PublishingImages/ssw%20staging%202.png" alt="crm staging.png" style="width&#58;808px;" /></dt><dd>Figure&#58; Staging uses blue background</dd></dl><dl class="image"><dt>
         <img src="/PublishingImages/ssw%20production%202.png" alt="crm production.png" style="width&#58;808px;" /></dt><dd>Figure&#58; Production uses red background&#160;</dd></dl><p>The way to change the default background color is to edit the CRM CSS files. These changes aren't supported and may be overwritten when CRM Rollups are applied.<br></p><h3 class="ssw15-rteElement-H3">CRM 2015 and CRM 2016<br></h3><p>Using theme feature to change the environment color.</p><dl class="image"><dt><img src="/PublishingImages/CRM2015Theme.JPG" alt="CRM2015Theme.JPG" /></dt><dd>Figure&#58; Changing CRM 2016 UI by using theme feature<br></dd></dl><h3 class="ssw15-rteElement-H3">​CRM 2013</h3><p>Edit&#58; 
   <strong>&lt;CrmWebsiteRoot&gt;</strong><strong>\_controls\navbar\navbar.css</strong></p><p class="ssw15-rteElement-CodeArea">.navigationControl<br>&#123;<br><span style="background-color&#58;#ffff00;">background-color&#58; #006600;</span><br>margin&#58; 0;<br>z-index&#58; 999;<br>float&#58; left;<br>width&#58; 100%;<br>position&#58; relative;<br>&#125;</p><dd class="ssw15-rteElement-FigureNormal">&#160;Figure&#58; Edit the background color to reflect the environment<br></dd><dl class="image"><dt><img alt="crm2013_greenbar.jpg" src="/PublishingImages/crm2013_greenbar.jpg" style="width&#58;650px;" /></dt><dd>&#160;Figure&#58; CRM 2013 with a green navigation bar</dd></dl>  </span>

<h3 class="ssw15-rteElement-H3">CRM 2011</h3><p>Edit 
   <strong>&lt;CrmWebsiteRoot&gt;\_static\css\1033\cui.css</strong>, locate and modify the section ms-cui-tabBody so that it reads&#58;</p><p> 
   <span class="ssw-rteStyle-CodeArea">background-color &#58; #ffffff;</span></p><p>Change&#160;color to&#160;a suitable color for the environment&#58;</p><p> 
   <span class="ssw-rteStyle-CodeArea">background-color &#58; #bbffaa;&#160;</span></p><p>&#160;<img src="/PublishingImages/CRM2011_ColorCodedRibbon.jpg" alt="" style="margin&#58;5px;" /><br></p><p> 
   <span class="ssw-rteStyle-FigureNormal">Figure&#58; CRM Ribbon color green to signify production environment</span></p><h3 class="ssw15-rteElement-H3">CRM 4</h3><p>Edit,<strong> &lt;CrmWebsiteRoot&gt;\</strong><strong>_common\styles\global.css.aspx</strong></p><dl class="image"><dt><div class="greyBox"><pre>         body.stage
            &#123;
                &lt;% if (CrmStyles.IsRightToLeft) &#123; %&gt;
                    dir&#58;rtl;
                &lt;%&#125; %&gt;
                border-top&#58;1px solid #6893cf;
                
                  
            
            
            
            
            <span style="background-color&#58;#ffff00;">/* background-color&#58; #d6e8ff; */</span>
                
                  
            
            
            
            
            <span style="background-color&#58;#ffff00;">background-color&#58; #ffff00;</span>
                
                  
            
            
            
            
            <span style="background-color&#58;#ffff00;">padding&#58; 4px;</span>
                
                  
            
            
            
            
            <span style="background-color&#58;#ffff00;">/* background-repeat&#58; repeat-x;</span>
                
                  
            
            
            
            
            <span style="background-color&#58;#ffff00;">background-image&#58; url(/_imgs/app_back.gif);
                  */</span>
            &#125;
       </pre></div></dt><dd> Figure&#58; In C&#58;\Inetpub\wwwroot\_common\styles\global.css.aspx comment out and change the reference in yellow so the users know what server they are on</dd></dl><dl class="image"><dt> 
      <img alt="Color of CRM Development Server" src="/PublishingImages/CRM_DevelopmentColor.jpg" /> 
   </dt><dd>Figure&#58; Color of CRM Development Server - Red</dd></dl><dl class="image"><dt> 
      <img alt="Color of CRM Test Server" src="/PublishingImages/CRM_TestColor.jpg" /> 
   </dt><dd>Figure&#58; Color of CRM Test Server - Yellow</dd></dl><dl class="image"><dt> 
      <img alt="Color of CRM Test Server" src="/PublishingImages/CRM_ProductionColor.jpg" /> 
   </dt><dd> Figure&#58; Color of CRM Production Server - Default<br></dd></dl><h3>SharePoint online</h3><p>Regarding the color codes, we use to differentiate Production to Test with SharePoint online.</p><p>Here is what we change&#58;</p><ul><li>Site Settings | Change The Look
      <ul><li>Test – Orange 
            <dl class="image"><dt>
                  <img src="/PublishingImages/sharepoint-orange-theme.jpg" alt="sharepoint-orange-theme.jpg" style="width&#58;750px;" />
               </dt><dd>Figure&#58; Selecting Orange theme for test</dd></dl><dl class="image"><dt>
                  <img src="/PublishingImages/sharepoint-orange-applied.jpg" alt="sharepoint-orange-applied.jpg" />
               </dt><dd>Figure&#58; orange theme applied</dd></dl></li><li>Production - Office 
            <dl class="image"><dt>
                  <img src="/PublishingImages/sharepoint-office-theme.jpg" alt="sharepoint-orange-theme.jpg" style="width&#58;750px;" />
               </dt><dd>Figure&#58; Selecting Office theme for Production</dd></dl><dl class="image"><dt>
                  <img src="/PublishingImages/sharepoint-office-applied.jpg" alt="sharepoint-orange-applied.jpg" />
               </dt><dd>Figure&#58; office (blue) theme applied</dd></dl></li></ul></li></ul>


