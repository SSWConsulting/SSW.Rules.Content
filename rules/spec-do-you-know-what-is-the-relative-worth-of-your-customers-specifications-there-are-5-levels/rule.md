---
type: rule
archivedreason: 
title: Spec - Do you know how thorough your customer's specifications are? (There are 5 levels)
guid: 4e313ea3-4b70-41fd-b579-10f76f5ee919
uri: spec-do-you-know-what-is-the-relative-worth-of-your-customers-specifications-there-are-5-levels
created: 2011-02-28T08:25:37.0000000Z
authors:
- title: Eric Phan
  url: https://ssw.com.au/people/eric-phan
- title: Ulysses Maclaren
  url: https://ssw.com.au/people/ulysses-maclaren
related: []
redirects:
- spec-do-you-know-what-is-the-relative-worth-of-your-customers-specifications-(there-are-5-levels)
- spec-do-you-know-how-thorough-your-customers-specifications-are-there-are-5-levels
- spec-do-you-know-how-thorough-your-customers-specifications-are-(there-are-5-levels)

---


Different clients will have different levels of documentation on what they want to be built. You need to be ready to do a spec review&#160;for any one of the following 5 possible cases&#58;<br>
<br><excerpt class='endintro'></excerpt><br>
<h4>Types of specifications</h4><h3 class="ssw15-rteElement-H3">1. I have an idea...</h3><p>Run from this<br>or<br>verify they have a really hefty bank account!</p><h3 class="ssw15-rteElement-H3">2.&#160;High-Level Requirements Document</h3><p class="ssw15-rteElement-GreyBox">This will read like a wish list with no details and many unanswered questions</p><dd class="ssw15-rteElement-FigureNormal">Figure&#58; High-Level Requirements are very vague and open to many interpretations</dd><h3 class="ssw15-rteElement-H3">3. Detailed Requirements Document</h3><ul class="ms-rteCustom-GreyBox">The details have been fleshed out and allow developers to write Functional and Technical Specifications<br> 
   <li>We need a login page for www.northwind.com</li><li>Must match existing site look and feel</li><li>Username is already in the Users table in the ABC database (SQL Server 2008)</li><li>Password should be at least 8 characters</li><li>.NET 4 is already used for the existing site so that is what this should use of course</li><li>Should look like this&#58;<br><img src="/PublishingImages/LoginInterface.jpg" alt="" />  </li></ul>
<font class="ms-rteCustom-FigureNormal" size="+0">Figure&#58; Detailed Requirements have more of the details you want </font> 
<h3 class="ssw15-rteElement-H3">4. Functional Specification</h3>This will include detailed mock-ups for the UI, use cases/user stories and might be at a level to allow for fixed price quoting on the project<ul class="ms-rteCustom-GreyBox"><li>We need a login page for <a href="http&#58;//www.northwind.com/" shape="rect">www.northwind.com</a> </li><li>Must match existing site look and feel</li><li>Users table must be defined and added to the ABC database (SQL Server 2008)</li><li> 
      <b>User Name consists of user first initial and first 7 characters of the last name</b><br>- <b>For example Joe Jones -{gtHTMLChar} jjones</b> </li><li>Password should be at least 8 characters</li><li>Site uses .NET 4 and this interface must be added to existing project</li><li>This is the layout for the login interface</li><li> 
      <b>A red asterisk (*) should be displayed if a value is left blank and Submit is pressed</b><br><img src="/PublishingImages/LoginInterface.jpg" alt="" /> </li></ul>
<font class="ms-rteCustom-FigureNormal" size="+0">Figure&#58; Functional Specifications go into more detail about the user interface and interactions in the system</font> 
<h3>5. Technical&#160;Specification<br></h3><p>This is the blueprint for the application. There should be no unanswered questions and should allow for a fixed price quote.</p><ul class="ms-rteCustom-GreyBox"><li>We need a login page for www.northwind.com</li><li>Must match existing site look and feel</li><li>Users table must be defined and added to the ABC database (SQL Server 2008)</li><li>User Name consists of user first initial and first 7 characters of the last name</li><li>For example Joe Jones -{gtHTMLChar} jjones</li><li>Password should be at least 8 characters</li><li>Site uses .NET 4 and this interface must be added to existing project</li><li>Define the data model explicitly<br><img src="/PublishingImages/Table.jpg" alt="" /> </li><li>Must work with IE7, IE8, IE9 and FF3</li><li>Must display correctly at 1024x768 resolution</li><li>Must support ANSI characters for Username and Password</li><li>Will not support mobile browsers</li><li>Will not be tested with localization (assumes en-us local on US versions of software)</li><li>SQL Membership provider will be leveraged<br></li></ul>
   <font class="ms-rteCustom-FigureNormal" size="+0">Figure&#58; Technical Specifications will become the blueprint of the application. There shouldn’t be any unknowns​</font>


