---
type: rule
archivedreason: 
title: Do you make it simple to get latest and compile?
guid: be2d36fd-bd6e-4e50-8b05-b76591961d5f
uri: make-it-simple-to-get-latest-and-compile
created: 2012-03-16T07:44:28.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: Damian Brady
  url: https://ssw.com.au/people/damian-brady
- title: Eric Phan
  url: https://ssw.com.au/people/eric-phan
related: []
redirects:
- do-you-make-sure-you-get-latest-and-compile

---

As a developer, there are few things more frustrating than troubles compiling an application. It's amazing how often you can't simply Clone a repository (aka "Get Latest") and compile it. Too often the response from other developers is "it works on my machine". 

A good developer makes it easy to get a new project, compile it, and have a smooth "F5" experience.

![Figure: The F5 Experience!](f5-key.jpg)  

<!--endintro-->

Check they have a README or instruction files in their solution as per the rule [Do you make instructions at the beginning of a project and improve them gradually?](/do-you-make-instructions-at-the-beginning-of-a-project-and-improve-them-gradually)

### Docker Containerization

Docker can make the experience even better for your developers. Development environments are liable to break easily or have documentation fall out of date. This problem is exacerbated if you come back to a project after a long time away. 

Docker containerization helps to standardize development environments. By using docker containers developers won't need to worry about the technologies and versions installed on the machine. Everything will be set up for them at the click of a button. Microsoft has a great [tutorial on setting up docker containers as development environments](https://docs.microsoft.com/en-us/learn/modules/use-docker-container-dev-env-vs-code/).

Docker containerization delivers a true f5 experience!
