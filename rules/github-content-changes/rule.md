---
type: rule
title: Do you know how to make content changes on GitHub?
uri: github-content-changes
authors:
  - title: Adam Cogan
    url: https://www.ssw.com.au/people/adam-cogan
  - title: Piers Sinclair
    url: https://www.ssw.com.au/people/piers-sinclair
created: 2022-05-02T23:52:00.699Z
guid: d48a43d5-83cd-4336-838b-b8e54187e3c1
---
Some websites use GitHub to manage their content (e.g. [SSW Rules](https://github.com/SSWConsulting/SSW.Rules.Content)). GitHub makes reviewing changes easy through "Pull Requests".

A Pull Request is a request to make changes to 1 or more files. GitHub provides out of the box functionality for reviewing changes in a pull request. This process is as follows:
            
<!--endintro-->

1. Open the Pull Request
2. Examine the changes using the tabs:
    * **Conversations:** Comments people have made about the change
    * **Commits:** Summary of the changes the requester has made
    * **Checks:** You can ignore this if you are not a developer
    * **Important - Files changed:** See the difference between the old and new files being changed. Red highlighting indicates deleted parts and green highlighting indicates added parts.  
  This visual preview of the changes to a markdown file is accessed via **Files changed | Display the rich diff**

![Figure: Reviewing tabs in a GitHub Pull Request](https://user-images.githubusercontent.com/79821522/113648288-bb515b80-96cf-11eb-9f9c-3169e2f64a95.png)

![Figure: The view via "Display the rich diff" button](https://user-images.githubusercontent.com/79821522/113648341-d15f1c00-96cf-11eb-8357-81a79ac0765d.png)

3. Approve OR ask for changes
  
    a. Go to **Files changed | Review changes**  
    b. Select an option: 
   - Choose "Approve" to mark it as ready to go live  
   Add a comment with feedback (if necessary) 
   - Choose "Comment" for general feedback when PR it's not ready for approval  
   - Choose "Request changes" for mandatory changes to the PR

    c. Press "Submit review" so that the requester can see it

![Figure: Steps for submitting a Pull Request review](https://user-images.githubusercontent.com/79821522/113798232-26656580-9796-11eb-92dd-00a4385cac8b.png)

4. Done - your review has been submitted ⭐