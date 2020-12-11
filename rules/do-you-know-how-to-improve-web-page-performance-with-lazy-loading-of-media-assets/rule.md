---
type: rule
archivedreason: 
title: Do you know how to improve web page performance with lazy loading of media assets?
guid: 3b77adac-4387-4ba1-8ece-0e4a32e75458
uri: do-you-know-how-to-improve-web-page-performance-with-lazy-loading-of-media-assets
created: 2019-06-21T22:41:38.0000000Z
authors:
- id: 9
  title: William Yin
related: []

---

If you are dealing with Content Management System (CMS), you are likely to play with pages with large amount of images and embedded videos. To improve the performance of those pages, and save bandwidth for the readers, loading content asynchronously (also called “lazy loading”) is recommended.

It means the browsers will only load images and embedded videos in the visible area by default, then load the rest images and videos while users are scrolling down to them.

<!--endintro-->

On our rules web site, one of the pages’ initial loading size of images reduced from 4.8MB to 500KB after being applied “lazy loading” of images:
<dl class="badImage">&lt;dt&gt;
      <img src="load-images-1.jpg" alt="load-images-1.jpg" style="width:750px;height:231px;">
   &lt;/dt&gt;<dd>Figure: Bad Example - load all images by default</dd></dl><dl class="goodImage">&lt;dt&gt;
         <img src="load-images-2.jpg" alt="load-images-2.jpg" style="width:750px;height:224px;">
      &lt;/dt&gt;<dd>Figure: Good Example - Do not load all images by default, only load them when they are visible while scrolling down the browsers</dd></dl>The page's initial loading size of JS scripts reduced from 2.3MB to 518KB after being applied “lazy loading” of embedded YouTube videos:<dl class="badImage">&lt;dt&gt;
            <img src="load-images-3.jpg" alt="load-images-3.jpg" style="width:750px;height:374px;">
         &lt;/dt&gt;<dd>Figure: Bad Example – load all embedded YouTube videos by default</dd></dl><dl class="goodImage">&lt;dt&gt;
            <img src="load-images-4.jpg" alt="load-images-4.jpg" style="width:750px;height:437px;">
         &lt;/dt&gt;<dd>Figure: Good Example - Do not load all embedded YouTube videos by default, only load them when they are visible while scrolling down the browsers</dd></dl>
To implement lazy loading for image:

1.	Check if the browser supports IntersectionObserver, if the browser supports IntersectionObserver, we will only load images and videos in the areas are visible to users by default. If the browser doesn’t support it, we will have to load all images and embedded videos on the page immediately after the page is loaded.

if (!('IntersectionObserver' in window)) {
    console.log("No Intersection");
} else {
               console.log("Support intersection");
}

**Note:** You can use a polyfill library to add  **IntersectionObserver** support to older browsers.

2.	If the browser supports IntersectionObserver, in your page html, change the “src” of “
![]()” to “data-src”
From


![]()<mark>src</mark>="https://rules.ssw.com.au/PublishingImages/flight.jpg">

to


![]()<mark>data-src</mark>="https://rules.ssw.com.au/PublishingImages/flight.jpg">

3.	Use the below Javascript to change “data-src” back to “src” for the 
![]() html objects, which become visible, so that those images will be loaded

function onIntersection(entries) {
  // Loop through the entries
  entries.forEach(entry => {
    // Are we in viewport?
    if (entry.intersectionRatio > 0) {


      // Stop watching and load the image
      observer.unobserve(entry.target);
                 //console.log(entry);
                 //console.log(entry.target);          
      preloadImage(entry.target);
    }
  });
}
function preloadImage(target){
console.log(target);
if (target.getAttribute('<mark>data-src</mark>')) {
            target.setAttribute('<mark>src</mark>', target.getAttribute('data-src'));
        } 
}

// Get images of class lazy

const images = document.querySelectorAll('.sswRuleSummaryUCDiv img');
const config = {
  // If image gets within 50px go get it
  rootMargin: '50px 0px',
  threshold: 0.01
};

let observer = new IntersectionObserver(onIntersection, config);
 
  images.forEach(image => {
    observer.observe(image);
  });

4.	More details can be found at           https://www.hanselman.com/blog/UpdatingJQuerybasedLazyImageLoadingToIntersectionObserver.aspx

To implement lazy loading for embedded YouTube videos:

1.	Use the same code as lazy loading images above, to check if IntersectionObserver is supported by browsers.
2.	In your page html code, convert “
`youtube: https://www.youtube.com/embed/OhVYTOKCsWI`

To

<!-- (1) video wrapper in div instead of iframe -->


<!-- (2) the "play" button -->






3.   Use the below code to convert “

” to “<iframe>” to load the embedded videos when they are visible while scrolling down:<p class="ssw15-rteElement-CodeArea">var youtube = document.querySelectorAll( "div[data-iframesrc]" );<br>          for (var i = 0; i < youtube.length; i++) {<br>        <br>        var source = "https://img.youtube.com/vi/"+ youtube[i].dataset.<mark>iframecode</mark> +"/sddefault.jpg";<br>        <br>        var image = new Image();<br>                image.src = source;<br>                image.addEventListener( "load", function() {<br>                    youtube[ i ].appendChild( image );<br>                }( i ) );<br>        <br>                youtube[i].addEventListener( "click", function() {<br><br><br>                    var iframe = document.createElement( "iframe" );<br><br><br>                            iframe.setAttribute( "frameborder", "0" );<br>                            iframe.setAttribute( "allowfullscreen", "" );<br>                            iframe.setAttribute( "width", this.dataset.<mark>iframewidth</mark> );<br>                            iframe.setAttribute( "height", this.dataset.<mark>iframeheight</mark> );<br>                            iframe.setAttribute( "src", this.dataset.<mark>iframesrc</mark> +"?rel=0&showinfo=0&autoplay=1" );<br>                            this.innerHTML = "";<br>                            this.appendChild( iframe );<br>                } );    <br>    };<br><br></p><p> 
         <br>4.	 <b></b> More details can be found at 
         <a href="https://webdesign.tutsplus.com/tutorials/how-to-lazy-load-embedded-youtube-videos--cms-26743">https://webdesign.tutsplus.com/tutorials/how-to-lazy-load-embedded-youtube-videos--cms-26743 </a><br></p>
</iframe>
