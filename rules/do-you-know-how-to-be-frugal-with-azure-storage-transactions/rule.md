---
type: rule
title: Cost - Do you know how to be frugal with Azure Storage Transactions?
uri: do-you-know-how-to-be-frugal-with-azure-storage-transactions
authors:
  - title: Adam Stephensen
    url: https://ssw.com.au/people/adam-stephensen
related: []
redirects: []
created: 2012-04-23T14:23:33.000Z
archivedreason: null
guid: 38ac2eba-4663-4e86-afb0-6bee2847d994

---

Azure transactions are CHEAP. You get tens of thousands for just a few cents. What is dangerous though is that it is very easy to have your application generate hundreds of thousands of transactions a day. 

<!--endintro-->

Every call to Windows Azure Blobs, Tables and Queues count as 1 transaction. Windows Azure diagnostic logs, performance counters, trace statements and IIS logs are written to Table Storage or Blob Storage.

If you are unaware of this, it can quickly add up and either burn through your free trial account, or even create a large unexpected bill.

**Note:** Azure Storage Transactions do not count calls to SQL Azure.

### Be aware that Azure Functions Queue and Event Hub Triggers can cause lots of transactions
Both of these triggers can cause a lot of transactions. Typically this is controlled by the batch size you configure. What happens is that the Functions runtime needs to read and write a watermark into blob storage. This is a record of what items have been read from the Queue or Event Hub. So the bigger the batch size, the less often these records get written. If you expect your function to potentially be triggered a lot, make the batch size bigger. 

Many people set the batch size to 1, which results in ~2 storage transactions per trigger, which can get expensive quite fast.

### Ensure that Diagnostics are Disabled for your web and worker roles

Having Diagnostics enabled can contribute 25 transactions per minute, this is 36,000 transactions per day.

Question for Microsoft: Is this per Web Role?

![Figure: Check the properties of your web and worker role configuration files](azure-check-properties.jpg)

![Figure: Disable diagnostics](azure-disable-diagnostics.jpg)

### Disable IntelliTrace and Profiling
![Figure: When publishing, ensure that IntelliTrace and Profiling are both disabled](azure-publishing-settings.jpg) 

### Robots.txt 

Search bots crawling your site to index it will lead to a lot of transactions. Especially for web "applications" that do not need to be searchable, use Robot.txt to save transactions.
![Figure: Place robots.txt in the root of your site to control search engine indexing](azure-robots.jpg)

### Continuous Deployment

When deploying to Azure, the deployment package is loaded into the Storage Account. This will also contribute to the transaction count.

If you have enabled continuous deployment to Azure, you will need to monitor your transaction usage carefully.

### References

* [Understanding Windows Azure Storage Billing – Bandwidth, Transactions, and Capacity](https://technet2.github.io/Wiki/blogs/windowsazurestorage/understanding-windows-azure-storage-billing-bandwidth-transactions-and-capacity.html)
* [Does Windows Azure hosted service use storage transactions](https://serverfault.com/questions/363803/does-windows-azure-hosted-service-use-storage-transactions)
