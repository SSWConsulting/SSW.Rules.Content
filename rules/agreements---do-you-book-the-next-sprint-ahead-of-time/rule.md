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
---


1. Add your website as a new device. 
![Figure: New device](running1.GIF)  

2. Ping monitor is added automatically. 
![Figure: Ping monitor](running2.GIF)  

3. Add an HTTP Content Scan monitor. 
![Figure: HTTP Content Scan](running3.GIF)  


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

```sql
WITH Level1 
       AS ( SELECT StaffMember , 
                   EventType , 
                   CAST(EventDate AS DATETIME) 
                   +   CAST(EventTime AS DATETIME) AS EventDateTime , 
                   LAG(EventType, 1, 'N/A') 
                      OVER ( PARTITION BY StaffMember 
                         ORDER BY EventDAGate, EventTime ) AS LastEvent , 
                   LEAD(EventType, 1, 'N/A') 
                      OVER ( PARTITION BY StaffMember 
                         ORDER BY EventDate, EventTime ) AS NextEvent 
            FROM StaffHours ), 
     Level2 
       AS ( SELECT StaffMember , 
                   EventType , 
                   EventDateTime , 
                   LastEvent , 
                   NextEvent 
            FROM   Level1 
            WHERE  NOT ( EventType = 'Enter' 
                         AND LastEvent = 'Enter' 
                       ) 
               AND NOT ( EventType = 'Exit' 
                         AND NextEvent = 'Exit' 
                       ) 
               AND NOT ( EventType = 'Enter' 
                         AND NextEvent = 'N/A' 
                       ) 
               AND NOT ( EventType = 'Exit' 
                         AND LastEvent = 'N/A' 
                       ) 
          ), 
     Level3 
       AS ( SELECT StaffMember , 
                   EventType , 
                   EventDateTime , 
                   DATEDIFF(second, EventDateTime, 
                            LEAD(EventDateTime) 
                               OVER ( PARTITION BY StaffMember 
                                  ORDER BY EventDateTime )) AS Seconds 
            FROM Level2 
           ) 
   SELECT StaffMember , 
          EventDateTime , 
          TIMEFROMPARTS(Seconds / 3600, Seconds % 3600 / 60, 
                        Seconds % 3600 % 60, 0, 0) AS WorkTime 
   FROM Level3 
   WHERE EventType = 'Enter';
```

**Figure: Javascript code block**
