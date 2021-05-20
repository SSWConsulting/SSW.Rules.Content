---
type: rule
archivedreason:
title: Agreements - Do You Book the Next Sprint Ahead of Time?
guid: 911032e8-861d-4b21-a00e-9e2822bb7e41
uri: agreements---do-you-book-the-next-sprint-ahead-of-time
redirects:
- jack-test-rule
created: 2021-04-07T06:35:55.0000000Z
authors: 
  - title: Nicholas Viet
    url: https://www.ssw.com.au/people/nick-viet
related:
- agreements---do-you-use-1-or-2-week-sprints
- agreements---do-you-know-who-pays-for-bugs
- agreements---do-you-join-the-team-as-a-tester
---


![Figure: Is this Broken?](Bad-Commit-Message.png)


Unless we're currently working on the last sprint of the development, you should always book the next sprint as soon as you start work on the current one.

<!--endintro-->

This is done during the [planning meeting](/Management/RulesToBetterScrumUsingTFS/Pages/SprintPlanning%28WHAT%29Meeting.aspx)and will ensure the availability of the developers who are up to speed on your project and stop them from being booked onto something else.



::: hidden  
e7d15b01-2a21-4e0f-bc71-c09e5d356cbc-7947936  
:::

::: hidden  
e7d15b01-2a21-4e0f-bc71-c09e5d356cbc-7947936  
:::

`oembed: https://twitter.com/MrHinsh/status/24123713864`
::: good
Figure: Not bad
:::

`oembed: https://twitter.com/MrHinsh/status/24123713864`

::: bad
Figure: Not good
:::


::: hidden  
e7d15b01-2a21-4e0f-bc71-c09e5d356cbc-7947936  
:::

::: hidden  
a854bdb8-1a3e-415e-b346-0a35466b6a93-7947936  
:::


![If you have booked the guys in, you will have an appointment like this in your Outlook.](Scheduled_Appointment.jpg)

::: email-template  
|         |     |
| ------- | --- |
| To:     | XXX |
| Cc:     | YYY |
| Bcc:    | ZZZ |
| Subject | This is the subject |  

::: email-content  
### Hi XXX,  
[Email content]    
:::  
:::  
::: good  
Figure: Good Example - Nice email template  
:::


```csharp
protected override void OnPreLoad(EventArgs e)
{
     //Fix for pages that allow edit in grids
     this.Controls.ForEach(c=>
     {   
          if (c is System.Web.UI.Timer)
          {
              c.Enabled = false;
          }
     });
     base.OnPreLoad(e);
}
```

```javascript
let iceCream = 'chocolate';
if(iceCream === 'chocolate') {
  alert('Yay, I love chocolate ice cream!');    
} else {
  alert('Awwww, but chocolate is my favorite...');    
}
```

```java
public class Main {
  public static void main(String[] args) {
    System.out.println("Hello World");
  }
}
```
