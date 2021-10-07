---
type: rule
title: Do you follow BDD?
uri: bdd
authors:
  - title: Matt Goldman
    url: https://www.ssw.com.au/people/matt-goldman
  - title: Piers Sinclair
    url: https://www.ssw.com.au/people/piers-sinclair
  - title: Jake Bayliss
    url: https://www.ssw.com.au/people/jake-bayliss
related:
  - automated-ui-testing
created: 2021-10-06T04:39:11.925Z
guid: c336ab74-ca08-4d86-864a-7b6a9b27359b
---
In the old days, reading and understanding test cases was something only developers could do. Behavioral-Driven Design (BDD) starts to solve this problem by enabling organizations to define their use cases in plain language and integrate these aspects with testing frameworks.

<!--endintro-->

Using gherkin syntax you can write test scenarios in plain text using a few key words (Given, When, Then). Plain text makes the test scenarios easy to understand and visualise from a user perspective, even for non-technical team members.

First think about the different scenarios that you want to test, then write them out in plain text using gherkin syntax.

```
Feature: Greeting Message
	Participant sees a greeting message

Scenario: Participant sees a greeting message
	Given I visit the website
	When I navigate to the greeting screen
	Then I see the greeting message
```
**Figure: Good example - Gherkin syntax scenarios (Given, When, Then)**

Once you have your scenarios lined up, you should begin to write the test steps for each scenario.

```cs
[Given(@"I visit the website")]
public async Task VisitTheWebsite()
{
    await HomePage.NavigateAsync();
}

[When(@"I navigate to the greeting screen")]
public async Task NavigateToWelcome()
{
    await HomePage.NavigateToGreeting();
}


[Then(@"I see the greeting message")]
public async Task ThenISeeTheGreetingMessage()
{
    var message = await HomePage.GetGreetingMessage();
    Assert.IsTrue(message == GreetingMessage);
}
```
**Figure: Good example - Test steps to run, matching the Gherkin Syntax**
