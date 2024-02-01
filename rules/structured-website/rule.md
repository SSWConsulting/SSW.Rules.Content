---
type: rule
archivedreason: 
title: Do you have a structured website?
guid: bc57c30a-d1d8-4796-883d-ae82d54338b5
uri: structured-website
created: 2016-08-03T18:48:19.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
- do-you-have-a-structured-website

---

The following structure allows you to keep your website clean of clutter:

<!--endintro-->

* **/Images** - for all static images
* **/Images/Dynamic** - for all images used in dynamically generated pages
  Note: The reason we recommend 2 images directories is so we can exclude images used by dynamically generated pages from our link checking program. This is so we can work out the **true** orphan images (they multiply quickly...like coat-hangers)
* **/Download** - [downloadable content](/centralize-downloadable-files), like PDFs and documents
* **/Includes** - for all include files
* **/Bin** - for mdb's, dll's and udl's
* **/Shop** - for the shopping basket and related pages
* **/Clients** - for the client login page and related pages
* **/Reports** - for any SQL Server Reporting Services
* **/zsMaintenance** - for the administration section to modify website settings
* **/zsValidate**  - for all web server status and validation checks

The root directory should be clean, having only:

* **default (.aspx, .asp, .htm)**
* **global.asa**
* **application.sln**
