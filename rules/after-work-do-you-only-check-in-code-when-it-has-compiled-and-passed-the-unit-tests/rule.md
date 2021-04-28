---
type: rule
archivedreason: 
title: After work - Do you only check-in code when it has compiled and passed the unit tests?
guid: 628ea729-95f9-4f55-8985-6ffe130b5a70
uri: after-work-do-you-only-check-in-code-when-it-has-compiled-and-passed-the-unit-tests
created: 2011-11-18T03:52:34.0000000Z
authors:
- title: David Klein
  url: https://ssw.com.au/people/david-klein
- title: Justin King
  url: https://ssw.com.au/people/justin-king
- title: Tristan Kurniawan
  url: https://ssw.com.au/people/tristan-kurniawan
- title: Ryan Tee
  url: https://ssw.com.au/people/ryan-tee
related: []
redirects:
- (after-work)-do-you-only-check-in-code-when-it-has-compiled-and-passed-the-unit-tests

---

Too many people treat Source Control as a networked drive. Don't just check-in when the clock ticks past 5 or 6 o'clock. If code doesn't pass its unit tests or won't even compile put your code in a [shelveset](http://msdn.microsoft.com/en-us/library/ms181403.aspx).

<!--endintro-->

![Figure: Put your dishes straight in the dishwasher otherwise you leave a mess for others (aka "Check-in" the right way otherwise you give other developers problems)](LeaveAMessToOthers.jpg)  

Other recommendations have included using "//TODO" or commenting the code out. However, we recommend avoiding this practice as it increases the risk that the code is forgotten about.

**Note:** Having [gated check-ins](/do-you-know-the-minimum-builds-to-create-for-your-project) will help prevent this from happening.

**Note:** A useful tool is [TFS Auto Shelve](https://marketplace.visualstudio.com/items?itemName=Vercellone.TFSAutoShelveforVisualStudio2017) - Protect your code by guaranteeing your pending changes are always backed up to the TFS server.
