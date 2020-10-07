---
type: rule
archivedreason: 
title: Do you use the MVVM Pattern?
guid: 4c5adf6a-bb9c-44b3-845b-94cbd7fa9dda
uri: do-you-use-the-mvvm-pattern
created: 2020-10-07T22:03:25.0000000Z
authors:
- id: 1
  title: Adam Cogan
- id: 97
  title: Matt Goldman
related: []

---


Xamarin follows the MVVM design pattern (see&#58;&#160;<a href="/_layouts/15/FIXUPREDIRECT.ASPX?WebId=3dfc0e07-e23a-4cbb-aac2-e778b71166a2&amp;TermSetId=07da3ddf-0924-4cd2-a6d4-a4809ae20160&amp;TermId=4d4194a8-4a95-4809-80b6-ae71a2ba5c8f">Do you use the MVVM pattern in your Silverlight and WPF Projects?</a>). MVVM was originally developed for WPF but is the dominant paradigm in Xamarin development (at least until 2021 when Xamarin.Forms evolves into MAUI, which will make the MVU pattern a first-class citizen. See&#58; <a href="https&#58;//devblogs.microsoft.com/dotnet/introducing-net-multi-platform-app-ui/">Introducing .NET Multi-platform App UI</a>.​)<br>
<br><excerpt class='endintro'></excerpt><br>
<p>MVVM allows for loose coupling between data, business logic, and UI. In Xamarin, UI is usually defined in XAML (although you can declaratively define your UI in C# code too). Your UI is called a 'view' - a view can be a page or a UI element, although UI elements that are not complete pages are more often referred to as 
   <em>controls</em>.&#160;<img src="file&#58;///Users/tiagoaraujo/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image001.png" alt="" style="width&#58;452px;margin&#58;5px;" /></p><dl class="badImage"><dt><img src="/PublishingImages/mvvm-bad.png" alt="mvvm-bad.png" style="width&#58;750px;" /></dt><dd>Figure&#58; Bad Example - Logic and properties are in the code behind, which decreases maintainability and leads to antipatterns like async void</dd></dl><dl class="goodImage"><dt><img src="/PublishingImages/mvvm-good.png" alt="mvvm-good.png" style="width&#58;750px;" /></dt><dd>Figure&#58; Good Example - Values are bound to properties of the ViewModel, and actions are bound to Commands in the ViewModel​<br></dd></dl><p>Xamarin supports MVVM out of the box, but there are several MVVM frameworks available that enhance this functionality. For example, some MVVM frameworks support &quot;convention over configuration&quot;, allowing you to just code your View and ViewModel and let the framework hook them up for you. Some include&#58;<br></p><ul><li>
      <b>Prism&#58;</b> Prism is an MVVM framework that was developed initially for WPF but has since been ported to Xamarin Forms. It is stable and mature.&#160;<a href="https&#58;//github.com/PrismLibrary/Prism">https&#58;//github.com/PrismLibrary/Prism</a></li><li>
      <b>FreshMVVM&#58;</b> FreshMVVM is a framework that was built from the ground up specifically for Xamarin Forms. It is open-source and maintained by a Microsoft and Xamarin MVP.&#160;<a href="https&#58;//github.com/rid00z/FreshMvvm">https&#58;//github.com/rid00z/FreshMvvm</a><br></li><li>
      <b>MVVMLight&#58;</b> This is another framework built especially for Xamarin, although it is not currently under active maintenance.&#160;<a href="https&#58;//github.com/lbugnion/mvvmlight">https&#58;//github.com/lbugnion/mvvmlight</a><br></li></ul>


