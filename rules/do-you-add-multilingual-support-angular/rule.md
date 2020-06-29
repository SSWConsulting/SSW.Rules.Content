---
type: rule
title: Do you add multilingual support (Angular)?
uri: do-you-add-multilingual-support-angular
created: 2018-11-13T22:06:41.0000000Z
authors:
- id: 1
  title: Adam Cogan
- id: 80
  title: Shane Ye

---



<span class='intro'> <h3 class="ssw15-rteElement-H3">How to implement multilingual support in an Angular project?<br></h3>There are several ways of implementing multilingual support in an Angular project, the following libraries are popularly&#58;<br>&#160;<br><b><a href="https&#58;//angular.io/guide/i18n">Internationalization (i18n)</a>&#58;</b>&#160;the standard Angular built-in module to help the application dealing with multilingual. It creates multiple language versions of your application.<br>&#160;&#160;<br><b><a href="http&#58;//www.ngx-translate.com/">ngx-translate</a>&#58;</b> a library enhanced the Angular built-in feature, it supports not only template translations but can also be used in the code by APIs.&#160;<br>&#160;<br><b><a href="https&#58;//angular-gettext.rocketeer.be/">angular-gettext&#58; </a></b>&#160;the simplest powerful 3rd party library providing translation support to Angular.<br>&#160;<br>The following table shows the pros and cons of the 3 libraries&#58;<br><br> </span>

<table class="t1 ssw15-rteTable-default  " width="750" cellspacing="0" cellpadding="0"><tbody><tr class="ssw15-rteTableEvenRow-default"><td class="td1 ssw15-rteTableEvenCol-default" valign="top"><p class="p2">&#160; <br></p></td><td class="td2 ssw15-rteTableOddCol-default" valign="top"><p class="p2">
               <b>Pros (<span class="s1">+</span>) <br></b></p></td><td class="td3 ssw15-rteTableEvenCol-default" valign="top"><p class="p2">
               <b>Cons (<span class="s2">-</span>)</b><br></p></td></tr><tr class="ssw15-rteTableOddRow-default"><td class="td1 ssw15-rteTableEvenCol-default" valign="top"><p class="p2">
               <br>
               <b>Internationalization<br></b></p><p class="p2">
               <b>(i18n)</b><br></p></td><td class="td2 ssw15-rteTableOddCol-default" valign="top"><ul class="p3"><li>Better support of displaying dates, number, percentages, and currencies in a local format.<br></li><li>Better support for handling plural forms of words, and alternative text.<br></li></ul></td><td class="td3 ssw15-rteTableEvenCol-default" valign="top"><ul class="ul1"><li class="li2">It only works with one language at a time, you have to completely reload the application to change the language</li><li class="li2">Only support translation in the template (by using HTML tag)<br></li><li class="li2">You need to build + deploy every time you make a change to the language, and you have to have a separate folder every time.</li><li class="li2">You can see the language in the URL.<br></li></ul></td></tr><tr class="ssw15-rteTableEvenRow-default"><td class="td1 ssw15-rteTableEvenCol-default" valign="top"><p class="p2"><b>ngx-translate</b></p></td><td class="td2 ssw15-rteTableOddCol-default" valign="top"><ul><li>It provides more powerful API support</li><li>It supports JSON files by default to store the translation resources</li></ul></td><td class="td3 ssw15-rteTableEvenCol-default" valign="top"><ul class="ul1"><li class="li2">It doesn’t provide good support for plural forms and date.</li><li class="li2">Ngx-translate will stop its releases when angular built-in modules catch up with the ngx-translate features.<br></li><li class="li2">The developer said that when Angular i18n catches up the library will be deprecated. Check&#160;<a href="https&#58;//github.com/ngx-translate/core/issues/495#issuecomment-291158036">article </a>.<br></li></ul></td></tr><tr class="ssw15-rteTableOddRow-default" style="text-decoration&#58;line-through;"><td class="td1 ssw15-rteTableEvenCol-default" valign="top" style="text-decoration&#58;line-through;">
            <b>angular-</b><b>gettext</b><br></td><td class="td2 ssw15-rteTableOddCol-default" valign="top" style="text-decoration&#58;line-through;"><ul><li>The simplest library to deal with multilingual.</li><li>Supports plural handling in different languages.</li></ul><br></td><td class="td3 ssw15-rteTableEvenCol-default" valign="top" style="text-decoration&#58;line-through;"><ul class="ul1" style="text-decoration&#58;line-through;"><li class="li2" style="text-decoration&#58;line-through;">It compiles the translations during the compiling period, which doesn’t support the change of translation at any time.</li><li class="li2" style="text-decoration&#58;line-through;">Only supports AngularJS</li></ul></td></tr></tbody></table><p class="p4">&#160;<br></p><p class="p4">
   <b>Ngx-translate</b> provides the APIs which you can use to translate the resources in the code&#58;</p><p class="p1"> 
   <img src="code-1.png" alt="code-1.png" style="margin&#58;5px;" /> <br> 
   <br> 
</p><p class="p5"> 
   <img src="code-2.png" alt="code-2.png" style="margin&#58;5px;" />&#160;<br></p><p class="p4">By comparing of the 3 libraries we can see <b> ngx-translate</b> provides the best functionality now due to the API support, even though the built-in i18n module will catch up in a certain time, but we still recommend using <b> ngx-translate</b> for multilingual support in your Angular application.</p>


