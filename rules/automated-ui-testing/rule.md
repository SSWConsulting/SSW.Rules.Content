---
type: rule
title: Do you do automated UI testing?
uri: automated-ui-testing
authors:
  - title: Matt Goldman
    url: https://www.ssw.com.au/people/matt-goldman
  - title: Jake Bayliss
    url: https://www.ssw.com.au/people/jake-bayliss
  - title: Piers Sinclair
    url: https://www.ssw.com.au/people/piers-sinclair
related:
  - the-different-types-of-test
  - bdd
redirects:
  - microsoft-recommended-frameworks-for-automated-ui-driven-functional-testing
created: 2021-10-06T05:04:07.186Z
guid: ca225c48-cf34-42c0-b125-3155dfef3398
---
Automated UI testing is a valuable component of a test strategy, to check interacting with the software in a similar way to end users.

<!--endintro-->

### Benefits

As part of an overall test strategy that blends human testing with automation, automating at the UI level can be helpful to check that key user workflows keep working as we expect.

Lower level automated tests (e.g. unit tests) are small in scope and are unlikely to catch problems with more sophisticated usage patterns of the software. Higher level tests via the user interface are much larger in scope and have the potential to mitigate the risk of important user workflows becoming broken in production.

### Tooling

There are numerous tools available for facilitating automated UI testing through the browser. These include tools like [Telerik Test Studio](https://www.telerik.com/teststudio/), [Cypress](https://www.cypress.io/), or [Puppeteer](https://pptr.dev/), to name a few.

[Selenium](https://www.selenium.dev/) was the gold standard in this area for many years, but Microsoft's [Playwright](https://playwright.dev/) is now recommended.

#### Playwright

Playwright allows you to write tests in many popular languages including .NET, Java, Python and Node.js.

Playwright has a few advantages over Selenium:

* [Actionability](https://playwright.dev/docs/actionability/)
* Performance
* Stability
* [Switching browser contexts for parallel testing](https://playwright.dev/docs/browser-contexts#browser-context)
* and more...

```JavaScript
//Store the ID of the original window
const originalWindow = await driver.getWindowHandle();

//Check we don't have other windows open already
assert((await driver.getAllWindowHandles()).length === 1);

//Click the link which opens in a new window
await driver.findElement(By.linkText('new window')).click();

//Wait for the new window or tab
await driver.wait(
    async () => (await driver.getAllWindowHandles()).length === 2,
    10000
  );

//Loop through until we find a new window handle
const windows = await driver.getAllWindowHandles();
windows.forEach(async handle => {
  if (handle !== originalWindow) {
    await driver.switchTo().window(handle);
  }
});

//Wait for the new tab to finish loading content
await driver.wait(until.titleIs('Selenium documentation'), 10000);
```

::: bad  
Figure: Bad example - Selenium only lets you have one window focused at a time meaning you can't do parallel testing easily
:::

```JavaScript
const { chromium } = require('playwright');

// Create a Chromium browser instance
const browser = await chromium.launch();

// Create two isolated browser contexts
const userContext = await browser.newContext();
const adminContext = await browser.newContext();

// Create pages and interact with contexts independently
```

::: good
Figure: Good example - Playwright makes it easy to spin up independent browser contexts for parallel testing
:::

#### Playwright codegen

Playwright offers a [cool feature](https://playwright.dev/docs/cli/#generate-code) that lets developers record actions in the browser to automatically generate the code for tests.

**Note:** While this feature is useful for learning the syntax and structure of Playwright tests, it **should not** be used to generate production-quality test code.

#### Example of using Playwright

Watch [Matt Goldman](https://www.ssw.com.au/people/matt-goldman) and Andreas Lengkeek from SSW demonstrate the use of Playwright to create a simple UI test in this YouTube video:

`youtube: https://www.youtube.com/watch?v=2hibiFfuPao`

### Caution

It's important not to rely too heavily on automated UI tests.

Due to their broad scope, they are slow to run and prone to high maintenance (since they will often need to be updated when the UI is changed). Other levels of automated tests should be considered first (see [What are the different types of test you can have?](/the-different-types-of-test)) and only add automated UI tests for important workflows in the product.

The use of "record & playback"/Low Code/No Code approaches to creating automated UI tests is fraught with danger. These approaches demo very well and can appear to give quick wins, but they generate code that is generally sub-optimal and may be hard to maintain. Building reliable and maintainable automated UI tests requires coding skills and forethought in terms of what really makes sense to automate at this high level.

See [Do you remember to use automated UI testing sparingly?](/automated-ui-testing-sparingly/)
