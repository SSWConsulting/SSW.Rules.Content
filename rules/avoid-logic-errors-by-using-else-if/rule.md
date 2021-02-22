---
type: rule
archivedreason: 
title: Do you avoid logic errors by using Else If?
guid: 1e259f2d-e97e-47cc-bbb7-1f449a258367
uri: avoid-logic-errors-by-using-else-if
created: 2018-04-25T17:44:41.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
- do-you-avoid-logic-errors-by-using-else-if

---

We see a lot of programmers doing this, they have two conditions - true and false - and they do not consider other possibilities - e.g. an empty string. Take a look at this example. We have an If statement that checks what backend database is being used.

<!--endintro-->

In the example the only expected values are "Development" and "Production".



```
void Load(string environment)
{
  if (environment == "Development")
  {
    // set Dev environment variables
  }
  else
  {
    // set Production environment variables	
  }
}
```




::: bad
Figure: Bad example with If statement  
:::

Consider later that extra environments may be added: e.g. "Staging"

By using the above code, the wrong code will run because the above code assumes two possible situations. To avoid this problem, change the code to be defensive .g. Use an Else If statement (like below).

Now the code will throw an exception if an unexpected value is provided.



```
void Load(string environment)
{
  if (environment == "Development")
  {
    // set Dev environment variables
  }
  else if (environment == "Production")
  {
    // set Production environment variables	
  }
  else
  {
    throw new InvalidArgumentException(environment); 
  }
}
```




::: good
Figure: Good example with If statement

:::
