---
type: rule
title: Do you shutdown VM's when you no longer need them?
uri: do-you-shutdown-vms-when-you-no-longer-need-them
created: 2013-07-22T04:39:27.0000000Z
authors:
- id: 28
  title: Daragh Bannigan
- id: 47
  title: Stanley Sidik

---



<span class='intro'> <p>Often we use Azure VM's for presentations, training and development. As there is a&#160;cost involved to store and use the VM it is important to ensure that the VM is shutdown when it is no longer required.​</p> </span>

<p>​<span style="line-height&#58;1.6;">This will prevent compute charges from incurring. There is still a cost involved for the storage of the VHD files but these charges are a lot less than the compute charges.&#160;</span></p><p>The following is stated on <a href="http&#58;//www.windowsazure.com/en-us/pricing/member-offers/msdn-benefits/">http&#58;//www.windowsazure.com/en-us/pricing/member-offers/msdn-benefits/</a>&#160;&quot;Stop your virtual machines and we will stop billing them within a minute. &quot; Please note that is for MSDN Azure subscriptions.&#160;</p><p>You can shutdown the VM by either making a remote desktop connection to the VM and shutdown server or using Azure portal to shutdown the VM.​</p><p><img src="/SoftwareDevelopment/Rules-to-Better-Azure/PublishingImages/Azure.jpg" alt="Azure.jpg" style="margin&#58;5px;width&#58;650px;" />​<br><strong>Figure&#58; Azure Portal​</strong></p>


