---
type: rule
archivedreason: 
title: Do you place scripts at the bottom of your page?
guid: a106c991-09fc-4e64-89cf-61c27685fc70
uri: do-you-place-scripts-at-the-bottom-of-your-page
created: 2012-07-24T18:10:46.0000000Z
authors:
- title: Tiago Araujo
  url: https://ssw.com.au/people/tiago-araujo
related: []
redirects: []

---

Bear in mind that the load time is a very important aspect on web development. The goal is to make the page load as quickly as possible for the user.  

<!--endintro-->

It's known that when a browser loads a script, it can’t continue on until the entire file has been loaded.

Once JavaScript files have the purpose to add functionality - something happen after a button is clicked for example — there is no good reason to load the JS file before the button itself.

So go ahead and place JS files at the bottom of the HTML, just before the closing body tag.

```
...
<script type="text/javascript" src="file.js"></script> 
  </body>
    </html>
```
**Figure: Place JavaScript at the bottom of your HTML**

Tests at a big online sales company revealed that every 100 ms increase in load time decreased sales by 1%.
