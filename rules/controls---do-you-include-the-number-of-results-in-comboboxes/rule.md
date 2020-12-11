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

When designing your form, you should try to help your user whenever it's possible. So it's a good idea to include the number of results in ComboBoxes.

<!--endintro-->
For Web Pages <dl class="goodImage">&lt;dt&gt; <img alt="Combo-box with multiple columns" src="combo-box-multiple-col.jpg"> &lt;/dt&gt;<dd>Figure: Good example – combo-box with multiple columns</dd></dl> Feel free to use our sample:
1. Download and install Kendo UI Controls from [Kendo UI](http://www.kendoui.com/)
2. **HTML (Razor)** 
Create a combo-box that has a custom template. Use a code bellow as an example:

@(Html.Kendo().ComboBoxFor(x => x.EmpTime.ProjectID)
.AutoBind(true)
.Suggest(true)
.Delay(300)
.DataSource(source => source.Read(read => read.Action("ProjectNameAjaxBind", "Ajax")
.Data("function() { return {clientId : getClientId()}; }")
.Type(HttpVerbs.Post)))
.Height(450)
.DataTextField("DisplayText")
.DataValueField("Value")
.Filter(FilterType.Contains)
.Template(@"



| ${data.DisplayText} |
 ${data.UsedCount} |
 ${data.LastUsedText} |
| --- | --- | --- |



")
.HighlightFirst(false)
.IgnoreCase(true)
.Events(e => e.Change("projectChanged").Open("onProjectOpened"))
)
3. **CSS** 
Customize the look & feel to suit your needs.

```
#projectsTableBorder { border-bottom: 1px solid rgb(217, 217, 217); margin: 0 -2px; } .comboBox-Projects#projectsHeader { color: black; font-weight: bold; margin: 4px 16px 4px 4px; } .comboBox-Projects td.projectName { width: 400px; text-align: left; } .comboBox-Projects td.projectTotalCount { width: 70px; text-align: right; padding-right: 16px; } .comboBox-Projects td.projectLastUsed { text-align: left; } #projectNameHeader:hover, #projectTotalCountHeader:hover, #projectLastUsedHeader:hover { cursor: pointer; text-decoration: underline; }
```
4. **JavaScript** 
Use JavaScript to change the combo-box's behaviour.

```
// resize the drop-down listfunction resizeComboBoxList(comboBoxListId, width) { var list = $(comboBoxListId); list.width(width); var height = list.height(); list.children("ul").height(height - 25);}function onProjectOpened() { resizeComboBoxList("#EmpTime_ProjectID-list", 600);}// execute sorting when a header column is clickedfunction onClick_ColumnHeader(senderId, comboBoxId, fieldName) { var column = $(senderId); column.unbind('click'); column.click(function() { sortComboBoxBy(comboBoxId, fieldName); });}// sort any combo-box based on a field namefunction sortComboBoxBy(comboBoxId, fieldName) { var comboBox = $(comboBoxId).data("kendoComboBox"); var sortDescriptors = comboBox.dataSource._sort; var direction = "asc"; if (typeof(sortDescriptors) != "undefined") { var sortDescriptor = sortDescriptors[0]; if (typeof(sortDescriptor) != "undefined") { if (sortDescriptor["field"] == fieldName) { if (sortDescriptor["dir"] == "asc") { direction = "desc"; } } } } comboBox.dataSource.sort({ field: fieldName, dir: direction, });}// prepare $(document).ready(function() { var projectsId = "#EmpTime_ProjectID"; var projectsListId = projectsId + '-list'; // prepend header to combo-box list. By default you only get  $(" Project Name" + "Used" + "Last Used" + "" + "") .prependTo(projectsListId); // register click events for each column onClick_ColumnHeader('#projectNameHeader', projectsId, "DisplayText"); onClick_ColumnHeader('#projectTotalCountHeader', projectsId, "UsedCount"); onClick_ColumnHeader('#projectLastUsedHeader', projectsId, "LastUsedValue");});});
```


### For Windows Forms
<dl class="badImage">&lt;dt&gt; <img alt="Options Form - ComboBox without Result Count" src="../../assets/ComboWF-1.jpg"> &lt;/dt&gt;<dd>Figure: Bad Example - You can't tell the number of results and there is a scroll bar</dd></dl><dl class="goodImage">&lt;dt&gt; <img alt="Options Form - ComboBox with Result Count" src="../../assets/ComboWF-2.jpg"> &lt;/dt&gt;<dd>Figure: Good Example - The number of results is clearly displayed. Long text boxes > 30 entries, another approach can be employed - putting the common ones at the top</dd></dl><dl class="badImage">&lt;dt&gt; <img alt="Long Text ComboBox" src="../../assets/Rule38LongTextCombobox.jpg"> &lt;/dt&gt;<dd>Figure: Bad Example - Firstly because it is manual, plus what about the 4th, 5th, etc most common used countries</dd></dl><dl class="badImage">&lt;dt&gt; <img alt="Sortable ComboBox" src="../../assets/rule38SortableCombobox.jpg"> &lt;/dt&gt;<dd>Figure: Bad Example – This was a highly unpopular method of the sorting and counting above</dd></dl>
We believe all combos should be able to be sorted ascending/descending and by popularity asc/desc.
<dl class="goodImage">&lt;dt&gt; <img alt="sort-alpha-numeric.jpg" src="sort-alpha-numeric.jpg" style="margin:5px;width:324px;"> &lt;/dt&gt;<dd>Figure: Good Example - Is there a better way to sort this?</dd></dl>
