---
seoDescription: Before configuring continuous deployment, ensure your solution compiles by creating a continuous integration build that verifies code quality.
type: rule
archivedreason:
title: Do you create a Continuous Integration Build for the Solution?
guid: e4c12ecd-319c-4b6a-94ac-13fde8bdb0df
uri: do-you-create-a-continuous-integration-build-for-the-solution-before-configuring-continuous-deployment
created: 2013-02-06T18:49:06.0000000Z
authors:
  - title: Adam Stephensen
    url: https://ssw.com.au/people/adam-stephensen
related: []
redirects:
  - do-you-create-a-continuous-integration-build-for-the-solution
---

(Before you configure continuous deployment) You need to ensure that the code that you have on the server compiles. A successful CI build without deployment lets you know the solution will compile.

<!--endintro-->

![Figure: The Build definition name should include the project name. The reason for this is that builds for all solutions are placed in the same folder, and including the build name makes the Build Drop folder organised](ci-build-1.jpg)

![Figure: On the Trigger tab choose Continuous Integration. This ensures that each check-in results in a build](ci-build-2.jpg)

![Figure: On the Workspace tab you need to include all source control folders that are required for the build](ci-build-3.jpg)

![Figure: Enter the path to your Drop Folder (where you drop your builds)](ci-build-4.jpg)

![Figure: Choose the Default Build template and enter the DeployOnBuild argument to the MSBuild Arguments parameter of the build template](ci-build-5.jpg)

![Figure: Queue a build, to ensure our CI build is working correctly](ci-build-6.jpg)

![Figure: Before we setup continuous deployment it is important to get a successful basic CI build](ci-build-7.jpg)
