---
seoDescription: Prevent simultaneous instances of your application to ensure smooth and expected behavior.
type: rule
title: Do you prevent users from running two instances of your application?
uri: prevent-users-from-running-two-instances-of-your-application
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan/
created: 2014-03-14T00:22:00.000Z
guid: 9fcfbe56-37b2-4f74-9247-12151fd21c8f
---

In some cases, running two instances of an application at the same time may cause unexpected result. See this issue is solved via the code below on [SSW Exchange Reporter](/ssw/ExchangeReporter/):

<!--endintro-->

```cs
try
{
	Process current = Process.GetCurrentProcess();
	Process[] processes = Process.GetProcessesByName( current.ProcessName);

	if ( processes.Length>1 )
	{
		DialogResult userOption = MessageBox.Show(Application.ProductName + " is already running on this machine. " + Environment.NewLine+Environment.NewLine + 		"Please click: "+Environment.NewLine+
		    " - 'Try again' to exit the other instance and try again, or "+Environment.NewLine+
		    " - 'Cancel' to exit now."+Environment.NewLine,
		    Application.ProductName+" "+(new Version(Application.ProductVersion)).ToString(2),

		MessageBoxButtons.RetryCancel, MessageBoxIcon.Warning);
		switch(userOption)
		{
			case DialogResult.Cancel: return;

			case DialogResult.Retry:
			foreach(Process currProcess in processes)
			{
				if ( currProcess.Id != current.Id)
				{
					currProcess.Kill();
				}
			}
			break;
		}
	}
}
catch (Exception ex)
{
	TracingHelper.Trace(null, Loggers.WindowsUILogger, TracingLevels.DEBUG, "Cannot get process information, Excpetion occured.", ex) ;

	DialogResult result = MessageBox.Show("Exchange Reporter cannot detect process information. This may be caused by disabled 'Performance Counter' on your machine. "+Environment.NewLine+
	"In such case, Exchange Reporter cannot ensure there is only one instance running. "+
	Environment.NewLine+
	"You may continue to run Exchange Reporter, however, please make sure you have only one instance of Exchange Reporter running. "+
	Environment.NewLine+
	"Multiple instances will cause unexpected behaviour. "+
	Environment.NewLine+Environment.NewLine+
	"Please click 'OK' to continue, or click 'Cancel' to quit."
	, Application.ProductName+" "+(new Version(Application.ProductVersion)).ToString(2),
	MessageBoxButtons.OKCancel,
	MessageBoxIcon.Warning);

	if ( result == DialogResult.Cancel)
	{
		return;
	}
}
```

**Code: Avoid running two instances of an application**
