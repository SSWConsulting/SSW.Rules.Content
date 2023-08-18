---
type: rule
title: Do you use "301" code to redirect renamed or moved pages?
uri: use-301-redirect-on-renamed-or-moved-pages
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
  - title: Tiago Araujo
    url: https://ssw.com.au/people/tiago-araujo
related: []
redirects:
  - do-you-use-301-code-to-redirect-renamed-or-moved-pages
created: 2015-11-09T19:16:40.000Z
archivedreason: null
guid: 775b4b29-6714-4df7-99b7-8716ff5c701d
---

Don't lose your Google juice when you rename a file. Do not use META refresh to redirect pages - "301" code is the most efficient and Search Engine Friendly method for webpage redirection. There are different ways to implement and it should preserve your search engine rankings for that particular page. If you have to change file names or move pages around, always use the code "301", which is interpreted as "moved permanently".

<!--endintro-->

### How to do a "301" redirect in .aspx

Any time you move a page or just delete a page you should add a "301" redirect to a new page or a page for missing pages.

1. You can add a 301 redirect in code:

    ```xml
    <% Response.RedirectPermanent("NEW PAGE URL HERE") %>
    ```

    Although this works well it is difficult to manage the list of redirects and you need to keep the page around.

2. **You can write an HTTP handler**   
   This is better as you can choose where to store the redirect list, but you still need to manage a custom codebase.

3. **You can use rewrite maps in IIS URL Rewrite to add a number of redirects**   
   See Storing URL rewrite mappings in a separate file  for an explanation of how to use rewrite maps.

**Note:**  If you are using a source control, like TFS, lock the old file so no-one can edit it by mistake.

### WordPress 

WordPress automatically redirects posts when you change the URL (permalink). No further action is required.
