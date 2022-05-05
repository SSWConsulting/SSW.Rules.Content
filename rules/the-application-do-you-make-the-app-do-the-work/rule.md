---
type: rule
title: The application – Do you make the app do the work?
uri: the-application-do-you-make-the-app-do-the-work
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
  - the-application-–-do-you-make-the-app-do-the-work
created: 2009-10-07T00:01:45.000Z
archivedreason: null
guid: 8e1e35ac-e3a7-462b-b341-8465a8b842a4
---

An Application upgrade might not only include the .exe and .dll but the database changes. How to deploy these changes, manually or using tools to deploy? 

 Let's see the bad and good examples:   
<!--endintro-->



```
Dear Mr Northwind, 

Before installing your application, you need to 
run this script by 
first opening up SQL Management Studio. 
Open the attached script, point it to Northwind and 
execute the script. 

Let me know if you have any issues... 
We worked very hard on this release. 

I hope you’re happy with it. 

Regards, 
Eric Phan
```

::: bad
**Figure: Bad example - run SQL scripts manually**
:::

```
Hi Mr. Northwind, 

Please run the attached Northwind_v5.exe. 

Click Run when the prompt appears. 

Regards,
Eric Phan
```
::: bad
**Figure: Better example - run SQL scripts using another package**        
::: 

```
Dear Mr Northwind, 

When you run the Northwind v1.0 (Rich Client) it will 
automatically upgrade the database for you. 

Just make sure you have dbo permissions ⚠️
 
Let me know if you run into any issues.

Regards, 
Eric Phan
```
::: good 
**Figure: Better example - run SQL scripts in the application. There is a tool called [SQL Deploy | Reconcile](http://sqldeploy.com/) .**
:::
        
```
Dear Mr Northwind, 

We have just deployed a new release and updated the database for you. Please view it live here.

If you have any questions please let me know.

Regards,
 
Eric Phan

```

::: good 
**Figure: Best example - All done as part of the release pipeline**
:::
