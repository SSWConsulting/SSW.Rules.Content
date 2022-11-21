---
type: rule
archivedreason: 
title: Do you return the correct response code?
guid: fa6f616b-ff7c-43c8-b7d9-4c80f22ac6d8
uri: do-you-return-the-correct-response-code
created: 2014-11-05T20:39:42.0000000Z
authors:
- title: Chris Briggs
  url: https://ssw.com.au/people/chris-briggs
- title: Drew Robson
  url: https://ssw.com.au/people/drew-robson
related: []
redirects: []

---

The use of correct response codes is a simple yet crucial step towards building a better WebAPI. In ASP.NET Core, by default the WebAPI framework sets the response status code to 200 (OK), regardless of whether the task succeed or an error occurred.

You can  **save yourself countless hours of painful debugging** , by specifying the correct response code.

<!--endintro-->

For example: According to the HTTP/1.1 protocol, when a POST request results in the creation of a resource, the server should reply with status 201 (Created).



```
public Product PostProduct(Product item)
 {
 item = repository.Add(item);
 return item;
 }
```

::: bad
Figure: Bad Example – By default a 200 status code is returned.
:::

```
[ResponseType(typeof(CreditSnapshot))]
 public HttpResponseMessage PostProduct(Product item)
 {
 item = repository.Add(item);
 var response = Request.CreateResponse(HttpStatusCode.Created, item);
 
         
 return response;
 }
```

::: good
Figure: Good Example – When creating objects the “Created” status code is returned. 
:::

```
public void PutProduct(int id, Product product)

{

    product.Id = id;

    if (!repository.Update(product))

    {

        return Request.CreateResponse(HttpStatusCode.NotFound, ex.Message);

    }

}
```

::: good
Figure: Good Example – When updating or deleting objects, if the object to be modified cannot be found throw exception with HttpStatusCode.NotFound
:::
