---
type: rule
archivedreason: 
title: Do you run load tests on your website?
guid: f010a6f8-a386-47b6-8d9c-bd7c9b1a37a8
uri: run-load-tests-on-your-website
created: 2016-11-16T16:36:53.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
- do-you-run-load-tests-on-your-website

---


<p>​Once you have a website up and running, it is important to make sure that it keeps running under load. Local testing of the website will not always reveal the latent problems in the website when it is subjected to thousands of users. Typical issues that result from inadequate load testing are:<br></p><ul><li>503 Service Is Temporarily Unavailable</li><li>Very slow load times​​​​​​​<br></li><li>Application Crashes due to:
   <ul><li>Insufficient resources - so application pools are recycled</li><li>Too many concurrent users causing race conditions</li><li>Too many users trying to connect to the database​​<br></li></ul></li></ul>
<br><excerpt class='endintro'></excerpt><br>
<p>Load Tests help you <strong>avoid these issues</strong> by prompting them before you go live. Some issues might be resolved by getting a better web server, while others might require code changes and optimizations.</p><p>In <strong>Visual Studio 2005 - Software Testers Edition</strong>, there is a built-in Test Project to conduct load testing.</p><ol><li>From the <strong>Test</strong> menu select <strong>New Test</strong></li><li>Select <strong>Web Test</strong> and <strong>Create a new Test Project</strong><br>
      <dl class="image"><dt> <img src="../../assets/add_new_test.gif" alt="Add a new Web Test" /> <br> 
         </dt></dl></li><li>Name the Test Project &lt;Namespace&gt;.WebUI.Tests</li><li>An Internet Explorer window will open with a recorder toolbar. Navigate to the web pages that need to be Load Tested<br> 
      <dl class="image"><dt> <img src="../../assets/record_website.gif" alt="Record the pages you want to Load Test" /> </dt></dl></li><li>Click Stop when you are finished recording the pages to be tested</li><li>Click the <strong>Run</strong> button to make sure the tests run<br>
   <dl class="image"><dt><img src="../../assets/run_webtest.gif" alt="Test our recorded test" />​<br></dt></dl></li><li>Add a new Load Test<br>
      <dl class="image"><dt> <img src="../../assets/add_load_test.gif" alt="Add Load Test" /> </dt></dl></li><li>Follow the <strong>Load Test Wizard</strong>:<ul><li>
            <strong>Load Pattern</strong> - Define the number of users hitting the site</li><li>
            <strong>Test Mix</strong> - Select the web test you recorded earlier</li><li>
            <strong>Browser Mix</strong> - Specify different types of browsers (leave as default)<br></li><li>
            <strong>Network Mix</strong> - Specify connection speeds of users (leave as default)</li></ul></li><li>Click <strong>Finish</strong></li><li>Click <strong>Run</strong> to run the load test<br>
      <dl class="image"><dt> <img src="../../assets/run_load_test.gif" alt="Run Load Test" /> </dt></dl></li><li>This will kick off the load test and show a live graph of user load, requests per second and response time</li></ol>​<br>


