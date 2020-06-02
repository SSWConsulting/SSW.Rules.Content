---
uri: do-you-get-a-new-tfs-server-ready
title: Do you get a new TFS2010 Server ready?
created: 2009-11-02 23:10:40
authors:
  - id: 1
    title: Adam Cogan
  - id: 3
    title: Eric Phan
---




<span class='intro'> 
  <ol>
    <li>Prepare a new image. We recommend running <strong>Windows 2008 R2 Server x64 </strong>using Hyper-V Manager. Your options are&#58;
    <ol>
        <li>Manually build a server </li>
        <li>A syspreped image (this will be quicker) </li>
        <li>System Center Virtual Machine Manager (recommended, quickest) </li>
    </ol>
    </li>
    <li>Add the roles
    <ol>
        <li>Application Server </li>
        <li>IIS </li>
    </ol>
    </li>
    <li>Install <strong>SQL Server 2008 x64</strong> default configuration </li>
    <li>Install <strong>SQL Server 2008 SP1</strong> </li>
    <li>Run <a shape="rect" href="http&#58;//www.ssw.com.au/ssw/Diagnostics/">www.ssw.com.au/ssw/Diagnostics/</a> and get all green ticks </li>
</ol>
 </span>




