---
type: rule
title: Do you know how to add a print server?
uri: print-server
authors:
  - title: Stanley Sidik
    url: https://ssw.com.au/people/stanley-sidik
  - title: Ash Anil
  - title: Kaique Biancatti
    url: https://ssw.com.au/people/kiki
    img: ""
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
  - do-you-know-how-to-add-a-printer
created: 2015-05-21T17:25:55.000Z
archivedreason: null
guid: 5b60b93d-f9af-467e-8d0c-41b1e37700ba
---
When you are connected to the company's network, you should complete the following procedure if you want to setup a printer server.

<!--endintro-->

### For Windows OS

Steps to add a printer to Active Directory:

1. In Windows Run | Type "printmanagement.msc" | Hit Enter
2. Right-click 'Print Server' | Choose 'Add/Remove Servers' | Add IP address or computer name | Finish\
   or\
   Right click the 'Print Server' | Add printer | Choose the best option (e.g TCP/IP) | Put the IP address of the Printer | Finish

![Figure: Add Print servers to AD ](46d5125c-b334-49f4-b1ee-45bc78b5dae1.png)

4. Add DNS entry for your print server (e.g \\printer) to make it friendly for the users to find

**Note:** Another method is using a Universal Printer in Azure  [https://azurescene.com/2020/04/10/how-to-configure-universal-print/](https://azurescene.com/2020/04/10/how-to-configure-universal-print/ "https\://azurescene.com/2020/04/10/how-to-configure-universal-print/") 

### Finding the Printers

Now your users can find the printers by doing the following:

1. In the File explorer | Type **\\printer** on the address bar to show all the printers connected to the server

::: bad

![Figure: Bad example – Windows 11 | Printers & scanners - Users won’t see all the printers by default](primt.jpg)

:::

::: good
![Figure: Good example - Printers listed in Printer Server](printers.jpg)
:::

2. Double click on your printer name to connect/add it. Follow prompt to finish the printer driver installation