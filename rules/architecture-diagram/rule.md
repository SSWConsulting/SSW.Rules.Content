---
type: rule
archivedreason: 
title: Do you have an Architecture Diagram?
guid: 356ef246-3c81-4f04-8d5e-bf10d98f0bb8
uri: architecture-diagram
created: 2020-08-31T18:10:45.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: Matt Goldman
  url: https://ssw.com.au/people/matt-goldman
related: []
redirects:
- have-an-architecture-diagram
- do-you-have-an-architecture-diagram

---

A good architecture diagram (aka a cloud architecture diagram or system architecture diagram) gives a great overview of your project. An architecture diagram lets you see at a glance what the overall structure of the solution is. This is useful for gaining an understanding of how the system fits together, how it flows, and what it does. It also helps to easily show which components can be improved due to updated or better components (or improved architectural guidelines).


`youtube: https://www.youtube.com/embed/ek8ArrOfJxA`
 

An architecture diagram is useful when:

<!--endintro-->

* In the initial discussion with a client (see Brendan Richards' quote below)
* You are onboarding a new developer
* You have been deep into one aspect of the system and need a refresher on another area
* You have been off the project for a while
* Whenever you are discussing requirements that may require structural changes


The architecture diagram is a technical diagram that demonstrates the technology in use. The purpose of the architecture diagram is to show how a solution has been built and what the technical dependencies are. It is not used for user journeys or business logic.


::: bad  
![Figure: Bad Example - a screenshot of the Azure resources used helps, but doesn't show data flows or dependencies](image001.jpg)  
:::



Depending on the complexity of your solution and your comfort/familiarity with the tools, an architecture diagram could take you anywhere from half an hour to a couple of days.

Usually, the longer an architecture diagram takes you to make, the more important it is for your project.
 - Matt Goldman, Software Architect



An architecture diagram is part of the 7 crucial documents you need for your project, see our rule: [Do you make awesome documentation?](/do-you-review-the-documentation)

### Tip 1: Include your most important components


At a minimum, your architecture diagram should include:

* Your data repository
* Your business logic component
* Your UI

Your diagram needs to include the relationships between these components, and how they share and process data.


### Tip 2: Don't use a .NET Dependency Graph as a System Architecture Diagram


The .NET dependency diagram is a useful tool, but it drills down into a specific component of the solution (the code) while ignoring the rest of it (the infrastructure). If it adds value to your documentation (i.e., there is a specific reason to include it) you can include the .NET dependency diagram, but don't use it here in place of the architecture diagram.

See SSW rule: [Do you generate the VS Dependency Graph?](/do-you-generate-the-vs-dependency-graph)
![](dependency-validation-01.png)

::: bad
Figure: Bad Example - the .NET dependency diagram shows code dependencies, but not the application's architecture


:::

### Tip 3: Show data dependencies and data flows

Your architecture diagram should show how the components of your solution fit together. It should also show **\*how\*** the components of the architecture depend on each other for functionality, as well as upstream and downstream data dependencies.


::: good  
![Figure: OK Example - Shows the technologies and data flows (from the data --&gt; Azure Data Factory --&gt;Azure Databricks --&gt; Power BI). This gives an overview of the whole application in one diagram.](architecture-diagram-good1.png)  
:::

### Tip 4: Put data at the top


It should be easy to tell at a glance which direction data flows in your diagram: left to right, right to left,        <mark>top to bottom</mark>(recommended). Pick a direction for your data flow, and keep it consistent across all your documentation. Where there are exceptions (for example data going to analytics or to/from partner sources) make these perpendicular to the primary data flow direction.
![sugarlearning-architecture-diagram (1).png](sugarlearning-architecture-diagram (1).png)

::: good
Figure: Good example - SugarLearning (an Angular + .NET project) - data flows from top to bottom, with exceptions (e.g. Application Insights / Raygun, not part of the main data flow) perpendicular to the primary direction


:::

### Tip 5: Group relevant components


Group components logically by enclosing them in a box. Components that operate independently can stand alone, and those that work together to deliver a logical function can be grouped together. Also show components that are out of scope, i.e. important for understanding the architecture but not necessarily part of it, e.g. legacy components, partner components, or components that have not been implemented yet.

Note: for clarity, out of scope items whether one or many, should be in a box.
![rewards-architecture-diagram (2).png](rewards-architecture-diagram (3).png)

::: good
Figure: Good example - SSW Rewards (Xamarin with Azure Active Directory B2C) - consistent styling is used, e.g. as well as all the icons and typography being consistent, you can see that data is a solid line and auth traffic is a dotted line


:::

### Tip 6: Start with paper...


Make sure you use the right tools when creating your architecture diagrams. There's nothing wrong with starting out with pen and paper, but your hand-drawn sketch should not be considered your 'done' final architecture diagram. \*\* If you want to save paper, and increase collaboration, a great alternate is the trusty old Whiteboard.

For me its all about building a shared understanding between the client and the developers. Most pieces of software architecture I do, work starts by building a rough solution architecture diagram on a whiteboard. 

Putting something on a whiteboard is "low risk" for the participants as its really easy to wipe and redraw. It allows us to start working together straight away, building a shared understanding of what we're trying to achieve. There is no software or skills required to participate in whiteboard collaboration. 

A key milestone in the early engagement is the first time a client takes the pen and starts using the whiteboard to explain something to me. Early use of the whiteboard is all about immediate communication. Later, the solution design starts to solidify and we can then use the last state of the whiteboard to make out first architecture diagram.

- Brendan Richards, SSW Solution Architect
![](IMG_9906.JPG)**Figure: OK Example - SSW Rewards - start out with a hand-drawn sketch if that's easier for you, but don't consider this your final architecture diagram
** 
**Tip** **:** [Microsoft Office Lens](https://www.google.com.au/url?sa=t&rct=j&q=&esrc=s&source=video&cd=&cad=rja&uact=8&ved=2ahUKEwi6-NTb1MvrAhWXA3IKHevqC-MQtwIwAHoECAEQAQ&url=https://www.youtube.com/watch?v%3DjzZ3WVhgi5w&usg=AOvVaw25XKH6ZRcPfM5jaVajFOlH) is a free mobile app that uses your smartphone camera to capture scan-like images of documents, photographs, business cards, and whiteboards (including searchable handwritten text).
![](IMG_9908.JPG)

::: good
Figure: Better Example - SSW Rewards - the same sketch but captured with Office Lens. How much clearer and more vibrant is this!


:::

### Tip 7: ...and Finish up with Diagrams.net

The best tool for creating these diagrams is        [diagrams.net](https://diagrams.net/) (previously draw.io). All the examples on this page were created with this tool.

It is definitely the most popular diagram tool at SSW:
![](FaveTool.png)

**Figure:** **Figure: When SSW developers were surveyed, diagrams.net was the clear winner (see green) for building architecture diagrams**
![](TimePRO Architecture Diagram v2.png)

::: good
Figure: Better Example - TimePro (an Angular + .NET project with Hangfire) - you can create diagrams quickly and easily with diagrams.net that still look very professional. This one is in the style of a technical document.

:::

Diagrams.net is free, can be used in the browser, or can be downloaded as a desktop app. But the best way to use diagrams.net is to integrate it directly into VS Code.
![](thumbnail_image003.jpg)

::: good
Figure: Great Example - Auctions (a Blazor + .NET + Cosmos DB project) - diagrams.net integrated directly into VS Code

:::

There are multiple extensions available that let you do this, the best one is [VS Code | Extensions | Draw.io Integration](https://marketplace.visualstudio.com/items?itemName=hediet.vscode-drawio). This makes it easy to create and edit the architecture diagram right alongside the code, and check-in with the relevant commits.
![](architecture-2.png)

::: good
Figure: Good Example - Auctions (a Blazor + .NET + Cosmos DB project) - system architecture diagram created within VS Code and checked into the repo in the same commit as the relevant code changes. Blazor UI layer encapsulated in thematic color


:::

### Tip 8: Polish up Diagrams.net


Maintain standards to keep your diagrams consistent:

* Diagram heading: Nameing Convention "Architecture Diagram - [product name]", in font size 43pts
* Use a standard font: e.g., at SSW we use Helvetica bold
* Arrowhead sizes: 14pts
* Bottom left - add location: e.g., DevOps | Wiki or GitHub | Repo | Docs, in font size 22pts
* Bottom right - add branding and URL, in font size 22pts
* Add color and icons to make your diagrams engaging and easier to distinguish

![](SSW.People-Architecture-Diagram.png)

::: good
Figure: Good Example - SSW People (a Static Site - Gatsby and React with Dynamics 365 and SharePoint Online) - you can just as easily create colorful, engaging diagrams suitable for all of your project stakeholders

:::

### Related links


* [Do you have an Azure resources diagram?](/azure-resources-visualizing)
* [8 Tips to Better Architecture Diagrams](https://adamcogan.com/2020/10/07/8-tips-to-better-architecture-diagrams/)
