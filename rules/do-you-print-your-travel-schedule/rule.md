---
type: rule
tips: ""
title: Do you print out the travel schedule for the months ahead?
seoDescription: "Discover the benefits of printed itineraries for staying
  organized and stress-free on your next trip. "
uri: do-you-print-your-travel-schedule
authors:
  - title: Stef Starcevic
    url: https://www.ssw.com.au/people/stef-starcevic/
  - title: Adam Cogan
    url: https://www.ssw.com.au/people/adam-cogan/
created: 2025-02-17T14:49:00.000Z
guid: 0fa64f9b-2d77-4762-946c-6afc21f6c6e8
---
\
\
Travel schedules can get complicated, especially when managing multiple trips or coordinating with team members. Relying solely on digital calendars can lead to missed details, especially when internet access is limited or when navigating multiple time zones. Having a printed version of your travel schedule can be a lifesaver in these situations.

<!--endintro-->

## Why It Matters

Printed travel schedules provide several benefits:

* **Quick Access:** No need to unlock devices or search through apps – just pull out the paper.
* **Reliability:** Battery life or technical issues won't hinder your ability to check your itinerary.
* **Comprehensive Overview:** Seeing your schedule on paper allows for a better overview, making it easier to spot conflicts or gaps.
* **Backup Plan:** If your device is lost or damaged, you still have your travel details on hand.

## How to Do It Right

1. **Plan in Advance:** Print your schedule at least a week before your trip to allow time for last-minute changes.
2. **Organize for Easy Access:** Use a travel folder or planner to keep the schedule organized along with other important documents like boarding passes and travel insurance.
3. **Update as Needed:** If plans change, update the schedule and reprint the necessary pages.

## Step by Step

![1. When you get an appointment, categorise it as "Travel"](pa-rule-1.png)

![2. Make a view that shows only your travel appointments](pa-rule-2.png)

![3. Set the date period to the end of year:  Print Options | Print Range| End Date](pa-rule-3.png)

![4. Print from that view](pa-rule-4.png)

## Notes

* If you want to view your boss's calendar to edit:
  * To give somebody else permissions to your calendar - right click on calendar | sharing and permissions. From there you can select someone to give permissions to.  
  * Alternatively, ask a SysAdmin - This had to be done in PowerShell – as per: https://learn.microsoft.com/en-us/powershell/module/exchange/add-mailboxfolderpermission
  *    The command is 
```Add-MailboxFolderPermission -Identity {{ BOSS'S EMAIL }}:\Calendar -User {{ YOUR EMAIL }} -AccessRights Editor```
* In the new Outlook, you cannot print your boss's calendar
  * Even though you can add categories, you cannot filter based on the boss's categories (as you only see your own filters in the filters list). Therefore you need to print from your boss's Outlook.

