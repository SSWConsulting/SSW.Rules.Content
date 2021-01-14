---
type: rule
archivedreason: 
title: Do you know deploying is so easy?
guid: ffddf84a-21df-4436-9ef5-7d5e943195d2
uri: do-you-know-deploying-is-so-easy
created: 2009-10-06T23:21:05.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects: []

---

You have worked hard on the coding, got a pass from the testers. Great! Now you have approval to deploy to production. With VS 2010 deployment becomes easier and easier, you can choose different ways for different kinds of projects.

 For example:   
<!--endintro-->

* Web Clients
    * Right click "Publish" (recommended if you can directly connect) 
<br>        or
    * Right click "Create Package"
<dl class="image">            <br><br>::: ok  <br>![Figure: For a web app it is just one click](PublishWeb.jpg)  <br>:::<br>
            
        </dl>
* Rich Clients
    * Right click "Publish" (recommended if you can use ClickOnce) 
<br>        or
    * Right click "Create Setup" (Suggestion to Microsoft as menu doesn't exist)

<dl class="image">        <br><br>::: ok  <br>![Figure: For a Windows clients it is also just one click](PublishRichClient.jpg)  <br>:::<br>
        
    </dl>
* The Database<br>    <dl class="image">        <br><br>::: ok  <br>![Figure: For the Database it is ..... well one click is what you need to aim for](PublishDatabase.jpg)  <br>:::<br>
        
        <dd></dd>
    </dl>

 Now all this works beautifully first time, when there is no existing database... and no existing data to worry about. Now you have a reason to read the rest of the rules :-)
