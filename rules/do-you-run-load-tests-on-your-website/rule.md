---
type: rule
title: Do you run load tests on your website?
uri: do-you-run-load-tests-on-your-website
created: 2016-11-16T16:36:53.0000000Z
authors:
- id: 1
  title: Adam Cogan

---



<span class='intro'> <p>​Once you have a website up and running, it is important to make sure that it keeps running under load. Local testing of the website will not always reveal the latent problems in the website when it is subjected to thousands of users. Typical issues that result from inadequate load testing are&#58;<br></p><ul><li>503 Service Is Temporarily Unavailable</li><li>Very slow load times​​​​​​​<br></li><li>Application Crashes due to&#58;
   <ul><li>Insufficient resources - so application pools are recycled</li><li>Too many concurrent users causing race conditions</li><li>Too many users trying to connect to the database​​<br></li></ul></li></ul> </span>

<p>Load Tests help you&#160;<strong>avoid these issues</strong>&#160;by prompting them before you go live. Some issues might be resolved by getting a better web server, while others might require code changes and optimizations.</p><p>In&#160;<strong>Visual Studio 2005 - Software Testers Edition</strong>, there is a built-in Test Project to conduct load testing.</p><ol><li>From the&#160;<strong>Test</strong>&#160;menu select&#160;<strong>New Test</strong></li><li>Select&#160;<strong>Web Test</strong>&#160;and&#160;<strong>Create a new Test Project</strong><br> 
      <dl class="image"><dt> <img src="https&#58;//www.ssw.com.au/ssw/standards/rules/Images/add_new_test.gif" alt="Add a new Web Test" /> <br>
         </dt></dl></li><li>Name the Test Project &lt;Namespace&gt;.WebUI.Tests</li><li>An Internet Explorer window will open with a recorder toolbar. Navigate to the web pages that need to be Load Tested<br>
      <dl class="image"><dt> <img src="https&#58;//www.ssw.com.au/ssw/standards/rules/Images/record_website.gif" alt="Record the pages you want to Load Test" /> </dt></dl></li><li>Click Stop when you are finished recording the pages to be tested</li><li>Click the&#160;<strong>Run</strong>&#160;button to make sure the tests run<br><img src="https&#58;//www.ssw.com.au/ssw/standards/rules/Images/run_webtest.gif" alt="Test our recorded test" style="width&#58;340px;margin&#58;5px;" /></li><li>Add a new Load Test<br> 
      <dl class="image"><dt> <img src="https&#58;//www.ssw.com.au/ssw/standards/rules/Images/add_load_test.gif" alt="Add Load Test" /> </dt></dl></li><li>Follow the&#160;<strong>Load Test Wizard</strong>&#58;<ul><li> 
         <strong>Load Pattern</strong>&#160;- Define the number of users hitting the site</li><li> 
         <strong>Test Mix</strong>&#160;- Select the web test you recorded earlier</li><li> 
         <strong>Browser Mix</strong>&#160;- Specify different types of browsers (leave as default)<br></li><li> 
         <strong>Network Mix</strong>&#160;- Specify connection speeds of users (leave as default)</li></ul></li>
   <li>Click&#160;<strong>Finish</strong></li><li>Click&#160;<strong>Run</strong>&#160;to run the load test<br> 
      <dl class="image"><dt> <img src="https&#58;//www.ssw.com.au/ssw/standards/rules/Images/run_load_test.gif" alt="Run Load Test" /> </dt></dl></li><li>This will kick off the load test and show a live graph of user load, requests per second and response time</li></ol>​<br>


