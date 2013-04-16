---
type: rule
archivedreason: 
title: Controls - Do you include the number of results in ComboBoxes?
guid: da34f7bf-dc4e-412c-97ad-bb7fdacf595b
uri: controls---do-you-include-the-number-of-results-in-comboboxes
created: 2012-11-27T08:40:47.0000000Z
authors:
- id: 1
  title: Adam Cogan
related: []

---


<p>When designing your form, you should try to help your user whenever it's possible. So it's a good idea to include the number of results in ComboBoxes.</p>
<br><excerpt class='endintro'></excerpt><br>
​<span style="color&#58;#ff0000;font-family&#58;'segoe ui', 'trebuchet ms', tahoma, arial, verdana, sans-serif;font-size&#58;1.15em;line-height&#58;1.4;">For Web Pages</span><dl class="goodImage"><dt> 
      <img alt="Combo-box with multiple columns" src="/DesignandPresentation/RulestoBetterInterfacesControls/PublishingImages/combo-box-multiple-col.jpg" /> 
   </dt><dd>Figure&#58; Good example – combo-box with multiple columns</dd></dl> Feel free to use our sample&#58; 
<ol><li>Download and install Kendo UI Controls from 
      <a href="http&#58;//www.kendoui.com/" target="_blank">Kendo UI</a></li><li>
      <strong>HTML (Razor)</strong><br> Create a combo-box that has a custom template. Use a code bellow as an example&#58; 
      <div class="greyBox"><pre>@(Html.Kendo().ComboBoxFor(x =&gt; x.EmpTime.ProjectID)
    .AutoBind(true)
    .Suggest(true)
    .Delay(300)
    .DataSource(source =&gt; source.Read(read =&gt; read.Action(&quot;ProjectNameAjaxBind&quot;, &quot;Ajax&quot;)
                                                .Data(&quot;function() &#123; return &#123;clientId &#58; getClientId()&#125;; &#125;&quot;)
                                                .Type(HttpVerbs.Post)))
    .Height(450)
    .DataTextField(&quot;DisplayText&quot;)
    .DataValueField(&quot;Value&quot;)
    .Filter(FilterType.Contains)
    .Template(@&quot;
&lt;table class='comboBox-Projects'&gt;
&lt;tr&gt;
&lt;td class='projectName'&gt;$&#123;data.DisplayText&#125;&lt;/td&gt;
&lt;td class='projectTotalCount'&gt;$&#123;data.UsedCount&#125;&lt;/td&gt;
&lt;td class='projectLastUsed'&gt;$&#123;data.LastUsedText&#125;&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
&quot;)
    .HighlightFirst(false)
    .IgnoreCase(true)
    .Events(e =&gt; e.Change(&quot;projectChanged&quot;).Open(&quot;onProjectOpened&quot;))
)

</pre></div></li><li>
      <strong>CSS</strong><br> Customize the look &amp; feel to suit your needs. 
      <div class="greyBox"><pre>#projectsTableBorder &#123;
        border-bottom&#58; 1px solid rgb(217, 217, 217);
        margin&#58; 0 -2px;
    &#125;
 
    .comboBox-Projects#projectsHeader &#123;
        color&#58; black;
        font-weight&#58; bold;
        margin&#58; 4px 16px 4px 4px;
    &#125;
 
    .comboBox-Projects td.projectName &#123;
        width&#58; 400px;
        text-align&#58; left;
    &#125;
 
    .comboBox-Projects td.projectTotalCount &#123;
        width&#58; 70px;
        text-align&#58; right;
        padding-right&#58; 16px;
    &#125;
 
    .comboBox-Projects td.projectLastUsed &#123; text-align&#58; left; &#125;
 
    #projectNameHeader&#58;hover, #projectTotalCountHeader&#58;hover, #projectLastUsedHeader&#58;hover &#123;
        cursor&#58; pointer;
        text-decoration&#58; underline;
    &#125;
</pre></div></li><li>
      <strong>JavaScript</strong><br> Use JavaScript to change the combo-box's behaviour. 
      <div class="greyBox"><pre>// resize the drop-down list
function resizeComboBoxList(comboBoxListId, width) &#123;
    var list = $(comboBoxListId);
    list.width(width);
 
    var height = list.height();
    list.children(&quot;ul&quot;).height(height - 25);
&#125;
 
function onProjectOpened() &#123;
    resizeComboBoxList(&quot;#EmpTime_ProjectID-list&quot;, 600);
&#125;
 
// execute sorting when a header column is clicked
function onClick_ColumnHeader(senderId, comboBoxId, fieldName) &#123;
    var column = $(senderId);
    column.unbind('click');
    column.click(function() &#123;
        sortComboBoxBy(comboBoxId, fieldName);
    &#125;);
&#125;
 
// sort any combo-box based on a field name
function sortComboBoxBy(comboBoxId, fieldName) &#123;
    var comboBox = $(comboBoxId).data(&quot;kendoComboBox&quot;);
    var sortDescriptors = comboBox.dataSource._sort;
    var direction = &quot;asc&quot;;
 
    if (typeof(sortDescriptors) != &quot;undefined&quot;) &#123;
        var sortDescriptor = sortDescriptors[0];
 
        if (typeof(sortDescriptor) != &quot;undefined&quot;) &#123;
            if (sortDescriptor[&quot;field&quot;] == fieldName) &#123;
                if (sortDescriptor[&quot;dir&quot;] == &quot;asc&quot;) &#123;
                    direction = &quot;desc&quot;;
                &#125;
            &#125;
        &#125;
    &#125;
 
    comboBox.dataSource.sort(&#123;
        field&#58; fieldName,
        dir&#58; direction,
    &#125;);
&#125;
 
// prepare 
$(document).ready(function() &#123;
    var projectsId = &quot;#EmpTime_ProjectID&quot;;
   var projectsListId = projectsId + '-list';
   
    // prepend header to combo-box list. By default you only get &lt;ul&gt;
    $(&quot;
            <div id="projectsTableBorder" class="comboBox-Projects">Project Name&lt;/td&gt;&quot; +
        &quot;&lt;td id='projectTotalCountHeader' class='projectTotalCount'&gt;Used&lt;/td&gt;&quot; +
        &quot;&lt;td id='projectLastUsedHeader' class='projectLastUsed'&gt;Last Used&lt;/td&gt;&quot; +
        &quot;&lt;/tr&gt;&lt;/table&gt;&quot; +
        &quot;&lt;/div&gt;&quot;)
        .prependTo(projectsListId);
 
    // register click events for each column
    onClick_ColumnHeader('#projectNameHeader', projectsId, &quot;DisplayText&quot;);
    onClick_ColumnHeader('#projectTotalCountHeader', projectsId, &quot;UsedCount&quot;);
    onClick_ColumnHeader('#projectLastUsedHeader', projectsId, &quot;LastUsedValue&quot;);
&#125;);
&#125;);
 </div></pre></div></li></ol><h3>For Windows Forms</h3><dl class="badImage"><dt> 
      <img alt="Options Form - ComboBox without Result Count" src="http&#58;//www.ssw.com.au/ssw/Standards/Rules/Images/ComboWF-1.jpg" /> 
   </dt><dd>Figure&#58; Bad Example - You can't tell the number of results and there is a scroll bar</dd></dl><dl class="goodImage"><dt> 
      <img alt="Options Form - ComboBox with Result Count" src="http&#58;//www.ssw.com.au/ssw/Standards/Rules/Images/ComboWF-2.jpg" /> 
   </dt><dd>Figure&#58; Good Example - The number of results is clearly displayed. Long text boxes &gt; 30 entries, another approach can be employed - putting the common ones at the top</dd></dl><dl class="badImage"><dt> 
      <img alt="Long Text ComboBox" src="http&#58;//www.ssw.com.au/ssw/Standards/Rules/Images/Rule38LongTextCombobox.jpg" /> 
   </dt><dd>Figure&#58; Bad Example - Firstly because it is manual, plus what about the 4th, 5th, etc most common used countries</dd></dl><dl class="badImage"><dt> 
      <img alt="Sortable ComboBox" src="http&#58;//www.ssw.com.au/ssw/Standards/Rules/Images/rule38SortableCombobox.jpg" /> 
   </dt><dd>Figure&#58; Bad Example – This was a highly unpopular method of the sorting and counting above</dd></dl><div>We believe all combos should be able to be sorted ascending/descending and by popularity asc/desc.</div>


