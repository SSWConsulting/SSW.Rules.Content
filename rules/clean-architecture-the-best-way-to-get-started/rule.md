---
type: rule
archivedreason: 
title: Do you know the best way to get started?
guid: 4e1e6234-c8b8-4065-83d5-74c8b6e30f2b
uri: clean-architecture-the-best-way-to-get-started
created: 2020-06-01T22:27:33.0000000Z
authors:
- title: Jason Taylor
  url: https://ssw.com.au/people/jason-taylor
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
- do-you-know-the-best-way-to-get-started

---


<p class="ssw15-rteElement-P">If you're building applications based on .NET Core then the Clean Architecture Solution Template is the best way to get started.<br></p>
<br><excerpt class='endintro'></excerpt><br>
<dl class="image"><dt><img src="clean-architecture-solution-template.png" alt="clean-architecture-solution-template.png" style="width:750px;" /></dt><dd>Figure: The Clean Architecture Solution Template by @JasonTaylorDev</dd></dl><p>​The template is designed for creating a Single Page App (SPA) with Angular and ASP.NET Core, but it can easily be used for other .NET Core applications. Create a new project based on this template by visiting <a href="https://github.com/jasontaylordev/CleanArchitecture/">https://github.com/jasontaylordev/CleanArchitecture/</a> and clicking <strong>Use this template</strong> or by installing the 
   <a href="https://www.nuget.org/packages/Clean.Architecture.Solution.Template">.NET Core Project Template</a> package. To do so, follow these steps:</p><ol><li>Install the latest <a href="https://dotnet.microsoft.com/download">.NET Core SDK</a></li><li>Install the latest <a href="https://nodejs.org/en/">Node.js LTS</a></li><li>Run <strong>dotnet new --install Clean.Architecture.Solution.Template</strong> to install the project template</li><li>Create a folder for your solution and cd into it (the template will use it as project name)</li><li>Run <strong>dotnet new ca-sln</strong> to create a new project</li><li>Navigate 
      <strong>to </strong><strong>src/WebUI</strong> and run <strong>dotnet run</strong> to launch the project</li></ol><p>If you would like to learn more, review the following blog post: <a href="https://jasontaylor.dev/clean-architecture-getting-started/">Clean Architecture with .NET Core: Getting Started</a>.<br></p>


