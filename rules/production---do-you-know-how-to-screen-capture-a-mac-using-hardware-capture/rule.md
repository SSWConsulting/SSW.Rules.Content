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


Capturing video from your mac can be done in different ways. One way is to use software that will capture the screen, and create a file that you can use in your editing software. The other is to use hardware capture that connects to the video output (i.e. HDMI) of your mac. This rule will focus on capturing&#160;video via hardware.
<br><excerpt class='endintro'></excerpt><br>
<p class="p1">At SSW, we use HDMI capture cards to record the video from a presenters’ laptop into our workstation. This video is then either recorded for later editing or used as part of the Live Stream.</p><p class="p2"><span style="line-height&#58;1.6;">PC’s will have no issues when connecting to the system. Outputting via HDMI, VGA or Display Port, you can connect directly or convert these connections via a splitter/scaler device.</span><br></p><p class="p2"><br></p><p class="p1">*Pic of Device*</p><p class="p2"><br></p><p class="p1">Mac’s however run into a issue with copy protection when outputting via a digital connection.</p><p class="p2"><br></p><p class="p1">*Pic of HDCP*</p><p class="p2"><br></p><p class="p1">If connecting a MAC via a digital connection, you will see the above message in XSplit (and any other similar streaming/capture software).</p><p class="p2"><span style="line-height&#58;1.6;">To overcome this, you need to convert the signal to VGA (analogue), which will strip out the HDCP protection.</span><br></p><p class="p2"><br></p><p class="p1">*Pic of VGA adapter*</p><p class="p2"><br></p><p class="p1">The second issue with this scenario is that the HDMI capture card in the workstation will not except a VGA signal. To overcome this you need to use a scaler device.</p><p class="p2"><br></p><p class="p1">Pic of Scaler</p><p class="p1"></p><p class="p1"><br></p><p class="p1">The scaler has multiple roles&#58;</p><ol class="ol1"><li class="li1">It converts digital and analogue signals into a digital HDMI output</li><li class="li1">It outputs 2 HDMI simultaneously (useful if you want to connect to a projector and a capture device at the same time)</li><li class="li1">It upscales low-resolution video to match the output resolution of 1080p/30, which means your capture hardware and software will correctly display the image.</li></ol><p class="p3"><span style="line-height&#58;1.6;">C</span><span style="line-height&#58;1.6;">onnecting the Mac to the capture devce&#58;</span><br></p><p class="p2"><br></p><ol class="ol1"><li class="li1">1.<span class="Apple-tab-span"> </span>Use the Mini DP to VGA to connect to the VGA input on the scaler.</li><li class="li1">2.<span class="Apple-tab-span"> </span>Connect the HDMI 2 output to the capture device on your workstation</li></ol><p class="p3"><br></p><p class="p1">If you use Windows natively on mac (not using Parallels), you will not have any issues with HDCP protection, so you can just connect via the display port or HDMI with no issues.</p>


