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
related: 
  - do-you-have-separate-development-testing-and-production-environments
redirects:
- do-you-identify-development-test-and-production-web-servers-by-colors

---

As per rule ["Do you have separate development, testing, and production environment?"](/do-you-have-separate-development-testing-and-production-environments), it's better to use different background colors to identify **Development**, **Test** and **Production** servers.

### CRM

![Figure: Staging uses blue background](ssw staging 2.png)  

![Figure: Production uses red background](ssw production 2.png)  

The way to change the default background color is to edit the CRM CSS files. These changes aren't supported and may be overwritten when CRM Rollups are applied.

### CRM 2015 and CRM 2016

Using theme feature to change the environment color.

![Figure: Changing CRM 2016 UI by using theme feature](CRM2015Theme.JPG)  

### CRM 2013

Edit `{{ CRM WEBSITE ROOT }}\_controls\navbar\navbar.css`:

``` css
.navigationControl
{
    background-color: #006600;
    margin: 0;
    z-index: 999;
    float: left;
    width: 100%;
    position: relative;
}
```

**Figure: Edit the background color to reflect the environment**

![Figure: CRM 2013 with a green navigation bar](crm2013\_greenbar.jpg)  

<!--endintro-->

### CRM 2011

Edit `{{ CRM WEBSITE ROOT }}\_static\css\1033\cui.css`, locate and modify the section ms-cui-tabBody so that it reads:

``` css
background-color : #ffffff;
```

Change color to a suitable color for the environment:

``` css
background-color : #bbffaa;
```

![Figure: CRM Ribbon color green to signify production environment](CRM2011_ColorCodedRibbon.jpg)

### CRM 4

Edit, `{{ CRM WEBSITE ROOT }}\_common\styles\global.css.aspx`

``` css
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

![Figure: Color of CRM Development Server - Red](CRM\_DevelopmentColor.jpg)  

![Figure: Color of CRM Test Server - Yellow](CRM\_TestColor.jpg)  

![Figure: Color of CRM Production Server - Default](CRM\_ProductionColor.jpg)  

### SharePoint online

Regarding the color codes, we use to differentiate Production to Test with SharePoint online.

Here is what we change:

* Site Settings | Change The Look
* Test – Orange

![Figure: Selecting Orange theme for test](sharepoint-orange-theme.jpg)  

![Figure: orange theme applied](sharepoint-orange-applied.jpg)  

### Production - Office

![Figure: Selecting Office theme for Production](sharepoint-office-theme.jpg)  

![Figure: office (blue) theme applied](sharepoint-office-applied.jpg)
