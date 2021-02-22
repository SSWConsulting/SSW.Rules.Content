---
type: rule
archivedreason: 
title: Do you look for duplicate code?
guid: 2c1f0b48-dc84-48ac-8255-0ffb0e4821d6
uri: do-you-look-for-duplicate-code
created: 2012-04-01T09:56:14.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: Damian Brady
  url: https://ssw.com.au/people/damian-brady
related: []
redirects: []

---


<span lang="EN-AU" style="font-family:calibri, sans-serif;font-size:11pt;">Code duplication is a big "code smell" that harms maintainability.  You should keep an eye out for repeated code and make sure you refactor it into a single place.</span>
<br><excerpt class='endintro'></excerpt><br>
<p>For example, have a look at these two Action methods in an MVC 4 controller.</p>
<span class="ssw-rteStyle-CodeArea"><pre>//
// GET: /Person/
[Authorize]
public ActionResult Index()
{
<span style="background-color:rgb(255, 255, 0);">    // get company this user can view
    Company company = null;
    var currentUser = Session["CurrentUser"] as User;
    if (currentUser != null)
    {
        company = currentUser.Company;
    }
</span>
    // show people in that company
    if (company != null)
    {
        var people = db.People.Where(p =&gt; p.Company == company);
        return View(people);
    }
    else
    {
        return View(new List());
    }
}

//
// GET: /Person/Details/5
[Authorize]
public ActionResult Details(int id = 0)
{
<span style="background-color:rgb(255, 255, 0);">    // get company this user can view
    Company company = null;
    var currentUser = Session["CurrentUser"] as User;
    if (currentUser != null)
    {
        company = currentUser.Company;
    }
</span>
    // get matching person
    Person person = db.People.Find(id);
    if (person == null || person.Company == company)
    {
        return HttpNotFound();
    }
    return View(person);
}
</pre></span><div class="ssw-rteStyle-FigureBad">Figure: Bad Example - The highlighted code is repeated and represents a potential maintenance issue.</div>
<p>We can refactor this code to make sure the repeated lines are only in one place.</p>
<span class="ssw-rteStyle-CodeArea"><pre><span style="background-color:rgb(255, 255, 0);">private Company GetCurrentUserCompany()
{
    // get company this user can view
    Company company = null;
    var currentUser = Session["CurrentUser"] as User;
    if (currentUser != null)
    {
        company = currentUser.Company;
    }
    return company;
}
</span>
//
// GET: /Person/
[Authorize]
public ActionResult Index()
{
    // get company this user can view
    <span style="background-color:rgb(255, 255, 0);">Company company = GetCurrentUserCompany();
</span>
    // show people in that company
    if (company != null)
    {
        var people = db.People.Where(p =&gt; p.Company == company);
        return View(people);
    }
    else
    {
        return View(new List());
    }
}


// GET: /Person/Details/5
[Authorize]
public ActionResult Details(int id = 0)
{
    // get company this user can view
    <span style="background-color:rgb(255, 255, 0);">Company company = Ge</span><span style="background-color:rgb(255, 255, 0);"></span><span style="background-color:rgb(255, 255, 0);">tCurrentUserCompany();
</span>
    // get matching person
    Person person = db.People.Find(id);
    if (person == null || person.Company == company)
    {
        return HttpNotFound();
    }
    return View(person);
}
</pre></span><div class="ssw-rteStyle-FigureGood">Figure: Good Example - The repeated code has been refactored into its own method.</div>
<p><strong>Tip: </strong>The Refactor menu in Visual Studio 11 can do this refactoring for you.</p>
<img alt="vs_refactor_extract.png" src="vs_refactor_extract.png" class="ms-rteCustom-ImageArea" />
<span class="ssw-rteStyle-FigureNormal">Figure: The Extract Method function in Visual Studio's Refactor menu.</span>


