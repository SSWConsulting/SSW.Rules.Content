---
type: rule
archivedreason: 
title: Do you return the correct response code?
guid: fa6f616b-ff7c-43c8-b7d9-4c80f22ac6d8
uri: do-you-return-the-correct-response-code
created: 2014-11-05T20:39:42.0000000Z
authors:
- id: 45
  title: Chris Briggs
- id: 38
  title: Drew Robson
related: []

---

The use of correct response codes is a simple yet crucial step towards building a better WebAPI. In ASP.NET Core, by default the WebAPI framework sets the response status code to 200 (OK), regardless of whether the task succeed or an error occurred.

You can  **save yourself countless hours of painful debugging** , by specifying the correct response code.

<!--endintro-->

For example: According to the HTTP/1.1 protocol, when a POST request results in the creation of a resource, the server should reply with status 201 (Created).
<dl class="badImage">&lt;dt&gt;<p class="ssw15-rteElement-CodeArea">public Product PostProduct(Product item)<br> &#123;<br> item = repository.Add(item);<br> return item;<br> &#125;<br> </p>&lt;/dt&gt;<dd>Figure&#58; Bad Example – By default a 200 status code is returned.</dd></dl><dl class="goodImage">&lt;dt&gt;<p class="ssw15-rteElement-CodeArea">[ResponseType(typeof(CreditSnapshot))] public HttpResponseMessage PostProduct(Product item)<br> &#123;<br> item = repository.Add(item);<br> var response = Request.CreateResponse(HttpStatusCode.Created, item);<br> 
         <br> return response;<br> &#125; </p>&lt;/dt&gt;<dd>Figure&#58; Good Example – When creating objects the “Created” status code is returned.&#160;</dd></dl><dl class="goodImage">&lt;dt&gt;<p class="ssw15-rteElement-CodeArea">public void PutProduct(int id, Product product)<br>
&#123;<br>
    product.Id = id;<br>
    if (!repository.Update(product))<br>
    &#123;<br>
        <mark>return Request.CreateResponse(HttpStatusCode.NotFound, ex.Message);</mark><br>
    &#125;<br>
&#125;
</p>&lt;/dt&gt;<dd>Figure&#58; Good Example – When updating or deleting objects, if the object to be modified cannot be found throw exception with HttpStatusCode.NotFound</dd></dl>
