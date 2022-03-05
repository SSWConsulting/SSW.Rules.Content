---
type: rule
title: Do you know how to add a print server?
uri: print-server
authors:
  - title: Stanley Sidik
    url: https://ssw.com.au/people/stanley-sidik
  - title: Ash Anil
related: []
redirects: []
created: 2015-05-21T17:25:55.000Z
archivedreason: null
guid: 5b60b93d-f9af-467e-8d0c-41b1e37700ba
---
When you are connected to the company's network, you should complete the following procedure if you want to setup a printer server.

<!--endintro-->

**For Windows OS:**

##### Steps to add a printer to Active Directory

1. In run | type "printmanagement.msc" | enter
2. Right-click 'Print Server' | Choose Add/Remove Servers | Add IP address or computer name\
   or
3. Right click the 'Print Server' | Add printer | Choose the best option (e.g TCP/IP) | Put the IP address of the Printer | Finish

![Figure: Print servers ](46d5125c-b334-49f4-b1ee-45bc78b5dae1.png)

4. Add DNS entry for your print server (e.g \printer) to make it friendly for the users to find.

Now your users can find the printers by doing the following:

1. In the File explorer | type **\printer** on the address bar to show all the printers connected to the server.

:::bad

![Figure: Bad example – Windows 11 | Printers & scanners - Users won’t see all the printers by default](image001.png)

:::

::: good

![Figure: Good example - Printers listed in Printer Server](printers.jpg)

:::



2. Double click on your printer name to connect/add it. Follow prompt to finish the printer driver installation.