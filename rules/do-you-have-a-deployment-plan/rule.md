---
type: rule
archivedreason: 
title: Do you have a deployment plan?
guid: f730bb7f-e390-4f50-90e6-5d460779aedc
uri: do-you-have-a-deployment-plan
created: 2011-08-26T19:34:05.0000000Z
authors: []
related: []
redirects: []

---

Instructions are very important when maintaining a project. When someone new joins the project, you want to make sure that they can easily find the documentation to do tasks like setting up the project and deploying it. 

See the rule "[Do you make instructions at the beginning and improve it gradually for web projects?](/do-you-make-instructions-at-the-beginning-of-a-project-and-improve-them-gradually)" 

<!--endintro-->

That being said, the deployment plan is an important part of the Instructions.docx. It should clearly layout all the steps required to:

1. Deploy from scratch to a new server
2. Update versions
3. Rollback to a previous version
4. Update Schema or data

It should also include checks to verify the deployment was successful. E.g.:

1. Check zsValidate.aspx
2. Check runtime settings (e.g. Payment Gateways, Google Analytics, Connection strings)
3. Manual testing procedure (e.g. Place an order)

This document should also be signed off by the project lead and verified by the client.
