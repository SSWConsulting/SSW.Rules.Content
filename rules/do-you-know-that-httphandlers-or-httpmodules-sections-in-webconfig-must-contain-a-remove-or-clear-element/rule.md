---
type: rule
title: Do you know that 'httpHandlers' or 'httpModules' sections in web.config must contain a 'remove' or 'clear' element?
uri: do-you-know-that-httphandlers-or-httpmodules-sections-in-webconfig-must-contain-a-remove-or-clear-element
created: 2013-02-06T12:55:03.0000000Z
authors:
- id: 1
  title: Adam Cogan
- id: 46
  title: Danijel Malik

---



<span class='intro'> <p>If web.config contains a &lt;httpHandlers&gt; or &lt;httpModules&gt; section, that section must contain a &lt;remove... /&gt; or a &lt;clear /&gt; element.
</p><p>This basically forces developers to explicitly enable inheritance in nested virtual directories. In 99% of cases this developers won't use inheritance on these two sections, however it causes issues when somebody wants to add a module or handler to the parent virtual directory.
</p> </span>

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


