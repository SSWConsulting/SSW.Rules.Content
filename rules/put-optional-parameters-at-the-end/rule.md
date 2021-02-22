---
type: rule
archivedreason: 
title: Do you put optional parameters at the end?
guid: 319aec53-73ec-4049-8d58-8d0bd84fc246
uri: put-optional-parameters-at-the-end
created: 2018-04-26T23:44:44.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
- do-you-put-optional-parameters-at-the-end

---


Optional parameters should be placed at the end of the method signature as optional ones tend to be less important. You should put the important parameters first.<br><br>
<br><excerpt class='endintro'></excerpt><br>
<p class="ssw15-rteElement-CodeArea">public void SaveUserProfile(<br>[Optional] string username,<br>[Optional] string password,<br>string firstName,<br>string lastName, <br>[Optional] DateTime? birthDate) <br></p><dd class="ssw15-rteElement-FigureBad">Figure&#58; Bad Example - Username and Password are optional and first - they are less important than firstName and lastName and should be put at the end</dd><p>​<br></p><p class="ssw15-rteElement-CodeArea">public void SaveUserProfile(<br>string firstName,<br>string lastName, <br>[Optional] string username,<br>[Optional] string password,<br>[Optional] DateTime? birthDate) <br></p><dd class="ssw15-rteElement-FigureGood">Figure&#58; Good Example - All the optional parameters are the end</dd><p>
   <br>
</p><p>
   <b>Note&#58; </b>When using optional parameters, please be sure to use&#160;<a href=/when-to-use-named-parameters>named para meters</a> <br></p>


