---
type: rule
title: Do You Know Which Packages To Add To Your New MVC Project?
uri: do-you-know-which-packages-to-add-to-your-new-mvc-project
created: 2014-12-30T00:24:02.0000000Z
authors:
- id: 3
  title: Eric Phan
- id: 34
  title: Brendan Richards
- id: 24
  title: Adam Stephensen

---



<span class='intro'> ​​​When you create a new MVC project in Visual Studio it is important to include the right packages from the start. This makes the project more manageable and you become more efficient in producing your final result.<br> </span>

<p>​If you add old, obsolete or incorrect NuGet packages, the project will suffer and you might have decreased performance or scope creep as new requirements are discovered.&#160;</p><p>Avoid old technologies such as&#58;</p><ul><li> MVC W​​​​eb Forms</li><li> KnockoutJS</li></ul>
   
<span style="line-height&#58;1.6;">When ​you create a project you should be adding the following NuGet Packages&#58;</span><br> 
<ul><li>SSW.DataOnion<br></li><li>SSW.HealthCheck​<br></li><li>​​AutoFac</li><li>Seril​og​<br></li></ul><p>You should also add the following NPM  packages&#58;</p><ul><li>​Angular JS</li><li>​Bootstrap</li><li>Gulp<br></li></ul><p> 
   <strong>Note</strong>&#58; Prior to 2016, SSW recommend developers choose bower over NPM as their front end package manager. That recomendation has chan​ged due to the industry trend away from bower.</p><p> 
   <img alt="Bower_v_NPM.png" src="Bower_v_NPM.png" style="margin&#58;5px;width&#58;808px;" />&#160;</p><dd class="ssw15-rteElement-FigureGood">Figure&#58; NPM Popularity has been increasing<br></dd><p class="ssw15-rteElement-YellowBorderBox">Part of 
   <span>
      <a href="https&#58;//sugarlearning.com/companies/SSW/modules/5099/induction-day-3-developer-induction" target="_blank">SugarLearning Developer Induction</a></span>. 
   <br></p>


