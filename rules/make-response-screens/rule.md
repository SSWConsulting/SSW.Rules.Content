---
type: rule
archivedreason: 
title: Microsoft Access - Do you make response screens? 
guid: 1db064f1-6b74-41a8-b8e8-0a6ae4528c1b
uri: make-response-screens
created: 2021-06-14T19:17:07.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects: []

---

One of the more common complaints about Microsoft Access databases is that some screens are slow to respond. **This is often misinterpreted as poor performance on the part of the database engine but the real culprit is usually the screen design.**

Here are a few techniques that developers can use to improve screen responsiveness.

<!--endintro-->

#### 1) Fetch fewer records

It is far too easy to create a screen that fetches all the records in a table. Such a time consuming exercise is seldom necessary and serves only to make screens appear sluggish. Users are usually interested in a few or perhaps only one specific record. They may simply wish to add a new record. In either case, it is a waste of time to fetch enormous quantities of data. If you are on a local area network, you will not only slow down your own application but probably annoy most of your cohorts by greatly increasing network traffic.

The solution is to open screens, or forms as they are called in Microsoft Access, with queries that contain 'where clauses' that use specific criteria to limit the number of records retrieved.

**Tip:** Open forms with criteria that return no records at all. Allow the user to enter criteria in the form header. It is quicker to refresh an existing form after the user enters criteria than it is to load a new form while fetching data.

Example:

You have a table named "Client" with 10,000 records. The poor way to retreive records from is:

`Form.RecordSource = "SELECT * FROM Client"`

Form.RecordSource = "SELECT * FROM Client"
Called by

`Docmd.OpenForm "frmClient","ClientID='SSW'"`

The problem with this method, is that all records are returned to the client, and then the client filters them to 1. A filter does not stop the records from returning. Fetching 10,000 records to view 1 is a large waste of resources, and leads to performance problems.

A better way to New Scenario he wants Big Forms to change to:

`Form.RecordSource = "SELECT * FROM Client WHERE 1<>1"`

The solution Called via a wrapper function for OpenForm: 

`Function aOpenForm("frmClient","ClientID='SSW')`

...So they open instantly with no records - Need a function to parse the where clause and then replace with passed in where clause - reruns query to get 1 record - much faster Note Some little form you don't want this behaviour So keep a table 'zsOneRecordForm' with the forms you want as a one record form So when you call aOpenForm it can look up this table 'zsOneRecordForm' and determine if it should change the RecordSource OR apply a filter.

#### 2) Fill those drop-down lists when you need them

Entering criteria almost always requires drop-down lists to avoid mistakes and tedious guessing. Unfortunately, drop-down lists are notoriously slow. A few drop-down lists can cause the opening of a form to become intolerably glacial. The reason is that drop-down lists always fetch as much data as they possibly can even if you limit the number of records they display.

Every drop-down list takes its time to fetch data and delays the loading of the form even if the user has no need to use the list. The obvious solution is to populate the drop-down lists when the user activates them.

**Tip:** Use an event procedure or a button to set the row source for the drop-down list. For example:

`Me!myDrop List.Row Source = Q`

...where Q is, once again, either the name of a query or an SQL string.

**Tip:** Drop-down lists themselves will be more responsive if they return fewer records. Try cascading criteria so that successive lists are limited by the selection in a previous list. The row source query for a list could depend on the item selected in a previous list as in this example: 

`Q = " SELECT Field1, Field2 FROM Table1 WHERE Field3 = " & Me!DropList1`

