---
type: rule
archivedreason: 
title: Do you use MSAjax for Live Data Binding which saves round trips?
guid: dd49c795-802e-4052-a15a-caea6b030794
uri: do-you-use-msajax-for-live-data-binding-which-saves-round-trips
created: 2009-08-25T02:47:57.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects: []

---

In old versions of ASP.NET AJAX the UI control couldn't get notification if the source had been changed. Developers had to write the extra code to refresh the value.

 In ASP.NET AJAX version 4.0, there is a new feature called "Live Data Binding", which means when there's any change in the data source, the changes are reflected to the data bound interface instantly and vice versa.    
<!--endintro-->
**Binding Modes:** 

* Sys.BindingMode.auto
<br>    This is the default binding mode. Two-way binding on an input control, and one-way binding on a context-type elements such as spans.<br>    <dl class="goodCode">        <dt>
        <pre>&lt;b&gt;Name&#58; &lt;/b&gt;&lt;input id=&quot;name&quot; type=&quot;text&quot; value=&quot;&#123;binding name, mode=auto&#125;&quot; /&gt;
&lt;b&gt;Echo&#58; &lt;/b&gt;&lt;span id=&quot;nameDisplay&quot;&gt;&#123;binding name, mode=auto&#125;&lt;/span&gt;
        </pre>
        </dt>
        <dd>Figure&#58; When you update either textbox, the other one will be updated with the same value. </dd>
    </dl>
* Sys.BindingMode.twoWay
<br>    This is the default binding mode for input controls.<br>    <dl class="goodCode">        <dt>
        <pre>&lt;b&gt;Name&#58; &lt;/b&gt;&lt;input id=&quot;name&quot; type=&quot;text&quot; value=&quot;&#123;binding name, mode=twoWay&#125;&quot; /&gt;
&lt;b&gt;Echo&#58; &lt;/b&gt;&lt;span id=&quot;nameDisplay&quot;&gt;&#123;binding name, mode=twoWay&#125;&lt;/span&gt;
        </pre>
        </dt>
        <dd>Figure&#58; When you update either textbox, the other one will be updated with the same value. </dd>
    </dl>
* Sys.BindingMode.oneWay <br>    <dl class="goodCode">        <dt>
        <pre>&lt;b&gt;Name&#58; &lt;/b&gt;&lt;input id=&quot;name&quot; type=&quot;text&quot; value=&quot;&#123;binding name, mode=oneWay&#125;&quot; /&gt;
&lt;b&gt;Echo&#58; &lt;/b&gt;&lt;span id=&quot;nameDisplay&quot;&gt;&#123;binding name, mode=twoWay&#125;&lt;/span&gt;
        </pre>
        </dt>
        <dd>Figure&#58; When you update the Name, it won't affect the Echo. </dd>
    </dl>
* Sys.BindingMode.oneWayToSource
<dl class="goodCode">        <dt>
        <pre>&lt;b&gt;Name&#58; &lt;/b&gt;&lt;input id=&quot;name&quot; type=&quot;text&quot; value=&quot;&#123;binding name&#125;&quot; /&gt;
&lt;b&gt;Echo&#58; &lt;/b&gt;&lt;span id=&quot;nameDisplay&quot;&gt;&#123;binding name, mode=oneWayToSource&#125;&lt;/span&gt;
        </pre>
        </dt>
        <dd>Figure&#58; When you update the Name, it won't affect the Echo. But if you update Echo, it will affect the Name. </dd>
    </dl>
* Sys.BindingMode.oneTime<br>    <dl class="goodCode">        <dt>
        <pre>&lt;b&gt;Name&#58; &lt;/b&gt;&lt;input id=&quot;name&quot; type=&quot;text&quot; value=&quot;&#123;binding name, mode=twoWay&#125;&quot; /&gt;
&lt;b&gt;Echo&#58; &lt;/b&gt;&lt;span id=&quot;nameDisplay&quot;&gt;&#123;binding name, mode=oneTime&#125;&lt;/span&gt;
        </pre>
        </dt>
        <dd>Figure&#58; When you update the Name in the first time, it will affect the Echo. After the first time, it won't affect the Echo. </dd>
    </dl>

 The live-binding syntax is similar to binding syntax in WPF (XAML).
