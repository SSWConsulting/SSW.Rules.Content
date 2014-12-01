---
type: rule
archivedreason: 
title: Do you use a Wizard to help a user through a complicated set of steps?
guid: c49c5f6a-312c-4a94-921f-bcdffa5b6279
uri: do-you-use-a-wizard-to-help-a-user-through-a-complicated-set-of-steps
created: 2014-12-01T03:43:47.0000000Z
authors: []
related: []

---


<p>
                    Though all software should be intuitive there are still times when users need extra
                    guidance. Wizards are ideal especially for stepping through more complicated steps
                    or when an application isn't going to be used regularly. E.g. SSW Code Auditor may
                    only run once a month, during which time the user may forget all the steps involved.
                    You can see an example of all the relevant steps at <a href="http&#58;//www.ssw.com.au/ssw/CodeAuditor/UserGuide.aspx">
                        Code Auditor User Guide</a>.</p><p>
                    Most importantly when a first time a user tries your program, they should be able
                    to step through the setting up process. A wizard helps to show how your application
                    flows from beginning to end.</p>
<br><excerpt class='endintro'></excerpt><br>
<p>​To ensure a consistent user experience, make sure to include these visual elements&#58;
                </p><ol><li><strong>Page name.</strong> It is important for the user to know which page they
                        are currently on. </li><li><strong>Page description.</strong> You should provide a short description of the
                        task to be performed on the page. </li><li><strong>Instructions.</strong> Not required for every page, this is a short description
                        requesting the user to perform a task, for example, entering some values into a
                        text field. </li><li><strong>Company logo.</strong> This helps promote branding, however it should be
                        inconspicuous and should not move visual focus away from the body of your application.
                    </li></ol>
                <br>
                <dl class="goodImage"><dt>
                        <img border="0" alt="SSW Link Auditor - Scan Target" src="http&#58;//www.ssw.com.au/ssw/Standards/Rules/Images/GoodInformationFlow.gif" style="margin&#58;5px;width&#58;600px;" /></dt><dd>Figure&#58; Good Example - SSW Link Auditor Wizard's
                                better flow of information</dd></dl><p>
                    Technical Note&#58; To ensure visual consistency across applications, create a base
                    form then set the properties in that form (application icon, menu structure, button
                    names etc.) Add any logic in for switching pages with the &quot;Next&quot; and &quot;Back&quot;
                    buttons. Then for all projects, add a reference to that one and inherit the customized
                    form.</p><p>
                    In the forms in your application, instead of inheriting from <strong>System.Windows.Forms.Form</strong>
                    (the Default), inherit from your new base form class.
                </p><dl class="code"><dt><pre>public class MyForm &#58; System.Windows.Form.Form</pre></dt><dd>
                        Figure&#58; Default code in a Windows Form</dd></dl><dl class="code"><dt><pre>public class MyForm &#58; Company.Framework.BaseCustomForm</pre></dt><dd>
                        Figure&#58; Change the form so that it inherits from your new base form class</dd></dl><p>
                    The &quot;finish&quot; button denotes the end of the Wizard; by clicking on it,
                    the user closes the Wizard.</p><p>
                    For longer processes, the Wizard should implement &quot;Start&quot; and &quot;Skip&quot;
                    features to guide the user through from start to finish.</p><dl class="goodImage"><dt>
                        <img border="0" alt="SSW Code Auditor - Start Process" src="http&#58;//www.ssw.com.au/ssw/Standards/Rules/Images/StartProcess.gif" style="margin&#58;5px;width&#58;550px;" /></dt><dd>Figure&#58; Good Example - SSW Code Auditor Wizard featuring
                                &quot;Start&quot; and &quot;Skip&quot; options</dd></dl><p>
                    Here's some more information on the <a href="http&#58;//www.ssw.com.au/ssw/Redirect/Microsoft/wizard.htm" target="_blank">
                        Microsoft Standard for Wizard Welcome and Completion Page art</a> and <a href="http&#58;//www.ssw.com.au/ssw/Redirect/Microsoft/wizard2.htm" target="_blank">Interior Page art</a>.<br></p>


