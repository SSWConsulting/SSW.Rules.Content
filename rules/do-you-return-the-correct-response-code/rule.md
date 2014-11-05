---
type: rule
title: Do you return the correct response code?
uri: do-you-return-the-correct-response-code
created: 2014-11-05T20:39:42.0000000Z
authors:
- id: 45
  title: Chris Briggs
- id: 38
  title: Drew Robson

---



<span class='intro'> <p class="p1"><span class="s1">The use of correct response codes is a simple yet crucial step, towards building a better WebAPI. </span>By default, the <span class="s1">WebAPI</span> framework sets the response status code to 200 (OK), regardless if the task succeed or an error occurred.&#160;&#160;</p><p class="p3">You can <b>save yourself countless hours of painful debugging</b>, by specifying the correct response code.</p> </span>

<p class="p1">For example&#58;&#160;According to the HTTP/1.1 protocol, when a POST request results in the creation of a resource, the server should reply with status 201 (Created).</p><dl class="badImage"><dt><p class="ssw15-rteElement-CodeArea">public Product PostProduct(Product item)<br> &#123;<br> item = repository.Add(item);<br> return item;<br> &#125;<br> </p></dt><dd>Figure&#58; Bad Example – By default a 200 status code is returned.</dd></dl><dl class="goodImage"><dt><p class="ssw15-rteElement-CodeArea">[ResponseType(typeof(CreditSnapshot))]<br> public HttpResponseMessage PostProduct(Product item)<br> &#123;<br> item = repository.Add(item);<br> var response = Request.CreateResponse(HttpStatusCode.Created, item);<br> 
         <br> return response;<br> &#125; </p></dt><dd>Figure&#58; Good Example – When creating objects the “Created” status code is returned.&#160;</dd></dl><dl class="goodImage"><dt><p class="ssw15-rteElement-CodeArea">​public void PutProduct(int id, Product product)<br>
&#123;<br>
    product.Id = id;<br>
    if (!repository.Update(product))<br>
    &#123;<br>
        <span class="ssw15-rteStyle-Highlight">return Request.CreateResponse(HttpStatusCode.NotFound, ex.Message);</span><br>
    &#125;<br>
&#125;
</p></dt><dd>Figure&#58; Good Example – When updating or deleting objects, if the object to be modified cannot be found throw exception with HttpStatusCode.NotFound</dd></dl> ​


