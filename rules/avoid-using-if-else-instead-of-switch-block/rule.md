---
type: rule
archivedreason: 
title: Do you avoid using if-else instead of switch block?
guid: 669b5f2d-6e38-4e12-be49-4619960435b2
uri: avoid-using-if-else-instead-of-switch-block
created: 2018-04-30T22:12:26.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
- do-you-avoid-using-if-else-instead-of-switch-block

---

The .NET framework and the C# language provide two methods for conditional handling where multiple distinct values can be selected from. The switch statement is less flexible than the if-else-if tree but is generally considered to be more efficient.

The .NET compiler generates a jump list for switch blocks, resulting in far better performance than if/else for evaluating conditions. The performance gains are negligible when the number of conditions is trivial (i.e. fewer than 5), so if the code is clearer and more maintainable using if/else blocks, then you can use your discretion. But be prepared to refactor to a switch block if the number of conditions exceeds 5.

<!--endintro-->



```
int DepartmentId = GetDepartmentId()
if(DepartmentId == 1)
{
// do something
}
else if(DepartmentId == 2)
{
// do something #2
}
else if(DepartmentId == 3)
{
// do something #3
}
else if(DepartmentId == 4)
{
// do something #4
}
else if(DepartmentId == 5)
{
// do something #5
}
else 
{
// do something #6
}
```




::: bad
Figure: Bad example of coding practice  
:::





```
int DepartmentId = GetDepartmentId()
switch(DepartmentId)
{
case 1:
// do something
break;
case 2:
// do something # 2
break;
case 3:
// do something # 3
break;
case 4:
// do something # 4
break;
case 1:
// do something # 5
break;
case 1:
// do something # 6
break;
default:
//Do something here
break;
}
```




::: good
Figure: Good example of coding practice which will result better performance 

:::

Further Reading: [Speed Test: Switch vs If-Else-If](http&#58;//www.blackwasp.co.uk/SpeedTestIfElseSwitch.aspx)
