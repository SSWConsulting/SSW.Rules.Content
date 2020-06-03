---
type: rule
title: Do you know how to be frugal with Azure Storage Transactions?
uri: do-you-know-how-to-be-frugal-with-azure-storage-transactions
created: 2012-04-23T14:23:33.0000000Z
authors:
- id: 24
  title: Adam Stephensen

---



<span class='intro'> Azure transactions are CHEAP. You get tens of thousands for just a few cents. What is dangerous though is that it is very easy to have your application generate hundreds of thousands of transactions a day. </span>

<p>Every call to Windows Azure Blobs, Tables and Queues count as 1 transaction. Windows Azure diagnostic logs, performance counters, trace statements and IIS logs are written to Table Storage or Blob Storage.</p>
<p>If you are unaware of this, it can quickly add up and either burn through your free trial account, or even create a large unexpected bill.</p>
<p><strong>Note&#58;</strong> Azure Storage Transactions do not count calls to SQL Azure.</p>
<h2>Ensure that Diagnostics are Disabled for your web and worker roles</h2>
<p>Having Diagnostics enabled can contribute 25 transactions per minute, this is 36,000 transactions per day.</p>
<p>Question for Microsoft&#58; Is this per Web Role?</p>

<img src="/PublishingImages/azure-check-properties.jpg" alt="Check properties" class="ms-rteCustom-ImageArea" />
<span class="ms-rteCustom-FigureNormal">Figure&#58; Check the properties of your web and worker role configuration files</span>

<img src="/PublishingImages/azure-disable-diagnostics.jpg" alt="Disable Diagnostics" class="ms-rteCustom-ImageArea" />
<span class="ms-rteCustom-FigureNormal">Figure&#58; Disable diagnostics</span>

<h2>Disable IntelliTrace and Profiling</h2>

<img src="/PublishingImages/azure-publishing-settings.jpg" alt="Azure publishing settings" class="ms-rteCustom-ImageArea" />
<span class="ms-rteCustom-FigureNormal">Figure&#58; When publishing, ensure that IntelliTrace and Profiling are both disabled</span>

<h2>Robots.txt </h2>
<p>Search bots crawling your site to index it will lead to a lot of transactions. Especially for web &quot;applications&quot; that do not need to be searchable, use Robot.txt to save transactions.</p>

<img src="/PublishingImages/azure-robots.jpg" alt="Place robots.txt" class="ms-rteCustom-ImageArea" />
<span class="ms-rteCustom-FigureNormal">Figure&#58; Place robots.txt in the root of your site to control search engine indexing</span>

<h2>Continuous Deployment</h2>
<p>When deploying to Azure, the deployment package is loaded into the Storage Account. This will also contribute to the transaction count.</p>
<p>If you have enabled continuous deployment to Azure, you will need to monitor your transaction usage carefully.</p>

<h3>References</h3>
<ul>

<li><a href="http&#58;//blogs.msdn.com/b/windowsazurestorage/archive/2010/07/09/understanding-windows-azure-storage-billing-bandwidth-transactions-and-capacity.aspx%20target=">Understanding Windows Azure Storage Billing – Bandwidth, Transactions, and Capacity</a></li>
<li><a href="http&#58;//serverfault.com/questions/363803/does-windows-azure-hosted-service-use-storage-transactions%20target=">Does Windows Azure hosted service use storage transactions</a></li>
</ul>






