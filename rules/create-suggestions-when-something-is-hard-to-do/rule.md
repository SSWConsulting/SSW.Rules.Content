---
type: rule
archivedreason: 
title: Do you always create suggestions when something is hard to do?
guid: 7058fd5e-0a18-4f25-b085-c499a2c5ab17
uri: create-suggestions-when-something-is-hard-to-do
created: 2018-04-30T22:04:43.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
- do-you-always-create-suggestions-when-something-is-hard-to-do

---

One of our goals is to make the job of the developer as easy as possible. If you have to write a lot of code for something that you think you should not have to do, you should make a suggestion and add it to the relevant page.

If you have to add a suggestion, make sure that you put the link to that suggestion into the comments of your code.

<!--endintro-->



```
/// <summary>
/// base class for command implementations
/// This is a work around as standard MVVM commands
/// are not provided by default. 
/// </summary>
public class Command : ICommand
{
 // code
}
```




::: bad
Figure: Bad example - The link to the suggestion should be in the comments

:::



```
/// <summary>
/// base class for command implementations
/// This is a work around as standard MVVM commands
/// are not provided by default. 
/// </summary>
///
/// <remarks>
///  Issue Logged here: https://github.com/SSWConsulting/SSW.Rules/issues/3
///</remarks>
public class Command : ICommand
{
 // code
}
```




::: good
Figure: Good example - When you link to a suggestion everyone can find it and vote it up  
:::
