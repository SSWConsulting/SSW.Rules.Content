---
uri: do-you-use-comment-based-help-in-powershell-functions-and-scripts
title: Do you use Comment-Based Help in PowerShell functions and scripts?
created: 2020-03-24 21:36:14
authors:
  - id: 1
    title: Adam Cogan
  - id: 73
    title: Kaique Biancatti
---




<span class='intro'> In PowerShell, you can use Comment-Based Help snippets to better define what your function or script is doing, its examples, inputs, and outputs.<br><br>When you are building functions in PowerShell, you can use Comment-Based Help snippets at the beginning of the function body, at the end of the function body or before the Function keyword.&#160;<br>If you do this, the Get-Help cmdlet will show the information contained in the code for your function (making it super easy for anyone to use and understand it!).<div><br>You can use it like this (beginning of the Function body)&#58;<br></div> </span>

<p class="ssw15-rteElement-CodeArea">​function Get-Function<br>&#123;<br>&lt;#<br>.&lt;help keyword&gt;<br>&lt;help content&gt;<br>#&gt;<br><br>&#160; # function logic<br>&#125;</p><dd class="ssw15-rteElement-FigureGood">Figure&#58; Good Example - Using Comment-Based Help for Functions​​<br></dd><p>Or like this (before the function keyword)&#58;</p><p class="ssw15-rteElement-CodeArea">&lt;#<br>.&lt;help keyword&gt;<br>&lt;help content&gt;<br>#&gt;<br>function Get-Function &#123; &#125;</p><dd class="ssw15-rteElement-FigureGood">​​​Figure&#58; Good Example - Using Comment-Based Help for Function</dd><p>You can do the same with scripts, with a little difference - you need to place the snippet at the beginning or end of the script file&#58;<br></p><p class="ssw15-rteElement-CodeArea">#Accept input parameters<br>param(<br>[switch]$FullAccess,<br>[switch]$SendAs,<br>[switch]$SendOnBehalf,<br>[switch]$UserMailboxOnly,<br>[switch]$AdminsOnly,<br>[string]$MBNamesFile,<br>[string]$UserName,<br>[string]$Password,<br>[switch]$MFA<br>)</p><dd class="ssw15-rteElement-FigureBad">Figure&#58; Bad Example - Script not using any Comment-Based Help snippet<br></dd><p class="ssw15-rteElement-CodeArea">​&lt;#<br>.SYNOPSIS<br>Gets THE IP addresses in a file and checks if they are on blacklists across the web.<br><br>.DESCRIPTION<br>Gets THE IP addresses in a file and checks if they are on blacklists across the web. If they are, add them to the final blacklist file that will be used by the firewall.<br><br>.EXAMPLE<br>PS C&#58;\&gt; Check-Blacklist -File &quot;FileWithNewIPs&quot; -BaseFile &quot;BaseBlacklistFile&quot; -Logfile &quot;LogfileLocation&quot;<br>​Checks the newly-generated blacklist file to see if any IPs are blacklisted, if yes, adds them to the final blacklist file.<br><br>.NOTES<br>Created by Kiki Biancatti for SSW.<br><br>#&gt;<br>Param(<br>[Parameter(Position = 0, Mandatory = $true)]<br>[string] $File,<br>[Parameter(Position = 1, Mandatory = $true)]<br>[string] $BaseFile,<br>[Parameter(Position = 2, Mandatory = $true)]<br>[string] $LogFile<br>) ...<br></p><dd class="ssw15-rteElement-FigureGood">Figure&#58; Good Example - Using Comment-Based Help at the beginning of a script file​<br></dd><p> 
   <br>You can check some good PowerShell examples in 
   <a href="https&#58;//github.com/SSWConsulting">SSW's GitHub</a>&#58;&#160; </p><ul><li> 
      <a href="https&#58;//github.com/SSWConsulting/SSWSysAdmins.ITPurchaseRequestForm">https&#58;//github.com/SSWConsulting/SSWSysAdmins.ITPurchaseRequestForm</a></li><li> 
      <a href="https&#58;//github.com/SSWConsulting/SSWSysAdmins.BlacklistChecker">https&#58;//github.com/SSWConsulting/SSWSysAdmins.BlacklistChecker</a></li><li> 
      <a>https&#58;//github.com/SSWConsulting/SSWSysAdmins.LeavingStandard​</a>​<br></li></ul>


