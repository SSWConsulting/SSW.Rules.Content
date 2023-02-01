---
type: rule
archivedreason: 
title: Do you know the correct way to develop Data Entry Forms?
guid: 98e8f4b2-a989-46a1-bbe7-f453baa414ae
uri: do-you-know-the-correct-way-to-develop-data-entry-forms
created: 2014-12-01T00:36:14.0000000Z
authors: 
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects: []

---

Data Entrees should be able to use your data entry form with ease. It should contain a logical flow that they are familiar with to maximise efficiency and overall user satisfaction.

<!--endintro-->

::: bad  
![Figure: Bad Example - New button should open another form, and Delete button should be on that new form](../../assets/BadAddDeleteSubForm.gif)  
:::


### 1. Form states and how to respond to them

The form is to be aware of the data state. If the data is dirty:

* The Apply button would be enabled until the record is saved
* The OK button would simply save the record and close the Form
* The Cancel button would pop up a dialog (shown in the figure below) asking to save changes;

If the user decides to save, it should save the record and close the form.   
If No, then close the form without saving.   
If Cancel, then return back to the dirty form.

For more information, read [Do you label your form buttons consistently?](/do-you-label-your-form-buttons-consistently) 

### 2. Searching on the data entry

Do not add buttons for searching on the data entry form, create a new form for search, through which you can open new instances of the form. The convenience of the search capability on the form will be overlooked as it makes the form more crowded. Another issue which can arise is if Sally searches for a criteria which returns multiple records, she cannot look at all those records. She can only open one at a time, navigating through them. The solution to the search dilemma is to create a new search form, which is shown in the figure below. The search form will allow multiple criteria, will not over crowd the data entry form, and will show you all the results that your search has retrieved.

::: bad  
![Figure: Bad Example - This implementation of a search utility is on the same form](../../assets/BadSearch.gif)  
:::

::: good  
![Figure: Good Example - This implementation of Search feature is on a separate form](../../assets/SearchForm.gif)  
:::

### 3. Button functionality for sub-forms

When including a sub-form in your main form (as shown in figure below), the options the user should generally have are "New", "Edit" and "Delete". When any of these options are selected, and data is created, updated or deleted, the datasource should **not** be modified until the parent form is saved or submitted. This allows the user to easily roll back their mistakes by simply refreshing the browser.


### 4. Validation

Validation is a essential of any form development, with the majority of fields requiring validation of some description. The three categories of validation include:

* Required - the field should be filled in
* Formatting - the field must be in a correct format. e.g. currency or date
* Logical - the field needs to pass some validation tests in the business layer

For more information, read [Validation - Do you put focus to the correct control on validation error?](/validation-do-you-put-focus-to-the-correct-control-on-validation-error) 

### 6. Relevant Menus

Make sure that the menu items are relevant to the current form. The main idea is that we don't want to show the user any dummy menu items. However, this may become complex when a base form (containing the menu) is inherited. Access to menus in the base form must be granted (maybe through properties), so that each menu can be customized according to each child form.

::: bad  
![Figure: Bad Example - Action and Tools are irrelevant on this form](../../assets/MenuBadExample.jpg)  
:::

::: good  
![Figure: Good Example - Menus are relevant](../../assets/MenuGoodExample.jpg)  
:::

In the above example, there are a couple of unused menus that have been inherited from the base form and not set to invisible.

### 7. Field Formatting

Ensure that the data is displayed in correct format. For example, when presenting a percentage data in a field, make sure it is displayed as '% xx.xx'.

To accompany formatting, you must also create a parse function for putting the correct value back in the database.

**Note:** This can be difficult for data bound fields, and in that case you will have to handle the parse and format event of the Field's Binding object. An example of handling these events is shown below.

``
            Dim controlBinding As Binding = New System.Windows.Forms.Binding(propertyName,dataSource, dataMember)
            Dim controlBinding As Binding = New System.Windows.Forms.Binding(propertyName,dataSource, dataMember)
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
``
**Figure: Code - Code for Handling Parse and Format Events for Data bound Control**

The Binding is created and added to the Data-Bindings of the Control all in one line in Visual Designer in VS.Net. Do not use Visual Designer to data-bind if you will be handling the Parse and Format events. You will have to create the handlers yourself.

### 8. Created/Last Updated By Fields

With all database entries, there are always some fields that are used over and over again. For example, these fields may be created date, created by, last updated date, updated by, etc.

A common UI to use for these fields can be seen in the example below. What we do is create a user control that is identical across all projects/UI.

::: bad  
![Figure: Bad Example - This form has no information to indicate who created this entry and who last modified it](../../assets/BadCreatedUpdated.jpg)  
:::

::: good  
![Figure: Good Example - This form contains Created by/Updated by fields used in a standard control which is put into all forms](../../assets/GoodCreatedUpdated.jpg)  
:::

An example of how to set the values for this user control is shown below.
``    
            updatedBy.CreatedDate = .DateCreated
            updatedBy.CreatedBy = .EmpCreated
            updatedBy.UpdatedDate = .DateUpdated
            updatedBy.UpdatedBy = .EmpUpdated
``
**Figure: Code - Code for Setting values for User Control**

Databinding is also available to be used with this user control.

![Figure: Data Binding using the Designer](../../assets/CommonFieldsDB.gif)  

### 9. Minimum Defaults

In many situations, there is a need for field defaults. These defaults can be extracted from a existing data object or a dynamic source. These values increase the efficicy of data entry and overall user satisfaction, allowing trival or repeatitive entries to be automatically filled. 

However, When a new form is opened ensure that only necessary defaults are loaded. By default some decimal fields will become 0.0, but make sure they are set to blank if they are required fields.

### 10. Resizing

Is the form resizable? What happens if the user resizes and/or maximizes the form?

With the diversity of modern devices used to access web-based applications, responsive design is a essental part of form development, ensuring that the fields can be accessed. Generally, the size of the form field should also be indicative of the amount of data it should posess.

For more information, read [Validation - Do you put focus to the correct control on validation error?](/validation-do-you-put-focus-to-the-correct-control-on-validation-error) 
