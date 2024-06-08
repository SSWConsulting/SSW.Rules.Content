---
type: rule
archivedreason: 
title: Do you get a developer to test the TFS 2015 migration?
guid: 4f9b5655-299b-4c7d-b281-722e72a13d88
uri: get-a-developer-to-test-the-migration-tfs2015-migration
created: 2015-08-14T11:37:58.0000000Z
authors:
- title: Martin Hinshelwood
  url: https://ssw.com.au/people/martin-hinshelwood
related: []
redirects:
- do-you-get-a-developer-to-test-the-migration1

---

It is important to get another developer to check the migration for issues.

<!--endintro-->

They should follow these steps:
1. Start Visual Studio 2013
2. Open Team Explorer and connect to the new TFS Server
3. Confirm that they can:
  - Source Code - Browse the projects and code using the Source Code Explorer
  - Source Code Operations - Get Latest on a file, make a change and check in
  - Source Code History - View the history of a number of files in different projects
  - Work Items - Browse and view recent work items
4. Open Visual Studio 2015 and repeat steps 1 to 3.
5. Test that your builds complete successfully on the upgraded build controller(s) and agent(s).
6. Check that they can create a new Team Project in Visual Studio 2015

### Congratulations! You've completed a successful migration!
