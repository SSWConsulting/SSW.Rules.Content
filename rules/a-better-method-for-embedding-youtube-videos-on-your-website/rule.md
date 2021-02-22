---
type: rule
archivedreason: 
title: Do you know the right way to embed a YouTube video?
guid: 9e18b84f-5af2-4a25-9d14-9135a3930171
uri: a-better-method-for-embedding-youtube-videos-on-your-website
created: 2017-09-11T01:29:34.0000000Z
authors:
- title: Farrukh Khan
  url: https://ssw.com.au/people/farrukh-khan
- title: Anthony Nguyen
  url: https://ssw.com.au/people/anthony-nguyen
related: []
redirects:
- do-you-know-the-right-way-to-embed-a-youtube-video

---


When you embed a YouTube video it will increase your page size from 500kbs to 1.5Mb or more, depending on how many videos are embedded on the page.<br><br>
<br><excerpt class='endintro'></excerpt><br>
<dl class="image"><dt> <img src="video-embed-load-time.png" alt="video-embed-load-time.png" /> </dt><dd>Figure: A side by side comparison – everyone wants less requests and a smaller page size</dd></dl><dl class="badImage"><dt><img src="video-embed-bad.png" alt="video-embed-bad.png" /> </dt> <dd>Figure: Bad example - Don’t add embed code directly from YouTube. For more details <a href="https://www.labnol.org/internet/light-youtube-embeds/27941/">read "A Better Method for Embedding YouTube Videos on your Website" </a></dd></dl><p class="ssw15-rteElement-CodeArea">&lt;iframe width="560" height="315" src="https://www.youtube.com/embed/eu0qhzevEXQ" frameborder="0" allowfullscreen&gt;&lt;/iframe&gt;</p><dd class="ssw15-rteElement-FigureBad">Figure: Bad example – The evil HTML code</dd> <br>There is a clever, lightweight way to embed a YouTube video, which Google itself practices on their Google+ pages which reduce it to 15kbs.<br>All you have to do is, whenever you need to embed a video to a page, add the below tag instead of the YouTube video embed code. (Remember to replace VIDEO_ID with actual ID of the YouTube video)<br><p class="ssw15-rteElement-CodeArea">&lt;div class="youtube-player" data-id="VIDEO_ID"&gt;&lt;/div&gt;</p><dd class="ssw15-rteElement-FigureGood">Figure: Good example – The good HTML code</dd><br> 
<p><strong>Note: </strong>This script needs to be added at the end of the document: <br></p><p class="ssw15-rteElement-CodeArea">&lt;script&gt;<br>/* Light YouTube Embeds by @labnol */<br>/* Web: http://labnol.org/?p=27941 */<br>document.addEventListener("DOMContentLoaded",<br>function() {<br>var div, n,<br>v = document.getElementsByClassName("youtube-player");<br>for (n = 0; n &lt; v.length; n++) {<br>div = document.createElement("div");<br>div.setAttribute("data-id", v[n].dataset.id);<br>div.innerHTML = labnolThumb(v[n].dataset.id);<br>div.onclick = labnolIframe;<br>v[n].appendChild(div);<br>}<br>});<br>function labnolThumb(id) {<br>var thumb = '&lt;img src="https://i.ytimg.com/vi/ID/hqdefault.jpg"&gt;',<br>play = '&lt;div class="play"&gt;&lt;/div&gt;';<br>return thumb.replace("ID", id) + play;<br>}<br>function labnolIframe() {<br>var iframe = document.createElement("iframe");<br>var embed = "https://www.youtube.com/embed/ID?autoplay=1";<br>iframe.setAttribute("src", embed.replace("ID", this.dataset.id));<br>iframe.setAttribute("frameborder", "0");<br>iframe.setAttribute("allowfullscreen", "1");<br>this.parentNode.replaceChild(iframe, this);<br>}<br>&lt;/script&gt;​<br></p><p>..and this needs to be added in the CSS: <br></p><p class="ssw15-rteElement-CodeArea">&lt;style&gt;<br>.youtube-player {<br>position: relative;<br>padding-bottom: 56.23%;<br>/* Use 75% for 4:3 videos */<br>height: 0;<br>overflow: hidden;<br>max-width: 100%;<br>background: #000;<br>margin: 5px;<br>}<br>.youtube-player iframe {<br>position: absolute;<br>top: 0;<br>left: 0;<br>width: 100%;<br>height: 100%;<br>z-index: 100;<br>background: transparent;<br>}<br>.youtube-player img {<br>bottom: 0;<br>display: block;<br>left: 0;<br>margin: auto;<br>max-width: 100%;<br>width: 100%;<br>position: absolute;<br>right: 0;<br>top: 0;<br>border: none;<br>height: auto;<br>cursor: pointer;<br>-webkit-transition: .4s all;<br>-moz-transition: .4s all;<br>transition: .4s all;<br>}<br>.youtube-player img:hover {<br>-webkit-filter: brightness(75%);<br>}<br>.youtube-player .play {<br>height: 72px;<br>width: 72px;<br>left: 50%;<br>top: 50%;<br>margin-left: -36px;<br>margin-top: -36px;<br>position: absolute;<br>background: url("//i.imgur.com/TxzC70f.png") no-repeat;<br>cursor: pointer;<br>}<br>&lt;/style&gt;</p><p>​<br></p>


