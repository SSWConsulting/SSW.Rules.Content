---
type: rule
title: Do you use Web Compiler extension?
uri: do-you-use-web-compiler-extension
created: 2018-06-19T01:38:21.0000000Z
authors:
- id: 76
  title: Eden Liang

---



<span class='intro'> You can use Visual Studio's Web Compiler&#160;extension&#160;to create a bundle.css and&#160;test if CSS was compiled successfully. <br> </span>

<p>More information and download at&#160;<a href="https&#58;//marketplace.visualstudio.com/items?itemName=MadsKristensen.WebCompiler">Visual Studio Marketplace</a>.</p><dl class="goodImage"><dt> <img src="/PublishingImages/web-compiler-find-error.png" alt="web-compiler-find-error.png" /> </dt><dd>Figure&#58; Web Compiler can find missing curly braces</dd></dl> Unfortunately different kinds of errors, like are not caught. <dl class="badImage"><dt> <img src="/PublishingImages/web-compiler-didnt-find-error.png" alt="web-compiler-didnt-find-error.png" /> </dt><dd>Figure&#58; Curly braces in the wrong place, but still compiled successfully <br></dd></dl><p>In addition, Gulp is wrongly successful too&#58; <br></p><dl class="badImage"><dt><img src="/PublishingImages/gulp-didnt-find-error.png" alt="gulp-didnt-find-error.png" /> </dt><dd>Figure&#58; Gulp couldn't find the curly braces error​<br></dd></dl>


