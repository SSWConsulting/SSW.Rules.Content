---
type: rule
archivedreason: 
title: Do you have servers around the world and use CDN?
guid: de201548-f9b2-4f54-95f2-300e8bb3b62e
uri: do-you-have-servers-around-the-world-and-use-cdn
created: 2014-09-03T19:17:30.0000000Z
authors:
- id: 1
  title: Adam Cogan
related: []

---


Having a very popular website is great. The only problem is where to host it. If you host it in your local country then it is very fast for your local market but what about the market on the other side of the world?
<br><excerpt class='endintro'></excerpt><br>
<p>The solution is to have 2 or more servers and direct users to the server that is the closest to them. This is possible with the help of Bind DNS server and a list of IP addresses and the country of origin.</p><p>The beauty of this solution is that it is not application specific. Anything like VoIP or game servers can be directed to their local server.<br>Follow the directions found in this article http&#58;//peen.net/2006/03/08/geo-dns to setup your Bind config file. The only problem is that the PHP script supplied in that article does not work correctly. It cannot convert the number based IP to the real IP and subnet. Because of this I had to create my own little app to make the file for Bind to use. You can find it and get the <a href="/Documents/IpToCountryConverter.zip"> source code</a>.</p><p>You can download a free list of IP to country’s from <a href="http&#58;//software77.net/geo-ip/"> http&#58;//software77.net/cgi-bin/ip-country/geo-ip.pl</a></p><p>
                    <strong>How it works&#58;<br>
                    </strong>Once you have made your acl files you can use views in the bind configuration to specify which zone file to use for each group of IP’s. Each zone file would have the relevant IP information for that target segment of the world.</p><p>Imagine you have 3 zone files&#58; one for europe, one for the america’s and one for the rest of the world. You simple edit named.conf.local to include the acls for europe and the america’s. E.g.&#58;</p><dl class="code"><dt>     include &quot;/etc/bind/named.conf.options&quot;; <br>    include &quot;/etc/bind/acl-europe_east.inc&quot;; <br>    include &quot;/etc/bind/acl-europe_sout.inc&quot;; <br>    include &quot;/etc/bind/acl-europe_west.inc&quot;; <br>    include &quot;/etc/bind/acl-europe_nort.inc&quot;; <br>    include &quot;/etc/bind/acl-america_cari.inc&quot;; <br>    include &quot;/etc/bind/acl-america_cent.inc&quot;; <br>    include &quot;/etc/bind/acl-america_nort.inc&quot;; <br>    include &quot;/etc/bind/acl-america_sout.inc&quot;; <br>    <br>    Next you create separate views. One for europe, one for the america’s     and one for everyone else. <br>    view &quot;europe&quot; &#123; <br>    &#160;match-clients &#123; <br>    &#160;&#160;europe_east; <br>    &#160;&#160;europe_nort; <br>    &#160;&#160;europe_sout; <br>    &#160;&#160;europe_west <br>    &#160;&#125;; <br>    &#160;zone &quot;peen.net&quot; &#123; <br>    &#160;&#160;type master; <br>    &#160;&#160;file &quot;/etc/bind/europe/db.peen.net&quot;; <br>    &#160;&#125;; <br>    &#125;; <br>
                        <br>    view &quot;americas&quot; &#123; <br>    &#160;match-clients &#123; <br>    &#160;&#160;america_cari; <br>    &#160;&#160;america_nort; <br>    &#160;&#160;america_sout; <br>    &#160;&#160;america_cent <br>    &#160;&#125;; <br>    &#160;zone &quot;peen.net&quot; &#123; <br>    &#160;&#160;type master; <br>    &#160;&#160;file &quot;/etc/bind/americas/db.peen.net&quot;; <br>    &#160;&#125;; <br>    &#125;; <br>
                        <br>    view &quot;others&quot; &#123; <br>    &#160;match-clients &#123; any; &#125;; <br>    &#160;zone &quot;peen.net&quot; &#123; <br>    &#160;&#160;type master; <br>    &#160;&#160;file &quot;/etc/bind/others/db.peen.net&quot;; <br>    &#160;&#125;; <br>    &#125;;</dt></dl>​


