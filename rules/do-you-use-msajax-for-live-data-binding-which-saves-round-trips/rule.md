---
type: rule
title: Do you use MSAjax for Live Data Binding which saves round trips?
uri: do-you-use-msajax-for-live-data-binding-which-saves-round-trips
created: 2009-08-25T02:47:57.0000000Z
authors:
- id: 1
  title: Adam Cogan

---



<span class='intro'> This field should not be null (Remove me when you edit this field). </span>


  <strong>Binding Modes&#58;</strong> <br>
<ul>
    <li>Sys.BindingMode.auto<br>
    This is the default binding mode. Two-way binding on an input control, and one-way binding on a context-type elements such as spans.
    <dl class="goodCode">
        <dt>
        <pre>&lt;b&gt;Name&#58; &lt;/b&gt;&lt;input id=&quot;name&quot; type=&quot;text&quot; value=&quot;&#123;binding name, mode=auto&#125;&quot; /&gt;
&lt;b&gt;Echo&#58; &lt;/b&gt;&lt;span id=&quot;nameDisplay&quot;&gt;&#123;binding name, mode=auto&#125;&lt;/span&gt;
        </pre>
        </dt>
        <dd>Figure&#58; When you update either textbox, the other one will be updated with the same value. </dd>
    </dl>
    </li>
    <li>Sys.BindingMode.twoWay<br>
    This is the default binding mode for input controls.
    <dl class="goodCode">
        <dt>
        <pre>&lt;b&gt;Name&#58; &lt;/b&gt;&lt;input id=&quot;name&quot; type=&quot;text&quot; value=&quot;&#123;binding name, mode=twoWay&#125;&quot; /&gt;
&lt;b&gt;Echo&#58; &lt;/b&gt;&lt;span id=&quot;nameDisplay&quot;&gt;&#123;binding name, mode=twoWay&#125;&lt;/span&gt;
        </pre>
        </dt>
        <dd>Figure&#58; When you update either textbox, the other one will be updated with the same value. </dd>
    </dl>
    </li>
    <li>Sys.BindingMode.oneWay&#160;
    <dl class="goodCode">
        <dt>
        <pre>&lt;b&gt;Name&#58; &lt;/b&gt;&lt;input id=&quot;name&quot; type=&quot;text&quot; value=&quot;&#123;binding name, mode=oneWay&#125;&quot; /&gt;
&lt;b&gt;Echo&#58; &lt;/b&gt;&lt;span id=&quot;nameDisplay&quot;&gt;&#123;binding name, mode=twoWay&#125;&lt;/span&gt;
        </pre>
        </dt>
        <dd>Figure&#58; When you update the Name, it won't affect the Echo. </dd>
    </dl>
    </li>
    <li>Sys.BindingMode.oneWayToSource<br>
    <dl class="goodCode">
        <dt>
        <pre>&lt;b&gt;Name&#58; &lt;/b&gt;&lt;input id=&quot;name&quot; type=&quot;text&quot; value=&quot;&#123;binding name&#125;&quot; /&gt;
&lt;b&gt;Echo&#58; &lt;/b&gt;&lt;span id=&quot;nameDisplay&quot;&gt;&#123;binding name, mode=oneWayToSource&#125;&lt;/span&gt;
        </pre>
        </dt>
        <dd>Figure&#58; When you update the Name, it won't affect the Echo. But if you update Echo, it will affect the Name. </dd>
    </dl>
    </li>
    <li>Sys.BindingMode.oneTime
    <dl class="goodCode">
        <dt>
        <pre>&lt;b&gt;Name&#58; &lt;/b&gt;&lt;input id=&quot;name&quot; type=&quot;text&quot; value=&quot;&#123;binding name, mode=twoWay&#125;&quot; /&gt;
&lt;b&gt;Echo&#58; &lt;/b&gt;&lt;span id=&quot;nameDisplay&quot;&gt;&#123;binding name, mode=oneTime&#125;&lt;/span&gt;
        </pre>
        </dt>
        <dd>Figure&#58; When you update the Name in the first time, it will affect the Echo. After the first time, it won't affect the Echo. </dd>
    </dl>
    </li>
</ul>
The live-binding syntax is similar to binding syntax in WPF (XAML). 



