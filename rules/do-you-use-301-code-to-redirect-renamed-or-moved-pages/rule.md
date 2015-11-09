---
type: rule
title: Do you use "301" code to redirect renamed or moved pages?
uri: do-you-use-301-code-to-redirect-renamed-or-moved-pages
created: 2015-11-09T19:16:40.0000000Z
authors:
- id: 1
  title: Adam Cogan
- id: 16
  title: Tiago Araujo

---



<span class='intro'> <p>Don't lose your Google juice when you rename a file. Do not use META refresh to redirect pages - &quot;301&quot; code is the most efficient and Search Engine Friendly method for webpage redirection. There are different ways to implement and it should preserve your search engine rankings for that particular page. If you have to change file names or move pages around, always use the code &quot;301&quot;, which is interpreted as &quot;moved permanently&quot;.​</p> </span>

<h3 class="ssw15-rteElement-H3">​How to do a &quot;301&quot; redirect</h3>Any time you move a page or just delete a page you should add a &quot;301&quot; redirect to a new page or a page for missing pages.<br><ol><li><span style="line-height&#58;20px;"><b>You can add a 301 redirect in code&#160;</b><br></span><span style="line-height&#58;20px;">Response.PermanentRedirect(&quot;~/MyNewPage.aspx&quot;)<br></span><span style="line-height&#58;20px;">Although this works well it is difficult to manage the list of redirects and you need to keep the page around.</span></li><li><span style="line-height&#58;20px;"><b>You can write an HTTP handler</b><br></span><span style="line-height&#58;20px;">This is better as you can choose where to store the redirect list, but you still need to manage a custom codebase.</span></li><li><span style="line-height&#58;20px;"><b>You can use rewrite maps in IIS URL Rewrite to add a number of redirects​</b><br></span><span style="line-height&#58;20px;">See&#160;Storing URL rewrite mappings in a separate file&#160;&#160;for an explanation of how to use rewrite maps.</span></li></ol><b>Note&#58;</b>&#160;If you are using a source control, like TFS, lock the old file so no-one can edit it by mistake.<br>


