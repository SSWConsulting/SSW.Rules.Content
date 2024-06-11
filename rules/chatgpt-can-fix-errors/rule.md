---
seoDescription: ChatGPT helps developers quickly resolve errors by providing instant feedback and solutions.
type: rule
title: Do you use ChatGPT to solve code errors?
uri: chatgpt-can-fix-errors
authors:
  - title: Adam Cogan
    url: https://www.ssw.com.au/people/adam-cogan
  - title: Piers Sinclair
    url: https://www.ssw.com.au/people/piers-sinclair
created: 2023-02-09T09:57:35.077Z
guid: 46827b4d-9efb-4783-8ade-e23068242c20
---

Sometimes, a developer runs into a complex error and they start googling all over the internet to fix the issue. In strange or unlucky cases this can result in hours of searching.

ChatGPT helps smooth this process. Simply paste the error into ChatGPT and it will give you instant feedback about the problem.

<!--endintro-->

For example, let's say you try to run ef migrations using the command:

```markup
dotnet ef database-update
```

If this command gives you an error like:

```markup
No project was found. Change the current working directory or use the --project option.
```

Then you could ask ChatGPT and it would give you the solution!

![Figure: ChatGPT helps you with an EF Core error message](ChatGPTFixesEFCoreError.png)

### Try it yourself, copy and paste this into [ChatGPT](https://chat.openai.com/)

```markup
What is this error in EF Core?
No project was found. Change the current working directory or use the --project option.
```
