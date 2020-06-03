---
type: rule
title: Do you know how to decommission a Virtual Machine?
uri: do-you-know-how-to-decommission-a-virtual-machine
created: 2011-06-14T04:32:43.0000000Z
authors:
- id: 21
  title: Matthew Hodgkins

---



<span class='intro'> It is important to properly decommission a Virtual Machine rather than just delete it. Developers have a knack for leaving important files everywhere, and inside a Virtual Machine is no exception. 
 </span>


  <ol>
    <li>Let the people that may have been using the Virtual Machine that it is going to be decommissioned. This might be difficult if it was being used for testing or staging. </li>
    <li>Make a text file that matches the name of the Virtual Machine. </li>
    <li>Note down the Virtual Machines static IP address in the text file. </li>
    <li>Check the DNS Manager on a domain controller and note down any DNS names that pointed to the IP Address of the Virtual Machine. </li>
    <li>Copy the Virtual Machines folder to a file server or backup drive. </li>
    <li>Copy the text file into the same location. </li>
    <li>Set a calendar reminder for yourself to delete the Virtual Machine if it hasn’t been requested in 3 months. </li>
</ol>



