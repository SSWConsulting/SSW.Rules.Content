---
seoDescription: Check for application updates using async code to simplify the process for users and ensure a seamless experience.
type: rule
title: Do you know to use async code to do the check for update?
uri: use-async-code-to-do-the-check-for-update
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
created: 2014-03-14T02:17:00.000Z
archivedreason: outdated
guid: 6139e272-8fec-4fc4-9e0b-56a7bd3e28fd
---

Application updates don't have to be difficult to do for the user. Pointing the user to a website where he can download an update is not ideal. A better way is to take advantage of the `System.Deployment.Application` namespace. You can develop custom upgrade behaviours into your ClickOnce/Smart client application.

<!--endintro-->

```cs
System.Diagnostics.Process.Start(@"http://www.ssw.com.au/ssw/Download/ProdBasket.aspx?ID=15");
```

::: bad
Figure: Bad example - Using web page to do the check for a new version
:::

```cs
long sizeOfUpdate = 0;

private void UpdateApplication()
{
    if (ApplicationDeployment.IsNetworkDeployed)
    {
        ApplicationDeployment ad = ApplicationDeployment.CurrentDeployment;
        ad.CheckForUpdateCompleted += new CheckForUpdateCompletedEventHandler(ad_CheckForUpdateCompleted);
        ad.CheckForUpdateProgressChanged += new DeploymentProgressChangedEventHandler(ad_CheckForUpdateProgressChanged);

        ad.CheckForUpdateAsync();
    }
}

void  ad_CheckForUpdateProgressChanged(object sender, DeploymentProgressChangedEventArgs e)
{
    downloadStatus.Text = String.Format("Downloading: {0}. {1:D}K of {2:D}K downloaded.", e.State, e.BytesCompleted/1024,
    e.BytesTotal/1024);
}

void ad_CheckForUpdateCompleted(object sender, CheckForUpdateCompletedEventArgs e)
{
    if (e.Error != null)
    {
        MessageBox.Show("ERROR: Could not retrieve new version of the application. Reason: \n" + e.Error.Message +
        "\nPlease report this error to the system administrator.");
        return;
    }
    else if (e.Cancelled == true)
    {
        MessageBox.Show("The update was cancelled.");
    }

    // Ask the user if they would like to update the application now.
    if (e.UpdateAvailable)
    {
        sizeOfUpdate = e.UpdateSizeBytes;

        if (!e.IsUpdateRequired)
        {
            DialogResult dr = MessageBox.Show("An update is available. Would you like to update the application now?
            \n\nEstimated Download Time: ", "Update Available", MessageBoxButtons.OKCancel);
            if (DialogResult.OK == dr)
            {
                BeginUpdate();
            }
        }
        else
        {
            MessageBox.Show("A mandatory update is available for your application. We will install the update now,
            after which we will save all of your in-progress data and restart your application.");
            BeginUpdate();
        }
    }
}

private void BeginUpdate()
{
    ApplicationDeployment ad = ApplicationDeployment.CurrentDeployment;
    ad.UpdateCompleted += new AsyncCompletedEventHandler(ad_UpdateCompleted);

    // Indicate progress in the application's status bar.
    ad.UpdateProgressChanged += new DeploymentProgressChangedEventHandler(ad_UpdateProgressChanged);
    ad.UpdateAsync();
}

void ad_UpdateProgressChanged(object sender, DeploymentProgressChangedEventArgs e)
{
    String progressText = String.Format("{0:D}K out of {1:D}K downloaded - {2:D}% complete",
    e.BytesCompleted / 1024, e.BytesTotal / 1024, e.ProgressPercentage);
    downloadStatus.Text = progressText;
}

void ad_UpdateCompleted(object sender, AsyncCompletedEventArgs e)
{
    if (e.Cancelled)
    {
        MessageBox.Show("The update of the application's latest version was cancelled.");
        return;
    }
    else if (e.Error != null)
    {
        MessageBox.Show("ERROR: Could not install the latest version of the application. Reason: \n" + e.Error.Message +
        "\nPlease report this error to the system administrator.");
        return;
    }

    DialogResult dr = MessageBox.Show("The application has been updated. Restart? (If you do not restart now,
    the new version will not take effect until after you quit and launch the application again.)",
    "Restart Application", MessageBoxButtons.OKCancel);
    if (DialogResult.OK == dr)
    {
        Application.Restart();
    }
}
```

::: good
Figure: Good example - Using System.Deployment.Application classes to do the check for a new version
:::

#### More Information

When testing whether your deployment has an available update by using either the CheckForUpdate or CheckForUpdateAsync methods; the latter method raises the CheckForUpdateCompleted event when it has successfully completed. If an update is available, you can install it by using Update or UpdateAsync; the latter method raises the UpdateCompleted event after installation of the update is finished.
