---
type: rule
title: Tools - Do you know the best tools to debug JavaScript?
uri: tools---do-you-know-the-best-tools-to-debug-javascript
created: 2016-11-29T19:58:36.0000000Z
authors:
- id: 1
  title: Adam Cogan
- id: 44
  title: Duncan Hunter

---



<span class='intro'> ​Debugging JavaScript application can be difficult. Having to console.log results can make for a slow and cumbersome development experience. There are five ways you can debug a JavaScript application without leaning on console.log() as your main tool.​<br> </span>

<h3 class="ssw15-rteElement-H3">Options for Debugging JavaScript applications<br></h3><ol><li><p><b>Debug your JavaScript using console.log()<br></b> While this is a valid approach it should only be utilized for the simplest of manual debugging tests as they are slow, you have to re-run the app every time, do not allow you to change state mid-flight and developers sometimes forget to clean up after themselves and the code becomes riddled&#160;with console.log statements.</p><dl class="badImage"><dt> <img src="/PublishingImages/debug-js-1.png" alt="debug-js-1.png" /> </dt><dd>Bad code - Using console.log() to debug your JavaScript <br><br></dd></dl></li><li>
      <b>Debug&#160;in the browser with a breakpoint<br></b> <a href="https&#58;//developer.chrome.com/devtools#debugging-javascript" target="_blank">Chrome </a> is by far the most popular browser for the average web developer followed by FireFox, but all the major browsers have a debugging tool. <dl class="image"><dt> <img src="/PublishingImages/debug-js-2.png" alt="debug-js-2.png" /> </dt><dd>Figure&#58; Old school JavaScript debugging with Chrome Dev Tools is still the best and most versatile tool</dd></dl></li><li>
      <b>Debug in an IDE</b><br>It is often more effort than it is worth to debug JavaScrtipt in your IDE and it is still not very popular. If your app is a Server Side NodeJS JavaScript app then it is very different&#160;since this type of JavaScript app does not run in the browser and this is what the IDE is designed for.&#160;<br> 
      <ul><li>
            <a href="https&#58;//github.com/Microsoft/vscode-chrome-debug" target="_blank">Visual Studio Code Chome Debugger<b></b> </a> - Painful to set up source maps for advanced&#160;JavaScript applications that run in memory dev servers like WebPack Dev Server.<br></li><li>Visual Studio 2015<b></b> - Only works with TypeScript in Internet Explorer <br></li></ul><dl class="image"><dt> <img src="/PublishingImages/debug-js-3.png" alt="debug-js-3.png" /> </dt><dd>Figure&#58; Visual Studio Chrome Debugger with breakpoint set</dd></dl></li><li>
      <b>Time Travel Debugging with Redux</b><br>Using tools like <a href="https&#58;//github.com/ngrx/store-devtools" target="_blank"> <span> ngrx's</span>&#160;store dev tools </a>. You can traverse back and forth between states with excellent UI tools. Debugging through your states is much better than just debugging the current state but also to be able to see the actions triggered to change state. <dl class="image"><dt> <img src="/PublishingImages/debug-js-4.png" alt="debug-js-4.png" /> </dt><dd>Figure&#58; Example of redux based time travel debugging</dd></dl></li><li>
      <b>Hot Module Reloading<br></b>The problem with the above approaches is every time you make a change to your code you need to reload the website and navigate back to the page and state of that page again and again to repeat your manual test.&#160;Hot Module Replacement (HMR) exchanges, adds, or removes modules while an application is running&#160;without&#160;a page reload.<br>​<ul><li><a href="https&#58;//webpack.github.io/docs/hot-module-replacement-with-webpack.html" target="_blank">WebPack Hot Module Reloader</a> <br></li></ul><dl class="image"><dt> <img src="/PublishingImages/debug-js-5.png" alt="debug-js-5.png" /> </dt><dd>Figure&#58; Hot module reloader documentation from WebPack website</dd></dl></li></ol>


