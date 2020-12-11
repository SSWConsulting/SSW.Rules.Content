---
type: rule
archivedreason: 
title: Do you have a Preflight Checklist?
guid: 8657ba34-afda-47b8-8728-f971fd3f699b
uri: do-you-have-a-preflight-checklist
created: 2015-11-01T21:13:26.0000000Z
authors:
- id: 37
  title: Ben Cull
related: []

---

Before starting any work, you should ensure developers take a look at your Application Insights data to make sure everything is performing correctly. 
<!--endintro-->



Most developers check only this first item before starting their work:

1. Check Unit Tests are Green


![Tests are green. I'm ready to start work... or am I?](unittests.png)



More advanced teams check their application insights data as well. This includes:

2. Look for any new Unhandled Exceptions


> See [Do you know the daily process to improve the health of your web application?](/_layouts/15/FIXUPREDIRECT.ASPX?WebId=3dfc0e07-e23a-4cbb-aac2-e778b71166a2&TermSetId=07da3ddf-0924-4cd2-a6d4-a4809ae20160&TermId=87dd82da-1716-4112-97f9-9161398eee1c)



> 
![](App-Insights-Failures.png)
> 
> **Figure: Unhandled Exceptions - Is there anything you don't know about here?**




3. Look for any obvious performance issues (Server then client).


> See [Do you know how to find performance problems with Application Insights?](/_layouts/15/FIXUPREDIRECT.ASPX?WebId=3dfc0e07-e23a-4cbb-aac2-e778b71166a2&TermSetId=07da3ddf-0924-4cd2-a6d4-a4809ae20160&TermId=ee100854-c5a4-44fd-ae5e-1d3a825ca4fe)





> 
![](performance-4.jpg)
> 
> **Figure: Performance - The Server Responses tab shows the slowest running pages.**
