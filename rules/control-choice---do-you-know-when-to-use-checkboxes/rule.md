---
type: rule
archivedreason: 
title: Control Choice - Do you know when to use CheckBoxes?
guid: 3176b22d-ed88-4909-8a77-3e6e652eae7e
uri: control-choice---do-you-know-when-to-use-checkboxes
created: 2012-11-27T08:51:11.0000000Z
authors: []
related: []

---

If the option only contains 2 choices, and the answer is a Boolean type value where the opposite value is clear (e.g. Enabled/Disabled, True/False, Yes/No, On/Off), it should always be a checkbox.
<dl class="badImage">&lt;dt&gt;<img alt="Boolean options not using CheckBox." src="../../assets/NotUsingCheckBox.gif">&lt;/dt&gt;
<dd>Figure: Bad Example - Boolean options not using CheckBox</dd></dl><dl class="goodImage">&lt;dt&gt;<img alt="A CheckBox is used for Boolean type value." src="../../assets/UsingCheckBox.gif">&lt;/dt&gt;
<dd>Figure: Good Example - A CheckBox is used for Boolean type value</dd></dl>
<!--endintro-->

Only 1 CheckBox is used as the opposite value is clear, such controls are often CheckBoxes in a ListView too. E.g.:
<dl class="goodImage">&lt;dt&gt;<img alt="CheckBoxes in a ListView." src="../../assets/CheckBoxesInListView.gif">&lt;/dt&gt;
<dd>Figure: Good Example - CheckBoxes in a ListView</dd></dl>
CheckBoxes are also suitable to use for enable or disable sections and to tell the user that these sections do not need configuring for the application to run.
<dl class="goodImage">&lt;dt&gt;<img alt="CheckBoxes are used to enable/disable sections." src="../../assets/CheckBoxSection.gif">&lt;/dt&gt;
<dd>Figure: Good Example - CheckBoxes are used (although no opposite values), because they are clear when the CheckBoxes aren't ticked, the sections are disabled</dd></dl><dl class="badImage">&lt;dt&gt;<img alt="Not using checkboxes" src="../../assets/UseCheckBoxBad.gif">&lt;/dt&gt;
<dd>Figure: Bad Example - This screen implies that Configuring Credentials is required</dd></dl><dl class="goodImage">&lt;dt&gt;<img alt="Good use of checkboxes" src="../../assets/UseCheckBoxGood.gif">&lt;/dt&gt;
<dd>Figure: Good Example - This screen uses a CheckBox to signify that Configure Credentials is optional</dd></dl>
If there are only two options available on the form (usually a yes/no answer), the use of a checkbox is more intuitive than radio buttons. Only use radio buttons if there are more than two options.
<dl class="badImage">&lt;dt&gt;<img alt="Radio buttons are not appropriate when there are only two options" src="../../assets/radio-for-two-options.jpg">&lt;/dt&gt;
<dd>Figure: Bad Example – Radio buttons are not appropriate when there are only two options</dd></dl><dl class="goodImage">&lt;dt&gt;<img alt="These yes/no questions have a better representation with checkboxes" src="../../assets/checkbox-for-two-options.jpg">&lt;/dt&gt;
<dd>Figure: Good Example – These yes/no questions have a better representation with checkboxes</dd></dl>
