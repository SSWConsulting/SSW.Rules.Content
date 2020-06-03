---
type: rule
title: Do you always use query strings?
uri: do-you-always-use-query-strings
created: 2016-08-26T17:39:16.0000000Z
authors:
- id: 1
  title: Adam Cogan

---



<span class='intro'> <p style="margin-top&#58;7px;margin-bottom&#58;7px;font-family&#58;verdana, sans-serif;font-size&#58;12px;line-height&#58;1.4em;color&#58;#000000;">When you build a web application, any dynamic page you think a user may wish to bookmark directly should be controlled through query string values rather than form values. In other words, search mechanisms should use the HTTP GET Request and Querystring values, rather than a POST with Form values. This allows&#58;</p><ul style="padding-top&#58;0px;padding-bottom&#58;0px;padding-left&#58;0px;margin-left&#58;10px;font-family&#58;verdana, sans-serif;font-size&#58;12px;color&#58;#000000;"><li style="padding-bottom&#58;0px;font-size&#58;1em;">Bookmarking of the pages</li><li style="padding-bottom&#58;0px;font-size&#58;1em;">Gives the user to the ability to change the query string values in the address bar, rather than having to go back to the input form. <br></li></ul><br> </span>

<dl class="goodImage"> <dt><img src="/PublishingImages/querystring.png" alt="querystring.png" /></dt><dd>Figure&#58; The URL should always have all the parameters the user enters. Here Google is a good example</dd></dl><p>You may hear that query strings are bad and they leave you wide open to SQL Injection Attacks (especially when you use SQL statements in the URL). I don't subscribe to the security issues being the determining factor... if I am determined enough, I can write a little application to send POST data to the webpage instead of in the query string. Both methods are open to SQL injection and invalid parameters, so you need to code to prevent that either way.​<br></p><p>The bottom line is that if you are not giving appropriate parameters in the query string then you are reducing functionality.</p><p><b>Note&#58;</b> We all agree bookmarks are useful - it's the same for query strings.</p>
​<br>


