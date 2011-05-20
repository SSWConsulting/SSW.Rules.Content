---
type: rule
title: Do you use the MVVM pattern in your Silverlight and WPF Projects?
uri: do-you-use-the-mvvm-pattern-in-your-silverlight-and-wpf-projects
created: 2011-05-20T07:30:32.0000000Z
authors:
- id: 1
  title: Adam Cogan

---



<span class='intro'> The term MVVM means Model-View-ViewModel design pattern. This pattern is an adaptation of the MVC and MVP patterns in which the view model provides a data model and behavior to the view but allows the view to declaratively bind to the view model. The view becomes a mix of XAML and C# (as WPF or Silverlight controls), the model represents the data available to the application, and the view model prepares the model in order to bind it to the view.
 </span>

The most important aspect of WPF or Silverlight that makes MVVM a great pattern to use is the data binding infrastructure. By binding properties of a view to a ViewModel, you get loose coupling between the two and entirely remove the need for writing code in a ViewModel that directly updates a view. In a sense, Views and unit tests are just two different types of ViewModel consumers. Having a suite of tests for an application's ViewModels provides free and fast regression testing, which helps reduce the cost of maintaining an application over time.<br>
<a href="http&#58;//msdn.microsoft.com/en-us/magazine/dd419663.aspx">A good article about MVVM</a>



