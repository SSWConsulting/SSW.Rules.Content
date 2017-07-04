---
type: rule
title: Do you know to connect to VSTS Git with Personal Access Tokens
uri: do-you-know-to-connect-to-vsts-git-with-personal-access-tokens
created: 2017-07-03T05:46:30.0000000Z
authors:
- id: 24
  title: Adam Stephensen
- id: 58
  title: Jernej Kavka

---



<span class='intro'> <div>​​​When you create a new git repository and need to push it to VSTS you need to provide login credentials.​<br>​<br></div><div>It isn't always clear how to do this.<br>​<br></div><div><img src="/PublishingImages/vsts-alternative-login.png" alt="vsts-alternative-login.png" style="margin&#58;5px;width&#58;808px;" />&#160;</div><div><dd class="ssw15-rteElement-FigureBad">Figure&#58; Bad Example - Alternate &#160;Authentication Credentials should not be used. When you change the password it invalidates all projects and can't be scoped to limit access to your Team Services data.<br></dd><p class="ssw15-rteElement-P">​<br></p><p class="ssw15-rteElement-P">Instead, you should use Personal Access Token. You can do this in two ways.</p><p class="ssw15-rteElement-P">The first option is to make sure your Git for Windows is up-to-date and when cloning the repository, you use Microsoft Account to log in. Personal Access Token for Git will be created for you.</p><p class="ssw15-rteElement-P"><img src="/PublishingImages/git-credentials-personal-access-token.png" alt="git-credentials-personal-access-token.png" style="margin&#58;5px;width&#58;808px;" />&#160;</p><dd class="ssw15-rteElement-FigureGood">Figure&#58; Good Example - Windows for Git credential manager will automatically create Personal Access Token for Git.<br></dd><p class="ssw15-rteElement-P"><br></p><p class="ssw15-rteElement-P">Option 2 is to manually create Personal Access Token and use it as a password for Git login.<br></p><p class="ssw15-rteElement-P">You can follow this blog post for full instructions&#58;&#160;<a href="https&#58;//roadtoalm.com/2015/07/22/using-personal-access-tokens-to-access-visual-studio-online/">Using Personal Access Tokens to access Visual Studio&#160;Online </a><br><br></p><p class="ssw15-rteElement-P"><img src="/PublishingImages/git-credentials-personal-access-token-manual.png" alt="git-credentials-personal-access-token-manual.png" style="margin&#58;5px;width&#58;808px;" /><br></p><dd class="ssw15-rteElement-FigureGood">Figure&#58; Good Example - You can also manually enter Personal Access Token into password section if the credential manager doesn't work.<br></dd><br></div> </span>




