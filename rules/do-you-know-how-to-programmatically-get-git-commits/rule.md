---
type: rule
archivedreason: 
title: Do you know how to programmatically get Git commits?
guid: 4a4daa31-0812-4975-bc5b-52066e3b1dd6
uri: do-you-know-how-to-programmatically-get-git-commits
created: 2014-08-07T23:07:23.0000000Z
authors:
- id: 38
  title: Drew Robson
related: []

---


<p>​​​​​​​​With <a href="http&#58;//www.visualstudio.com/">Visual Studio Online</a> now supporting Git, ​​​​more developers are changing their source control repositories. What happens if an application you developed relies on the <a href="http&#58;//msdn.microsoft.com/en-us/library/bb130146.aspx">TFS Client Object Model</a> to get information out of source control (e.g. changeset comments) and the developers start using Git?​</p>
<br><excerpt class='endintro'></excerpt><br>
<p>That's where the new <a href="http&#58;//www.visualstudio.com/en-us/integrate/reference/reference-vso-overview-vsi.aspx">Visual Studio Online REST APIs</a> come in. You can get a list of commits from your VSO Git repository with only a HTTP request.​</p><p><br></p><p><img src="/PublishingImages/8-08-2014-9-58-37-AM-compressor.png" alt="8-08-2014-9-58-37-AM-compressor.png" style="margin&#58;5px;width&#58;650px;" /><br><strong>Figure&#58; HTTPS GET commits from your VSO Git repository</strong></p><p><span style="line-height&#58;20.7999992370605px;"><span style="line-height&#58;20.7999992370605px;"><br></span></span></p><p><span style="line-height&#58;20.7999992370605px;"><span style="line-height&#58;20.7999992370605px;">​Using&#160;H​TTPS with basic authentication, make a GET request to a URL as below, substituting in your VSO details. A JSON object will be returned.</span>&#160;</span>To quickly create classes from a JSON response, see the rule&#160;<a href="/do-you-know-how-to-easily-get-classes-from-a-json-response">Do you know how to easily get classes from a JSON response?</a></p><p><br></p><p><img src="/PublishingImages/8-08-2014-4-24-34-PM-compressor.png" alt="8-08-2014-4-24-34-PM-compressor.png" style="margin&#58;5px;width&#58;650px;" /><br><strong>Figure&#58; Using the Chrome extension Postman to execute our request with Basic Authentication</strong></p><p><span style="line-height&#58;20.7999992370605px;"><br></span></p><p><span style="line-height&#58;20.7999992370605px;">​For a C# implementation, see&#160;this blog post&#160;<a href="http&#58;//blog.damianbrady.com.au/2014/09/02/getting-git-commits-with-the-vso-rest-api/">Getting Git Commits with the VSO REST API​</a>​.​</span></p><p><span style="line-height&#58;20.7999992370605px;">(This is based on&#160;</span><a href="http&#58;//www.visualstudio.com/en-us/integrate/get-started/get-started-rest-basics-vsi.aspx" style="line-height&#58;20.7999992370605px;">Get started with the REST APIs</a><span style="line-height&#58;20.7999992370605px;">&#160;and&#160;</span><a href="http&#58;//www.visualstudio.com/integrate/reference/reference-vso-git-overview-vsi" style="line-height&#58;20.7999992370605px;">VSO Integration Reference</a><span style="line-height&#58;20.7999992370605px;">)​</span><br></p>


