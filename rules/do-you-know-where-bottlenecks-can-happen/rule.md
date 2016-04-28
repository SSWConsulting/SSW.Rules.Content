---
type: rule
title: Do you know where bottlenecks can happen?
uri: do-you-know-where-bottlenecks-can-happen
created: 2016-04-28T18:32:53.0000000Z
authors:
- id: 3
  title: Eric Phan
- id: 78
  title: Matt Wicks

---



<span class='intro'> <p>For modern applications, there are many layers and moving parts that need to seamlessly work together to deliver our application to the end user.&#160;</p> </span>

<dl class="image"> <dt> <img src="/PublishingImages/bottleneck.png" alt="bottleneck.png" /> </dt><dd>Figure&#58; Bottlenecks can happen anywhere! </dd></dl><p>The issues can be in&#58;</p><h3>SQL Server</h3><ul><li><span style="line-height&#58;1.5em;">Slow </span><span style="line-height&#58;1.5em;">queries&#160;</span></li><li><span style="line-height&#58;1.5em;">Bad configuration&#160;</span></li><li><span style="line-height&#58;1.5em;">Bad query plans&#160;</span></li><li><span style="line-height&#58;1.5em;">Lack of resources&#160;</span></li><li><span style="line-height&#58;1.5em;">Locking</span><br></li></ul><h3>Business Logic</h3><ul><li><span style="line-height&#58;1.5em;">Inefficient code&#160;</span></li><li><span style="line-height&#58;1.5em;">Chatty code&#160;</span></li><li><span style="line-height&#58;1.5em;">Long running processes&#160;</span></li><li><span style="line-height&#58;1.5em;">Not making use of multicore processors</span><br></li></ul><h3>Front end</h3><ul><li><span style="line-height&#58;1.5em;">Too man</span><span style="line-height&#58;1.5em;">y requests to server a page&#160;</span></li><li><span style="line-height&#58;1.5em;">Page size</span></li><li><span style="line-height&#58;1.5em;">Large images</span></li><li><span style="line-height&#58;1.5em;">No Caching</span><br></li></ul><h3>Connection between SQL and Web</h3><ul><li><span style="line-height&#58;1.5em;">Lack of bandwidth</span></li><li><span style="line-height&#58;1.5em;">T</span><span style="line-height&#58;1.5em;">oo much chatter</span><br></li></ul><h3>Connection between Web and Internet</h3><ul><li><span style="line-height&#58;1.5em;">Poor uplink ( </span><span style="line-height&#58;1.5em;">e.g. 1mbps uploads)</span></li><li><span style="line-height&#58;1.5em;">Too many hops</span><br></li></ul><h3>Connection between Web and End users</h3><ul><li><span style="line-height&#58;1.5em;">Geographic </span><span style="line-height&#58;1.5em;">ally too far (e.g. US servers, AU users)</span><br></li></ul><h3>Infrastructure</h3><ul><li><span style="line-height&#58;1.5em;">Misconfiguration</span></li><li><span style="line-height&#58;1.5em;">​Resou</span><span style="line-height&#58;1.5em;">rce contention</span><br></li></ul>


