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


<p class="ssw15-rteElement-P">In PowerShell, you can easily create variables without explicitly typing them and that leads to some hardcoded &quot;magic&quot; strings.​​<br></p><p class="ssw15-rteElement-P">Instead of using XML, JSON, YAML, or TXT files, PowerShell &quot;accidentally&quot; created a very nice configuration file format, PSD1.<br>PSD1 us the filename extension for PowerShell module descriptions, and this file contains metadata for that module. You can, however, load any kind of data from a PSD1 file using a simple cmdlet&#160;​​​<br></p>
<br><excerpt class='endintro'></excerpt><br>
<p class="ssw15-rteElement-CodeArea">Import-PowerShellDataFile.<br></p><p>You can check a sample PSD1 file here&#58; 
   <a href="https&#58;//gist.github.com/ssg/a8e31af18ae8e03dcdc0f23e02793eca%22%20%5cl%20%22file-sample-psd1">https&#58;//gist.github.com/ssg/a8e31af18ae8e03dcdc0f23e02793eca#file-sample-psd1</a><br></p><p class="ssw15-rteElement-P">Some of the things we can do in a PSD1 file&#58;</p><ol><li>We can write comments;</li><li>We can use lots of data types, like int, float, bool, string, array...</li><li>We don't need to use quotes around field names like JSON;</li><li>And more.</li></ol><p>Instead of keeping all your important URLs and FQDNs inside your PowerShell script, you should keep the script itself clean and &quot;sanitized&quot; from those hard-coded variables, so it can be freely shared on GitHub without any security concerns for you or your company. It also makes the script much more maintainable, where you can easily change the variables in the .PSD1 file without needing to change your core script.<br>Don't forget to add the configuration file to .gitignore!</p><dl class="badImage"><dt>
      <img src="/PublishingImages/bad-script-variables.png" alt="bad-script-variables.png" style="width&#58;750px;" />
   </dt><dd>Figure&#58; Bad Example - Your script variables are in the script itself, making it insecure to share outside</dd></dl><p>Credits to&#58; 
   <a href="https&#58;//medium.com/%40ssg/powershell-accidentally-created-a-nice-configuration-format-3efde5448090">PowerShell Accidentally Created A Nice Configuration Format</a>.​​<br></p>


