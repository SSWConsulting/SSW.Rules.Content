---
type: rule
archivedreason: 
title: Do You Help Users By Selecting A Default Field
guid: 052a145d-827a-435d-afb7-d80911e36266
uri: do-you-help-users-by-selecting-a-default-field
created: 2012-04-19T04:31:18.0000000Z
authors: []
related: []
redirects: []

---

Help your users by setting the default field when your MVC WebSite loads. 
<!--endintro-->

By selecting a default field for your users when a page loads you can improve the usability of your web site by reducing the amount of steps needed to perform a task.




Here is a way to do this with MVC 3 and Razor:

1. Add a div with a class around the field you want to set focus on





> ```
> <div class="focus">
> ```
> 
> 
> 
> ```
> @Html.EditorFor(model => model.FirstName)
>     @Html
> ```
> 
> 
> 
> ```
> @Html.ValidationMessageFor(model => model.FirstName)
> ```
> 
> 
> 
> ```
> </div>
> ```






2. Then use jQuery to select the class and set focus:






> ```
> $(function() {
> ```
> 
> 
> 
> ```
> $('.focus :input').focus();
> ```
> 
> 
> 
> ```
> });
> ```
