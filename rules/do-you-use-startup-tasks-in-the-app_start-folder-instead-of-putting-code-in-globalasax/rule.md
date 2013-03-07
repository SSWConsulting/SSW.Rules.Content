---
type: rule
title: Do you use startup tasks in the ~/App_Start folder instead of putting code in Global.asax?
uri: do-you-use-startup-tasks-in-the-app_start-folder-instead-of-putting-code-in-globalasax
created: 2013-03-07T18:37:31.0000000Z
authors:
- id: 23
  title: Damian Brady

---



<span class='intro'> <p>Adding code to the Application_Start method in the Global.asax file is the easiest and most straight-forward approach for executing startup logic, however this code should be encapsulated in static methods outside the Global.asax file.  Doing this helps provide cleaner code and encourages proper adherence to the Single Responsibility principle.</p> </span>

<dl class="badImage"><dt><div class="greyBox"><pre>public class MvcApplication &#58; System.Web.HttpApplication
&#123;
    protected void Application_Start()
    &#123;
        AreaRegistration.RegisterAllAreas();

        routes.IgnoreRoute(&quot;&#123;resource&#125;.axd/&#123;*pathInfo&#125;&quot;);

        routes.MapRoute(
            name&#58; &quot;Default&quot;,
            url&#58; &quot;&#123;controller&#125;/&#123;action&#125;/&#123;id&#125;&quot;,
            defaults&#58; new &#123; controller = &quot;Home&quot;, action = &quot;Index&quot;, id = UrlParameter.Optional &#125;
        );        &#125;
&#125;

</pre></div></dt><dd>Figure&#58; Bad Example – Logic is implemented in the Application_Start method which breaks the Single Responsibility Principle</dd></dl><dl class="goodImage"><dt><div class="greyBox"><pre>public class MvcApplication &#58; System.Web.HttpApplication
&#123;
    protected void Application_Start()
    &#123;
        AreaRegistration.RegisterAllAreas();

        WebApiConfig.Register(GlobalConfiguration.Configuration);
        FilterConfig.RegisterGlobalFilters(GlobalFilters.Filters);
        RouteConfig.RegisterRoutes(RouteTable.Routes);
        BundleConfig.RegisterBundles(BundleTable.Bundles);
        AuthConfig.RegisterAuth();
    &#125;
&#125;
</pre></div><br>
      <img src="/PublishingImages/startup-task.jpg" alt="" />
   </dt><dd>Figure&#58; Good Example – Startup tasks are called from the Application_Start method but are located in the App_Start folder</dd></dl><p>
   <strong>Note&#58;</strong> You can also use the 
   <a href="http&#58;//nuget.org/packages/WebActivator/">WebActivator Nuget package</a> to avoid putting any code in your Global.asax at all.&#160; This is particularly useful for creating your own Nuget packages that need to execute code on startup of the application.</p>


