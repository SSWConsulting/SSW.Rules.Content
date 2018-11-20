---
type: rule
title: Do you know the pros and cons of joining the domain?
uri: do-you-know-the-pros-and-cons-of-joining-the-domain
created: 2018-11-20T00:56:28.0000000Z
authors:
- id: 73
  title: Kaique Biancatti

---



<span class='intro'> <p>Do you know if your computer should be joined to the domain or not?<br></p> </span>

<p>Joining your company's domain is a trade-off. If you join the domain, the company is the one responsible for managing your device, so all company rules and policies will be applied to it (Windows Update frequency, users, password resets, etc) and you will need to go through your SysAdmins if you have troubles with it. <br></p><p>If you choose to not join the domain, the machine management is all yours, giving you more freedom on the machine, but any automatic scripts would need to be done manually.</p><p>Below some pros and cons of joining the domain&#58;<br></p><table class="ssw15-rteTable-default" width="100%" cellspacing="0"><tbody><tr class="ssw15-rteTableEvenRow-default"><td class="ssw15-rteTableEvenCol-default" style="width&#58;33.3333%;">​</td><td class="ssw15-rteTableOddCol-default" style="width&#58;33.3333%;"><strong>Pros (+)</strong><br></td><td class="ssw15-rteTableEvenCol-default" style="width&#58;33.3333%;"><strong>Cons (-)</strong><br></td></tr><tr class="ssw15-rteTableOddRow-default"><td class="ssw15-rteTableEvenCol-default">Machine Management<br></td><td class="ssw15-rteTableOddCol-default">Client management through GPOs (Group Policy Objects)<br></td><td class="ssw15-rteTableEvenCol-default">Lack of autonomy<br></td></tr><tr class="ssw15-rteTableEvenRow-default"><td class="ssw15-rteTableEvenCol-default">Resource Access<br></td><td class="ssw15-rteTableOddCol-default">Direct access to resources (e.g. fileserver)<br></td><td class="ssw15-rteTableEvenCol-default">Needs to sign in first, or be attached to a VPN or the network to access resources<br></td></tr><tr class="ssw15-rteTableOddRow-default"><td class="ssw15-rteTableEvenCol-default">Automatic Scripts<br></td><td class="ssw15-rteTableOddCol-default">GPOs apply automatic scripts like the Login Script and Backup Scripts<br></td><td class="ssw15-rteTableEvenCol-default">Need to run Login and Backup scripts manually<br></td></tr><tr class="ssw15-rteTableEvenRow-default"><td class="ssw15-rteTableEvenCol-default" rowspan="1">Support Level <br></td><td class="ssw15-rteTableOddCol-default" rowspan="1">More support from your SysAdmins, you have someone to rely on for any troubleshooting on all computer applications<br></td><td class="ssw15-rteTableEvenCol-default" rowspan="1">Less support from SysAdmins, you can run any obscure application on your computer but that may not be supported by your company <br></td></tr><tr class="ssw15-rteTableFooterRow-default"><td class="ssw15-rteTableFooterEvenCol-default" rowspan="1"><br></td><td class="ssw15-rteTableFooterOddCol-default" rowspan="1"><br></td><td class="ssw15-rteTableFooterEvenCol-default" rowspan="1"><br></td></tr></tbody></table><p><br></p>


