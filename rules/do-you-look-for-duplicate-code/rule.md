---
type: rule
title: Do you look for duplicate code?
uri: do-you-look-for-duplicate-code
created: 2012-04-01T09:56:14.0000000Z
authors:
- id: 1
  title: Adam Cogan
- id: 23
  title: Damian Brady

---



<span class='intro'> <span lang="EN-AU" style="font-family&#58;calibri, sans-serif;font-size&#58;11pt;">Code duplication is a big &quot;code smell&quot; that harms maintainability.&#160; You should keep an eye out for repeated code and make sure you refactor it into a single place.</span> </span>

<p>For example, have a look at these two Action methods&#160;in an MVC 4 controller.</p>
<span class="ssw-rteStyle-CodeArea"><pre>//
// GET&#58; /Person/
[Authorize]
public ActionResult Index()
&#123;
<span style="background-color&#58;rgb(255, 255, 0);">    // get company this user can view
    Company company = null;
    var currentUser = Session[&quot;CurrentUser&quot;] as User;
    if (currentUser != null)
    &#123;
        company = currentUser.Company;
    &#125;
</span>
    // show people in that company
    if (company != null)
    &#123;
        var people = db.People.Where(p =&gt; p.Company == company);
        return View(people);
    &#125;
    else
    &#123;
        return View(new List());
    &#125;
&#125;

//
// GET&#58; /Person/Details/5
[Authorize]
public ActionResult Details(int id = 0)
&#123;
<span style="background-color&#58;rgb(255, 255, 0);">    // get company this user can view
    Company company = null;
    var currentUser = Session[&quot;CurrentUser&quot;] as User;
    if (currentUser != null)
    &#123;
        company = currentUser.Company;
    &#125;
</span>
    // get matching person
    Person person = db.People.Find(id);
    if (person == null || person.Company == company)
    &#123;
        return HttpNotFound();
    &#125;
    return View(person);
&#125;
</pre></span><div class="ssw-rteStyle-FigureBad">Figure&#58;&#160;Bad Example - The highlighted code is repeated and represents a potential maintenance issue.</div>
<p>We can refactor this code to make sure the repeated lines are only in one place.</p>
<span class="ssw-rteStyle-CodeArea"><pre><span style="background-color&#58;rgb(255, 255, 0);">private Company GetCurrentUserCompany()
&#123;
    // get company this user can view
    Company company = null;
    var currentUser = Session[&quot;CurrentUser&quot;] as User;
    if (currentUser != null)
    &#123;
        company = currentUser.Company;
    &#125;
    return company;
&#125;
</span>
//
// GET&#58; /Person/
[Authorize]
public ActionResult Index()
&#123;
    // get company this user can view
    <span style="background-color&#58;rgb(255, 255, 0);">Company company = GetCurrentUserCompany();
</span>
    // show people in that company
    if (company != null)
    &#123;
        var people = db.People.Where(p =&gt; p.Company == company);
        return View(people);
    &#125;
    else
    &#123;
        return View(new List());
    &#125;
&#125;


// GET&#58; /Person/Details/5
[Authorize]
public ActionResult Details(int id = 0)
&#123;
    // get company this user can view
    <span style="background-color&#58;rgb(255, 255, 0);">Company company = Ge</span><span style="background-color&#58;rgb(255, 255, 0);"></span><span style="background-color&#58;rgb(255, 255, 0);">tCurrentUserCompany();
</span>
    // get matching person
    Person person = db.People.Find(id);
    if (person == null || person.Company == company)
    &#123;
        return HttpNotFound();
    &#125;
    return View(person);
&#125;
</pre></span><div class="ssw-rteStyle-FigureGood">Figure&#58; Good Example - The repeated code has been refactored into its own method.</div>
<p><strong>Tip&#58; </strong>The Refactor menu in Visual Studio 11 can do this refactoring for you.</p>
<img alt="vs_refactor_extract.png" src="/PublishingImages/vs_refactor_extract.png" class="ms-rteCustom-ImageArea" />
<span class="ssw-rteStyle-FigureNormal">Figure&#58; The Extract Method function in Visual Studio's Refactor menu.</span>


