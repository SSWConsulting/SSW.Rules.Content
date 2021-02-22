---
type: rule
archivedreason: 
title: Do you use TryUpdateModel instead of UpdateModel?
guid: 74fbd7d4-7391-494d-b855-44426f7170eb
uri: do-you-use-tryupdatemodel-instead-of-updatemodel
created: 2013-03-07T18:11:22.0000000Z
authors:
- title: Damian Brady
  url: https://ssw.com.au/people/damian-brady
related: []
redirects: []

---

UpdateModel will throw an exception if validation of the model fails.  Instead of managing an exception, you should use TryUpdateModel as it adds the error to the ModelState dictionary.  This lets you check the ModelState.IsValid property and decide how to handle the issue from there.  This is an important distinction to be made because if we had used UpdateModel then our if (ModelState.IsValid) would not be hit in the event of a failure to bind.

<!--endintro-->


::: greybox


```
public ActionResult Create()
{
    Entity myEntity = new Entity();
    UpdateModel(myEntity);
}
```


:::
Figure: Bad Example – UpdateModel may throw an exception and the ModelState dictionary won’t be updated 

::: greybox


```
public ActionResult Create()
{
    Entity myEntity = new Entity();
    TryUpdateModel(myEntity);

    if (ModelState.IsValid)
    {
        // ...
    }
}
```


:::
Figure: Good Example – TryUpdateModel will gracefully handle validation and will add to the ModelState dictionary so we can check for validity
