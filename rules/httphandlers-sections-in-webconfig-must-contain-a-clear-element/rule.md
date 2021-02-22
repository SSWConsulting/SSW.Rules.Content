---
type: rule
archivedreason: 
title: Do you know that 'httpHandlers' or 'httpModules' sections in web.config must contain a 'remove' or 'clear' element?
guid: 14359e59-b047-4e0b-aef5-f79ccd3eb373
uri: httphandlers-sections-in-webconfig-must-contain-a-clear-element
created: 2013-02-06T12:55:03.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: Danijel Malik
  url: https://ssw.com.au/people/danijel-malik
related: []
redirects:
- do-you-know-that-httphandlers-or-httpmodules-sections-in-web-config-must-contain-a-remove-or-a-clear-element
- do-you-know-that-httphandlers-or-httpmodules-sections-in-web-config-must-contain-a-remove3f3f3f-or-a-clear-element
- https-rules-ssw-com-au-do-you-know-that-httphandlers-or-httpmodules-sections-in-web-config-must-contain-a-remove-or-a-clear-element
- you-know-that-httphandlers-or-httpmodules-sections-in-web-config-must-contain-a-remove-or-a-clear-element
- do-you-know-that-httphandlers-or-httpmodules-sections-in-web-config-must-contain-a-remove-or-clear-element

---


<p>If web.config contains a &lt;httpHandlers&gt; or &lt;httpModules&gt; section, that section must contain a &lt;remove... /&gt; or a &lt;clear /&gt; element. <br></p><p>This basically forces developers to explicitly enable inheritance in nested virtual directories. In 99% of cases this developers won't use inheritance on these two sections, however it causes issues when somebody wants to add a module or handler to the parent virtual directory.</p>
<br><excerpt class='endintro'></excerpt><br>
<dl class="badImage"><dt><div class="greyBox"><pre>&lt;configuration&gt;
   &lt;system.web&gt;
      &lt;httpHandlers&gt;
         &lt;add verb=&quot;*&quot; 
              path=&quot;*.New&quot; 
              type=&quot;MyHandler.New,MyHandler&quot;/&gt;
         &lt;add verb=&quot;GET,HEAD&quot; 
              path=&quot;*.MyNewFileExtension&quot; 
              type=&quot;MyHandler.MNFEHandler,MyHandler.dll&quot;/&gt;
     &lt;/httpHandlers&gt;
   &lt;system.web&gt;
&lt;/configuration&gt;
</pre></div></dt><dd>Figure&#58; Bad example</dd></dl><dl class="goodImage"><dt><div class="greyBox"><pre>&lt;configuration&gt;
   &lt;system.web&gt;
      &lt;httpHandlers&gt;
         &lt;clear/&gt;
         &lt;add verb=&quot;*&quot; 
              path=&quot;*.New&quot; 
              type=&quot;MyHandler.New,MyHandler&quot;/&gt;
         &lt;add verb=&quot;GET,HEAD&quot; 
              path=&quot;*.MyNewFileExtension&quot; 
              type=&quot;MyHandler.MNFEHandler,MyHandler.dll&quot;/&gt;
     &lt;/httpHandlers&gt;
   &lt;system.web&gt;
&lt;configuration&gt;
</pre></div>
   </dt><dd>Figure&#58; Good example</dd></dl>


