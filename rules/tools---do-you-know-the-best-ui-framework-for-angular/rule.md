---
type: rule
title: Tools - Do you know the best UI framework for Angular?
uri: tools---do-you-know-the-best-ui-framework-for-angular
created: 2016-08-02T14:52:08.0000000Z
authors:
- id: 24
  title: Adam Stephensen
- id: 1
  title: Adam Cogan
- id: 34
  title: Brendan Richards

---



<span class='intro'> <p></p><p>The main contenders for the best UI framework for Angular are&#58;<br></p><ul><li><b>Angular Material</b> - <a href="https&#58;//material.angular.io/">https&#58;//material.angular.io/</a>&#160;</li><li><b>Bootstrap</b> - <a href="https&#58;//getbootstrap.com/">https&#58;//getbootstrap.com</a><br></li></ul><p>Making the choice of which to use will depend on several factors related to your project&#58;</p><ol><li>The look and feel of the site that your client is seeking</li><li>The range of components that will be required in the application</li><li>The developers' familiarity with the framework</li><li>The designers' familiarity with theming in the framework​<br><br></li></ol> </span>

<h3 class="ssw15-rteElement-H3">Angular Material</h3><p>Angular Material has a very specific design metaphor, and if the look and feel is one that your client likes, then consider using it. But if the Material metaphor doesn't match the rest of the client's applications, then it may not be a good choice.</p><dl class="image"><dt> 
      <img src="/PublishingImages/angular-material.png" alt="angular-material.png" style="width&#58;650px;" /> 
   </dt><dd>Figure&#58; &#160;Angular Material is built by the Angular team</dd></dl><p>The components available in Angular Material are solid, but it doesn't have the range of components that are available in Bootstrap. It is actively being developed though, and new, exciting components are being added regularly. For example, an infinite scroll component was added in October 2018. 
   <br></p><p>Angular Material uses Angular components for its widgets. This means that the HTML rendered in the browser will include directives, divs, and classes that are not present in the component template HTML. It is for this reason that Designers without a good understanding of Angular may have difficulties tweaking the look of the Angular Material components.<br></p><p>Here are some tips for working with Angular Material&#58;</p><ul><li>Information regarding theme can be found here&#58;&#160;<a href="https&#58;//material.angular.io/guide/theming">https&#58;//material.angular.io/guide/theming</a></li><li>Tweaking individual components can be done by wrapping it in a CSS class and using ng-deep&#58; 
      <a href="https&#58;//blog.angular-university.io/angular-host-context/">https&#58;//blog.angular-university.io/angular-host-context/</a><br>If you prefer, all such modifications can be done in a separate SCSS file that is then added into styles.scss.<br>Make sure you use a wrapper class so you do not change all other same Angular Material components in the project.</li><li>Add the 
      <a href="https&#58;//github.com/angular/flex-layout">Flex Layout</a> library to your project to take advantage of 
      <a href="https&#58;//css-tricks.com/snippets/css/a-guide-to-flexbox/%22%20%5co%20%22https&#58;//css-tricks.com/snippets/css/a-guide-to-flexbox/">Flexbox</a>.&#160; It makes it easy to use Flexbox classes via directives in your Angular HTML templates.<br>Here is a demo website for Flex Layout&#58; 
      <a href="https&#58;//tburleson-layouts-demos.firebaseapp.com/%22%20%5cl%20%22/docs">https&#58;//tburleson-layouts-demos.firebaseapp.com/#/docs</a><br></li><li>For the creation of custom Angular Material components, the CDK can be used&#58;&#160;<a href="https&#58;//material.angular.io/cdk/categories">https&#58;//material.angular.io/cdk/categories</a></li><li>If you need additional colours&#160;for the standard 'warn', 'primary', and 'accent', you can add that into global SCSS files&#58;
      <p class="ssw15-rteElement-CodeArea">.mat-success &#123;&#160; color&#58; $white !important;&#160; background-color&#58; $success !important;&#125;</p>Now you can do following&#58;
      <p class="ssw15-rteElement-CodeArea">&lt;button mat-raised-button color=&quot;success&quot;&gt;Primary&lt;/button&gt;&#160;<br></p></li></ul><h3>Bootstrap</h3><p>Bootstrap is the obvious choice if your UI design requires extensive customization.​​ Bootstrap makes it easy to theme your application's design and to tweak the design of individual components. In addition to components, Bootstrap 4 provides powerful layout and theming capabilities. These features make it popular with Designers.​</p><dl class="image"><dt> <img src="/PublishingImages/bad-bootstrap.png" alt="bad-bootstrap.png" style="width&#58;650px;" /></dt><dd>Figure&#58; Bootstrap has been the recommended UI framework for the web for years<br></dd></dl><p>There are two popular bootstrap-based Angular component libraries - 
   <a href="https&#58;//ng-bootstrap.github.io/%22%20%5cl%20%22/home">ng-bootstrap</a> and 
   <a href="https&#58;//github.com/valor-software/ngx-bootstrap">ngx-bootstrap</a>. Both support Bootstrap 4 and provide a rich choice of components.</p>


