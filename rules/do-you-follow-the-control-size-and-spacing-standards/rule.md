---
type: rule
archivedreason: 
title: Do you follow the control size and spacing standards?
guid: e06dfe0b-7271-45ab-b818-57a8223e37b2
uri: do-you-follow-the-control-size-and-spacing-standards
created: 2014-12-01T00:31:14.0000000Z
authors: []
related: []

---


<h3>Introduction</h3><p>Despite seeming trivial, the most subtle elements of your form can have the greatest impact on your users.</p>
<br><excerpt class='endintro'></excerpt><br>
<dl class="badImage"><dt>
      <img src="http&#58;//www.ssw.com.au/ssw/Standards/Rules/Images/ScreenBadControls.gif" alt="SSW SQL Auditor - Choose Data Source" style="margin&#58;5px;" />
   </dt><dd>Figure&#58; Bad Example - What's wrong with this form?</dd></dl><p>The form shown in this screenshot is an example of bad control placement&#58;</p><ol><li>The fonts used are non-standard (see&#58; 
      <a href="http&#58;//www.ssw.com.au/ssw/Standards/Rules/RulestoBetterInterfaces-Controls.aspx#Font"> Do you use Microsoft's Recommended Font in your Application?</a>)</li><li>The controls have 
      <strong>no consistency</strong> in terms of margins, spacing or even control alignment. See, for example&#58; 
      <ol><li type="a">The navigation buttons at the bottom of the screen having uneven margin space on the right and bottom sides. They're also the wrong size.</li><li type="a">The dimensions of all input controls and buttons do not follow standard convention (see below)</li><li type="a">The right side of the &quot;Build...&quot; button is not aligned with the right of the &quot;Connection String&quot; text box</li><li type="a">The left margins inside the two frames are inconsistent.</li><li type="a">The space surrounding the logo in the top right corner is uneven</li></ol></li></ol><p>This detracts from the visual appeal of the user interface, and results in an uneven user experience. After looking at all of this you may be thinking &quot;<strong>do I really need to work out exactly what spacing and dimensions I want to use for 
      <strong>every</strong> detail of a form I make?</strong>&quot;</p><p>The good news is that<strong> you don't need to</strong>&#58; Microsoft have gone to a great deal of effort to 
   <a href="http&#58;//www.ssw.com.au/ssw/Redirect/Microsoft/MSDNVisualDesign.htm">define standards</a> 
   <img src="http&#58;//www.ssw.com.au/ssw/images/external.gif" title="You are now leaving SSW" alt="" style="margin&#58;5px;" /> for exactly how your form controls should be laid out, and these standards are worth taking into consideration. By all means, if you have disagreements with anything listed here then please discuss it with us and we'll consider changing our own standards (Microsoft have changed theirs over the years, after all), but we recommend using the following as a guide.</p><p>These examples assume that you are using the standard system font as defined in the rule mentioned above. Please note that although Dialog Units (DLUs) are better suited for generic (font independent) use, they are not available in the Visual Studio designer.</p><dl class="goodImage"><dt>
      <img src="http&#58;//www.ssw.com.au/ssw/Standards/Rules/Images/GoodStandardForm.jpg" alt="SSW SQL Auditor - Choose a Data Source" style="margin&#58;5px;" />
   </dt><dd>Figure&#58; Good Example - The form follows Standards of good form design discussed below</dd></dl><h3>The Rules</h3><ol><li>
      <strong>Buttons must be...</strong> 
      <ul><li>Spaced apart by 6 pixels from other buttons 
            <strong>except</strong> in the case of wizards where the 
            <em>&lt; Back</em> and 
            <em>Next &gt;</em> buttons may be closer together</li><li>Spaced 6 pixels from the inside border of a form on the sides closest to it</li><li>usually 75 pixels wide</li><li>23 pixels high</li></ul></li><li>
      <strong>Single-line textboxes and most controls must be...</strong> 
      <ul><li>21 pixels high (width depends on content) </li><li>Aligned correctly with any related controls</li></ul></li><li>
      <strong>In a form...</strong> 
      <ul><li>Margins must be consistent (see 
            <a href="http&#58;//www.ssw.com.au/ssw/Redirect/Microsoft/MSDNMargins.htm" class="external">Microsoft's diagram illustrating this</a> 
            <img src="http&#58;//www.ssw.com.au/ssw/images/external.gif" title="You are now leaving SSW" alt="" style="margin&#58;5px;" />)</li></ul></li></ol><p>These are some of the more common examples. Please read Microsoft's 
   <a href="http&#58;//www.ssw.com.au/ssw/Redirect/Microsoft/MSDNLayout.htm" class="external">Visual Design Guidelines</a> 
   <img src="http&#58;//www.ssw.com.au/ssw/images/external.gif" title="You are now leaving SSW" alt="" style="margin&#58;5px;" /> for more information and greater detail.</p><p>
   <strong>Ultimately the goal of all of this is to ensure consistency</strong>. Keeping these ideas in mind at all times while doing user interface design will give users a better overall experience and will boost the professionalism of your products.</p><h3>One From The Good Guys</h3><p>Here's a good example for you to take inspiration from. This dialog is from Microsoft Outlook. Let's check out some points&#58;</p><ol><li>Consistency across wizard pages is very good</li><li>Spacing and sizing of buttons is precise</li><li>The logo has been positioned evenly</li></ol><dl class="goodImage"><dt>
      <img src="http&#58;//www.ssw.com.au/ssw/Standards/Rules/Images/ScreenGoodControls.gif" alt="Outlook - Email Accounts" style="margin&#58;5px;" />
   </dt><dd>Figure&#58; Good Example - Microsoft have defined to exacting measures what spacing should be used in their Microsoft Outlook wizards</dd></dl><p>Read more about control size on the 
   <a href="http&#58;//www.ssw.com.au/ssw/Standards/Rules/RulesToBetterWindowsForms.aspx#CommonControl"> Rules to Better Windows Forms</a> page</p><p class="productBox">We have a program called 
   <a href="http&#58;//www.ssw.com.au/ssw/CodeAuditor/Rules.aspx#SizeSpacing">SSW Code Auditor</a> to check for this rule.</p>


