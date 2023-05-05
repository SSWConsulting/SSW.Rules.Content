---
type: rule
title: Do you keep your networks separated?
uri: separate-networks
authors:
  - title: Chris Schultz
    url: https://ssw.com.au/people/chris-schultz
created: 2023-05-05T06:10:19.136Z
guid: 97f4f1b1-b161-40c4-ab97-6fbd765e8327
---
Keeping networks and VLANs separated is an essential aspect of a robust security strategy. This is particularly true for less secure networks such as automation and HVAC systems, which are often overlooked by cybercriminals looking to gain unauthorized access to the network.        

<!--endintro-->

The following guidelines can help system administrators maintain the separation of VLANs.

### Define VLANs

Assigning different VLANs for different client types and services provides a logical division of the network. This will help ensure that each network is independent, even if they share the same physical infrastructure.

### Implement Security Measures

VLANs should be separated using access control lists and firewalls. Ensure that there are no unauthorized access points between VLANs and that the only devices that can communicate between VLANs are those that are authorized.

### Monitor Network Traffic

Regular monitoring of network traffic can help identify anomalies and suspicious activities. Also, implement traffic shaping controls to restrict traffic entering less secure VLANs.

### Data Encryption

All data should be encrypted using secure protocols such as SSL, SSH, and VPNs, to align with industry best practices. This will help ensure that data exchanged between VLANs remains secure.



By following these guidelines, system administrators can keep networks and VLANs separated while enacting security measures that will prevent unauthorized access to every part of the network. Thus, creating a safer and more secure network environment.