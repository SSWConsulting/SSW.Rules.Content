---
type: rule
title: Do you know what is broken in workflow?
uri: do-you-know-what-is-broken-in-workflow
created: 2009-06-16T01:59:00.0000000Z
authors:
- id: 8
  title: John Liu
- id: 18
  title: Jay Lin

---



<span class='intro'> 
  <p>
    <span lang="EN-US">SharePoint comes with some very basic workflows out of the box.&#160; A particular example is the content approval workflow.</span>
  </p>
<p><span lang="EN-US"></span><span lang="EN-US"><span lang="EN-US">When a content approval workflow is used, it modifies the process of publishing content to be&#58;</span>
</span></p>
<ol>
    <li><span lang="EN-US">User clicks publish (click 1)</span> </li>
    <li><span lang="EN-US">Workflow starts, and asks the user to request for approval, there’s an option to add additional messages (click 2)</span> </li>
    <li><span lang="EN-US">The workflow sends an email to the user to tell him an approval workflow has started. (email 1)</span> </li>
    <li><span lang="EN-US">The workflow also sends an email to the approver(s) (email 2)</span> </li>
    <li><span lang="EN-US">The approver receives an email, then returns to the page – they can Approve or Reject the workflow. (click 3)</span> </li>
    <li><span lang="EN-US">Either way, a new workflow screen appears, with an option to add additional messages, the approver clicks accept (click 4)</span> </li>
    <li><span lang="EN-US">The approval workflow completes and publishes the page.&#160; </span></li>
    <li><span lang="EN-US">It then sends an email telling the user that an approval workflow has been completed (email 3).</span></li>
</ol>
<p><span lang="EN-US"></span><span lang="EN-US">What is the problem?</span></p>
<p class="MsoNormal"><span lang="EN-US">The out of the box workflow is extremely generic.&#160; It has no customizations or shortcuts.&#160; Even if you are an approver, you cannot skip any of the steps.&#160; The end result is that you will have to click 4 times and receive 3 emails, for approving your own finalized content.</span><span lang="EN-US">
</span></p>
<p class="MsoNormal"><span lang="EN-US">These kind of workflows are designed generic to fit any business’ needs – and in fact, businesses using these out of the box workflows have to adjust their staff’s workflow to match SharePoint’s ones.&#160; Which can be counter intuitive.</span></p>
<p></p>
<p></p>
 </span>


  <p class="MsoNormal">
    <span lang="EN-US">We think these SharePoint workflows need to be far more customizable.</span>
    <span lang="EN-US">&#160;</span>
  </p>
<p class="MsoNormal"><span lang="EN-US"></span><span lang="EN-US" style="font-family&#58;&quot;calibri&quot;,&quot;sans-serif&quot;;font-size&#58;11pt;">SharePoint does not provide support for complex reusable workflows easily - most companies go for a 3rd party solution&#58;</span></p>
<dl class="image">
    <dt><img src="/PublishingImages/Blackpearl.png" alt="" /> </dt>
    <dd>Figure&#58; 3rd party tool - Blackpearl
    <dl class="image">
        <dt><img src="/PublishingImages/Ninetex.png" alt="" /> </dt>
        <dd>Figure&#58; 3rd party tool - Nintex </dd>
    </dl>
    </dd>
</dl>



