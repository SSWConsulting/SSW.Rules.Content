---
type: rule
archivedreason: 
title: Do you know to create a Custom Library Provider?
guid: caefbc5c-6d48-421b-ba07-c8424ede2604
uri: do-you-know-to-create-a-custom-library-provider
created: 2013-04-10T21:24:21.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects: []

---

If you need to create a custom CDN library provider... Sitefinity manages images, videos, and content on a file system which the website uses. For larger sites, CDN providers are used for all content that doesn’t need to be on the servers.

<!--endintro-->

Make a new class that inherits from **Telerik.Sitefinity.Modules.Libraries.BlobStorage.CloudBlobStorageProvider** and override all the methods.

You want to save the items to a local path but show an external URL on the actual page.

Once you have made your class then you need to register it in Sitefinity, open the config file “App\_Data\Sitefinity\Configuration\LibrariesConfig.config” in notepad and register your Class

```xml
<?xml version="1.0" encoding="utf-8"?>
    <librariesConfig xmlns:config="urn:telerik:sitefinity:configuration" xmlns:type="urn:telerik:sitefinity:configuration:type" config:version="5.1.3270.0">
        <blobStorage defaultProvider="CDN">
     <providers>
  <remove name="FileSystem" />
  <add type="SSW.Sitefinity.Modules.Libraries.BlobStorage.CdnBlobStorageProvider" enabled="True" name="CDN" />
     </providers>
 </blobStorage>
    </librariesConfig>
```
