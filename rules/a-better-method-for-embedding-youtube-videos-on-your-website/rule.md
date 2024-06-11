---
seoDescription: Learn a clever, lightweight way to embed YouTube videos and reduce your page size from 500kb to 15kb!
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

When you embed a YouTube video it will increase your page size from 500kbs to 1.5Mb or more, depending on how many videos are embedded on the page.

<!--endintro-->

![Figure: A side by side comparison – everyone wants less requests and a smaller page size](video-embed-load-time.png)

::: bad  
![Figure: Bad example - Don’t add embed code directly from YouTube. For more details read "A Better Method for Embedding YouTube Videos on your Website"](video-embed-bad.png)  
:::

```html
<iframe
  width="560"
  height="315"
  src="https://www.youtube.com/embed/eu0qhzevEXQ"
  frameborder="0"
  allowfullscreen
></iframe>
```

::: bad
Figure: Bad example – The evil HTML code  
:::

There is a clever, lightweight way to embed a YouTube video, which Google itself practices on their Google+ pages which reduce it to 15kbs.
All you have to do is, whenever you need to embed a video to a page, add the below tag instead of the YouTube video embed code. (Remember to replace VIDEO_ID with actual ID of the YouTube video)

```html
<div class="youtube-player" data-id="VIDEO_ID"></div>
```

::: good
Figure: Good example – The good HTML code  
:::

**Note:** This script needs to be added at the end of the document:

```html
<script>
  /* Light YouTube Embeds by @labnol */
  /* Web: http://labnol.org/?p=27941 */
  document.addEventListener("DOMContentLoaded", function () {
    var div,
      n,
      v = document.getElementsByClassName("youtube-player");
    for (n = 0; n < v.length; n++) {
      div = document.createElement("div");
      div.setAttribute("data-id", v[n].dataset.id);
      div.innerHTML = labnolThumb(v[n].dataset.id);
      div.onclick = labnolIframe;
      v[n].appendChild(div);
    }
  });
  function labnolThumb(id) {
    var thumb = '<img src="https://i.ytimg.com/vi/ID/hqdefault.jpg">',
      play = '<div class="play"></div>';
    return thumb.replace("ID", id) + play;
  }
  function labnolIframe() {
    var iframe = document.createElement("iframe");
    var embed = "https://www.youtube.com/embed/ID?autoplay=1";
    iframe.setAttribute("src", embed.replace("ID", this.dataset.id));
    iframe.setAttribute("frameborder", "0");
    iframe.setAttribute("allowfullscreen", "1");
    this.parentNode.replaceChild(iframe, this);
  }
</script>
```

..and this needs to be added in the CSS:

```html
<style>
  .youtube-player {
    position: relative;
    padding-bottom: 56.23%;
    /* Use 75% for 4:3 videos */
    height: 0;
    overflow: hidden;
    max-width: 100%;
    background: #000;
    margin: 5px;
  }
  .youtube-player iframe {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    z-index: 100;
    background: transparent;
  }
  .youtube-player img {
    bottom: 0;
    display: block;
    left: 0;
    margin: auto;
    max-width: 100%;
    width: 100%;
    position: absolute;
    right: 0;
    top: 0;
    border: none;
    height: auto;
    cursor: pointer;
    -webkit-transition: 0.4s all;
    -moz-transition: 0.4s all;
    transition: 0.4s all;
  }
  .youtube-player img:hover {
    -webkit-filter: brightness(75%);
  }
  .youtube-player .play {
    height: 72px;
    width: 72px;
    left: 50%;
    top: 50%;
    margin-left: -36px;
    margin-top: -36px;
    position: absolute;
    background: url("//i.imgur.com/TxzC70f.png") no-repeat;
    cursor: pointer;
  }
</style>
```
