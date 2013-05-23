

---
authors:
  - id: 23
    title: Damian Brady
---




<span class='intro'> <p>If you’re upgrading TFS 2010 to 2012, it’s highly recommended that you assign sysadmin privileges to the user account that’s doing the upgrade.</p> </span>

<p>Some database upgrade steps involve ALTER DATABASE statements and other commands that can’t be done by a normal user.  If a step fails, you are likely to end up with a corrupted Configuration database (so you have to restore from backup).​​​</p>


