---
type: rule
archivedreason: 
title: Do you identify Development, Test and Production Web Servers by colors?
guid: 9b723127-5c2d-4e40-a2a5-45ccd4840d2b
uri: do-you-identify-development-test-and-production-web-servers-by-colors
created: 2012-12-10T19:42:40.0000000Z
authors:
- id: 1
  title: Adam Cogan
- id: 69
  title: Jean Thirion
related: []

---

As per rule ["Do you have separate development, testing, and production environment?"](/_layouts/15/FIXUPREDIRECT.ASPX?WebId=3dfc0e07-e23a-4cbb-aac2-e778b71166a2&TermSetId=07da3ddf-0924-4cd2-a6d4-a4809ae20160&TermId=ae2ccef9-6cdc-4767-8e5a-e0e3dbf46fe2), it's better to use different background colors to identify Development, Test and Production servers.

### CRM 

<dl class="image">&lt;dt&gt;<img src="ssw staging 2.png" alt="crm staging.png" style="width:808px;">&lt;/dt&gt;<dd>Figure: Staging uses blue background</dd></dl><dl class="image">&lt;dt&gt; <img src="ssw production 2.png" alt="crm production.png" style="width:808px;">&lt;/dt&gt;<dd>Figure: Production uses red background </dd></dl>
The way to change the default background color is to edit the CRM CSS files. These changes aren't supported and may be overwritten when CRM Rollups are applied.

### CRM 2015 and CRM 2016


Using theme feature to change the environment color.
<dl class="image">&lt;dt&gt;<img src="CRM2015Theme.JPG" alt="CRM2015Theme.JPG">&lt;/dt&gt;<dd>Figure: Changing CRM 2016 UI by using theme feature<br></dd></dl>
### CRM 2013

Edit:   **\\_controls\navbar\navbar.css**

.navigationControl
{
background-color: #006600;
margin: 0;
z-index: 999;
float: left;
width: 100%;
position: relative;
}
 **Figure: Edit the background color to reflect the environment
** <dl class="image">&lt;dt&gt;<img alt="crm2013_greenbar.jpg" src="crm2013_greenbar.jpg" style="width:650px;">&lt;/dt&gt;<dd> Figure: CRM 2013 with a green navigation bar</dd></dl>
<!--endintro-->

### CRM 2011

Edit      **<crmwebsiteroot>\_static\css\1033\cui.css</crmwebsiteroot>** , locate and modify the section ms-cui-tabBody so that it reads:

background-color : #ffffff;

Change color to a suitable color for the environment:

background-color : #bbffaa;


![CRM Ribbon color green to signify production environment](CRM2011_ColorCodedRibbon.jpg)

### CRM 4

Edit, **<crmwebsiteroot>\</crmwebsiteroot>** **\_common\styles\global.css.aspx**
<dl class="image">&lt;dt&gt;<br><br>::: greybox<br><pre>         body.stage
            {
                <% if (CrmStyles.IsRightToLeft) { %>
                    dir:rtl;
                <%} %>
                border-top:1px solid #6893cf;

            <span style="background-color:#ffff00;">/* background-color: #d6e8ff; */</span>

            <span style="background-color:#ffff00;">background-color: #ffff00;</span>

            <span style="background-color:#ffff00;">padding: 4px;</span>
            
            <span style="background-color:#ffff00;">/* background-repeat: repeat-x;</span>
            
            <span style="background-color:#ffff00;">background-image: url(/_imgs/app_back.gif);
                  */</span>
            }
       </pre><br>:::<br><br>&lt;/dt&gt;<dd> Figure: In C:\Inetpub\wwwroot\_common\styles\global.css.aspx comment out and change the reference in yellow so the users know what server they are on</dd></dl><dl class="image">&lt;dt&gt;
      <img alt="Color of CRM Development Server" src="CRM_DevelopmentColor.jpg">
   &lt;/dt&gt;<dd>Figure: Color of CRM Development Server - Red</dd></dl><dl class="image">&lt;dt&gt;
      <img alt="Color of CRM Test Server" src="CRM_TestColor.jpg">
   &lt;/dt&gt;<dd>Figure: Color of CRM Test Server - Yellow</dd></dl><dl class="image">&lt;dt&gt;
      <img alt="Color of CRM Test Server" src="CRM_ProductionColor.jpg">
   &lt;/dt&gt;<dd> Figure: Color of CRM Production Server - Default<br></dd></dl>
### SharePoint online

Regarding the color codes, we use to differentiate Production to Test with SharePoint online.

Here is what we change:

* Site Settings | Change The Look
    * Test – Orange <br>            <dl class="image">&lt;dt&gt; 
                  <img src="sharepoint-orange-theme.jpg" alt="sharepoint-orange-theme.jpg" style="width:750px;"> 
               &lt;/dt&gt;<dd>Figure: Selecting Orange theme for test</dd></dl><dl class="image">&lt;dt&gt; 
                  <img src="sharepoint-orange-applied.jpg" alt="sharepoint-orange-applied.jpg"> 
               &lt;/dt&gt;<dd>Figure: orange theme applied</dd></dl>
    * Production - Office <br>            <dl class="image">&lt;dt&gt; 
                  <img src="sharepoint-office-theme.jpg" alt="sharepoint-orange-theme.jpg" style="width:750px;"> 
               &lt;/dt&gt;<dd>Figure: Selecting Office theme for Production</dd></dl><dl class="image">&lt;dt&gt; 
                  <img src="sharepoint-office-applied.jpg" alt="sharepoint-orange-applied.jpg"> 
               &lt;/dt&gt;<dd>Figure: office (blue) theme applied</dd></dl>
