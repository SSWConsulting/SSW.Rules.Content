---
type: rule
title: Do You Know to not 'Push' your Pull Requests? (a.k.a. discuss then build)
uri: do-you-know-to-not-push-your-pull-requests-aka-discuss-then-build
created: 2016-03-29T18:35:55.0000000Z
authors:
- id: 24
  title: Adam Stephensen

---



<span class='intro'> <p>For the original article check out&#160;<a href="https&#58;//www.igvita.com/2011/12/19/dont-push-your-pull-requests/" target="_blank">​​​​​Don't &quot;Push&quot; Your Pull Requests ​</a>b​y Ilya Grigorik.​</p><p>Open source software projects love it when the community get involved and pitch in.</p><p>It's great when someone fixes a bug.​</p><p>A short pull request to fix a small problem is easy to review and accept.</p> </span>

<p>It's great when someone adds a much-needed feature<br>...as long as the feature fits in with the project the core contributors have for the project<br>...and it meets the existing coding patterns and engineering standards.</p><p>This is where frustration often starts to set in on open source projects.</p><p>A contributor has a great idea for a feature, or identifies an area where they can add value and does so without consulting with the core contributors who have often spent hundreds of hours working on the project.</p><p>Their contribution might solve their problem, but after it has been accepted it will most likely be left for the core contributors to maintain.</p><div class="greyBox"><p>
      <b># Poor Communication Contribution</b></p><ul><li>developer has good idea for project</li><li>bashes away and writes 600 lines of code</li><li>submits pull request</li><li>core contributor looks at large pull request<br>she doesn't fully understand purpose of request / the problem it solves<br>she doesn't like that the PR author hasn't followed the existing coding standards<br>she makes a push back comment</li></ul></div><dd class="ssw15-rteElement-FigureBad">Figure&#58; Bad Example - Poor early communication can lead to mis-directed work and pull requests not being accepted</dd><div class="greyBox"><p>
      <b># Good Communication Contribution</b></p><ul><li>developer (PR Author) has good idea for project</li><li>reviews the list of outstanding issues for the project and confirms that someone hasn't already had the same idea and started a discussion on it</li><li>author creates an issue on GitHub and outlines the problem they are trying to solve, and outlines their suggested solution</li><li>the core contributors and other interested parties can help refine both the idea for the feature and the suggested implementation</li><li>the author can then start working on the feature knowing that their idea for the project complies with the maintainers vision for the project and know it is likely to be merged into the core codebase</li></ul></div><dd class="ssw15-rteElement-FigureGood">Figure; Good &#160;Example - Good communication leads to collaboration and better outcomes for the author and the project</dd> <div class="greyBox">
   <p>
      <b># Projects with Internal Teams</b></p><ul><li>Internal SSW team members should only work on features during work hours that have been assigned to a release by the core contributors for a project</li><li>Features will be assigned to a release during the Community Standup</li></ul></div>


