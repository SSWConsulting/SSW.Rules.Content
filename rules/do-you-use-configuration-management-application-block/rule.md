---
type: rule
archivedreason: 
title: Do you use configuration management application block?
guid: 83914d3f-6c83-49cc-a2bc-f9cdd244c952
uri: do-you-use-configuration-management-application-block
created: 2009-04-29T04:40:53.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: Ryan Tee
  url: https://ssw.com.au/people/ryan-tee
  noimage: true
related: []
redirects: []

---

How do you get a setting from a configuration file? What do you do when you want to get a setting from a registry, or a database? Everyone faces these problems, and most people come up with their own solution. We used to have a few different standards, but when Microsoft released the Configuration Application Blocks, we have found that working to extend it and use it in all our projects saves us a lot of time! Use a local configuration file for machine and/or user specific settings (such as a connection string), and use a database for any shared values such as Tax Rates.

See how we configured this reset default settings functionality with the Configuration Block in the [.NET Toolkit](http&#58;//www.ssw.com.au/ssw/NetToolKit/06ConfigurationBlock.aspx)

<!--endintro-->
