---
type: rule
title: Do you do automated UI testing?
uri: automated-ui-testing
authors:
  - title: Matt Goldman
    url: https://www.ssw.com.au/people/matt-goldman
  - title: Piers Sinclair
    url: https://www.ssw.com.au/people/piers-sinclair
created: 2021-10-06T05:04:07.186Z
guid: ca225c48-cf34-42c0-b125-3155dfef3398
---

Automated UI testing (aka end-to-end testing) is an awesome way to automate the process of browser based testing.

<!--endintro-->

In the old days, [Selenium](https://www.selenium.dev/) was the gold standard, but these days it has been overtaken by [Playwright](https://playwright.dev/) which lets you write tests in many popular languages including .NET, Java, Python and Node.js



```
import org.apache.commons.io.FileUtils;
import org.openqa.selenium.chrome.ChromeDriver;
import java.io.*;
import org.openqa.selenium.*;

public class SeleniumTakeScreenshot {
    public static void main(String args[]) throws IOException {
        WebDriver driver = new ChromeDriver();
        driver.get("http://www.example.com");
        File scrFile = ((TakesScreenshot)driver).getScreenshotAs(OutputType.FILE);
        FileUtils.copyFile(scrFile, new File("./image.png"));
        driver.quit();
    }
}
```
::: bad  
Figure: Bad Example - Taking a screenshot in Selenium is fairly complex
:::


```
await page.screenshot({ path: 'screenshot.png' });
```
::: good
Figure: Good Example - Taking a screenshot in Playwright is just one line!
:::