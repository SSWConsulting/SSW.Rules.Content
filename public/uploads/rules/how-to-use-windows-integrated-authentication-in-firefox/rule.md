---
seoDescription: Use Firefox's built-in Windows Integrated Authentication feature to automatically log in to SharePoint or CRM without re-authenticating.
type: rule
archivedreason: Outdated
title: Do you know how to use Windows Integrated Authentication in Firefox?
guid: bb5713f5-6832-4704-8676-af0cafb7d9f7
uri: how-to-use-windows-integrated-authentication-in-firefox
created: 2016-02-02T19:28:24.0000000Z
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
  - title: Peter Gfader
    url: https://ssw.com.au/people/peter-gfader
related: []
redirects:
  - do-you-know-how-to-use-windows-integrated-authentication-in-firefox
---

Internet Explorer has a great feature that you hardly notice. The Authentication credentials of the current user will be used by default.

![Figure: Internet Explorer has the Integrated Authentication feature built in](ie-integrated.JPG)

In Firefox, if you sign-in to an internal server like SharePoint or CRM, you will get an authentication dialog. Even though you are already authenticated to the local domain.

![Figure: We want to avoid authenticating using Firefox (so it works like IE)](ff-auth1.JPG)

<!--endintro-->

### The Solution

1. Open Firefox
2. Go to "about:config"
3. Click "I'll be careful, I promise!"
4. Enter in the Filter box above: "network.automatic"
5. You see 2 records
6. Double-click the second one - It is the key called network.automatic-ntlm-auth.trusted-uris
7. Enter the servers delimited by ",", e.g. "aphrodite, mermaid"
8. Close browser and test

![Figure: Showed how to find "network.automatic-ntlm-auth.trusted-uris" by using filter: "network.automatic"](ff-auth2.JPG)

More info on this blog: [Firefox and Sharepoint](http://www.cauldwell.net/patrick/blog/PermaLink%2cguid%2cc7f1e799-c4ae-4758-9de7-5c3e7a16f3da.aspx).

**Tip:** To test this without the Integrated Authentication enabled, you need to clear your session. You do this via: **Tools** | **Clear private data** | **Authenticated Sessions** .

![Figure: To test you will need to clear your "Authenticated Sessions" to completely logout from a site (SharePoint, CRM)](ff-auth3.JPG)
