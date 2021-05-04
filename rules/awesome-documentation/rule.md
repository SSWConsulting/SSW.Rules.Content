---
type: rule
archivedreason: 
title: Do you make awesome documentation?
guid: d9a17cdf-0f7c-43dc-91a1-7b8fcc29467d
uri: awesome-documentation
created: 2012-03-16T08:01:26.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: Damian Brady
  url: https://ssw.com.au/people/damian-brady
- title: Eric Phan
  url: https://ssw.com.au/people/eric-phan
- title: Ulysses Maclaren
  url: https://ssw.com.au/people/ulysses-maclaren
- title: Adam Stephensen
  url: https://ssw.com.au/people/adam-stephensen
- title: Matt Goldman
  url: https://ssw.com.au/people/matt-goldman
related:
- reference-do-you-use-the-correct-symbols-when-documenting-instructions
- reference-do-you-use-the-right-order-of-instructions
- do-you-highlight-actions-correctly-in-your-document
- do-you-make-numbers-more-readable
- do-you-include-version-numbers-in-your-file
- do-you-refer-to-the-reader-and-author-consistently-throughout-your-document
- tiny-do-you-use-active-phrases-no-zombies-please
redirects:
- do-you-review-the-documentation
- do-you-make-awesome-documentation

---

There are a few styles of documentation:

<!--endintro-->

### Bad Example – Old School


::: bad  
![Figure: Bad example - The dinosaur’s method of documentation](old-documentation.png)  
:::

The old school way is document first – lots of planning, and lots of heavy documentation created upfront before even a single line of code is written.

This is the method most familiar to teams who are comfortable with Waterfall and have possibly never heard of Agile. Documentation can normally be characterized by:

* Heavy, long documents
* Sequence Diagrams
* UML

This is a well-established way to do documentation, but it has several problems:

* Gets out of date quickly
* High maintenance overhead
* Needs a business analyst



::: bad  
![Figure: Bad example - Documentation can take the form of Sequence Diagrams](enterprisearchitect1.jpg)  
:::


::: bad  
![Figure: Bad example - Use Case Diagrams are even worse!](EnterpriseArchitectUseCases.jpg)  
:::

There may be exceptions – some situations benefit from this kind of documentation; for example, it may be necessary to support a business case – although a well-defined spec is a better document to support a business case.



::: greybox
 **More info:** https://rules.ssw.com.au/rules-to-better-specification-reviews

:::
**Tip:** Documentation should be as minimal as possible. If your circumstances require this style of documentation, start by limiting it to just enough to cover your first couple of Sprints. And recognize that by going down this path you make a commitment to keeping it up-to-date.



### Good example – The 7 Important Documents


This style of documentation is used by modern teams who are Agile only.


There are 7 crucial documents for your project:

**In the repository (for developers):**

**1. README.md** – Explains the overview of the project and provides links to the rest of the documentation.

**2. docs\Instructions-Compile.md** – Instructions on how to build and run the project (AKA the F5 experience).

**3. docs\Instructions-Deployment.md** – Explains how to deploy the solution, including any additional processes (e.g. DevOps)

**4. docs\Business** – explains the purpose of the application, including the problem, goals, and statement of intent.

