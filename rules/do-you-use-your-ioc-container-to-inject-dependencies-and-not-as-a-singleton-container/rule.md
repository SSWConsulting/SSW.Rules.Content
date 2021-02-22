---
type: rule
archivedreason: 
title: Do you use your IOC container to Inject Dependencies – and not as a singleton container
guid: 3a4bf441-83ed-4443-bbe6-c2551ee698f9
uri: do-you-use-your-ioc-container-to-inject-dependencies-and-not-as-a-singleton-container
created: 2013-11-11T03:53:14.0000000Z
authors:
- title: Brendan Richards
  url: https://ssw.com.au/people/brendan-richards
related: []
redirects:
- do-you-use-your-ioc-container-to-inject-dependencies-–-and-not-as-a-singleton-container

---


A common practice we see when developers start to use IOC containers is that the IOC container becomes a central service and configuration repository that all the components across the project become dependent upon.
<br><excerpt class='endintro'></excerpt><br>
<p>​Using an IOC container in this manner can bring advantages such as centralised configuration and dependency lifecycle and scope managment. If implemented correctly, however, your classes can benefit from the above without any direct dependency on the IOC container itself.</p><p><strong style="line-height:1.6;"></strong></p><img src="IOC_badexample.png" alt="IOC_badexample.png" style="margin:5px;" /><br><div><br><dd class="ssw15-rteElement-FigureBad">Figure: Bad Example - the dependency is manually fetched from the IOC container, This class now has a hard dependency on your IOC container</dd><p><br></p><p><img src="IOC_GoodExample.png" alt="IOC_GoodExample.png" style="margin:5px;" /><br></p><dd class="ssw15-rteElement-FigureGood">Figure: Good example -  The dependency is enforced via a constuctor parameter. The class does not need to know anything about the IOC container being used and can potentially be reused in different contexts and with different IOC containers. </dd><p> </p><p>For more information and insight on IOC usage, read the following: ​<a href="http://www.devtrends.co.uk/blog/how-not-to-do-dependency-injection-the-static-or-singleton-container">http://www.devtrends.co.uk/blog/how-not-to-do-dependency-injection-the-static-or-singleton-container</a>​</p></div>


