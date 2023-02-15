---
type: rule
archivedreason: 
title: Do you know the correct way to develop Web-based Data Entry Forms?
guid: 98e8f4b2-a989-46a1-bbe7-f453baa414ae
uri: data-entry-forms-for-web
created: 2014-12-01T00:36:14.0000000Z
authors: 
- title: Toby Churches
  url: https://github.com/TobyChurches
- title: Piers Sinclair
  url: https://www.ssw.com.au/people/piers-sinclair
related: []
redirects: []

---

Data Entrees should be able to use your data entry form with ease. It should contain a logical flow that they are familiar with to maximise efficiency and overall user satisfaction.

<!--endintro-->

::: bad  
![Figure: Bad example - This old Microsoft Access form is poorly designed, containing a number of design flaws that would today be considered bad practice](../../assets/BadAddDeleteSubForm.gif)  
:::

### 1. Form states and how to respond to them

When developing a form, it is ideal for the form to be aware of the state of its data, determining if the state has been modified and behaving accordingly. If the data is dirty:

* The "Save" button would be enabled until the record is saved
* The "Save and Close" button would simply save the record and close the Form
* The "Cancel" button would pop up a dialog asking to save changes

Additionally, these form action buttons should be [labelled consistently](/label-buttons-consistently/) across the application.  

### 2. No Delete Button for Grids in Main forms

When including a grid of information within your main form (as shown in the figure below), the only options the user should generally be presented are "New" and "Edit". When the "Edit" button is selected, all of the data associated with that record should be made visible to the user. This expansion should also present a option to "Delete". This forces the user to examine all of the information before deleting.

::: good  
![Figure: Good example - This form grid contains no delete button, requiring the user to examine the entire record via "Edit" before deletion](./NoDeleteButtonOnGrid.png)  
:::

However, this rule is contextual. For instances where the importance of the data is trivial or all of the necessary information is immediately presented within the grid, it would be acceptable to include a "Delete" or "Remove" button on the main form.

::: good  
![Figure: Good example - This form grid contains delete button becasue all of the required information can be seen from the main form](./AppropriateUseOfRemove.png)  
:::

### 3. Validation

Validation is essential for any form development, with the majority of fields requiring validation of some description. The 3 main categories of validation include:

* Required - The field should be filled in
* Formatting - The field must be in the correct format. e.g. currency or date
* Logical - The field needs to pass some validation tests in the business layer

Furthermore, the desired behaviour for when a validation error occurs is to take the user back to improper field via a scrolling motion. This is particularly important for mobile devices where the responsive layout may cause the form to be extended, requiring further effort to identifty the issue. 

You should also [put focus to the correct control on validation error](/validation-do-you-put-focus-to-the-correct-control-on-validation-error). 

### 4. Field Formatting

With the various requirements of different forms, field formatting is essential, ensuring that the data is displayed in a logical manner for the particular input. To guarantee consistency across your data entry forms, we suggest that the following conventions are followed:

* Numerical values contain decimal places
* Numerical values have right-alignment
* Currency and Percentage fields contain relevant notation (i.e. '% xx.xx') 
* Data is converted into the database standard format before being saved

**Note:** This format conversion can be difficult for data-bound fields. Luckily, many frameworks such as Angular provide convenient methods for handling such situations. In the following code extract, an example of angular pipes can be seen to format the currency and percentage fields.

``` html
<div>
    <!-- When amount = 10 , output = '$ 10.00' -->
    <p>Currency: {{ amount | currency}}</p>

    <!-- When percentage = 0.1 , output = '10.00 %' -->
    <p>Percentage: {{ percentage | percent: '1.2-5'}}
</div>
```
**Figure: Code - Angular Pipes for formatting data**

Alternatively, this could be done by triggering a transformation method in the typescript file with event binding. This would ensure that the input field would be reformated when modified.

### 5. Created/Last Updated By Fields

For the purposes of logging and change history, it is highly recommended that the following information is maintained:

* **DateCreated** - The date on which the record was created
* **EmployeeCreated** - The employee responsible for its creation 
* **DateUpdated** - The date on which the record was last updated
* **EmployeeUpdated** - The employee that last updated the record 

This will assist with accountability, allowing users to quickly see information about recent changes.

Additionally, these fields of the form should remain 'Read only' ensuring that the data is accurate and reliable.

::: bad  
![Figure: Bad example - This form does not contain Created by/Updated by fields](./NoCreatedUpdatedField.png)  
:::

::: good  
![Figure: Good example - This form contains Created by/Updated by fields](./FormWithCreatedUpdatedFields.png)  
:::

### 6. Minimum Defaults

In many situations, there is a need for field defaults. These defaults can be extracted from an existing data object or a dynamic source (Such as the system time). These values increase the efficiency of data entry and improve the overall user satisfaction, allowing trivial or repetitive entries to be automatically filled. 

However, when a new form is opened ensure that only necessary defaults are loaded. By default, some decimal fields will become '0.0', but make sure they are set to blank if they are required fields.

### 7. Resizing

Is the form resizable? What happens if the user resizes and/or maximizes the form?

With the diversity of modern devices used to access web-based applications, responsive design is an essential part of form development, ensuring that the fields can be accessed. Generally, the size of the form field should also be indicative of the amount of data it should possess.

For more information, read about [providing alternate sizings for Bootstrap columns](/do-you-provide-alternate-sizings-for-bootstrap-columns/).
