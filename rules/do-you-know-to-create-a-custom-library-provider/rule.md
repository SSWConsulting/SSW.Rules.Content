---
type: rule
title: Do you know to create a Custom Library Provider?
uri: do-you-know-to-create-a-custom-library-provider
created: 2013-04-10T21:24:21.0000000Z
authors:
- id: 1
  title: Adam Cogan

---



<span class='intro'> <p>We have needed to create a custom CDN library provider.</p><p>Sitefinity manages images, videos, and content on a file system which the website uses.<br>
                        For larger sites, CDN providers are used for all content that doesn’t need to be on the servers.</p> </span>

<p>Make a new class that inherits from Telerik.Sitefinity.Modules.Libraries.BlobStorage.CloudBlobStorageProvider and override all the methods.<br> You want to save the items to a local path but show an external URL on the actual page.</p><p>Once you have made your class then you need to register it in Sitefinity.<br> Open the config file “App_Data\Sitefinity\Configuration\LibrariesConfig.config” in notepad and register your Class</p><div class="greyBox"><pre>    &lt;?xml version=&quot;1.0&quot; encoding=&quot;utf-8&quot;?&gt;
    &lt;librariesConfig xmlns&#58;config=&quot;urn&#58;telerik&#58;sitefinity&#58;configuration&quot; xmlns&#58;type=&quot;urn&#58;telerik&#58;sitefinity&#58;configuration&#58;type&quot; config&#58;version=&quot;5.1.3270.0&quot;&gt;
        &lt;blobStorage defaultProvider=&quot;CDN&quot;&gt;
     &lt;providers&gt;
  &lt;remove name=&quot;FileSystem&quot; /&gt;
  &lt;add type=&quot;SSW.Sitefinity.Modules.Libraries.BlobStorage.CdnBlobStorageProvider&quot; enabled=&quot;True&quot; name=&quot;CDN&quot; /&gt;
     &lt;/providers&gt;
 &lt;/blobStorage&gt;
    &lt;/librariesConfig&gt;

</pre></div>


