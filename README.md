# SSW.Rules

v2 of the Rules.

This is a Gatsby generated site pulling data from:
- [SSW Rules Repo](https://github.com/SSWConsulting/SSW.Rules)


## Getting Started

### Required Tools
- Install nodejs via https://nodejs.org/en/ (required versions: ^8.10.0 or ^10.13.0 or >=11.10.1)

### Getting ready for development
- Clone the repo from https://github.com/SSWConsulting/rules.ssw.com.au
- Run *npm install* to install packages
- Create environment files (.env.development and .env.production) and fill out the values for the following keys:
```
GOOGLE_ANALYTICS=
VERSION_DEPLOYED=
```

### Development
1. Branch off master for your PBI
2. Run *npm run-script build* (.env.production is required for this step)
3. Do your work
4. Run the site in development mode by *npm run-script develop* (.env.development is required for this step)
5. Commit code and push
6. Raise a PR
7. Get it merged!

### Definition of Done

- Code Compiles
- Check the Acceptance Criteria.
- Code is squash-merged to master via a pull request that was approved by a 2nd developer.
- Another team member agrees it’s ready for Production.
- Pushed to Production.
- Use @Mention (**OR** Send email) to notify Product Owner/PBI stakeholder that PBI is done (be sure to include screenshots/done video as proof) 

> <As per rule: [Done - Do you go beyond 'Done' and follow a 'Definition of Done'](https://rules.ssw.com.au/done-do-you-go-beyond-done-and-follow-a-definition-of-done)?>

### Branches
- Branching strategy is based off [Release Flow](https://docs.microsoft.com/en-us/azure/devops/learn/devops-at-microsoft/release-flow) 
- **Master** is the main 'dev' branch
- **Release/xx** is the 'production' one (where xx is the Sprint number)
- Always create a new branch for your PBIs 
- Always delete your branch once your PR has been merged

### Builds
- Changes made to http://github.com/SSWConsulting/SSW.Rules (i.e. profile changes) trigger builds that deploy:
  - **master** to the **staging** site: https://sydiisp01.sydney.ssw.com.au/rules/
  - latest **release/xx** to the **production** site: https://www.ssw.com.au/rules
  
- Branching off **master** to **release/xx**, or making changes to **release/xx** will build and deploy to the **production** site: https://www.ssw.com.au/rules


### Rules repository

> Rules repository lives here: https://github.com/SSWConsulting/SSW.Rules

Merging changes to **master** on this repo will trigger:
- a build/release of the **master** branch in Staging (https://sydiisp01.sydney.ssw.com.au/rules/).
- a build/release of the **release** branch Production (https://www.ssw.com.au/rules)
