---
type: rule
archivedreason: 
title: Do you avoid using if-else instead of switch block?
guid: 669b5f2d-6e38-4e12-be49-4619960435b2
uri: do-you-avoid-using-if-else-instead-of-switch-block
created: 2018-04-30T22:12:26.0000000Z
authors:
- id: 1
  title: Adam Cogan
related: []

---

The .NET framework and the C# language provide two methods for conditional handling where multiple distinct values can be selected from. The switch statement is less flexible than the if-else-if tree but is generally considered to be more efficient. .NET compiler generates a jump list for switch block for that reason it is faster for long list of condition. And also complier has the ability to optimize the switch block. Condition in the switch block is faster as compiler evaluated the condition once but for if-else block, compiler need to evaluate the condition for each 'else if' block

**Note:** Performance is very much negligible when number of condition is less than 5. So if the code design is clearer & easily maintainable by using if-else block, then Developer should use if-else block for fewer conditions.


<!--endintro-->

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


::: bad
Figure: Bad example of coding practice
:::




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


::: good
Figure: Good example of coding practice which will result better performance 

:::


Further Reading: [Speed Test: Switch vs If-Else-If](http&#58;//www.blackwasp.co.uk/SpeedTestIfElseSwitch.aspx)
