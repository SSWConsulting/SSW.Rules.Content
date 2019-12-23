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



<span class='intro'> <p>​U​sing DOM is fine, but manipulating DOM directly in your component is not.&#160;​With the introduction of Angular, there has been a big push in ensuring the DOM stays out of your JavaScript code.&#160; It is designed in such a way that an existing Angular application can be ported to another target by simply replacing the template and template loader.&#160; Projects such as&#160;<a href="http&#58;//angularjs.blogspot.com.au/2016/04/angular-2-react-native.html">Angular&#160;React Native Renderer</a>&#160;leverages this to allow native mobile app development in Angular.​​<br></p> </span>

<ul><li>Smaller component code making it easier to maintain</li><li>Faster running and easier to write unit tests</li><li>Easier for designers to get involved <br></li></ul><p>This means that the component's state must expose things that are useful to the template as public properties or fields, and the Angular should read these fields to draw itself.</p><dl class="badImage"><dt><img src="/PublishingImages/dom1.png" alt="dom1.png" /> </dt><dd>This component manipulates the DOM directly to show and hide the menu</dd></dl><dl class="goodImage"><dt><img src="/PublishingImages/dom2.png" alt="dom2.png" /></dt><dd>This component sets component state, which the template can use.&#160; It is simpler, more descriptive and easier to test</dd></dl>


