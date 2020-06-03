---
type: rule
title: Do you know how to integrate RayGun with Octopus Deploy?
uri: do-you-know-how-to-integrate-raygun-with-octopus-deploy
created: 2016-10-25T17:17:59.0000000Z
authors:
- id: 3
  title: Eric Phan

---



<span class='intro'> <p>One of the best features of RayGun is the ability to track crash reports against deployments. This feature allows you to tell if a particular deployment has introduced a lot of new bugs or caused a regression of exceptions.&#160;​<br></p><p>To set it up&#58;​<br></p> </span>

<ol><li>Under Deployments<br></li><li>Select Octopus Deploy (Set up)<br> 
      <dl class="image"><dt> <img src="/PublishingImages/raygun-octopus-1.jpg" alt="raygun-octopus-1.jpg" /> </dt></dl><p>Raygun will product you with a <a href="https&#58;//raygun.com/docs/deployments/octopus-deploy" target="_blank">PowerShell script </a> to add into your octopus deployment steps that will call the RayGun API and log a new deployment</p></li><li>Trigger a new deployment</li><li>Then you’ll see the deployment in RayGun<br>
   <dl class="image"><dt><img src="/PublishingImages/raygun-octopus-2.png" alt="raygun-octopus-2.png" /></dt></dl><p>Drilling into a deployment you’ll see&#58;</p><ul><li>New errors</li><li>Regressions</li><li>Recurring errors</li></ul><dl class="goodImage"><dt> <img src="/PublishingImages/raygun-octopus-3.jpg" alt="raygun-octopus-3.jpg" /> </dt><dd>Figure&#58; Good Example – Now you can measure the quality of your deployments <br></dd> </dl></li></ol>


