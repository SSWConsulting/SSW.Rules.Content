---
type: rule
archivedreason: 
title: Do you clean useless calendars in SharePoint?
guid: 1e12b128-b34c-4435-af21-81bdef31f061
uri: do-you-clean-useless-calendars-in-sharepoint
created: 2013-09-05T23:49:53.0000000Z
authors:
- title: William Yin
  url: https://ssw.com.au/people/william-yin
- title: Brendan Richards
  url: https://ssw.com.au/people/brendan-richards
related: []
redirects: []

---

Most SharePoint site templates contain a calendar list, this will bring lots of useless calendars.


<!--endintro-->

Use the below PowerShell script to clean them:



```
$site = Get-SPSite("http://<site collection URL>/"); # Specify url here
foreach ($web in $site.AllWebs) {    
    $lists = $web.Lists
    for ($i=($lists.Count-1);$i -gt 0; $i--) {  
        $list = $lists[$i]
        #Write-host $i  $list.Title $list.BaseTemplate.ToString()
        if ($list.BaseTemplate.ToString().ToLower().contains('events')) {      
            if ($list.Items.Count -eq 0)
            {
                Write-Host $list.Items.Count "items in the list" $list.Title '('$list.BaseTemplate') at '$web.Url "- cleaning it!"
                $list.Recycle()
                #$list.Delete()
            }
        }
    }
}
```



This script will put the calendars which do not have any events into  **Site Settings** |  **Recycle Bin** :
![](EmptyCalendarsInRecyckeBin.png) **Figure: Empty Calendars in Recycle Bin folder**
