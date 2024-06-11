---
seoDescription: Resetting user settings to default values ensures a consistent application experience, even when debug configurations don't match production environments.
type: rule
title: Do you have a ResetDefault() function to handle messed up user settings?
uri: have-a-resetdefault-function-to-handle-messed-up-user-settings
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan/
created: 2014-03-14T00:22:00.000Z
guid: 6696b1b2-dcd7-475a-990e-b5d610f0a122
---

In development life cycle, developers always have different settings to the user's settings. Because of this, debug settings won't always work on the remote machine.

In order to have settings.config, we also have a defaults.config. This is good because this gives a chance for the user to roll back bad settings without reinstalling the application. The application can also roll back the settings it automatically. Below is the code that what we do.

<!--endintro-->

VB.NET

```vb
Public Sub RuneXtremeEmail(ByVal state As Object)

    If Environment.MachineName <> Configuration.MachineName Then

        resetSettings()

    Else
End
```

We have a program called [SSW Code Auditor](https://ssw.com.au/ssw/CodeAuditor/) to check for this rule.

We have a program called [SSW .NET Toolkit](https://ssw.com.au/ssw/NETToolkit/) that implements this rule.

_Note: in Access we do like this_

```vb
Private Sub Form_Load()

    If Nz(DLookup("CurrentComputerName", "ControlLocal", "ID=1"), "") <> CurrentComputerName
    Then
        Me.ctlCurrentComputerName.Value = CurrentComputerName
    Else ...
```
