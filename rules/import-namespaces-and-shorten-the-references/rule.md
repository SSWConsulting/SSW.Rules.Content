---
type: rule
archivedreason: 
title: Do you import namespaces and shorten the references?
guid: 0bf92b2c-b378-4e05-bd4c-d91f783138ac
uri: import-namespaces-and-shorten-the-references
created: 2018-04-25T22:28:24.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
- do-you-import-namespaces-and-shorten-the-references

---


You should import namespaces and shorten the references.<br>
<br><excerpt class='endintro'></excerpt><br>
<p class="ssw15-rteElement-CodeArea">​System.Text.StringBuilder myStringBuilder = new System.Text.StringBuilder();<br></p><dd class="ssw15-rteElement-FigureBad">Figure: Bad code - Long reference to object name​​<br></dd><p class="ssw15-rteElement-CodeArea">using System.Text;<br>...<br>...<br>StringBuilder myStringBuilder = new StringBuilder(); </p><dd class="ssw15-rteElement-FigureGood">Figure: Good code - Import the namespace and remove the repeated System.Text reference<br></dd><p>​<br></p><p>If you have ReSharper installed, you can let ReSharper take care of this for you:</p><dl class="image"><dt>
      <img src="ReSharperReformatCode.gif" alt="ReSharperReformatCode.gif" />
   </dt><dd>Figure: Right click and select "Reformat Code..."<br></dd></dl><dl class="image"><dt>
         <img src="ReSharperShortenReferences.gif" alt="ReSharperShortenReferences.gif" />
      </dt><dd>Figure: Make sure "Shorten references" is checked and click "Reformat"​<br></dd></dl>​​<br>


