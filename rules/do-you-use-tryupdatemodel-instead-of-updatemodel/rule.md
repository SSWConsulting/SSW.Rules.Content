---
type: rule
title: Do you use TryUpdateModel instead of UpdateModel?
uri: do-you-use-tryupdatemodel-instead-of-updatemodel
created: 2013-03-07T18:11:22.0000000Z
authors:
- id: 23
  title: Damian Brady

---



<span class='intro'> <p>UpdateModel will throw an exception if validation of the model fails.  Instead of managing an exception, you should use TryUpdateModel as it adds the error to the ModelState dictionary.  This lets you check the ModelState.IsValid property and decide how to handle the issue from there.  This is an important distinction to be made because if we had used UpdateModel then our if (ModelState.IsValid) would not be hit in the event of a failure to bind.</p><dl class="badImage"><dt><div class="greyBox"><pre>public ActionResult Create()<br> &#123;<br> Entity myEntity = new Entity();           
            <br>UpdateModel(myEntity);<br> &#125;</pre></div></dt><dd>Figure&#58; Bad Example – UpdateModel may throw an exception and the ModelState dictionary won’t be updated
   </dd></dl><dl class="goodImage"><dt><div class="greyBox"><pre>public ActionResult Create()<br> &#123;<br> Entity myEntity = new Entity();<br> TryUpdateModel(myEntity);<br><br> if (ModelState.IsValid)<br> &#123;<br> // ...<br> &#125;<br> &#125; </pre></div></dt><dd>Figure&#58; Good Example – TryUpdateModel will gracefully handle validation and will add to the ModelState dictionary so we can check for validity
   </dd></dl> </span>




