---
type: rule
title: Do you make deploying easy?
uri: do-you-know-deploying-is-so-easy
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
  - title: Matt Wicks
    url: https://www.ssw.com.au/people/matt-wicks
  - title: Jack Pettit
    url: https://www.ssw.com.au/people/jack-pettit
related: []
redirects: []
created: 2009-10-06T23:21:05.000Z
archivedreason: null
guid: ffddf84a-21df-4436-9ef5-7d5e943195d2
---
You have worked hard on the coding, got a "Test Pass" from the testers. Great! Now you have approval to deploy to production. Let's see some ways that allow for easy deployments.

<!--endintro-->

### Modern Projects 

If you are using Entity Framework Code First migrations this can be handled within your pipeline. 

::: good
![Figure: Using EF Migrations within your pipeline to apply these changes automatically](efmigrations.png) 
:::

### Legacy Projects

With Visual Studio, deployment becomes easier and easier, you can choose different ways for different kinds of projects.

**Web Clients**

* Right-click "Publish" (recommended if you can directly connect)  
OR
* Right-click "Create Package"  

![Figure: For a web app it is just one click](PublishWeb.jpg)

**Rich Clients**

* Right-click "Publish" (recommended if you can use ClickOnce)   
OR
* Right-click "Create Setup" (Suggestion to Microsoft as menu doesn't exist)

![Figure: For a Windows clients it is also just one click](PublishRichClient.jpg)

**Database**
            
![Figure: For the Database it is... well one click is what you need to aim for](PublishDatabase.jpg)

Now all this works beautifully first time, when there is no existing database... and no existing data to worry about. Now you have a reason to read the rest of the rules :-)
