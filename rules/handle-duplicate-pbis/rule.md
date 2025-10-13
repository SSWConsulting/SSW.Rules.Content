---
type: rule
tips: ""
title: Do you know how to handle duplicate PBIs in your backlog?
seoDescription: Learn the best way to handle duplicate PBIs in GitHub backlogs
  to keep your project clean, organized, and user-focused.
uri: handle-duplicate-pbis
authors:
  - title: Zach Keeping
guid: 85612086-fd82-4d02-abd0-baf0b310004a
---


A clean backlog is crucial for maintaining focus, visibility, and productivity.  
When Product Backlog Items (PBIs) are duplicated, it creates confusion, unnecessary noise, and wasted effort as multiple team members may end up investigating or working on the same issue.


Instead of keeping multiple PBIs for the same topic, **always close duplicates** and **link them to the single active PBI** that will track the actual work.  
This keeps your backlog organised and ensures all updates, discussions, and history remain in one place.


---


## 💡 Why this is important


Duplicate PBIs can arise when:
- Different team members raise the same issue
- Similar feature requests come from separate sources (clients, the general public, internal QA, etc.)
- Old PBIs get forgotten and recreated


If left unmanaged, duplicates lead to:
- Confusion over which PBI to update or complete
- Redundant notifications and wasted triage time
- Incomplete communication — especially if the original raiser isn’t notified when their duplicate issue is closed


Cleaning duplicates ensures that:
- The backlog stays lean and accurate
- Work tracking is centralised
- Everyone who raised or was affected by the issue is informed when it’s resolved


---


### 🚫 Bad example


Multiple duplicate PBIs are left open for the same issue, creating clutter and confusion.


**Bad:**
- PBI #123 “Fix login timeout issue”  
- PBI #145 “Users logged out too quickly”  
- PBI #172 “Session expires unexpectedly”  


All three describe the same problem, but they remain open separately.  
Developers don’t know which one to update, and the backlog becomes messy.


📸 _Screenshot_


---


### ✅ Good example


Duplicate PBIs are closed and linked to a single active PBI.


**Good:**
- PBI #123 “Fix login timeout issue” remains active  
- PBI #145 and #172 are closed with a comment:
  > “Closing as duplicate of #123. Please track progress there.”


- The raisers of #145 and #172 are mentioned in #123 so they’re notified when the issue is completed.


📸 _Screenshot_


---


### 🧭 The process


When you find duplicate PBIs:


1. **Identify the main PBI**  
   Choose the most complete or widely referenced one to keep active.


2. **Close the duplicates**  
   Add a note to each duplicate such as:  
   > “Closing as duplicate of #123 – tracking will continue there.”


3. **Link them to the main PBI**  
   Use GitHub’s issue linking feature (`#123`) so others can follow the chain easily.


4. **Notify the original raisers**  
   Mention (`@username`) anyone who created or commented on the duplicate in the main PBI, so they’re informed when it’s closed.


5. **Consider automation**  
   If your workflow supports it, automate duplicate detection or user notification to reduce manual work.
