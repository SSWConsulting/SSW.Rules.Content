---
seoDescription: Use threading to improve user interface responsiveness during long-running processes.
type: rule
title: Do you use Threading to make your user interfaces more responsive?
uri: use-threading-to-make-your-user-interfaces-more-responsive
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan/
created: 2014-03-14T00:22:00.000Z
guid: e32158bf-07a5-4039-bf77-13ff9983545b
---

Threading is not only used to allow a server to process multiple client requests - it could make your user interfaces responsive when your application is performing a long-running process, allowing the user to keep interactive.

<!--endintro-->

:: bad
![Figure: Bad example - Unresponsive UI because no threading code](nothreading.gif)
:::

```cs
private void Form1_Load(object sender, EventArgs e)
{
    this.ValidateSQLAndCheckVersion();// a long task
}
```

**Code: No threading code for long task**

::: good
![Figure: Good example - Responsive UI in progress](threadingstart.gif)
:::

::: good
![Figure: Good example - Responsive UI completed](threadingend.gif)
:::

```cs
private void Page05StorageMechanism_Load(object sender, EventArgs e)
{
    this.rsSetupOk = false;

    this.databaseSetupOk = false;

    this.NextButtonState.Enabled = false;

    CheckDatabase();

    CheckReports();

}

public void CheckDatabase()
{
    if(sqlConnectionString == null)
    {
       OnValidationFinished(false, false);
    }

    if(upgradeScriptPath ==null && createScriptPath == null)
    {
        OnValidationFinished(false, false);
    }

    Thread thread = new Thread(new ThreadStart(this.ValidateSQLAndCheckVersion) ) ;

    thread.Name = "DBCheckingThread";

    thread.Start();
}
```

**Code: Threading code for long task**
