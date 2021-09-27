---
type: rule
archivedreason: 
title: Do you know how to programmatically get Git commits?
guid: 4a4daa31-0812-4975-bc5b-52066e3b1dd6
uri: do-you-know-how-to-programmatically-get-git-commits
created: 2014-08-07T23:07:23.0000000Z
authors:
- title: Drew Robson
  url: https://ssw.com.au/people/drew-robson
related: []
redirects: []

---

Using the [Azure DevOps API](https://docs.microsoft.com/en-us/rest/api/azure/devops/git/commits/get-commits?view=azure-devops-rest-6.0) you can programmatically get a list of commits from your repository with only a HTTP request.



![](devops-get-commits.png)
 **Figure: HTTPS GET commits from your repository**



Using HTTPS with basic authentication, make a GET request to a URL as below, substituting in your project details. A JSON object will be returned. To quickly create classes from a JSON response, see the rule [Do you know how to easily get classes from a JSON response?](/do-you-know-how-to-easily-get-classes-from-a-json-response)



![](8-08-2014-4-24-34-PM-compressor.png)
 **Figure: Using the Chrome extension Postman to execute our request with Basic Authentication**



For a C# implementation, see this blog post [Getting Git Commits with the VSO REST API](http://blog.damianbrady.com.au/2014/09/02/getting-git-commits-with-the-vso-rest-api/).
