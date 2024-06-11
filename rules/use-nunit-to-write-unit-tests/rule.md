---
seoDescription: Write unit tests using NUnit to ensure code stability and prevent introducing new bugs when fixing issues in someone else's code.
type: rule
title: Do you use NUnit to write Unit Tests?
uri: use-nunit-to-write-unit-tests
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan/
created: 2014-03-14T00:22:00.000Z
guid: 63a5f8ba-42ad-4d32-aa65-7b9c1fdab799
related: []
redirects: []
archivedreason: See a more generic and up to date rule [https://www.ssw.com.au/rules/rules-to-better-unit-tests/](/rules/rules-to-better-unit-tests)
---

When anyone sends you a bug that happen in their environment do a unit test. Just because the code runs on your machine it doesnt mean it will work on the users machine. E.g permissions issues - you are an admin while the user is only a simple user, registry & io reads might fail, NUnit will test for this and let you know.

<!--endintro-->

Unit testing is a valuable tool when maintaining code, particularly in a team environment where you may have to fix a bug in someone else's code. Unit Tests ensure that you do not introduce new bugs in someone else's code, or code that you have not looked at for a while. We like [NUnit](https://nunit.org/) because it is free, we have found that it is easy for developers to learn and it integrates well with Visual Studio. Visual Studio .NET 2005 integrates Unit Testing with Visual Studio Team System.

You should always try to write unit tests for:

1. Code that is a core component to your application
2. Any regular expressions (as these change it is easy to change functionality and cause errors)
3. Any external factors that your program relies on like hyperlinks to websites

One important test that should be implemented (if your setup package or build script doesn't pick it up) is to validate that your application installs all required DLLs. .NET loads DLLs just in time (JIT) - which means that a missing DLL is will not generate an error unless it is required.

Example: You may have a shared project that your application uses. Another developer adds a reference to that project - unbeknownst to you. You build the application with no errors, and the application passes basic user testing. Problem is that the user did not run the tutorial component - which is missing from the setup package. Users who run the tutorial report runtime errors. You can resolve this issue by creating a unit test to check that all DLLs are included in the setup.

![Figure: Unit Tests accessible from the help menu](unittestsinhelpmenu.jpg)

Unit tests should also be accessible from the Help menu to assist in troubleshooting when your users call up tech support. For more information see [Rules to Better Interfaces](RulestoBetterInterfaces-Windows-Applications.aspx#HelpMenu).

Note: Unit testing also works with Web projects.

For more information on unit testing see [Rules to Better Unit Tests](https://ssw.com.au/ssw/Standards/Rules/RulesToBetterUnitTests.aspx#NotVSTS)

Also see [Suggestions to TFS](https://ssw.com.au/ssw/Standards/BetterSoftwareSuggestions/TeamFoundationServer.aspx)

We have a program called [SSW .NET Toolkit](https://ssw.com.au/ssw/NETToolkit/) that implements these Unit Tests
