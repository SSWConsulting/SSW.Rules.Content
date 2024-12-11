---
type: rule
tips: ""
title: Do you limit MAC addresses on your network switches?
seoDescription: Limiting MAC addresses on your network switches to enhance security, control access, and optimize network performance. Learn how and why to implement MAC address restrictions effectively.
uri: limit-mac-addresses-network-switches
authors:
  - title: Kiki Biancatti
    url: https://ssw.com.au/people/kaique-biancatti
related:
  - separate-networks
  - do-you-use-network-intrusion-prevention-systems
guid: a1a2c8c4-efe5-42e8-8e25-bc52fac8ded5
---

Have you ever faced a scenario where an unauthorized device is discreetly connected to an open port on your network switch, potentially intercepting sensitive data or disrupting critical services? This situation isn’t just theoretical - it can lead to serious security breaches, data theft, and system downtime if you do not restrict the MAC addresses allowed to connect.        

<!--endintro-->

::: bad
![Figure: Bad example - An access port with continuous learn mode, meaning any device can connect to it and no security traps will be raised](badexampleports.png)
:::

An open switch port accepts any device, allowing a malicious actor to connect and compromise internal systems.

::: good
![Figure: Good example - A switch port accepts only predefined MAC addresses, or is limited on the number of MAC addresses it can learn. Unauthorized devices are immediately blocked, safeguarding the network’s perimeter](goodexampleports.png)
:::

## Benefits of limiting MAC addresses on network switches

* **Increased security** - Restricts unauthorized hardware from accessing sensitive resources
* **Stronger perimeter** - Keeps dangerous devices from infiltrating your network, especially at high-risk access points like camera ports
* **Data protection** - Maintains the integrity and confidentiality of your data by ensuring only trusted devices connect

### Particularly Vulnerable: Camera Ports

Outdoor or easily accessible camera ports are prime targets, as attackers can physically connect rogue devices to these less protected areas. By setting static or pre-approved MAC addresses on these ports, you ensure only the intended camera is allowed—keeping bad actors out.

Together with other security standards like [keeping your networks separated via Virtual LANs](/separate-networks/) and [using Intrusion Prevention Systems](/do-you-use-network-intrusion-prevention-systems/), your network should always be tested and protected against malicious actors in the wild.
