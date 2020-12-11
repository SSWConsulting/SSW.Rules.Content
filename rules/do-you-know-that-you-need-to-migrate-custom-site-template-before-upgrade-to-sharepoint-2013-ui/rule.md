---
type: rule
archivedreason: 
title: Do you know that you need to migrate 'custom site template' before upgrade to SharePoint 2013 UI?
guid: f211a3b0-3339-4baf-87c8-a9e82f1352ae
uri: do-you-know-that-you-need-to-migrate-custom-site-template-before-upgrade-to-sharepoint-2013-ui
created: 2013-04-24T01:37:07.0000000Z
authors:
- id: 3
  title: Eric Phan
- id: 9
  title: William Yin
related: []

---


<p>If you have “custom site template” for  your site, you can’t upgrade your site to the SharePoint 2013 UI unless you have a site template with the same name ready for new UI.</p><p><img src="missingSiteTemplateError.jpg" alt="missingSiteTemplateError.jpg" style="margin:5px;width:593px;" /><br></p><p><span class="ssw-rteStyle-FigureNormal">Figure:SharePoint will show you an error “Missing Site Templates” that prevents you from upgrading</span><br></p>
<br><excerpt class='endintro'></excerpt><br>
<p>​To fix this issue</p><div><ol><li>Upgrade your site template’s <strong>content </strong>files and <strong>definition </strong>XML file to SharePoint 2013 (refer to SharePoint 2013 default site template for details).<br></li><li>Package the site template’s <strong>content </strong>files to map location “<strong>{SharePointRoot}\Template\SiteTemplate</strong>”.<br></li></ol></div><div><blockquote style="margin:0px 0px 0px 40px;border:none;padding:0px;"><div><img src="siteTemplateStructure.jpg" alt="siteTemplateStructure.jpg" style="margin:5px;" /> </div><div><span style="line-height:21px;">3</span><span style="line-height:21px;">.Package the site template’s <strong>definition </strong>XML file to map location “<strong>{SharePointRoot}\TEMPLATE\1033\XML</strong>”.</span><br></div></blockquote></div><p></p><blockquote style="margin:0px 0px 0px 40px;border:none;padding:0px;"><p><img src="siteTemplateDefinitionFile.jpg" alt="siteTemplateDefinitionFile.jpg" style="margin:5px;" /> </p><span style="line-height:1.6;">4.</span><span style="line-height:1.6;">Deploy the package.</span><br></blockquote><blockquote style="margin:0px 0px 0px 40px;border:none;padding:0px;"><div><span style="line-height:1.6;">5.</span><span style="line-height:1.6;">Try to upgrade to SharePoint 2013 UI again.</span><br></div><p><br></p></blockquote><p></p>


