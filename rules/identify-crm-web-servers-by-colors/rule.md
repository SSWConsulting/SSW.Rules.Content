---
type: rule
title: Do you identify Development, Test and Production web servers by colors?
seoDescription: Identify Development, Test, and Production Web Servers by colors
  to ensure a seamless transition between environments.
uri: identify-crm-web-servers-by-colors
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
  - title: Jean Thirion
    url: https://ssw.com.au/people/jean-thirion
related:
  - do-you-have-separate-development-testing-and-production-environments
redirects:
  - do-you-identify-development-test-and-production-web-servers-by-colors
  - do-you-identify-development-test-and-production-crm-web-servers-by-colors
created: 2012-12-10T19:42:40.000Z
archivedreason: null
guid: 9b723127-5c2d-4e40-a2a5-45ccd4840d2b
---
![]()

As per rule ["Do you have separate development, testing, and production environment?"](/do-you-have-separate-development-testing-and-production-environments), it's better to use different background colors to identify **Development**, **Test** and **Production** servers.

### CRM

![Figure: Staging uses blue background](ssw staging 2.png)

![Figure: Production uses red background](ssw production 2.png)

The way to change the default background color is to edit the CRM CSS files. These changes aren't supported and may be overwritten when CRM Rollups are applied.

### CRM 2015 and CRM 2016

Using theme feature to change the environment color.

![Figure: Changing CRM 2016 UI by using theme feature](CRM2015Theme.jpg)

### CRM 2013

Edit `{{ CRM WEBSITE ROOT }}\_controls\navbar\navbar.css`:

```css
.navigationControl {
  background-color: #006600;
  margin: 0;
  z-index: 999;
  float: left;
  width: 100%;
  position: relative;
}
```

**Figure: Edit the background color to reflect the environment**

![Figure: CRM 2013 with a green navigation bar](crm2013_greenbar.jpg)

<!--endintro-->

### CRM 2011

Edit `{{ CRM WEBSITE ROOT }}\_static\css\1033\cui.css`, locate and modify the section ms-cui-tabBody so that it reads:

```css
background-color: #ffffff;
```

Change color to a suitable color for the environment:

```css
background-color: #bbffaa;
```

![Figure: CRM Ribbon color green to signify production environment](CRM2011_ColorCodedRibbon.jpg)

### CRM 4

Edit, `{{ CRM WEBSITE ROOT }}\_common\styles\global.css.aspx`

```css
body.stage
{
    <% if (CrmStyles.IsRightToLeft) { %>
        dir:rtl;
    <%} %>
    border-top:1px solid #6893cf;

    /* background-color: #d6e8ff; */

    background-color: #ffff00;

    padding: 4px;

    /* background-repeat: repeat-x;

    background-image: url(/_imgs/app_back.gif);
    */
}
```

**Figure: In `C:\Inetpub\wwwroot\\_common\styles\global.css.aspx` comment out and change the reference in yellow so the users know what server they are on**

![Figure: Color of CRM Development Server - Red](CRM_DevelopmentColor.jpg)

![Figure: Color of CRM Test Server - Yellow](CRM_TestColor.jpg)

![Figure: Color of CRM Production Server - Default](CRM_ProductionColor.jpg)

### SharePoint Online

In SharePoint Online, we use Theme colours to differentiate between Production and Development environments.

To change the Theme, simply navigate to Site Settings | Change The Look | Theme

![](2024-09-16_18-10-35.jpg "Figure: To change the theme, navigate to Settings | Change the look | Theme")

### Development - Default Microsoft Blue Theme

![](2024-09-16_18-03-50.jpg "Figure: Selecting Blue default theme for Development")

### Production - SSW Custom Theme

![Figure: Selecting Red SSW Custom theme for Production ](2024-09-16_18-06-09.jpg)

More about SharePoint Online custom themes: https://learn.microsoft.com/en-us/sharepoint/dev/general-development/how-to-deploy-a-custom-theme-in-sharepoint?WT.mc_id=M365-MVP-33518
