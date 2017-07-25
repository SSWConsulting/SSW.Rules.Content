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



<span class='intro'> ​<p>Inevitably, our well-engineered Angular ​application will need to send and receive data from a service of some sort – usually a Web API. A common mistake people make when doing this is using typescript’s built in <strong>any</strong> type for these services, which offers no type safety whatsoever.</p> </span>

<dl class="badImage"><dt> <img src="/PublishingImages/dtogs-bad.png" alt="dtogs-bad.png" /> </dt><dd>Figure&#58; Bad example - The &quot;any&quot; type is used as the DTO for this service. There is no type safety.</dd></dl><p>One step better is to manually create interfaces for the DTOs. This gives type safety, but still means a lot of manual, tedious work to generate the interfaces.</p><dl class="image"><dt> <img src="/PublishingImages/dtogs-ok.png" alt="dtogs-ok.png" /> </dt><dd>Figure&#58; Better example - Manually coded interface ensures any object passed to the service is in the correct format </dd></dl><p>But this still doesn’t give safety over-the-wire – if the server side model changes, a developer has to remember to update it here, and hope that there are no typos.&#160; This is also extra effort to perform something mindlessly repetitive – something a machine is much better at doing.&#160; And we are programmers, right?</p><p>An example of such a generator is <a href="https&#58;//github.com/Evertras/gulp-typescript-cs-poco" target="_blank">gulp-typescript-cs-poco</a> ​, but there are many out there.</p><dl class="goodImage"><dt> <img src="/PublishingImages/dtos-good.png" alt="dtos-good.png" /> </dt><dd>Figure&#58; Good example - Writing a small bit of code means I don’t have to write a lot of code every time I change a DTO</dd></dl>


