---
type: rule
archivedreason: 
title: What are the different images available?
guid: c0f129f6-4237-424a-8575-37817f283c60
uri: what-are-the-different-images-available
created: 2009-02-26T02:03:35.0000000Z
authors: []
related: []

---

We have three types of VM images around the office.

1. The master.vhd is for upgrading future VMs and sysprep VM's are built from the master.vhd
The  **master.vhd is versioned (e.g. master\_v8.vhd)** to track which version it is, and to assist us in upgrading the master image.
2. The sysprep.vhd is the one that we use to create a new SharePoint server 
When you run the sysprep.vhd it will create a new SharePoint server. Always make a copy of this to your own machine. The  **sysprep.vhd is versioned (e.g. sysprep\_v8.vhd)**
3. You may find various other VM's created from sysprep.vhd and used for various projects or experiments
These images are usually renamed but kept the original version number that it was created from. (e.g. sswsp\_v8.vhd)


<!--endintro-->
