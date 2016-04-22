---
type: rule
title: Practices - Do you generate strongly-typed interfaces for your DTOs?
uri: practices---do-you-generate-strongly-typed-interfaces-for-your-dtos
created: 2016-04-22T22:33:50.0000000Z
authors:
- id: 55
  title: Steve Leigh
- id: 34
  title: Brendan Richards

---



<span class='intro'> Inevitably, our well-engineered Angular2 application will need to send and receive data from a service of some sort – usually a Web API. A common mistake people make when doing this is using typescript’s built in <span class="s1"><strong>any</strong></span> type for these services, which offers no type safety whatsoever. <br> </span>

<p>​​<img src="/PublishingImages/dtogs-bad.png" alt="dtogs-bad.png" style="margin&#58;5px;" /></p><p class="p1"><strong>BAD&#58; The “any” type is used as the DTO for this service. There is no type safety.</strong></p><p class="p2"><br></p><p class="p1">One step better is to manually create interfaces for the DTOs. This gives type safety, but still means a lot of manual, tedious work to generate the interfaces.</p><p class="p2"><img src="/PublishingImages/dtogs-ok.png" alt="dtogs-ok.png" style="margin&#58;5px;" /><br></p><p class="p1"><strong>Better&#58; Manually coded interface ensures any object passed to the service is in the correct format </strong></p><p class="p1"><strong><br></strong></p><p class="p1">But this still doesn’t give safety over-the-wire – if the server side model changes, a developer has to remember to update it here, and hope that there are no typos.&#160; This is also extra effort to perform something mindlessly repetitive – something a machine is much better at doing.&#160; And we are programmers, right?</p><p class="p2"><br></p><p class="p1">An example of such a generator is <a href="https&#58;//github.com/Evertras/gulp-typescript-cs-poco" target="_blank">gulp-typescript-cs-poco, but there are many out there. </a></p><p class="p1"><strong><strong><br></strong></strong></p><p class="p1"><strong><strong><img src="/PublishingImages/dtos-good.png" alt="dtos-good.png" style="margin&#58;5px;" />Good&#58; Writing a small bit of code means I don’t have to write a lot of code every time I change a DTO</strong> <br></strong></p>


