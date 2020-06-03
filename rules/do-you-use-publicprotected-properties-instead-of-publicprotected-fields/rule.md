---
type: rule
title: Do you use Public/Protected Properties instead of Public/Protected Fields?
uri: do-you-use-publicprotected-properties-instead-of-publicprotected-fields
created: 2018-04-25T21:45:02.0000000Z
authors:
- id: 1
  title: Adam Cogan

---



<span class='intro'> <p>Public/Protected properties have a number of advantages over public/protected fields&#58;</p><ul><li><strong>Data validation</strong><br>Data validation can be performed in the get/set accessors of a public property. This is especially important when working with the Visual Studio .NET Designer.</li><li><strong>Increased flexibility</strong><br>Properties conceal the data storage mechanism from the user, resulting in less broken code when the class is upgraded. Properties are a recommended object-oriented practice for this reason.</li><li><strong>Compatibility with data binding</strong><br>You can only bind to a public property, not a field.</li><li><strong>Minimal performance overhead</strong><br>The performance overhead for public properties is trivial. In some situations, public fields can actually have inferior performance to public properties.​<br></li></ul> </span>

<p class="ssw15-rteElement-CodeArea">​public int Count; </p><dd class="ssw15-rteElement-FigureBad">Figure&#58; Bad code. Variable declared as a Field<br></dd><p class="ssw15-rteElement-CodeArea">public int Count<br>&#123;<br> get<br> &#123;<br> return _count;<br> &#125;<br> set<br> &#123;<br> _count = value; <br> &#125;<br>&#125;<br></p><dd class="ssw15-rteElement-FigureGood">Figure&#58; Good code. Variable declared as a Property​​<br></dd><p>We agree that the syntax is tedious and think&#160;<a href="https&#58;//www.ssw.com.au/ssw/Standards/BetterSoftwareSuggestions/VisualStudio.aspx#PropertyShortcut">Microsoft should improve this.</a>​<br><br></p>


