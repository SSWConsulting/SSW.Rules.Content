---
seoDescription: Discover why Windows Forms remain a popular choice despite the rise of web forms, offering benefits such as bandwidth efficiency, caching, and richer interfaces.
type: rule
title: Do you know why you choose Windows Forms?
uri: do-you-know-why-you-choose-windows-forms
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
created: 2014-03-14T01:48:00.000Z
guid: dc5f2302-9b68-4735-8c67-9e787bb675af
---

Almost everyone assumes today to use web forms for broad reach because of easy installation and cross platform compatibility. That is correct.

In the old days (1995-2000) companies used Windows Forms, later (2000-2007) they rolled their own ASP.NET solution, however since then (2007+) [SharePoint](https://www.ssw.com.au/consulting/sharepoint) has become the default choice for an intranet. When you need something richer and you can control the environment.

<!--endintro-->

1. **Bandwidth - Presentation Layer**  
   Only the data is transferred from the server, not the presentation code. Web forms must download the data and the rendered UI taking up large bandwidth.

2. **Bandwidth - Compression**  
   Data transfer can be compressed and uncompressed to use less bandwidth.  
   For example, using a Pkzip scale (1-9) of 6, we used the Open source algorithm 'Blowfish' to compress/encrypt 240K of data to 30K. i.e. 87% compression.

3. **Caching**  
   If you are going to the same record within a certain time period, Windows forms will retrieve the data from cache instead of calling the data service again.  
   For example, when you click search on a Windows form, you don't have to do a request again if the search was done recently.

4. **Faster Server**  
   Because of the bandwidth advantages above, the server will make less requests and hence runs faster. The client has become thicker, using more processing power and capable of more complex business logic.

5. **Richer Interface**  
   The application's interface can be richer as you can design your own custom controls and do not need complicated resource-intensive and complex DHTML and JavaScript.

6. **More Responsive**  
   The interface will respond quicker to your clicks, no need to post a request for an interface response. i.e. no 10 second latency.

7. **Better Development**  
   Development is much easier with quick feedback. There are no compliance issues to follow as in web development with browsers.
8. **More people are happy!**  
   By choosing windows forms you are making the developer, end user and accounts groups happier. The only group which may rather a Web solution is the network admins.

| Group          | Browser Based | Rich Client |
| -------------- | :-----------: | :---------: |
| Network Admins |      ✅       |     ❌      |
| Developers     |      ❌       |     ✅      |
| End Users      |      ❌       |     ✅      |
| Accounts       |      ❌       |     ✅      |

**Figure: Table of who benefits from Windows Forms, and Web Forms**
