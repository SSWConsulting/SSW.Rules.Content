---
type: rule
title: Do you set retention policy?
uri: do-you-set-retention-policy
created: 2016-05-30T06:41:05.0000000Z
authors:
- id: 46
  title: Danijel Malik

---



<span class='intro'> <p>Octopus
Deploy will by default keep all packages (NuGet, ZIP, …) as well as files
deployed on all Tentacles. Because of that your hard drive will fill up very
fast as you keep pushing in more packages and creating more releases,
especially if you are using Continuous Integration and pushing out new packages
with every commit to a repository.</p> </span>

That's why you need to set up a retention policy. Octopus Deploy supports two options&#58;<br><ul><li><span style="line-height&#58;1.5em;">Retention policy for packages</span><br></li><li><span style="line-height&#58;1.5em;">Retention policy for deployments (via Lifecycle phases)</span></li></ul>You should set up both.<div><br></div><h3 class="ssw15-rteElement-H3">Package&#160;Policy​</h3><div><br></div><div><img src="/SiteAssets/do-you-set-retention-policy/2016-05-30_15-00-04.png" alt="2016-05-30_15-00-04.png" style="margin&#58;5px;width&#58;808px;" /><br></div><dd class="ssw15-rteElement-FigureBad">​Bad
Example - Retention policy is set to Keep forever​​</dd><p class="ssw15-rteElement-P">​​<br></p><p class="ssw15-rteElement-P">​​<img src="/SiteAssets/do-you-set-retention-policy/2016-05-30_15-00-29.png" alt="2016-05-30_15-00-29.png" style="margin&#58;5px;width&#58;808px;" /><br></p><dd class="ssw15-rteElement-FigureGood">​Good
Example - Retention policy is set to a number of days​</dd><p class="ssw15-rteElement-P">​<br></p><h3 class="ssw15-rteElement-H3">Lifecycle Policy<br></h3><p><img src="/SiteAssets/do-you-set-retention-policy/2016-05-30_15-01-55.png" alt="2016-05-30_15-01-55.png" style="margin&#58;5px;width&#58;808px;" /><br></p><dd class="ssw15-rteElement-FigureBad">Bad
Example - Lifecycle's retention policy is set to Keep all​</dd><p class="ssw15-rteElement-P">​​<br></p><p class="ssw15-rteElement-P"><img src="/SiteAssets/do-you-set-retention-policy/2016-05-30_15-49-37.png" alt="2016-05-30_15-49-37.png" style="margin&#58;5px;width&#58;808px;" /><br></p><dd class="ssw15-rteElement-FigureGood">​Good
Example - Lifecycle's retention policy is set to 3 Releases<br></dd><div><br></div>


