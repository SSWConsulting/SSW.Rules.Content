---
seoDescription: Rollback changes in TFS by undoing pending changes or using Team Foundation Server Power Tools to revert unwanted code revisions.
type: rule
archivedreason:
title: Do you know how to rollback changes in TFS?
guid: 6980541f-5084-4ef7-b997-51d90f4e6885
uri: do-you-know-how-to-rollback-changes-in-tfs
created: 2011-11-18T03:52:54.0000000Z
authors:
  - title: David Klein
    url: https://ssw.com.au/people/david-klein
    noimage: true
  - title: Justin King
    url: https://ssw.com.au/people/justin-king
  - title: Ryan Tee
    url: https://ssw.com.au/people/ryan-tee
    noimage: true
  - title: Tristan Kurniawan
    url: https://ssw.com.au/people/tristan-kurniawan
related: []
redirects: []
---

This field should not be null (Remove me when you edit this field).

<!--endintro-->

There are two ways to do this:

**A.** If you haven’t checked in any files since you started modifying them then the process is simple:

* Right click your solution and **Undo Pending Changes**

  ![](rollback1.gif)

**B.** If you aren’t so lucky and have made some commits along the way then the only option is to use the Rollback command:

To use this you will need to install Team Foundation Server Power Tools v1.2

* Find the revision before you started checking code in using the **History command**

  ![Figure: The last revision before Tristan made changes was 5367](rollback2.gif)

* Open the Command Prompt in your current working directory and type **“c:\Program Files\Microsoft Team Foundation Server Power Tools\tfpt.exe” rollback /changeset:5367**

  ![](rollback3.gif)

* Click  **Yes** and the rollback will proceed

---

It would be nice if there was a GUI for this tool so that I can just right click and select rollback.

See [Better Software Suggestion – TFS](https://www.ssw.com.au/archive/standards/better-software-suggestions/team-foundation-server.html#RollbackGUI)
