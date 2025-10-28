---
seoDescription: Learn the best methods to provide exceptional customer support and control client machines remotely with Microsoft Teams, AnyDesk, and Splashtop.
type: rule
archivedreason:
title: Do you know the best remote customer support tools?
guid: 09255b34-91b3-4404-b7f4-6fff46392c87
uri: remote-customer-support
created: 2009-03-04T06:49:46.0000000Z
authors:
  - title: Christian Morford-Waite
    url: https://ssw.com.au/people/christian-morford-waite
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
related:
  - remote-desktop-manager
redirects:
  - do-you-know-the-best-way-to-give-the-best-customer-support
---

Providing remote customer support is essential for IT administrators and support teams, especially when users are scattered across the globe. However, choosing the right tool can make or break the support experience.

<!--endintro-->

## Remote Desktop Support

For supporting end users' workstation machines remotely, consider the following tools in order of preference:

### 1. Microsoft Teams (Recommended)

* [Microsoft Teams](https://products.office.com/en-AU/microsoft-teams/group-chat-software) allows you to share screens and give remote control access securely
* It integrates seamlessly with the Microsoft ecosystem, making it ideal for organizations already using Microsoft 365

![Figure: Teams allow you to give remote control, making it the best option for giving support](Teams-give-control.png)

### 2. AnyDesk

* Lightweight and fast, [AnyDesk](https://anydesk.com/) is excellent for quick remote support sessions
* It supports cross-platform functionality and offers strong encryption for secure connections

### 3. Splashtop

* A cost-effective alternative to TeamViewer, [Splashtop](https://www.splashtop.com/) is easy to use and provides robust remote access features
* It is particularly useful for IT teams managing multiple devices

### 4. TeamViewer

* A popular choice for remote support, [TeamViewer](https://www.teamviewer.com/) offers a wide range of features, including file transfer and multi-monitor support
* However, it can be expensive for commercial use

## Remote Server Management

For managing server machines, the following tools are recommended:

### 1. Windows Remote Desktop (RDP)

* Built into Windows, RDP is a reliable choice for managing servers remotely
* It allows authenticated users to access a dedicated Windows login session without disrupting others

![Figure: Enable Remote Desktop](remoteconnection.png)

Remote Desktop works for workstations, but it's not recommended due to a security risk if Remote Support isn't disabled. Also, because of the End User License Agreement (EULA), only allows 1 user at a time, if you log in to client's Windows machine, the client will be logged off.

### 2. VNC-Based Tools

* Tools like [TightVNC](https://www.tightvnc.com/) and [UltraVNC](https://www.uvnc.com/) are useful when RDP is not an option
* VNC tools share the same session as the logged-in user, making them suitable for collaborative troubleshooting

If you can't use TeamViewer, Teams, or Remote Desktop, you can try VNC. There are a number of VNC servers and clients available. VNC-based sessions typically behave as if you're physically using the computer. This means that it shares the same login session with the user who is currently logged on the machine. VNC software allows you to configure a specific username and password for remote access, which means that you don't have to share Windows usernames and passwords or create a temporary Windows user account. Some clients may also prefer this as they can sit in and watch what is happening.
