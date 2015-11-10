---
type: rule
title: Do you keep your files under the Google file size limit?
uri: do-you-keep-your-files-under-the-google-file-size-limit
created: 2015-11-10T19:57:28.0000000Z
authors:
- id: 1
  title: Adam Cogan

---



<span class='intro'> <p>As per Google on&#160;<a href="https&#58;//developers.google.com/webmasters/control-crawl-index/docs/robots_txt?hl=en">Robots.txt Specifications</a>&#58;</p><p class="ssw15-rteElement-Reference">A maximum file size may be enforced per crawler. Content which is after the maximum file size may be ignored. Google currently enforces a size limit of 500kb.​</p> </span>

<p>Regarding other files&#58;</p><ul><li>All files larger than 30MB will be completely ignored.</li><li>HTML, the search appliance indexes up to 2.5MB of the document, caches it, and discards the rest.</li><li>A non-HTML format, the search appliance&#58;</li></ul><span style="line-height&#58;1.6;"><ol><li><span style="line-height&#58;1.6;">Downloads the non-HTML file.</span><br></li><li><span style="line-height&#58;1.6;">Converts the non-HTML file to HTML.</span><br></li><li><span style="line-height&#58;1.6;">If the converted content is less than 4,000,000 bytes, indexes the first 2MB of the HTML file. (Take note that 4MB=4,194,304 bytes.) If the converted content exceeds 4,000,000 bytes, the document is not indexed. However, the document and a link to it do appear in search results.</span></li><li><span style="line-height&#58;1.6;">Caches the first 2MB of the HTML file.</span></li><li><span style="line-height&#58;1.6;">Discards the rest of the HTML file and the non-HTML file.​</span></li></ol></span>


