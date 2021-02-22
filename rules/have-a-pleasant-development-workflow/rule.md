---
type: rule
archivedreason: 
title: Tips - Do you have a pleasant development workflow?
guid: 8a51eaf0-0c2e-4fc5-8772-52c0082e772a
uri: have-a-pleasant-development-workflow
created: 2016-04-22T22:24:13.0000000Z
authors:
- title: Steve Leigh
  url: https://ssw.com.au/people/steve-leigh
- title: Gabriel George
  url: https://ssw.com.au/people/gabriel-george
related: []
redirects:
- tips-do-you-have-a-pleasant-development-workflow

---

**UPDATE:** This has been properly fixed since Angular 4. So now, this rule is irrelevant because Angular CLI provides a pleasant development workflow. Using ng serve, TypeScript transpilation occurs automatically and quickly (almost instantly).

When dealing with client-side development – especially when transpiling TypeScript – it is common to have to wait for several seconds between writing code, and seeing the results.

This adds up quickly – if you have to wait for 5 seconds every 3 minutes, you've spent 13 minutes of your day just *waiting*. This is a conservative estimate - we change code much more frequently than every 3 minutes!

<!--endintro-->

A naïve development experience is as follows:


::: greybox

1. Make a code change using a misconfigured IDE
    * See errors everywhere as you type (even though the code is perfectly fine)
    * Inaccurate IntelliSense information
2. Compile the code
    * Since the TypeScript compilation task is often part of the project build, this is a common way to recompile to JavaScript
3. Run a gulp task to copy files around appropriately
    * This often takes a few seconds to run, especially if it “cleans” the folder beforehand
4. Refresh the page
    * Depending on the setup, this may take anywhere from milliseconds to seconds
5. Click around until the app is in the right state to test the functionality
    * If there is too much built-up state, and no routes set up, this chews up time


:::
 Bad example - Many hours each week are wasted just waiting for the code you wrote to run

A more ideal workflow is:


::: greybox

1. Make the change using a properly configured IDE
    * One that only shows errors when they’re appropriate
    * Intellisense shows everything available, and nothing more
2. Refresh the page (maybe)
    * With well set up watches for compilation and appropriate use of BrowserLink or LiveReload, this is very fast
    * With proper bundling, the initial page load is also fast in development environments.
3. Already be at the component required, ready to check it works


:::
 Good example - No time is wasted doing repetitive and slow tasks 
**Remember** : Spending 4 hours setting up a good dev experience will pay for itself within the week, and make your work like much happier.

### Guidelines to follow


* Ensure that only the files that are changed need to be compiled – TypeScript handles this quite well with --watch
* Avoid the use of task runners (eg. gulp) as part of your development flow. A few watches should be all you need. Save the task runners for release builds
* Consider separate index pages for production and development, using the dev libraries for development, and minified/bundled ones for production
* Use module loaders (eg. SystemJS) to manage dependencies and their associated bundlers/builders for releases
* Load 3rd party modules (eg. Angular2 and Rx) as a bundle, not as their individual files – speed up development first-page load
* Think about your routing – a refresh should almost always return the page to the exact same state or at the very least, the same screen
* Most importantly,  **be unsatisfied** - if things are slow, fix it. If you constantly have to manually close IISExpress to run your app, *find out why* and fix it! You will save everyone time in the long run