**5. docs\Technologies-and-Architecture** – Provides a technical overview of the solution, including any 3rd party libraries or utilities, patterns followed (e.g.        [https://rules.ssw.com.au/rules-to-better-clean-architecture](/rules-to-better-clean-architecture)), architecture decisions, etc. This document should cover software architecture and cloud architecture (or on-premises if you’re a dinosaur 🦕), and should \*always\* have a system architecture diagram (see:        [https://rules.ssw.com.au/have-an-architecture-diagram](/have-an-architecture-diagram)), as well as an Azure resources diagram, see: [https://rules.ssw.com.au/azure-resources-diagram/](/azure-resources-visualizing)

**6. docs\Definition-of-Done** - Ensures that your team [maintains a high level of quality with a Definition of Done](/done-do-you-go-beyond-done-and-follow-a-definition-of-done)

**7. docs\Definition-of-Ready** – Ensures that all your PBIs are well defined to an agreed standard before adding them to a sprint (see:        [https://rules.ssw.com.au/have-a-definition-of-ready](/have-a-definition-of-ready))


Keeping these documents in the repository means that you ensure that any documentation the developers need to work on or run the code is where they need it - with the code.

It also means that when a developer makes a change to the code that needs an update to the documentation, the documentation changes can be checked in along with the code in the same commit.


**Exposing documentation through a Wiki (for developers and other stakeholders):**

Documents to be read or edited by the Product Owner (or other members of the Scrum team) should be exposed through a Wiki. The advantage of this approach is that the writing experience in the Wiki is more friendly for non-developers. We recommend that your Wiki is sourced from the repo **docs\\** folder to ensure documentation is kept up to date with development. There are several options for creating a Wiki:

Azure DevOps
* [Wiki edited via the repo](https://docs.microsoft.com/en-us/azure/devops/project/wiki/publish-repo-to-wiki?view=azure-devops&tabs=browser) (recommended)
* [Wiki edited via the portal](https://docs.microsoft.com/en-us/azure/devops/project/wiki/wiki-create-repo?view=azure-devops&tabs=browser)
* An alternative wiki platform (e.g. [Confluence](https://www.atlassian.com/software/confluence))

GitHub
* On [GitHub Pages](https://pages.github.com/) (recommended)
* The [GitHub repo Wiki](https://docs.github.com/en/communities/documenting-your-project-with-wikis/about-wikis)
* An alternative wiki platform (e.g. [Confluence](https://www.atlassian.com/software/confluence))


**Tip** : All of your documents (in your Wiki and your repository) should be written in Markdown (see:     [https://rules.ssw.com.au/using-markdown-to-store-your-content](/using-github-and-markdown-to-store-you-content))




::: bad  
![Figure: Bad example - Github project without any documentation or instruction](documentation__level2__bad-example-gh.png)  
:::


::: bad  
![Figure: Bad example - Azure DevOps project without any documentation or instruction](azuredevops-bad.png)  
:::

![Figure: OK example - Github project with README instructions on how to compile and run the project (but still has a TODO)](documentation__level2__good-example-1-gh.png)  


::: good  
![Figure: Good example - Azure DevOps project with README instructions on how to compile and run the project](azuredevops-good.png)  
:::


::: good  
![Figure: Good example - Github project with Wiki instructions for product owners, stakeholders, or public consumption (Source: https://github.com/christoment/Northwind/wiki)](documentation__level2__good-example-2-gh.png)  
:::


::: good  
![Figure: Good example - Azure DevOps project with Wiki instructions for product owners, stakeholders, or public consumption](azuredevops-wiki-good.png)  
:::

**Tip:** Use your documentation for onboarding developers



::: bad  
![Figure: Bad Example - No documentation, go and sit with another developer](sit-dev-bad.png)  
:::


::: good  
![Figure: Good example - Developer onboarding can be self-guided by good documentation, and offers a structure for feedback and improvement if the developer hits any issues](documentation\_\_level2\_\_onboarding-pbi-3.png)  
:::

**Tip:** Keep your documentation as minimal as possible - automate the F5 experience and deployment process (documents 2 and 3) using PowerShell scripts. Then your documents can just say "run these scripts"

### The rest of the jigsaw



**Scrum Tip: Update your Acceptance Criteria** - If you use a policy that requires commits to be linked to PBIs, then you understand that the PBI is now the documentation. If requirements change (based on a conversation with the Product Owner of course) then the PBI should be updated.

When updating the Acceptance Criteria,        ~~strike through~~ the altered Acceptance Criteria, and add the new ones. Get the PO to confirm your understanding.

E.g.
~~Enter search text, click ‘Google’, and see the results populate below.~~
[Updated]
Enter search text and automatically see the results populate below.

This should be added to the        [Definition of Done](/done-do-you-go-beyond-done-and-follow-a-definition-of-done).


![Technical Debt](Debt.jpg)
**What's "Technical Debt"?**

During a project, when you add functionality, you have a choice:

One way is quick but messy - it will make further changes harder in the future (i.e. quick and dirty).

The other way is cleaner – it will make changes easier to do in the future but will take longer to put in place.

'Technical Debt' is a metaphor to help us think about this problem. In this metaphor (often mentioned during Scrum software projects), doing things the quick and dirty way gives us a 'technical debt', which will have to be fixed later. Like financial debt, the technical debt incurs interest payments - in the form of the extra effort that we must do in future development.

We can choose to continue paying the interest, or we can pay the debt in full by redoing the piece of work in a cleaner way.

The same principle is true with documentation. Using the 'old school' method will leave you with a build-up of documentation that you will need to keep up to date as the project evolves.

Warning: if you want to follow Scrum and have zero technical debt, then you must throw away all documentation at the end of each sprint. If you do want to keep it, make sure you add it to your [definition of done](/done-do-you-go-beyond-done-and-follow-a-definition-of-done)to keep it updated.
