---
type: rule
archivedreason: 
title: Do you have tests for Performance?
guid: a0b93a9e-1367-4a8c-985a-e46df21db9d1
uri: have-tests-for-performance
created: 2020-03-12T19:58:01.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
- do-you-have-tests-for-performance

---

Typically there are User Acceptance Tests that need to be written to measure the performance of your application. As a general rule of thumb, Forms should not load in more than 4 seconds. This can be automated with your unit testing framework.

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
            string.Format("Loading time ({0:#,##0.0} seconds) exceed the expected time ({1:#,##0.0} seconds).",
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

While Visual Studio Enterprise came with load and performance testing components this has now been deprecated as of VS 2019. For more information, see the [Cloud-based load testing service end of life] https://devblogs.microsoft.com/devops/cloud-based-load-testing-service-eol/

Some popular open source load testing tools are: 

* [Apache JMeter](https://jmeter.apache.org/) - 100% Java application with built in reporting - 5.6k Stars on GitHub
* [k6](https://k6.io/open-source/) - Write load tests in javascript - 14k Stars on GitHub
* [NBomber](https://github.com/PragmaticFlow/NBomber) - Write tests in C# - 1k Stars on GitHub

