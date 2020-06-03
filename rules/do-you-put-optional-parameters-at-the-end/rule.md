---
type: rule
title: Do you put optional parameters at the end?
uri: do-you-put-optional-parameters-at-the-end
created: 2018-04-26T23:44:44.0000000Z
authors:
- id: 1
  title: Adam Cogan

---



<span class='intro'> Optional parameters should be placed at the end of the method signature as optional ones tend to be less important. You should put the important parameters first.<br><br> </span>

<p class="ssw15-rteElement-CodeArea">public void SaveUserProfile(<br>[Optional] string username,<br>[Optional] string password,<br>string firstName,<br>string lastName, <br>[Optional] DateTime? birthDate) <br></p><dd class="ssw15-rteElement-FigureBad">Figure&#58; Bad Example - Username and Password are optional and first - they are less important than firstName and lastName and should be put at the end</dd><p>​<br></p><p class="ssw15-rteElement-CodeArea">public void SaveUserProfile(<br>string firstName,<br>string lastName, <br>[Optional] string username,<br>[Optional] string password,<br>[Optional] DateTime? birthDate) <br></p><dd class="ssw15-rteElement-FigureGood">Figure&#58; Good Example - All the optional parameters are the end</dd><p>
   <br>
</p><p>
   <b>Note&#58; </b>When using optional parameters, please be sure to use&#160;<a href="/_layouts/15/FIXUPREDIRECT.ASPX?WebId=3dfc0e07-e23a-4cbb-aac2-e778b71166a2&amp;TermSetId=07da3ddf-0924-4cd2-a6d4-a4809ae20160&amp;TermId=ba22dc4c-aec4-471d-8157-0a540ddf6310">named para meters</a> <br></p>


