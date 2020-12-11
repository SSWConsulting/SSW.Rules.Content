---
type: rule
archivedreason: 
title: Production - Do You Know How to Screen Capture a Mac Using Hardware Capture?
guid: b144c772-9c63-4f5f-8075-f56b1100909d
uri: production---do-you-know-how-to-screen-capture-a-mac-using-hardware-capture
created: 2014-10-29T01:51:33.0000000Z
authors:
- id: 29
  title: Raj Dhatt
related: []

---

Capturing video from your mac can be done in different ways. One way is to use software that will capture the screen, and create a file that you can use in your editing software. The other is to use hardware capture that connects to the video output (i.e. HDMI) of your mac. This rule will focus on capturing video via hardware. 
<!--endintro-->

At SSW, we use HDMI capture cards to record the video from a presenters’ laptop into our workstation. This video is then either recorded for later editing or used as part of the Live Stream.

PC’s will have no issues when connecting to the system. Outputting via HDMI, VGA or Display Port, you can connect directly or convert these connections via a splitter/scaler device.



\*Pic of Device\*



Mac’s however run into a issue with copy protection when outputting via a digital connection.



\*Pic of HDCP\*



If connecting a MAC via a digital connection, you will see the above message in XSplit (and any other similar streaming/capture software).

To overcome this, you need to convert the signal to VGA (analogue), which will strip out the HDCP protection.



\*Pic of VGA adapter\*



The second issue with this scenario is that the HDMI capture card in the workstation will not except a VGA signal. To overcome this you need to use a scaler device.



Pic of Scaler





The scaler has multiple roles:

1. It converts digital and analogue signals into a digital HDMI output
2. It outputs 2 HDMI simultaneously (useful if you want to connect to a projector and a capture device at the same time)
3. It upscales low-resolution video to match the output resolution of 1080p/30, which means your capture hardware and software will correctly display the image.


Connecting the Mac to the capture devce:



1. 1. Use the Mini DP to VGA to connect to the VGA input on the scaler.
2. 2. Connect the HDMI 2 output to the capture device on your workstation




If you use Windows natively on mac (not using Parallels), you will not have any issues with HDCP protection, so you can just connect via the display port or HDMI with no issues.
