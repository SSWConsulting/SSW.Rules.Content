---
type: rule
title: Do you know what DNS is and how it works?
uri: dns-what-and-how-it-works
authors:
  - title: Dhruv Mathur
    url: https://www.ssw.com.au/people/dhruv-mathur/
created: 2024-02-28T07:04:54.685Z
guid: 21275f4c-aaf4-4964-9d25-804f3cb56e75
---

            
The Domain Name System (DNS) is akin to the internet's phonebook. It's easy to remember a website's name, like www.ssw.com.au, but computers and networks need numerical IP addresses to access websites. DNS translates human-readable domain names to machine readable IP addresses.

### DNS explained

`youtube: https://www.youtube.com/embed/27r4Bzuj5NQ`

**Video: Everything You Need to Know About DNS (5 min)**
        
<!--endintro-->
Understanding DNS is crucial for troubleshooting connectivity issues, optimizing network performance, and ensuring secure internet navigation. Here's a breakdown of how DNS works:

- **Domain Name Input:** When you type a web address into your browser, the DNS process begins. Your browser requests the DNS to translate the human-friendly domain name into a machine-friendly IP address.

- **DNS resolver query:** Your computer sends this request to a DNS resolver, typically operated by your ISP (Internet Service Provider). If the resolver doesn't have the IP address cached, it queries further.

- **Root Nameserver Query:** The resolver contacts a root nameserver, which responds with the address of a Top-Level Domain (TLD) nameserver based on the TLD of the requested domain (e.g., `.com`, `.au`).

- **TLD Nameserver Query:** The resolver then asks the TLD nameserver for the authoritative nameserver of the domain, which holds the actual IP address.

- **Authoritative Nameserver Response:** The authoritative nameserver provides the IP address for the requested domain to the resolver.

- **Resolver Caching:** The resolver caches the IP address for a predetermined time, determined by the TTL (Time to Live), to improve response times for future queries to the same domain.

- **Browser Connection:** With the IP address now known to your machine, your browser can establish a connection to the web server hosting the domain and load the website.

**Note** The resolver's queries to root, TLD, and authoritative nameservers are recursive, meaning each server points to the next server in the chain until the IP address is found.



DNS is a foundational internet technology, enabling the seamless translation of domain names into IP addresses, making it easier for users to access websites without memorizing complex numerical addresses.
