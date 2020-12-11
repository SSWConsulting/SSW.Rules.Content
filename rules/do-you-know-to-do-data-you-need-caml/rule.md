---
type: rule
archivedreason: 
title: Do you know to do data you need CAML?
guid: 81609e41-a911-4a99-9f54-fdaa2fb4a374
uri: do-you-know-to-do-data-you-need-caml
created: 2009-05-21T23:18:19.0000000Z
authors:
- id: 8
  title: John Liu
- id: 18
  title: Jay Lin
related: []

---

CAML is the XML definition for all things in SharePoint, in deployment, and in creating templates, CAML is the only format.
In SharePoint development, you will also need to know CAML, in particular, how to write a query in CAML.

* Widely used in Content Query Web Parts
* Also used in SharePoint content reports
* In code, used by SPSiteDataQuery object



[Introduction to Collaborative Application Markup Language (CAML)](http://msdn.microsoft.com/en-us/library/ms426449.aspx)
 


[Query Schema](http://msdn.microsoft.com/en-us/library/ms467521.aspx)




<!--endintro-->


<dl class="goodCode">    &lt;dt&gt;
    <pre><query><br>    <orderby><br>        <fieldref name="Modified" ascending="FALSE"></fieldref><br>    </orderby><br>    <where><br>        <and><br>            <neq><br>                <fieldref name="Status"></fieldref><br>                <value type="Text">Completed</value><br>            </neq><br>            <isnull><br>                <fieldref name="Sent"></fieldref><br>            </isnull><br>        </and><br>    </where><br></query></pre>
    &lt;/dt&gt;
    <dd>Figure: Example of CAML query </dd></dl>
You can see - CAML is essentially the same as SQL WHERE syntax, but wrapped in an XML format.

Problems with CAML:

1. CAML is XML and is case sensitive – including attributes names. <dl class="badCode">        &lt;dt&gt;
        <pre><query><br>    <where><br>        <or><br>            <eq><br>              <fieldref></fieldref><font color="#400040" style="background-color:rgb(255, 255, 0);">name</font>="Status" /> <br>            <value type="Text">Completed</value><br>            </eq><br>            <isnull><br>                <fieldref></fieldref><font style="background-color:rgb(255, 255, 0);">Name</font>="Status" /><br>            </isnull><br>        </or><br>    </where><br></query></pre>
        &lt;/dt&gt;
        <dd>     Figure: Example of CAML query </dd>
    </dl>
2. SharePoint is not good at telling you if you made a mistake with your CAML query. <dl class="badImage">        &lt;dt&gt;<img src="CAMLError.png" alt=""> &lt;/dt&gt;
        <dd>     Figure: Debug error message</dd>
    </dl>
3. Hard to debug.
<font color="#ff0000">Tips:</font> Use 3rd Party tools - U2U CAML Query Builder<br>    <dl class="goodImage">        &lt;dt&gt;<img src="U2U.png" alt=""> &lt;/dt&gt;
        <dd>     Figure: U2U CAML Query Builder</dd>
    </dl><font color="#ff0000">Note:</font> U2U CAML Builder is the best tool that we have. There are some occasional UI and interface issues, but for creating CAML and testing it against live SharePoint lists it gets the job done. And it’s FREE!
