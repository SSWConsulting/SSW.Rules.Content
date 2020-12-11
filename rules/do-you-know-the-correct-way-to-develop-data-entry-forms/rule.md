---
type: rule
archivedreason: 
title: Do you know the correct way to develop Data Entry Forms?
guid: 98e8f4b2-a989-46a1-bbe7-f453baa414ae
uri: do-you-know-the-correct-way-to-develop-data-entry-forms
created: 2014-12-01T00:36:14.0000000Z
authors: []
related: []

---


<p>Data Entrees should be able to use your data entry form with ease. It should follow the flow that they are familiar with.</p>
<br><excerpt class='endintro'></excerpt><br>
<dl class="badImage"><dt>
      <img alt="Access - Clients Form" src="../../assets/BadAddDeleteSubForm.gif" style="margin:5px;" />
   </dt><dd>Figure: Bad Example - New button should open another form, and Delete button should be on that new form</dd></dl><ol style="list-style-type:lower-alpha;"><li><h3>Multiple Form Instances</h3><p>Imagine, while the Sally is entering a Quote on the Quote Form, they receive a Phone call from a client needing a new Quote. The user will not want to close the current Quote, because they are 1/2 way through it.</p><p>As we saw in the example above, Sally needs to open multiple instances of the same form. A reputable example for this is Microsoft's Outlook. When you are 1/2 way through an email, and you chose to start writing another, Outlook makes it convenient by placing every email you open in the taskbar. The figure below illustrates this.</p><dl class="goodImage"><dt>
            <img alt="Outlook - Multiple Emails" src="../../assets/Outlookemails.jpg" style="margin:5px;" />
         </dt><dd>Figure: Good Example - Outlook opens multiple instances of the data entry form (email message)</dd></dl>
      <dl class="goodImage"><dt>
            <img alt="Outlook Taskbar" src="../../assets/outlooktaskbar.jpg" style="margin:5px;" />
         </dt><dd>Figure: Good Example - Each form instance is shown in the taskbar, and easily opened again</dd></dl><p>A method of implementing this is through New and Delete buttons on the form.</p><p>New and Delete buttons should appear, in a toolbar for example, docked to the top.<br> The figure in 
         <a href="http://www.ssw.com.au/ssw/Standards/Rules/RulestoBetterInterfaces-Forms.aspx#DrillAround">Data Entry Drill Downs</a> below illustrates this.</p><dl class="goodImage"><dt>
            <img alt="SSW Time PRO .NET -  Time Sheets" src="../../assets/GoodAddDeleteSubForm.jpg" style="margin:5px;" />
         </dt><dd>Figure: Good Example - New and Delete buttons docked in the Toolbar providing easy data entry for new Timesheets</dd></dl><p> The Delete button resides there to make sure that Sally has seen the record before she deletes it. The New button should instantiate a new data entry form in add mode (as compared to "edit"), leaving the current one in the background.</p><p>It can be argued that navigation is required in a data entry form. As an option, a good navigation system will navigate through a subset of records (ideally records which are search results). The idea of navigating through all records can be tedious, and most of the time useless.</p><h3>However there is a problem</h3><p>Do you open the same record with two different instances of the form? For example, if attempt to open a form instance for editing a Quote from the database, then while editing you open up another form instance for the same Quote. Besides the fact that there will be loss of data, and dirty reading, this is a very confusing interface.</p><p>A possible solution for this issue is to implement a form manager.</p><p>The "form manager" will keep track of every instance opened. So in our example, the second time we try to open the same Quote for editing, the "form manager" will recognize that there is a form currently being edited that Quote, and would select that form.</p></li><li><h3>Form states and how to respond to them</h3><p>The form is to be aware of the data state. If the data is dirty:</p><ul><li>The Apply button would be enabled until the record is saved</li><li>The OK button would simply save the record and close the Form</li><li>The Cancel button would pop up a dialog (shown in the figure below) asking to save changes;<br> If the user decides to save, it should save the record and close the form.<br> If No, then close the form without saving.<br> If Cancel, then return back to the dirty form. </li></ul><dl class="goodImage"><dt>
            <img alt="Centrix - Save Changes" src="../../assets/SaveChangesDialog.jpg" style="margin:5px;" />
         </dt><dd>Figure: Good Example - Save Changes Dialog must appear when form is dirty</dd></dl></li><li><p>Do not add buttons for searching on the data entry form, create a new form for search, through which you can open new instances of the form. The convenience of the search capability on the form will be overlooked as it makes the form more crowded. Another issue which can arise is if Sally searches for a criteria which returns multiple records, she cannot look at all those records. She can only open one at a time, navigating through them. The solution to the search dilemma is to create a new search form, which is shown in the figure below. The search form will allow multiple criteria, will not over crowd the data entry form, and will show you all the results that your search has retrieved.</p><dl class="badImage"><dt>
            <img alt="Integrated Search" src="../../assets/BadSearch.gif" style="margin:5px;" />
         </dt><dd>Figure: Bad Example - This implementation of a search utility is on the same form</dd></dl><dl class="goodImage"><dt>
            <img alt="Separate Search" src="../../assets/SearchForm.gif" style="margin:5px;" />
         </dt><dd>Figure: Good Example - This implementation of Search feature is on a separate form</dd></dl></li><li><h3>No Delete Button for sub forms</h3><p>When including a sub form in your main form (as shown in figure below), the only options the user should have are "New" and "Edit". When "Edit" is clicked, another data entry form is opened to edit selected record. In this data entry form, you will have a "Delete" button on the toolbar. This saves the user from making mistakes and forcing them to see the record before deleting.</p><dl class="goodImage"><dt>
            <img alt="Centrix - Loan Estimate Details" src="../../assets/SubFormsExample.gif" style="margin:5px;" />
         </dt><dd>Figure: Good Example - No Delete button for Sub forms</dd></dl></li><li><h3>Validation</h3><p>Most fields required validation. There are three types of validations:</p><ul><li>Required Field - the field should be filled in</li><li>Formatting - the field must be in a correct format. e.g. currency or date</li><li>Logical - the field needs to pass some validation tests in the business layer</li></ul><p>To show an error, display an error provider icon next to the field on the right. An example of this is shown in the figure below.<br> Validation must not be done on TextChanged, this may chew the processor if it is a logical validation. It can also give unpleasant results, e.g. when entering -6.00, as soon as the '-' is entered the validation control would turn on.</p><p>Validation for Required fields must be done in the validating event.<br> Validation for format should be done in parse/format methods.<br> Validation for Logic should be done in Validated, since it must be entered if required, and in correct format.</p><p>The reason for the above validation placement is that these events run in the following order:</p><ul><li>Validating</li><li>Parse/Format</li><li>Validated</li></ul><dl class="goodImage"><dt>
            <img alt="Centrix - Error Provider" src="../../assets/ErrorProviderIconExample.jpg" style="margin:5px;" />
         </dt><dd>Figure: Good Example - Error Provider Icon next to a required field</dd></dl><p>
         <strong>Do not</strong> show a message box after every error in validation. You may show a message box as an error summary when an OK or Apply is clicked. Make sure you warn the user that there is an error on the form when they attempt to save.</p></li><li><h3>Relevant Menus</h3><p>Make sure that the menu items are relevant to the current form. The main idea is that we don't want to show the user any dummy menu items. However, this may become complex when a base form (containing the menu) is inherited. Access to menus in the base form must be granted (maybe through properties), so that each menu can be customized according to each child form.</p><dl class="badImage"><dt>
            <img alt="Centrix - File, Action, Report, Tools & Help Menus" src="../../assets/MenuBadExample.jpg" style="margin:5px;" />
         </dt><dd>Figure: Bad Example - Action and Tools are irrelevant on this form</dd></dl><dl class="goodImage"><dt>
            <img alt="Centrix - File, Report & Help Menus" src="../../assets/MenuGoodExample.jpg" style="margin:5px;" />
         </dt><dd>Figure: Good Example - Menus are relevant</dd></dl><p>In the above example, there are a couple of unused menus that have been inherited from the base form and not set to invisible.</p></li><li><h3>Field Formatting</h3><p>Ensure that the data is displayed in correct format. For example, when presenting a percentage data in a field, make sure it is displayed as '% xx.xx'.<br> To accompany formatting, you must also create a parse function for putting the correct value back in the database.</p><p>
         <strong>Note:</strong> This can be difficult for data bound fields, and in that case you will have to handle the parse and format event of the Field's Binding object. An example of handling these events is shown below.</p><dl class="Code"><dt><pre>            Dim controlBinding As Binding = New System.Windows.Forms.Binding(propertyName,dataSource, dataMember)
            AddHandler controlBinding.Format, AddressOf DecimalToCurrencyString
            AddHandler controlBinding.Parse, AddressOf CurrencyStringToDecimal
            controlToBeBound.DataBindings.Add(controlBinding)
            Private Sub DecimalToCurrencyString(sender As Object, cevent As ConvertEventArgs)
            ' The method converts only to string type. Test this using the DesiredType.
            If Not cevent.DesiredType Is GetType(String) 
            Then
                Exit Sub
            End If
            ' Use the ToString method to format the value as currency ("c").
            cevent.Value = CType(cevent.Value, Decimal).ToString("c")
                End Sub
            Private Sub CurrencyStringToDecimal(sender As Object, cevent As ConvertEventArgs)
            ' The method converts back to decimal type only.
            If Not cevent.DesiredType Is GetType(Decimal) 
            Then
                Exit Sub
            End If
            ' Converts the string back to decimal using the static ToDecimal method.
            cevent.Value = Decimal.Parse(cevent.Value.ToString, NumberStyles.Currency, nothing)
            End Sub
            </pre></dt><dd>Code: Code for Handling Parse and Format Events for Data bound Controls</dd></dl><p>The Binding is created and added to the Data-Bindings of the Control all in one line in Visual Designer in VS.Net. Do not use Visual Designer to data-bind if you will be handling the Parse and Format events. You will have to create the handlers yourself.</p></li><li>
      <a name="CreatedBy"></a> 
      <h3>Created/Last Updated By Fields</h3><p>With all database entries, there are always some fields that are used over and over again. For example, these fields may be created date, created by, last updated date, updated by, etc.</p><p>A common UI to use for these fields can be seen in the example below. What we do is create a user control that is identical across all projects/UI.</p><dl class="badImage"><dt>
            <img alt="SSW Time PRO .NET - Time Sheets" src="../../assets/BadCreatedUpdated.jpg" style="margin:5px;" />
         </dt><dd>Figure: Bad Example - This form has no information to indicate who created this entry and who last modified it</dd></dl><dl class="goodImage"><dt>
            <img alt="SSW Time PRO .NET - Time Sheets" src="../../assets/GoodCreatedUpdated.jpg" style="margin:5px;" />
         </dt><dd>Figure: Good Example - This form contains Created by/Updated by fields used in a standard control which is put into all forms</dd></dl><p>An example of how to set the values for this user control is shown below.</p><dl class="code"><dt><pre>            updatedBy.CreatedDate = .DateCreated
            updatedBy.CreatedBy = .EmpCreated
            updatedBy.UpdatedDate = .DateUpdated
            updatedBy.UpdatedBy = .EmpUpdated
            </pre></dt><dd>Code: Code for Setting values for User Control</dd></dl><p>Databinding is also available to be used with this user control.</p><dl class="image"><dt>
            <img alt="User Control - Data Binding in the Designer" src="../../assets/CommonFieldsDB.gif" style="margin:5px;" />
         </dt><dd>Figure: Data Binding using the Designer</dd></dl></li><li><h3>Minimum Defaults</h3><p>In many situations, there is a need for field Defaults. These Defaults can be extracted from the Database for example. When a new form is opened ensure that only necessary Defaults are loaded. By Default some decimal fields will become 0.0, but make sure they are set to blank because they may be required fields.</p></li><li><h3>Resizing</h3><p>Is the form resizable? What happens if the user resizes and/or maximizes the form?</p><p>Data entry forms, and forms containing List View controls, should be resizable. Use either anchoring or docking, or a combination, to handle window resizing. Restricting the user from resizing or maximizing the form is not recommended.</p></li></ol>


