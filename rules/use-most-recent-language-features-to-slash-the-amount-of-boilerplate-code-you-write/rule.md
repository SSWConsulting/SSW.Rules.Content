---
type: rule
archivedreason: Rule is dated. Broken apart into individual rules
title: Do you use the new C# 7 language features to slash the amount of boilerplate code you write?
guid: a1f628a2-b249-4057-bb34-74280db06e8f
uri: use-most-recent-language-features-to-slash-the-amount-of-boilerplate-code-you-write
created: 2018-04-30T22:39:55.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
- do-you-use-the-new-c-7-language-features-to-slash-the-amount-of-boilerplate-code-you-write

---

Up until this point, .NET developers had to write a lot of boilerplate code in order to properly format strings or check for null. This boilerplate code required a lot of work to ensure code readability and maintainability.

The new C# 6 that comes with Visual Studio 2015 is a game changer that empowers devs to do more with less.

These 3 features will slash the amount of boilerplate code you have to write and improve code quality:


<!--endintro-->

1. nameof expressions - allows us to get the name of the type of object    Now when we throw an exception, we can use the name of expressions feature to create robust code, which is more resistant to common mistakes when refactoring. This is achieved by reducing the amount of hard coding.
    As you can see, when in the past you would have to write the following code:



```
(if customer.Address.ZipCode == null) throw new ArgumentNullException("ZipCode");
```




::: bad
Figure: Bad example - Amount of boiler plate code for a simple task  

:::
    Now you only have write:



```
(if customer.Address.ZipCode == null) throw new ArgumentNullException(nameof(customer.Address.ZipCode));
```




::: good
Figure: Good example - The same functionality as the Bad Example in a single line of code  
:::
 The benefit of this change is when refactoring our code, we don't need to worry about searching for magic strings. Which commonly slip through the cracks and lead to confusing error messages.
2. String Interpolation - greatly reduces the amount of boilerplate code required when working with strings
    Formatting strings on the fly was previously a task which required a stack of boilerplate code. In the Visual Studio 2015, we can use the smart String Interpolation feature. Not only does this feature reduce the amount of code we have to write, it also improves code readability.
    For example, before C# 6, we would write:



```
var s = String.Format("Profit is ${0} this year", p.TotalEarnings - p.Totalcost);
```




::: bad
Figure: Bad example - Using the string format make the code difficult to read

:::
    Now we are able to:



```
var s = "Profit is ${p.TotalEarnings - p.Totalcost} this year";
```




::: good
Figure: Good example - Very human readable code

:::
    As can be seen above by making use of the new String Interpolation feature, the understandability of your code is greatly improved.
3. Null-conditional operators - makes checking for null as easy as inserting a single question mark    This great new feature has had a raft of positive reactions from developers. The new Null-conditional operators feature boils down all of the previously laborious clunky code into a single question mark.
    For example, previously we would of had to write a chunk of code to achieve a simple task



```
if(customers.Length != null) { int length = customers.Length; } else { int length = 0; }
```




::: bad

Figure: Bad example - Fragile code

:::
    Now we are able to replace that chunk of code with a single line



```
int length = customers?.Length ?? 0;
```




::: good
Figure: Good example - Robust code 

:::
    In short, these new features will save you time, and help you write cleaner, more robust code - what's not to love?
