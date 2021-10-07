---
type: rule
title: Do you do automated UI testing?
uri: automated-ui-testing
authors:
  - title: Matt Goldman
    url: https://www.ssw.com.au/people/matt-goldman
  - title: Piers Sinclair
    url: https://www.ssw.com.au/people/piers-sinclair
related:
  - bdd
created: 2021-10-06T05:04:07.186Z
guid: ca225c48-cf34-42c0-b125-3155dfef3398
---

Automated UI testing (aka end-to-end testing) is an awesome way to automate the process of browser based testing.

<!--endintro-->

`youtube: https://www.youtube.com/watch?v=2hibiFfuPao `

In the old days, [Selenium](https://www.selenium.dev/) was the gold standard, but these days it has been overtaken by [Playwright](https://playwright.dev/) which lets you write tests in many popular languages including .NET, Java, Python and Node.js

Playwright has a few advantages over Selenium:
* [Actionability](https://playwright.dev/docs/actionability/)
* Performance
* Stability
* [Switching browser contexts for parallel testing](https://playwright.dev/docs/multi-pages/)


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
Figure: Bad Example - Selenium only lets you have one window focused at a time meaning you can't do parallel testing
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
Figure: Good Example - Playwright makes it easy to spin up independent browser contexts for parallel testing
:::