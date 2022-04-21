---
type: rule
archivedreason: 
title: Spec - Do you know how to estimate a Project (include the 'General Project Costs')?
guid: c7fa5a0d-0be1-46f7-8100-ebf27cec9b23
uri: spec-do-you-know-how-to-estimate-a-project-that-include-the-general-project-costs
created: 2009-09-16T02:44:19.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: Cameron Shaw
  url: https://ssw.com.au/people/cameron-shaw
- title: Justin King
  url: https://ssw.com.au/people/justin-king
- title: Ulysses Maclaren
  url: https://ssw.com.au/people/ulysses-maclaren
related: []
redirects:
- spec-do-you-know-how-to-estimate-a-project-(that-include-the-general-project-costs)
- spec-do-you-know-how-to-estimate-a-project-include-the-general-project-costs
- spec-do-you-know-how-to-estimate-a-project-(include-the-general-project-costs)

---

Estimates contain 2 main classes of work: 
- Relating to the particular product (e.g. create page 'customers.aspx') 
- Relating to the project as a whole (e.g. management, administration, testing, software audit etc.).

PBIs may only make up about 60% of the total project time. Project Managers and developers should not think that the only work being charged on a project are coding tasks.

<!--endintro-->

### General Project Costs
Management costs can change depending on how much management the client requires. You should recommend a suitable level of management. 'Management, accountability and transparency' has a cost.

You should add general project costs as a % of the work items generally in line with the following (note that these numbers are just best guesses):

* Testing: 20%
* Bug Fixes: 20%
* Software Audit (if relevant): 4 hours per Release - usually conducted by two experienced Architects
* Fixes from the Software Audit: 5%
* DevOps: 10%
* Project Management: 15% - this includes items like stand up meetings, timesheets, standard updates, reviews, etc.
* Unknowns (for risky projects): 10%. While this is arbitrary it raises awareness for everybody that 'there are things we still don't know!'

### Project Specific Costs

Estimates for a project should be done by a developer, checked by another developer, and finally triple checked by an Account Manager. While every project is different in some way, there are common elements.

SSW has built an estimates calculator to assist in creating estimates. See the [Estimates Calculator](https://github.com/SSWConsulting/SSW.Rules.Content/raw/main/rules/spec-do-you-know-how-to-estimate-a-project-that-include-the-general-project-costs/4.%20Estimates%20Calculator.xlsx) here.

If the client requires a fixed price quotation, a 20% premium is added to the estimates for the sprints specified in the Specification Release only (i.e. a fixed price is not given on the entire project). Requests for variations to a fixed price contract must wait until the contract is completed. If development is based on a fixed price contract, work is completed offsite only to facilitate project management and prevent unauthorized scope development.

::: greybox
**Note:** A suggestion for Microsof - It would be great if Azure DevOps had functionality to “Add Standard Items" to a Sprint.
:::
