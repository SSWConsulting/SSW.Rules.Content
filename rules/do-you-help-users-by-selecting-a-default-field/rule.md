---
type: rule
title: Do You Help Users By Selecting A Default Field
uri: do-you-help-users-by-selecting-a-default-field
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
related: []
redirects: []
created: 2012-04-19T04:31:18.000Z
archivedreason: null
guid: 052a145d-827a-435d-afb7-d80911e36266
---
Help your users by setting the default field when your MVC Website loads. 

By selecting a default field for your users when a page loads you can improve the usability of your website by reducing the amount of steps needed to perform a task.

<!--endintro-->

Here is a way to do this with MVC 3 and Razor:

1. Add a div with a class around the field you want to set focus on
```html
<div class="focus">
    @Html.EditorFor(model => model.FirstName)
    @Html.ValidationMessageFor(model => model.FirstName)
</div>
```

2. Then use jQuery to select the class and set focus:
```html
$(function() {
    $('.focus :input').focus();
});
```
