

---
authors:
  - id: 1
    title: Adam Cogan
  - id: 34
    title: Brendan Richards
---




<span class='intro'> Both NUnit and xUnit are great choices for unit testing – and are highly recommended. Both these frameworks are optimized for unit testing - and xUnit, in particular, has been designed to encourage strong unit test principles by keeping tests isolated.​<br> </span>

<p>​When it comes to writing integration tests, you often write tests against slower shared resources and you need more flexibility on how to discover, set up and run your tests.<br></p><p>Fixie solves this issue by providing an extensible conventions based system to control how tests are discovered and executed.</p>
<ul>
   <li>You can switch from the default frequent instance-per-test test class construction (xUnit-style) to infrequent shared class instance (NUnit style)<br></li><li>You can configure async setup methods to manage expensive dependencies</li><li>This configuration is via conventions to keep your testing code concise</li><li>In fixie, tests don't run in parallel – which is more suitable for integration tests over shared resources<br></li></ul><p>Read the Fixie Documentation here&#58; 
   <a href="https&#58;//github.com/fixie/fixie/wiki">https&#58;//github.com/fixie/fixie/wiki</a><br></p>


