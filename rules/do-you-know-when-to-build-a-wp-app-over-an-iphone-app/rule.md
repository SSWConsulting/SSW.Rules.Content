---
type: rule
archivedreason: 
title: Do you know when to build a WP app over an iPhone app?
guid: b1c20a73-4a7e-41d1-a983-a7dc322369e1
uri: do-you-know-when-to-build-a-wp-app-over-an-iphone-app
created: 2014-11-25T23:57:57.0000000Z
authors: []
related: []

---


<ol><li>
                    <s>If your app is built on Silverlight today.</s> Stop building things on Silverlight today.
                </li><li>
                    Reasons are&#58;<br>
                <ul><li>Time to market</li><li>Lower cost</li><li>Reuse MVVM</li><li>Reuse Silverlight controls</li><li>Reuse the Business and Data layer</li></ul></li><li>
                    The Biggest thing going for windows phone is&#58;<br>
                <ul><li>.NET dev shops</li><li>Environment more productive than xcode</li></ul><p>
                    Note&#58; WP7 is built on Silverlight 3 (not Silverlight 4)</p><p>
                    Note&#58; WP7 was built by a 'web team' not &quot;Rich client app team', so some issues exist&#58;</p><ul><li>Bing map control relies on host page (authentication)</li><li>Avoid using System.Windows.Browser.dll in your Silverlight App (as it works only
                        OOB on desktop) and you will have to use a different control on Windows Phone 7</li></ul></li><li>
                    Others reasons are&#58;
                    <ul><li>You can deploy your app without going through the appstore/market place. E.g. my
                    SSW business app<br>
                <table class="data"><tbody><tr><td>
                            Appstore&#58;
                        </td><td>
                            No
                        </td></tr><tr><td>
                            Market place&#58;
                        </td><td>
                            Yes
                        </td></tr></tbody></table>
                        <br>
                </li><li>
                    Turn around through the appstore is quicker&#58;
                <table class="data"><tbody><tr><td>
                            Appstore&#58;
                        </td><td>
                            1-3 weeks
                        </td></tr><tr><td>
                            Market place&#58;
                        </td><td>
                            2 days (Quicker since it is managed code. Unmanaged code is easy to spot)
                        </td></tr></tbody></table>
                    <br>
                </li><li>
                    App store is blocking applications MS won't.
                </li></ul></li></ol>
<br><excerpt class='endintro'></excerpt><br>



