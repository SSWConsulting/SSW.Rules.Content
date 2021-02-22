---
type: rule
archivedreason: 
title: Do you use lodash to perform your daily _.foreach?
guid: 02d5d6d1-3af7-40f8-8480-d532ce9b8040
uri: do-you-use-lodash-to-perform-your-daily-_-foreach
created: 2015-05-05T18:45:14.0000000Z
authors:
- title: Ben Cull
  url: https://ssw.com.au/people/ben-cull
- title: Duncan Hunter
  url: https://ssw.com.au/people/duncan-hunter
related: []
redirects: []

---

In a nutshell, Lo-Dash is a super useful library that gives you access to over 100 extremely performant functions to help you avoid reinventing the wheel whilst writing JavaScript.

You can get lodash from [GitHub repository](https&#58;//github.com/lodash/lodash), [cdnjs](https&#58;//cdnjs.com/libraries/lodash.js) or via [NPM](https&#58;//www.npmjs.com/package/lodash). Once done you can include a reference in your HTML.

<!--endintro-->

A simple example of the power of lodash is this snippet of code which is looping through a shared Kendo datasource that is being used in large Kendo grid. The shared datasource has many duplicates and this snippet does four things:

1. Removes duplicate account numbers
2. Plucks out only the account numbers into a new array
3. Sorts the array by alphabetical order
4. Removes blank entries


This new simplified array of account numbers was then used in a dropdown to filter the Kendo grid. This single line saves a call to the database for another array of data and populates the dropdown with the same shared datasource. This would be a pain to write with vanilla javascript and difficult to read.



```
this.accountNumberDropDownData = _.chain(this.sharedDataSource).pluck('AccountNumber').uniq().sortBy().value();
```




::: good
Good example - Simple one line of TypeScript which would take many line of code without lodash  
:::

If you have been into JavaScript development for a while you may of also heard about underscore.js which is very similar to Lo-Dash but has some fundamental differences.

I created Lo-Dash to provide more consistent cross-environment iteration support for arrays, strings, objects, and arguments objects1. It has since become a superset of Underscore, providing more consistent API behavior, more features (like AMD support, deep clone, and deep merge), more thorough documentation and unit tests (tests which run in Node, Ringo, Rhino, Narwhal, PhantomJS, and browsers), better overall performance and optimizations for large arrays/object iteration, and more flexibility with custom builds and template pre-compilation utilities.

**— John-David Dalton**

Further reading:

1. [https://lodash.com](https&#58;//lodash.com/)
2. [http://underscorejs.org](http&#58;//underscorejs.org/)
