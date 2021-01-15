---
type: rule
archivedreason: 
title: Do you initialize variables outside of the try block?
guid: ef08f3ac-8434-4e07-bfea-c33b7e03ae38
uri: do-you-initialize-variables-outside-of-the-try-block
created: 2018-04-26T21:41:56.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
- initialize-variables-outside-of-the-try-block

---

You should initialize variables outside of the try block.
  
<!--endintro-->



```
Cursor cur;
try
{
...
cur = Cursor.Current; //Bad Code - initializing the variable inside the try block
Cursor.Current = Cursors.WaitCursor;
...
}
finally
{
Cursor.Current = cur;
}
```




::: bad
Bad Example: Because of the initializing code inside the try block. If it failed on this line then you will get a NullReferenceException in Finally

:::



```
Cursor cur = Cursor.Current; //Good Code - initializing the variable outside the try block
try
{
...
Cursor.Current = Cursors.WaitCursor;
...
}
finally
{
Cursor.Current = cur;
}
```




::: good
Good Example : Because the initializing code is outside the try block

:::
