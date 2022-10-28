---
type: rule
title: Do you use emoji in Dynamics label?
uri: use-emoji-in-dynamics-label
authors:
  - title: Lu Zhang
created: 2022-10-28T02:58:56.919Z
guid: f9803ec8-a3a3-488e-b34d-98b7ef0a6b25
---
How do you show a tooltip or a note to a Dynamics user?

![Figure: How to show a tooltip like this in Dynamics?](image002.jpg "Figure: How to show a tooltip like this in Dynamics?")

### Option 1 -  Description attribute

Advantages:

* Out of box feature.  No customizations needed.

Disadvantages:

* Not obvious to see - user normally doesn't aware to hover to the label to see the note.

![Figure: The out-of-box description attribute can be used as a tooltip. But it's not obvious to see.](screenshot-at-oct-28-11-17-04.png "Figure: The out-of-box description attribute can be used as a tooltip. But it's not obvious to see.")



### Option 2 -  PCF control

Advantages:

* Flexibility - allow to customize any style or behaviour.

Disadvantages:

* Need more time to develop or install a package.
* Introduce a dependent package to the system.

![Figure: Use a PCF control to show a note and link to a web page](screenshot-at-oct-28-11-23-52.png "Figure: Use a PCF control to show a note and link to a web page")

### Option 3 -  Description field + Emoji (Recommended)

Add a emoji in the label to remind people to hover to see the tooltip. 

![Figure: Add a emoji on the label to remind to people it's a tooltip ](screenshot-at-oct-28-11-29-40.png "Figure: Add a emoji on the label to remind to people it's a tooltip ")