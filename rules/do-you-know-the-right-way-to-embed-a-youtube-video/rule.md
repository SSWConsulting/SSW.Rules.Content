---
type: rule
archivedreason: 
title: Do you know the right way to embed a YouTube video?
guid: 9e18b84f-5af2-4a25-9d14-9135a3930171
uri: do-you-know-the-right-way-to-embed-a-youtube-video
created: 2017-09-11T01:29:34.0000000Z
authors:
- id: 51
  title: Farrukh Khan
- id: 60
  title: Anthony Nguyen
related: []

---

When you embed a YouTube video it will increase your page size from 500kbs to 1.5Mb or more, depending on how many videos are embedded on the page.


<!--endintro-->
<dl class="image">&lt;dt&gt; <img src="video-embed-load-time.png" alt="video-embed-load-time.png"> &lt;/dt&gt;<dd>Figure: A side by side comparison – everyone wants less requests and a smaller page size</dd></dl><dl class="badImage">&lt;dt&gt;<img src="video-embed-bad.png" alt="video-embed-bad.png"> &lt;/dt&gt; <dd>Figure: Bad example - Don’t add embed code directly from YouTube. For more details <a href="https://www.labnol.org/internet/light-youtube-embeds/27941/">read "A Better Method for Embedding YouTube Videos on your Website" </a></dd></dl>
`youtube: https://www.youtube.com/embed/eu0qhzevEXQ`


::: bad
Figure: Bad example – The evil HTML code
:::

 
There is a clever, lightweight way to embed a YouTube video, which Google itself practices on their Google+ pages which reduce it to 15kbs.
All you have to do is, whenever you need to embed a video to a page, add the below tag instead of the YouTube video embed code. (Remember to replace VIDEO\_ID with actual ID of the YouTube video)






::: good
Figure: Good example – The good HTML code
:::



**Note:** This script needs to be added at the end of the document:

<script><br>/* Light YouTube Embeds by @labnol */<br>/* Web: http://labnol.org/?p=27941 */<br>document.addEventListener("DOMContentLoaded",<br>function() {<br>var div, n,<br>v = document.getElementsByClassName("youtube-player");<br>for (n = 0; n < v.length; n++) {<br>div = document.createElement("div");<br>div.setAttribute("data-id", v[n].dataset.id);<br>div.innerHTML = labnolThumb(v[n].dataset.id);<br>div.onclick = labnolIframe;<br>v[n].appendChild(div);<br>}<br>});<br>function labnolThumb(id) {<br>var thumb = '<img src="https://i.ytimg.com/vi/ID/hqdefault.jpg">',<br>play = '<div class="play"></div>';<br>return thumb.replace("ID", id) + play;<br>}<br>function labnolIframe() {<br>var iframe = document.createElement("iframe");<br>var embed = "https://www.youtube.com/embed/ID?autoplay=1";<br>iframe.setAttribute("src", embed.replace("ID", this.dataset.id));<br>iframe.setAttribute("frameborder", "0");<br>iframe.setAttribute("allowfullscreen", "1");<br>this.parentNode.replaceChild(iframe, this);<br>}<br></script>

..and this needs to be added in the CSS:
