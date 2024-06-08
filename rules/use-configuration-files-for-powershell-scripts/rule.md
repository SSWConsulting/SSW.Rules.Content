---
type: rule
archivedreason: 
title: Do you use configuration files for PowerShell scripts?
guid: 91fcf87e-5709-47fb-9ff1-997bd716cdda
uri: use-configuration-files-for-powershell-scripts
created: 2020-10-22T18:25:28.0000000Z
authors:
- title: Kaique Biancatti
  url: https://ssw.com.au/people/kaique-biancatti
- title: Steven Andrews
  url: https://ssw.com.au/people/steven-andrews
related: []
redirects:
- do-you-use-configuration-files-for-powershell-scripts

---

In PowerShell, you can easily create variables without explicitly typing them and that leads to some hardcoded "magic" strings.

Instead of using XML, JSON, YAML, or TXT files, PowerShell "accidentally" created a very nice configuration file format, PSD1.

PSD1 us the filename extension for PowerShell module descriptions, and this file contains metadata for that module. You can, however, load any kind of data from a PSD1 file using a simple cmdlet.

<!--endintro-->

``` ps1
Import-PowerShellDataFile.
```

Some of the things we can do in a PSD1 file:

1. We can write comments;
2. We can use lots of data types, like int, float, bool, string, array...
3. We don't need to use quotes around field names like JSON;
4. And more.

Instead of keeping all your important URLs and FQDNs inside your PowerShell script, you should keep the script itself clean and "sanitized" from those hard-coded variables, so it can be freely shared on GitHub without any security concerns for you or your company. It also makes the script much more maintainable, where you can easily change the variables in the .PSD1 file without needing to change your core script.
Don't forget to add the configuration file to .gitignore!

::: bad  
![Figure: Bad Example - Your script variables are in the script itself, making it insecure to share outside](bad-script-variables.png)  
:::

Credits to: [PowerShell Accidentally Created A Nice Configuration Format](https://medium.com/%40ssg/powershell-accidentally-created-a-nice-configuration-format-3efde5448090).
