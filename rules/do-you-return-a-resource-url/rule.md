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

When the Web API creates a resource, it should include the URI of the new resource in the Location header of the response.

<!--endintro-->



```cs
public Product PostProduct(Product item)
 {
 item = repository.Add(item);
 return item;
 }
```

::: bad  
Figure: Bad example – The response does not contain a reference to the location of the new resource  
:::

```cs
public HttpResponseMessage PostProduct(Product item)

{

    item = repository.Add(item);

    var response = Request.CreateResponse(HttpStatusCode.Created, item);



    string uri = Url.Link("DefaultApi", new { id = item.Id });

    response.Headers.Location = new Uri(uri);

    return response;

}
```

::: good  
Figure: Good example – The response message contains a link in the header to the created resource (plus the “Created” status code is returned)  
:::
