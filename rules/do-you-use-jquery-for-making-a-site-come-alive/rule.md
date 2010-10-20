---
type: rule
archivedreason: 
title: Do you use jQuery for making a site come alive?
guid: 27612f09-8114-4b19-b7c3-66f172c94a15
uri: do-you-use-jquery-for-making-a-site-come-alive
created: 2009-08-25T00:13:02.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects: []

---


To please&#160;customers every business knows they need to keep their services and offerings fresh and up-to-date. The same is true for websites. In order to attract new traffic, we should make the website vivid. 

<br><excerpt class='endintro'></excerpt><br>

  <dl class="badImage">
    <dt><img alt="Bad example – there is no response when mouse is over the image" src="/PublishingImages/OldFashionSite.jpg" /> </dt>
    <dd>Figure&#58; Bad example – there is no response when mouse is over the image </dd>
</dl>
<dl class="goodImage">
    <dt><img alt="Good example – apply the different style when mouse is over" src="/PublishingImages/NewFashionSite.jpg" /> </dt>
    <dd>Figure&#58; Good example – apply the different style when mouse is over </dd>
</dl>
<dl class="goodCode">
    <dt>
    <pre>        
        $(&quot;p&quot;).hover(function () &#123;
            $(this).css(&#123; &quot;background-color&quot;&#58;&quot;yellow&quot;, &quot;font-weight&quot;&#58;&quot;bolder&quot; &#125;); &#125;,
            function () &#123; 
                var cssObj = &#123; &quot;background-color&quot;&#58; &quot;#ddd&quot;, 
                &quot;font-weight&quot;&#58; &quot;&quot;, 
                color&#58; &quot;rgb(0,40,244)&quot;
            &#125;
            $(this).css(cssObj);
        &#125;); 
    </pre>
    </dt>
    <dd>Figure&#58; Mouse hover sample </dd>
</dl>



