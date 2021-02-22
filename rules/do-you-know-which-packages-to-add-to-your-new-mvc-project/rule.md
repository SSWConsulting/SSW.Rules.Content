---
type: rule
archivedreason: 
title: Do You Know Which Packages To Add To Your New MVC Project?
guid: ff1fcbc9-abe1-44f8-bfda-1d8720cb3799
uri: do-you-know-which-packages-to-add-to-your-new-mvc-project
created: 2014-12-30T00:24:02.0000000Z
authors:
- title: Eric Phan
  url: https://ssw.com.au/people/eric-phan
- title: Brendan Richards
  url: https://ssw.com.au/people/brendan-richards
- title: Adam Stephensen
  url: https://ssw.com.au/people/adam-stephensen
related: []
redirects: []

---


​​​When you create a new MVC project in Visual Studio it is important to include the right packages from the start. This makes the project more manageable and you become more efficient in producing your final result.<br>
<br><excerpt class='endintro'></excerpt><br>
<p>​If you add old, obsolete or incorrect NuGet packages, the project will suffer and you might have decreased performance or scope creep as new requirements are discovered. </p><p>Avoid old technologies such as:</p><ul><li> MVC W​​​​eb Forms</li><li> KnockoutJS</li></ul>
   
<span style="line-height:1.6;">When ​you create a project you should be adding the following NuGet Packages:</span><br> 
<ul><li>SSW.DataOnion<br></li><li>SSW.HealthCheck​<br></li><li>​​AutoFac</li><li>Seril​og​<br></li></ul><p>You should also add the following NPM  packages:</p><ul><li>​Angular JS</li><li>​Bootstrap</li><li>Gulp<br></li></ul><p> 
   <strong>Note</strong>: Prior to 2016, SSW recommend developers choose bower over NPM as their front end package manager. That recomendation has chan​ged due to the industry trend away from bower.</p><p> 
   <img alt="Bower_v_NPM.png" src="Bower_v_NPM.png" style="margin:5px;width:808px;" /> </p><dd class="ssw15-rteElement-FigureGood">Figure: NPM Popularity has been increasing<br></dd><p class="ssw15-rteElement-YellowBorderBox">Part of 
   <span>
      <a href="https://sugarlearning.com/companies/SSW/modules/5099/induction-day-3-developer-induction" target="_blank">SugarLearning Developer Induction</a></span>. 
   <br></p>


