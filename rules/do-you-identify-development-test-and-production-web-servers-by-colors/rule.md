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



<span class='intro'>  <p>As per rule <a href="/Management/RulesToSuccessfulProjects/Pages/SeparateDevelopmentTestingAndProductionEnvironment.aspx"> &quot;Do you have separate development, testing and production environment?&quot;</a>, it's better to use different background colors to identify Development, Test and Production servers.</p><p>The way to change the default background color is to edit the CRM css files. These changes aren't supported and may be overwritten when CRM Rollups are applied.</p><h3 class="ssw15-rteElement-H3">CRM 2015 (Update 1)</h3><p>Using theme feature to change the environment color.</p><p><img src="/SoftwareDevelopment/RulesToBetterCRMForDevelopers/PublishingImages/CRM2015Theme.JPG" alt="CRM2015Theme.JPG" style="margin&#58;5px;" /><br><span class="ssw15-rteStyle-Caption">Figure&#58; Changing CRM UI by using theme</span></p><h3 class="ssw15-rteElement-H3">CRM 2013</h3><p>Edit&#58; <strong>&lt;CrmWebsiteRoot&gt;</strong><strong>\_controls\navbar\navbar.css</strong></p><p class="ssw15-rteElement-CodeArea">.navigationControl<br>&#123;<br><span style="background-color&#58;#ffff00;">background-color&#58; #006600;</span><br>margin&#58; 0;<br>z-index&#58; 999;<br>float&#58; left;<br>width&#58; 100%;<br>position&#58; relative;<br>&#125;</p><dd class="ssw15-rteElement-FigureNormal">&#160;Figure&#58; Edit the background color to reflect the environment</dd><p>&#160;<img alt="crm2013_greenbar.jpg" src="/SoftwareDevelopment/RulesToBetterCRMForDevelopers/PublishingImages/crm2013_greenbar.jpg" style="margin&#58;5px;width&#58;650px;" /></p><dd class="ssw15-rteElement-FigureNormal">&#160;Figure&#58; CRM 2013 with a green navigation bar&#160;&#160;&#160;&#160;&#160;&#160;&#160; </dd>

 </span>

<dl class="image"><dt><h3 class="ssw15-rteElement-H3">CRM 2011 </h3></dt><dt><p>Edit <strong>&lt;CrmWebsiteRoot&gt;\_static\css\1033\cui.css</strong>, locate and modify the section ms-cui-tabBody so that it reads&#58; </p><p><span class="ssw-rteStyle-CodeArea">background-color &#58; #ffffff;</span></p><p>Change&#160;color to&#160;a suitable color for the environment&#58;</p><p><span class="ssw-rteStyle-CodeArea">background-color &#58; #bbffaa;&#160;</span></p><p>&#160;<img src="/SoftwareDevelopment/RulesToBetterCRMForDevelopers/PublishingImages/CRM2011_ColorCodedRibbon.jpg" alt="" style="margin&#58;5px;" /></p><p><span class="ssw-rteStyle-FigureNormal">Figure&#58; CRM Ribbon color green to signify production environment</span></p></dt><dt></dt><dt><h3 class="ssw15-rteElement-H3">CRM 4 </h3></dt><dt><p>Edit,<strong> &lt;CrmWebsiteRoot&gt;\</strong><strong>_common\styles\global.css.aspx</strong></p></dt><dt><dl class="image"><dt><div class="greyBox"><pre>         body.stage
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
       </pre></div></dt><dd>          Figure&#58; In C&#58;\Inetpub\wwwroot\_common\styles\global.css.aspx comment out and change          the reference in yellow so the users know what server they are on</dd></dl></dt><dt><img alt="Color of CRM Development Server" src="/SoftwareDevelopment/RulesToBetterCRMForDevelopers/PublishingImages/CRM_DevelopmentColor.jpg" /></dt>
          <dd>
            Figure&#58; Color of CRM Development Server - Red</dd>
        </dl>
        <dl class="image">
          <dt>
            <img alt="Color of CRM Test Server" src="/SoftwareDevelopment/RulesToBetterCRMForDevelopers/PublishingImages/CRM_TestColor.jpg" /></dt>
          <dd>
            Figure&#58; Color of CRM Test Server - Yellow</dd>
        </dl>
        <dl class="image">
          <dt>
            <img alt="Color of CRM Test Server" src="/SoftwareDevelopment/RulesToBetterCRMForDevelopers/PublishingImages/CRM_ProductionColor.jpg" /></dt>
          <dd>
            Figure&#58; Color of CRM Production Server - Default</dd></dl><p><strong class="ssw-rteStyle-FigureNormal"></strong>&#160;</p><dl class="image">
        </dl>



