---
type: rule
archivedreason: 
title: Do you know to do data you need CAML?
guid: 81609e41-a911-4a99-9f54-fdaa2fb4a374
uri: do-you-know-to-do-data-you-need-caml
created: 2009-05-21T23:18:19.0000000Z
authors:
- title: John Liu
  url: https://ssw.com.au/people/john-liu
- title: Jay Lin
  url: https://ssw.com.au/people/jay-lin
related: []
redirects: []

---

CAML is the XML definition for all things in SharePoint, in deployment, and in creating templates, CAML is the only format.
In SharePoint development, you will also need to know CAML, in particular, how to write a query in CAML.

* Widely used in Content Query Web Parts
* Also used in SharePoint content reports
* In code, used by SPSiteDataQuery object



[Introduction to Collaborative Application Markup Language (CAML)](http://msdn.microsoft.com/en-us/library/ms426449.aspx)
 


[Query Schema](http://msdn.microsoft.com/en-us/library/ms467521.aspx)




<!--endintro-->




```
<query>
    <orderby>
        <fieldref name="Modified" ascending="FALSE"></fieldref>
    </orderby>
    <where>
        <and>
            <neq>
                <fieldref name="Status"></fieldref>
                <value type="Text">Completed</value>
            </neq>
            <isnull>
                <fieldref name="Sent"></fieldref>
            </isnull>
        </and>
    </where>
</query>
```

          Figure: Example of CAML query   
You can see - CAML is essentially the same as SQL WHERE syntax, but wrapped in an XML format.

Problems with CAML:

1. CAML is XML and is case sensitive – including attributes names.         
        <pre>&lt;Query&gt;
    &lt;Where&gt;
        &lt;Or&gt;
            &lt;Eq&gt;
              &lt;FieldRef <font color="#400040" style="background-color:rgb(255, 255, 0);">name</font>="Status" /&gt; 
            &lt;Value Type="Text"&gt;Completed&lt;/Value&gt;
            &lt;/Eq&gt;
            &lt;IsNull&gt;
                &lt;FieldRef <font style="background-color:rgb(255, 255, 0);">Name</font>="Status" /&gt;
            &lt;/IsNull&gt;
        &lt;/Or&gt;
    &lt;/Where&gt;
&lt;/Query&gt;</pre>
        
        <dd>     Figure: Example of CAML query </dd>
    
2. SharePoint is not good at telling you if you made a mistake with your CAML query.         

::: bad  
![Figure: Debug error message](CAMLError.png)  
:::

        
    
3. Hard to debug.
<font color="#ff0000">Tips:</font> Use 3rd Party tools - U2U CAML Query Builder
            

::: good  
![Figure: U2U CAML Query Builder](U2U.png)  
:::

        
    <font color="#ff0000">Note:</font> U2U CAML Builder is the best tool that we have. There are some occasional UI and interface issues, but for creating CAML and testing it against live SharePoint lists it gets the job done. And it’s FREE!
