---
type: rule
title: Do you use your IOC container to Inject Dependencies – and not as a singleton container
uri: do-you-use-your-ioc-container-to-inject-dependencies--and-not-as-a-singleton-container
created: 2013-11-11T03:53:14.0000000Z
authors:
- id: 34
  title: Brendan Richards

---



<span class='intro'> A common practice&#160;we&#160;see when developers start to use IOC containers is that the IOC container becomes a central service and configuration repository that all the components across the project become dependent upon. </span>

<p>​Using an IOC container in this manner can bring advantages such as centralised configuration and dependency lifecycle and scope managment. If implemented correctly, however, your classes can benefit from the above without any direct dependency on the IOC container itself.</p><p><strong style="line-height&#58;1.6;"></strong></p><img src="/PublishingImages/IOC_badexample.png" alt="IOC_badexample.png" style="margin&#58;5px;" /><br><div><br><dd class="ssw15-rteElement-FigureBad">Figure&#58; Bad Example - the dependency is&#160;manually fetched from the IOC container, This class now has a hard dependency on your IOC container</dd><p><br></p><p><img src="/PublishingImages/IOC_GoodExample.png" alt="IOC_GoodExample.png" style="margin&#58;5px;" /><br></p><dd class="ssw15-rteElement-FigureGood">Figure&#58; Good example - &#160;The dependency is enforced via a constuctor parameter.&#160;The class does not need to know anything about the&#160;IOC container being used and&#160;can potentially be reused in different contexts and with different IOC containers.&#160;</dd><p>&#160;</p><p>For more information and insight on IOC usage,&#160;read the following&#58;&#160;​<a href="http&#58;//www.devtrends.co.uk/blog/how-not-to-do-dependency-injection-the-static-or-singleton-container">http&#58;//www.devtrends.co.uk/blog/how-not-to-do-dependency-injection-the-static-or-singleton-container</a>​</p></div>


