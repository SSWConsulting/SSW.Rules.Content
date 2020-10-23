---
type: rule
archivedreason: 
title: Do you return a Resource URL?
guid: c9bcc58a-f5a3-4662-a210-a379dce8b933
uri: do-you-return-a-resource-url
created: 2014-11-05T18:22:22.0000000Z
authors:
- title: Adam Stephensen
  url: https://ssw.com.au/people/adam-stephensen
related: []
redirects: []

---


<p>When the Web API creates a resource, it should include the URI of the new resource in the Location header of the response.​<br></p>
<br><excerpt class='endintro'></excerpt><br>
<dl class="badImage"><dt><p class="ssw15-rteElement-CodeArea">public Product PostProduct(Product item)<br> &#123;<br> item = repository.Add(item);<br> return item;<br> &#125;&#160;​</p></dt><dd>Figure&#58; Bad Example – The response does not contain a reference to the location of the new resource </dd></dl><dl class="goodImage"><dt><p class="ssw15-rteElement-CodeArea">public HttpResponseMessage PostProduct(Product item)<br>
&#123;<br>
    item = repository.Add(item);<br>
    var response = Request.CreateResponse(HttpStatusCode.Created, item);<br><br>

    string uri = Url.Link(&quot;DefaultApi&quot;, new &#123; id = item.Id &#125;);<br>
    response.Headers.Location = new Uri(uri);<br>
    return response;<br>
&#125;
</p></dt><dd>Figure&#58; Good Example – The response message contains a link in the header to the created resource (and the “Created” status code is returned )​</dd></dl>


