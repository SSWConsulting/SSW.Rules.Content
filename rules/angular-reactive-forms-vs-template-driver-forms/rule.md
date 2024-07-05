---
type: rule
tips: ""
title: Do you know when to use Reactive Forms vs Template-driven Forms in Angular?
uri: angular-reactive-forms-vs-template-driver-forms
authors:
  - title: ""
created: 2024-07-05T07:06:37.135Z
guid: 0643130f-a25d-41c3-bfc8-3d9029cf1244
---
Angular provides two approaches to building forms: Reactive Forms and Template-driven Forms. Understanding the differences between them can help you choose the right approach for your project.
            
<!--endintro-->

### Template-driven Forms
Template-driven Forms are more suitable for simpler forms. They are easier to implement and work with, at a cost of less flexibility.
 They rely heavily on Angular's directives and are defined directly in the HTML template.

When to use Template-driven Forms:
- When the form logic is simple.
- When you prefer a less structured and more declarative approach.
- When you are working on a smaller project or a quick prototype.



### Reactive Forms
Reactive Forms are the preferred approach. They are more powerful and scalable. They are built around a model-driven approach, providing more control and flexibility in form validation and data handling.

When to use Reactive Forms:
- When you need more complex form validation logic.
- When the form is dynamic (fields are added or removed at runtime).
- When you prefer a more structured and predictable approach to form handling.
- When you need to handle form data within the component class.

### Which one should I use?
Choosing between Reactive Forms and Template-driven Forms depends on the complexity of your form. Reactive Forms offer more control and flexibility, making them ideal for complex scenarios, while Template-driven Forms provide a simpler and more declarative approach, suitable for straightforward forms.


2. Place your content here. Markdown is your friend. See this [example rule](https://www.ssw.com.au/rules/rule) for all the things you can do with Rules.
3. Submit your rule for review.
4. Add your rule to a category. See [How to Add and Edit Categories and Top Categories](https://github.com/SSWConsulting/SSW.Rules.Content/wiki/How-to-Add-and-Edit-Categories-and-Top-Categories).
