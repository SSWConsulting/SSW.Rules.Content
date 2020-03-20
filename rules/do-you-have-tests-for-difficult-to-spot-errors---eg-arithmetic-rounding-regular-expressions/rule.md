

---
authors:
  - id: 1
    title: Adam Cogan
---




<span class='intro'> By difficult to spot errors we mean errors that do not give the user a prompt that an error has occurred. Things such as&#58; Arithmetic, Rounding or Regular Expressions should have unit tests written for them.<br> </span>

<p>Sample Code&#58;<br><img src="/SiteAssets/have-tests-for-difficult-to-spot-errors/unit%20test%20-%20arithmetic%20code.jpg" alt="unit test - arithmetic code.jpg" style="margin&#58;5px;" /><br><br></p><dd class="ssw15-rteElement-FigureNormal">​Figure&#58; Function to calculate a total for a list of items</dd><p class="ssw15-rteElement-P">For a function&#160;like this, it might be simple to spot errors when there are one or two items, but if you were to calculate the total for 50 items, then the task of spotting an error isn't so easy. That's why a unit test should be written so that you know when the function doesn't work.<br></p><p><b>Sample Test&#58;</b></p><p><b><img src="/SiteAssets/have-tests-for-difficult-to-spot-errors/unit%20test%20-%20arithmetic%20tests.jpg" alt="unit test - arithmetic tests.jpg" style="margin&#58;5px;" /><br></b></p><dd class="ssw15-rteElement-FigureNormal">​Figure&#58; Test calculates total by checking something we know the result of. (Note&#58; it doesn't need a failure case because it isn't a Regex.)​<br></dd>


