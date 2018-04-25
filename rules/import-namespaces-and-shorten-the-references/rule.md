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
<p class="ssw15-rteElement-CodeArea">​System.Text.StringBuilder myStringBuilder = new System.Text.StringBuilder();<br></p><dd class="ssw15-rteElement-FigureBad">Figure&#58; Bad code - Long reference to object name​​<br></dd><p class="ssw15-rteElement-CodeArea">using System.Text;<br>...<br>...<br>StringBuilder myStringBuilder = new StringBuilder(); </p><dd class="ssw15-rteElement-FigureGood">Figure&#58; Good code -&#160;Import the namespace and remove the repeated System.Text reference<br></dd><p>​<br></p><p>If you have&#160;ReSharper&#160;installed, you can let ReSharper take care of this for you&#58;</p><dl class="image"><dt>
      <img src="/PublishingImages/ReSharperReformatCode.gif" alt="ReSharperReformatCode.gif" />
   </dt><dd>Figure&#58; Right click and select &quot;Reformat Code...&quot;<br></dd></dl><dl class="image"><dt>
         <img src="/PublishingImages/ReSharperShortenReferences.gif" alt="ReSharperShortenReferences.gif" />
      </dt><dd>Figure&#58; Make sure &quot;Shorten references&quot; is checked and click &quot;Reformat&quot;​<br></dd></dl>​​<br>


