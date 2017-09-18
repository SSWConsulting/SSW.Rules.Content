---
type: rule
title: Do you know the right way to embed a YouTube video?
uri: do-you-know-the-right-way-to-embed-a-youtube-video
created: 2017-09-11T01:29:34.0000000Z
authors:
- id: 51
  title: Farrukh Khan
- id: 60
  title: Anthony Nguyen

---



<span class='intro'> When you embed a YouTube video it will increase your page size from 500kbs to 1.5Mb or more, depending on how many videos are embedded on the page.<br><br> </span>

<dl class="image"><dt> <img src="/PublishingImages/video-embed-load-time.png" alt="video-embed-load-time.png" /> </dt><dd>Figure&#58; A side by side comparison – everyone wants less requests and a smaller page size</dd></dl><dl class="badImage"><dt><img src="/PublishingImages/video-embed-bad.png" alt="video-embed-bad.png" /> </dt> <dd>Figure&#58; Bad example - Don’t add embed code directly from YouTube. For more details https&#58;//www.labnol.org/internet/light-youtube-embeds/27941/&#160;</dd></dl><p class="ssw15-rteElement-CodeArea">&lt;iframe width=&quot;560&quot; height=&quot;315&quot; src=&quot;https&#58;//www.youtube.com/embed/eu0qhzevEXQ&quot; frameborder=&quot;0&quot; allowfullscreen&gt;&lt;/iframe&gt;</p><dd class="ssw15-rteElement-FigureBad">Figure&#58; Bad example – The evil HTML code</dd> ​<br>There is a clever, lightweight way to embed a YouTube video, which Google itself practices on their Google+ pages which reduce it to 15kbs.<br>All you have to do is, whenever you need to embed a video to a page, add the below tag instead of the YouTube video embed code. (Remember to replace VIDEO_ID with actual ID of the YouTube video)<br><p class="ssw15-rteElement-CodeArea">&lt;div class=&quot;youtube-player&quot; data-id=&quot;VIDEO_ID&quot;&gt;&lt;/div&gt;</p><dd class="ssw15-rteElement-FigureGood">Figure&#58; Good example – The good HTML code</dd><br> 
<p></p>


