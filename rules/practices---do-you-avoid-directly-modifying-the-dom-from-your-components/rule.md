---
type: rule
title: Practices - Do you avoid directly modifying the DOM from your components?
uri: practices---do-you-avoid-directly-modifying-the-dom-from-your-components
created: 2016-04-22T22:18:30.0000000Z
authors:
- id: 55
  title: Steve Leigh
- id: 72
  title: Gabriel George

---



<span class='intro'> <p>With the introduction of Angular2, there has been a big push in ensuring the DOM stays out of your JavaScript code.&#160; It is designed in such a way that an existing angular2 application can be ported to another target by simple replacing the template and template loader.&#160; Projects such as&#160;<a href="http&#58;//angularjs.blogspot.com.au/2016/04/angular-2-react-native.html" target="_blank">Angular2 React Native Renderer​</a>&#160;leverages this to allow native mobile app development in Angular2.&#160;</p><p>For this to work well, there has to be a clear separation between the component’s logic and the component’s view – which means avoiding using the DOM in your component’s code.&#160; This gives a few further advantages&#58;<br></p> </span>

<ul><li>Smaller component code making it easier to maintain</li><li>Faster running and easier to write unit tests</li><li>Easier for designers to get involved​</li></ul><p>This means that the component's state must expose things that are useful to the template as public properties or fields, and the template should read these fields to draw itself.​</p><dl class="badImage"><dt><img src="/PublishingImages/dom1.png" alt="dom1.png" />​</dt><dd>This component manipulates the DOM directly to show and hide the menu</dd></dl><dl class="goodImage"><dt><img src="/PublishingImages/dom2.png" alt="dom2.png" /></dt><dd>This component sets component state, which the template can use.&#160; It is simpler, more descriptive and easier to test</dd></dl>


