---
type: rule
title: Do you know how to troubleshoot Lync connectivity or configuration issues?
uri: do-you-know-how-to-troubleshoot-lync-connectivity-or-configuration-issues
created: 2012-04-17T21:06:54.0000000Z
authors:
- id: 1
  title: Adam Cogan

---



<span class='intro'> At times especially during the initial implementation, you may encounter some issues with Lync. The following are some of the useful tools which will assist you in identifying where the problem lies.<br> </span>

<p>Remote UC Troubleshooting Tool (RUCT) for Lync will show that the DNS records used by the Lync mobility clients to auto-discover the Lync mobility service have been added. This tool can be acquired from <a href="http&#58;//insideocs.com/" target="_blank">Inside OCS blog</a>.</p><p>Specifically, you now have the option of querying the locally configured DNS server for the following records&#58;</p><ul><li>Lyncdiscover. (both CNAME or A record)</li><li>Lyncdiscoverinternal. (both CNAME or A record)</li><li>From the same screen, you can ping the resulting hostname or test the port availability on any of the Lync DNS record matches</li></ul><dl class="image"><dt> <img src="lync-auto-discovery.jpg" alt="Lync Auto-discovery" class="ms-rteCustom-ImageArea" /> </dt><dd>Figure&#58; Lync Auto-Discovery Mobility DNS record</dd></dl><h3 class="ssw15-rteElement-H3">Lync Monitoring Reports</h3><p>The Monitoring Server collects data from the call detail recording (CDR) and Quality of Experience (QoE) databases and presents that data with the help of the SQL Server Reporting Services and the predefined Monitoring reports. These reports will show statistics which will assist in identifying issues such as network issues such as latency and packet loss.</p><h3 class="ssw15-rteElement-H3">Internet Network connectivity tests</h3><p>Tools such as&#160;VisualRoute 2010 will assist in highlight problems related latency and packet loss.</p><dl class="image"><dt><img src="visualroute-tool.jpg" alt="VisualRoute 2010 tool" class="ms-rteCustom-ImageArea" /> </dt><dd>Figure&#58; VisualRoute 2010 tool showing a test to a Google DNS server</dd></dl><p>Read more about implementing&#160;<a href="http&#58;//www.ssw.com.au/ssw/Consulting/Lync.aspx">Microsoft Lync</a>.​<br></p>


