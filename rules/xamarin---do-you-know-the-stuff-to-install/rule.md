---
type: rule
archivedreason: 'Requested by Matt on RE: [SSW] Rules to Better Xamarin (mobile)'
title: Xamarin - Do you know the stuff to install?
guid: a167dacd-86d8-4ba7-8e6e-67a398b739a1
uri: xamarin---do-you-know-the-stuff-to-install
created: 2016-08-19T17:53:30.0000000Z
authors:
- id: 1
  title: Adam Cogan
related: []

---


​Installing Visual Studio is not enough.... There is another 2 hours plus of downloading and installing to get to your first successful Xamarin hello world app.<br>
<br><excerpt class='endintro'></excerpt><br>
<h3>Step 1</h3><p>Install VS 2015 + the Xamarin extension:  <a href="https://msdn.microsoft.com/en-us/library/mt613162.aspx" target="_blank">https://msdn.microsoft.com/en-us/library/mt613162.aspx</a></p><dl class="image"><dt> <img src="xamarin-1.png" alt="xamarin-1.png" /> </dt><dd>Figure: You need "C#/.NET (Xamarin v4.1.0)</dd></dl><p> 
   <b>Note:</b> Xamarin Studio doesn't exist on the PC anymore.<br></p><h3>Step 2 - Android SDK Manager<span class="s2"> (about 2 hours)</span></h3><p>This one is painful... <br></p><dl class="image"><dt> <img src="xamarin-2.png" alt="xamarin-2.png" /> </dt></dl><p>Then get all the ones that say "Installed" :<br></p><dl class="image"><dt> <img src="xamarin-3.png" alt="xamarin-3.png" /> </dt></dl><h3>Step 3 - "Manage NuGet Packages for Solution" (about 30 minutes)  <br></h3><p class="p2">Create a Blank App (xamarin.Forms Portable) project (this way it will trigger grabbing all extra stuff).<br><span style="line-height:1.6;">Check and ensure Nuget Packages are up to date . </span></p><dl class="image"><dt> <img src="xamarin-4.png" alt="xamarin-4.png" /> </dt></dl><dl class="image"><dt> <img src="xamarin-5.png" alt="xamarin-5.png" /> </dt></dl><h3>Step 4 - run the app<br></h3><p>Actually run the application you’ve created. Ensure it builds. It won't =D well first time it often won't, if it does then congratulations you have got everything!</p>


