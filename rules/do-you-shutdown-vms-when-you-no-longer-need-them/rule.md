---
type: rule
archivedreason: 
title: Do you shutdown VM's when you no longer need them?
guid: 5ec42693-3dd0-4b21-ad0d-0c51814d0643
uri: do-you-shutdown-vms-when-you-no-longer-need-them
created: 2013-07-22T04:39:27.0000000Z
authors:
- title: Daragh Bannigan
  url: https://ssw.com.au/people/daragh-bannigan
- title: Stanley Sidik
  url: https://ssw.com.au/people/stanley-sidik
related: []
redirects: []

---


<p>​​Often we use Azure VM's for presentations, training and development. As there is a cost involved to store and use the VM it is important to ensure that the VM is shutdown when it is no longer required.​</p>
<br><excerpt class='endintro'></excerpt><br>
<p><span style="line-height:1.6;">Shutting down the VM will prevent compute charges from incurring. There is still a cost involved for the storage of the VHD files but these charges are a lot less than the compute charges. </span></p><p>The following is stated on <a href="http://www.windowsazure.com/en-us/pricing/member-offers/msdn-benefits/">http://www.windowsazure.com/en-us/pricing/member-offers/msdn-benefits/</a> "Stop your virtual machines and we will stop billing them within a minute. " Please note that is for MSDN Azure subscriptions. </p><p>You can shutdown the VM by either making a remote desktop connection to the VM and shutdown server or using Azure portal to shutdown the VM.​</p><p><img src="Azure.jpg" alt="Azure.jpg" style="margin:5px;width:650px;" />​<br><strong>Figure: Azure Portal​</strong></p>


