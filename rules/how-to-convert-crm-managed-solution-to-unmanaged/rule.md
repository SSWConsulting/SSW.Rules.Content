---
type: rule
archivedreason: 
title: Do you know how to convert Dynamics CRM managed solution to unmanaged?
guid: d8ccbbb0-b1a9-4864-933f-9c59b7e49931
uri: how-to-convert-crm-managed-solution-to-unmanaged
created: 2015-06-18T04:36:23.0000000Z
authors: []
related: []
redirects:
- do-you-know-how-to-convert-dynamics-crm-managed-solution-to-unmanaged

---

You might need to modify solutions during migration. But if that solution is managed, you cannot edit directly. If you have the unmanaged version in development environment, you can edit it and override the production managed solution. 

<!--endintro-->

If you don't have the unmanaged version (which is bad practice), see [here](https://community.dynamics.com/ax/b/thedynamicsblog/posts/converting-managed-solutions-to-unmanaged-solutions-crm-2013) for good practice about CRM ALM. Use the following script to hack the org database

```
 declare @solutionId uniqueidentifier, @systemSolutionId uniqueidentifier

-- specify the uniquename of the managed solution you'd like to unmanage here it is StagingOrg

select @solutionId = solutionid from SolutionBase where UniqueName='Your solution name'
-- DO NOT TOUCH FROM HERE ON --

select @systemSolutionId = solutionid from SolutionBase where UniqueName='Active' update PublisherBase set IsReadonly=0 where PublisherId in (select PublisherId from SolutionBase where SolutionId=@solutionId) print 'updated publisher' declare @tables table (id int identity, name nvarchar(100), ismanaged bit, issolution bit) declare @count int, @currentTable nvarchar(100), @currentM bit, @currentS bit, @sql nvarchar(max)
-- go through all the tables that have the ismanaged/solutionid flag, find the related records for the current solution and move them to the crm active solution.

insert into @tables (name, ismanaged, issolution) select name, 1, 0 from sysobjects where id in (select id from syscolumns where name in ('IsManaged')) and type='U' order by name
 

insert into @tables (name, ismanaged, issolution) select name, 0, 1 from sysobjects where id in (select id from syscolumns where name in ('SolutionId')) and type='U' and name not in ('SolutionComponentBase') and name not like '%ribbon%' -- ignore this table because it doesn't make a difference. it does cause dependency errors on the exported solution but we can manually edit the xml for that. order by name
 

select @count = count(*) from @tables while (@count > 0)
begin

select @currentTable =name, @currentM =ismanaged, @currentS =issolution from @tables where id=@count
 

if (@currentM = 1) begin select @sql ='update ' + @currentTable + ' set IsManaged=0 where SolutionId=N''' + cast(@solutionId as nvarchar(100)) + '''' exec (@sql)
 

print 'updated IsManaged to 0 on: ' + @currentTable end
 

if (@currentS = 1) begin select @sql ='update ' + @currentTable + ' set SolutionId=N''' + cast(@systemSolutionId as nvarchar(100)) + ''' where SolutionId=N''' + cast(@solutionId as nvarchar(100)) + '''' exec (@sql)
 

print 'updated SolutionId on: ' + @currentTable end
 

select @count = @count -1, @currentTable = NULL
end
```
