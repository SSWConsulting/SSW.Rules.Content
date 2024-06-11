---
seoDescription: Migrate to TFS 2010 seamlessly by having a developer test the migration process.
type: rule
archivedreason:
title: Do you get a developer to test the TFS 2010 migration?
guid: 0b9c4772-0345-4b76-878d-206e328f4fff
uri: get-a-developer-to-test-the-migration-tfs2010-migration
created: 2009-11-08T02:06:26.0000000Z
authors:
  - title: Martin Hinshelwood
    url: https://ssw.com.au/people/martin-hinshelwood
related: []
redirects:
  - do-you-get-a-developer-to-test-the-migration
---

Getting someone else to test the migration is the best way to make sure that you have not missed anything.

<!--endintro-->

1. Run [SSW Diagnostics](https://www.ssw.com.au/ssw/Diagnostics/Default.aspx), check it’s all green ticks
2. Diagnostics will pick up that you need the Visual Studio 2008 SP1 Forward Compatibility Update for Team Foundation Server 2010 installed
3. Start Visual Studio 2008
4. Open Team Explorer
5. Add a new server. E.g. tfs.northwind.com:8080/tfs/

![Figure: Remember to use the "/tfs" option when connecting to the new server](AddTeamFoundationServer.png)

6. Confirm that the following are correct
   1. Source Code - connect to TFS2010 server and confirm that you can get latest.
   2. Source Code history - check that the source history is intact
   3. Work Items - confirm that you can see the last work items that you created
   4. Team Project - Create a new team project and check the SharePoint portal and reports work

**Note:** This will need to be done using Team Explorer 2010 as it is not supported in 2008.

### Congratulations, you’ve done a successful migration
