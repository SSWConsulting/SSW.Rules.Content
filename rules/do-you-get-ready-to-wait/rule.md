---
type: rule
title: Do you get ready to wait?
uri: do-you-get-ready-to-wait
created: 2013-04-10T21:16:31.0000000Z
authors:
- id: 1
  title: Adam Cogan

---



<span class='intro'> <p>Initial Sitefinity load times are quite bad.<br>
                    On a live site you can do things like keeping the site warm though IIS however for developers this process takes quite a bit of time.</p> </span>

<p>Sitefinity caches everything, checks licenses, creates in memory pages from the content in the DB, etc.<br>
                    There will be a lot of small quick query's against the Sitefinity SQL database and it is important that these remain quick.</p><ol><li>Only compile when you are sure your code will work. It is also a good idea to complete 2 or 3 different things that you can test upon a rebuild to save time.</li><li><p>Disable Sitefinity modules that you are not using or don't need.<br>
                            We recommend disabling all modules and only enabling items that you require.</p><p>You can access the Module list via the Sitefinity backend.</p><dl class="image"><dt><img src="/PublishingImages/sitefinity-admin-module.jpg" alt="" /></dt><dd>Figure&#58; Administration -&gt; System -&gt; Modules</dd></dl></li><li>Ensure that the Sitefinity database is indexed and the Statistics are updated.<br>
                            This will ensure that the Sitefinity query's remain quick&#58;<br>
                           <a href="http&#58;//www.sitefinity.com/devnet/kb/sitefinity-5-x/sitefinity-database-maintenance.aspx">Sitefinity Database maintenance</a>

                        </li><li>Use a reflection tool like DotTrace that can show you what is slow on application start time.<br>
                        Using this method we determined that Sitefinity was using reflection on assemblies to find any MVC widgets and add them into the Sitefinity widget list. This process took a few seconds and we removed tags to speed this up.</li></ol><p><strong>Telerik Suggestion&#58;</strong> Have a best practise analyser wizard that is available in the backend which will look at the project and what is used and recommend settings that could be changed, modules that are not used, and any other improvements that can be applied.</p>


