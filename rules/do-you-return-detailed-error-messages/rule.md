---
type: rule
archivedreason: 
title: Do you return detailed error messages?
guid: 7af36676-1eed-48dd-854b-2a956ef10e50
uri: do-you-return-detailed-error-messages
created: 2015-08-27T01:00:17.0000000Z
authors:
- title: Jeremy Cade
  url: https://ssw.com.au/people/jeremy-cade
related: []
redirects: []

---


<p>Good error design is as important to the sucess of an API as the API design itself. A good error message provides context and visibility on how to troubleshoot and resolve issues at critical times. <br></p>
<br><excerpt class='endintro'></excerpt><br>
<h3 class="ssw15-rteElement-H3">Start by using the correct HTTP Status Codes.</h3><p>The HTTP/1.1 RFC lists over 70 different HTTP Status&#160;Codes. Very few developers will be able to remember all of them, so it pays to keep it simple and use the most common Status Codes. The basic rule is to use the following three&#58;<br></p><ul><li><strong>200 OK</strong> - Everything worked. Success</li><li><strong>400 Bad Request</strong> - The consuming application did something wrong.<br></li><li><strong>500 Internal Server Error</strong> - The API Application did something wrong.</li></ul><h3 class="ssw15-rteElement-H3">Make your error messages as verbose as possible.</h3><p>Error messages should contain a sufficient level of information that a developer or consuming client can act upon.<br></p><p class="ssw15-rteElement-CodeArea">&#123;<br>&#160;&#160;&#160; &quot;<span>errorMessage</span>&quot;&#58; &quot;An error has occurred.&quot;<br>&#125;</p><dd class="ssw15-rteElement-FigureBad">Figure&#58; Bad Example - The error message does not contain information that can be acted upon.</dd><p class="ssw15-rteElement-CodeArea">&#123;<br>&#160;&#160;&#160; &quot;<span>errorMessage</span>&quot;&#58; &quot;Client ID is a required field. Please provide a Client ID.&quot;<br>&#125;<br></p><dd class="ssw15-rteElement-FigureGood">Figure&#58; Good Example - The error message provides explicit detail and a short description on how to fix the issue.</dd><h3 class="ssw15-rteElement-H3">Provide a Tracking or Correlation ID</h3><p>A tracking or correlation ID will allows the consuming clients to provide the API developers with a reference point in their logs. </p><p class="ssw15-rteElement-CodeArea">&#123;<br>&#160;&#160;&#160; &quot;errorMessage&quot;&#58; &quot;An error has occurred. Please contact technical support&quot;<br>&#125;<br></p><dd class="ssw15-rteElement-FigureBad">Figure&#58; Bad Example - No tracking or correlation ID is provided.</dd><p class="ssw15-rteElement-CodeArea">&#123;<br>&#160;&#160;&#160; &quot;errorMessage&quot;&#58; &quot;An error has occurred. Please contact technical support&quot;,<br>&#160;&#160;&#160; &quot;errorId&quot;&#58; &quot;3022af02-482e-4c06-885a-81d811ce9b34&quot;<br>&#125;</p><dd class="ssw15-rteElement-FigureGood">Figure&#58; Good Exmaple - A error ID is provided as part of the reponse.</dd><h3 class="ssw15-rteElement-H3">Provide an additional Help Resource</h3><p>Providing a URI to an additional help resources as part of your request will allow consuming clients to&#160;find additional resources or&#160;documentation that relates to the defined problem.&#160; <br></p><p class="ssw15-rteElement-CodeArea"><code>&#123;
  <br>&#160; &quot;ErrorType&quot;&#58; &quot;DoesNotExist&quot;,
  <br>&#160; &quot;Id&quot;&#58; &quot;3022af02-482e-4c06-885a-81d811ce9b34&quot;,
  <br>&#160; &quot;Message&quot;&#58; &quot;No Client with a ID of 999999999 was found&quot;,
  <br>&#160; &quot;StatusCode&quot;&#58; 404
<br>&#125;</code></p><dd class="ssw15-rteElement-FigureBad"><code></code>Figure&#58; Bad Example - No Help Link Provided<br></dd><p class="ssw15-rteElement-CodeArea"><code>&#123;
  <br>&#160; &quot;ErrorType&quot;&#58; &quot;DoesNotExist&quot;,
  <br>&#160; &quot;HelpLink&quot;&#58; &quot;http&#58;//www.myapiapplication/api/help/doesnotexist&quot;,
  <br>&#160; &quot;Id&quot;&#58; &quot;3022af02-482e-4c06-885a-81d811ce9b34&quot;,
  <br>&#160; &quot;Message&quot;&#58; &quot;No Client with a ID of 999999999 was found&quot;,
  <br>&#160; &quot;StatusCode&quot;&#58; 404
<br>&#125;</code></p><dd class="ssw15-rteElement-FigureGood">Figure&#58; Good Example - A help link is provided as part of the response.<br></dd><dt><br></dt>


