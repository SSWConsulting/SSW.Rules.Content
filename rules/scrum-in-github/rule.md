---
type: rule
title: GitHub Projects - Do you know how to do Scrum?
uri: scrum-in-github
authors:
  - title: Piers Sinclair
    url: https://www.ssw.com.au/people/piers-sinclair
related:
  - github-sprint-templates
created: 2021-10-28T01:49:43.558Z
guid: 1e308570-5ab0-43d7-8a83-6bdfd04d212e
---
GitHub is an awesome place to manage your code, but initially it wasn't the easiest place to manage Scrum.  Things improved in 2021 with GitHub Projects. 

[GitHub Projects](https://docs.github.com/en/issues/trying-out-the-new-projects-experience/about-projects) lets you create Sprints and manage Issues (aka PBIs or Tasks) with far more powerful. 

Let's take a look at some of the great new things you can do...

<!--endintro-->

* Track Sprints
* Track Complexity
* Add custom fields to Issues
* Collate Issues from multiple repos
* Set up automated workflows for your Issues in a project

That's a tonne of awesome features....but it requires a bit of set up, follow these steps to get up and running:

1. Navigate to **Projects | Projects (Beta) | New project**

![Figure: Create a new GitHub Project](newbetaproject.png)

1. Now we have a blank slate, we need to setup our Sprint (they call them Iterations). Navigate to **+ | + New field**

![Figure: Create a new field for your Sprint](newfield.png)

3. Select the **Iteration** field type

![Figure: Turn this into an Sprint via the Iteration field type](selectiteration.png)

4. You will see a window with options for your new Iteration, name it **Sprint** and enter **Start on** and **Duration**.

![Figure: Pick the name and the dates via the Iteration field options](iterationoptions.png)

5. Now add some Issues to the project and then you can assign them to the correct Sprint, by clicking the drop down in the **Sprint** field.

**Note:** You can even add Issues from different Repos

![Figure: Pick the Sprint you want for your Issues](assignpbitodropdown.png)

6. To add more Sprints, navigate to **Settings | Sprint | Add iteration**

**Note:** You can also change **Starts on** and **Duration** here

![Figure: To add a Sprint, Settings | Sprint | Add Iteration](settingsnav.png)

![Figure: To add new Sprints, select Settings | Add iteration](additerations.png)

7. To give yourself a better view of things, you might want to create a view that groups by Sprint. Name your current view **Backlog** then create a new view and name it **Sprints**
8. To see the Sprints grouped, and the issues ordered by status, click the view drop down and select **group:Sprint** and **sort:Status-asc** 

![Figure: To create a list of Sprints add grouping and sorting](groupandsort.png)

9. Voila! You have Scrum all setup! For bonus points check out the workflow screen where you can automate parts of your issue workflow

![Figure: You can enable or disable predefined Workflows](workflownav.png)

![Figure: There are a bunch of predefined workflows (Coming soon: the ability to create your own! )](workflows.png)