---
type: rule
title: Do you have your cluster network on a separate Active Directory domain?
uri: do-you-have-your-cluster-network-on-a-separate-active-directory-domain
created: 2012-03-02T19:21:26.0000000Z
authors: []

---



<span class='intro'> Being able to communicate with the domain is so important for Hyper-V and clustering. To protect yourself from Active Directory problems, you can completely separate your primary Active Directory domain. </span>

<p>Having a separate Active Directory domain will allow your Hyper-V machines to run without problems in the case that your main Active Directory domain fails for any reason. </p>
<p>When you setup a new Active Directory domain for your Hyper-V cluster, create a trust between to 2 domains. </p>



