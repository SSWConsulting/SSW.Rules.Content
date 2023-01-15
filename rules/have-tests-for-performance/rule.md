---
type: rule
title: Do you have tests for Performance?
uri: have-tests-for-performance
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
  - title: Prem Radhakrishnan
    url: https://www.ssw.com.au/people/prem-radhakrishnan
related: []
redirects:
  - do-you-have-tests-for-performance
created: 2020-03-12T19:58:01.000Z
archivedreason: null
guid: a0b93a9e-1367-4a8c-985a-e46df21db9d1
---

Typically, there are User Acceptance Tests that need to be written to measure the performance of your application. As a general rule of thumb, forms should load in less than 4 seconds. This can be automated with your unit testing framework.

<!--endintro-->

**Sample Code:**



```cs
public abstract class FormTestBase<F>
    where F : Form, new()
{
    protected TimeSpan _ExpectedLoadTime = TimeSpan.FromSeconds(4);

    [Test]
    public void LoadTest()
    {
        Stopwatch stopwatch = new Stopwatch();

        stopwatch.Start();
        F testForm = new F();
        testForm.Show();
        testForm.Close();
        stopwatch.Stop();

        Console.WriteLine("Form [{0}] took {1:#,##0.0} seconds to open", typeof(F), stopwatch.Elapsed.TotalSeconds);
        Assert.IsTrue(stopwatch.Elapsed < _ExpectedLoadTime,
            string.Format("Loading time ({0:#,##0.0} seconds) exceeded the expected time ({1:#,##0.0} seconds).",
                stopwatch.Elapsed.TotalSeconds, _ExpectedLoadTime.TotalSeconds));
    }
}

[TestFixture]
public class LoginFormTests : FormTestBase<LoginForm>
{
}

[TestFixture]
public class MainFormTests : FormTestBase<MainForm>
{
}
```

 **Figure: This code tests that the LoginForm and MainForm load in under 4 seconds**

While Visual Studio Enterprise used to come with load and performance testing components, these were deprecated as of VS 2019. For more information, see [Cloud-based load testing service end of life](https://devblogs.microsoft.com/devops/cloud-based-load-testing-service-eol/).

Some popular open source load testing tools are: 

* [Apache JMeter](https://jmeter.apache.org/) - 100% Java application with built in reporting - 5.6k Stars on GitHub
* [k6](https://k6.io/open-source/) - Write load tests in javascript - 14k Stars on GitHub
* [NBomber](https://github.com/PragmaticFlow/NBomber) - Write tests in C# - 1k Stars on GitHub

