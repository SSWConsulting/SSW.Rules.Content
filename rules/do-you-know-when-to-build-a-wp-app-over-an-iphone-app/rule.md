---
type: rule
title: Do you know when to build a WP app over an iPhone app?
uri: do-you-know-when-to-build-a-wp-app-over-an-iphone-app
authors: []
related: []
redirects: []
created: 2014-11-25T23:57:57.000Z
archivedreason: Deprecated
guid: b1c20a73-4a7e-41d1-a983-a7dc322369e1
---

1. ~~If your app is built on Silverlight today.~~ Stop building things on Silverlight today.

<!--endintro--> 

2. Reasons are:
    * Time to market
    * Lower cost
    * Reuse MVVM
    * Reuse Silverlight controls
    * Reuse the Business and Data layer

3. The Biggest thing going for windows phone is:

    * .NET dev shops
    * Environment more productive than xcode

    Note: WP7 is built on Silverlight 3 (not Silverlight 4)
    Note: WP7 was built by a 'web team' not "Rich client app team', so some issues exist:

    * Bing map control relies on host page (authentication)
    * Avoid using System.Windows.Browser.dll in your Silverlight App (as it works only
                        OOB on desktop) and you will have to use a different control on Windows Phone 7
4. Others reasons are:
    * You can deploy your app without going through the appstore/market place. E.g. my SSW business app
