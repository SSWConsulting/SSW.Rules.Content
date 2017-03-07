---
type: rule
archivedreason: 
title: Reports - Do you have a standard Report footer?
guid: 12e2004d-f293-418f-bb64-427cb37e3b18
uri: reports---do-you-have-a-standard-report-footer
created: 2014-12-01T05:46:16.0000000Z
authors: []
related: []

---


<p>When designing custom applications you want to include branding on reports. 
                    You should always include a useful and informative footer at the bottom of your reports.<br></p>
<br><excerpt class='endintro'></excerpt><br>
<div>Include&#58;</div><ol><li>​​Date and Time Printed and User who printed it - see warning below (e.g. Printed by SSW2000\JatinValabjee on 3/1/2006 3&#58;16&#58;30 PM)<br></li><li>Execution Time (e.g. Execution time&#58; 1 minute, 10 seconds)<br></li><li>Page x of y (e.g. Page 3 of 10)<br></li><li>Link to company website + slogan&#160; (e.g. www.ssw.com.au - Writing software people understand)<br></li></ol><div>
   <img alt="RSRulesBadFooter.gif" src="/SiteAssets/reports-do-you-have-a-standard-report-footer/RSRulesBadFooter.gif" style="margin&#58;5px;" />
   <br>&#160;</div><dd class="ssw15-rteElement-FigureBad">Bad Example - This footer doesn't provide any useful information </dd><p>
   <br>&#160;</p><p>
   <img alt="RSRulesGoodFooter.gif" src="/SiteAssets/reports-do-you-have-a-standard-report-footer/RSRulesGoodFooter.gif" style="margin&#58;5px;" />&#160;</p><dd class="ssw15-rteElement-FigureGood">Good Example - Useful and informative information should be displayed in your report footer</dd><div class="ssw15-rteElement-FigureGood">
   <br>&#160;</div><p>Use these handy report expressions to show the above information.</p><p><strong>NOTE&#58;</strong> Do not&#160;use System.DateTime.Now​ for your Execution Time because if you do it will return the result at time of printing the document/PDF.&#160; Instead store the value in a variable (for example GroupExecutionTime) and then call that.<br><br></p><table class="clsSSWTable" border="0" cellspacing="0" cellpadding="5"><tbody><tr><th>Footer Item</th><th>Expression</th><th>Sample Output</th></tr><tr><td valign="top">Date and Time Printed / User ID</td><td valign="top">=&quot;Printed by &quot; + User!UserID + &quot; on &quot; + 
                            Globals!ExecutionTime.ToString()</td><td valign="top">Printed by SSW2000\JatinValabjee on 3/1/2006 3&#58;16&#58;30 PM</td></tr><tr style="background-color&#58;white;"><td valign="top">Execution Time</td><td valign="top">
                            =&quot;Execution Time&#58; &quot; +<br>
                            IIf((Variables!GroupExecutionTime.Value.Subtract(Globals!ExecutionTime).TotalSeconds &lt; 1, &quot;0 
                            seconds&quot;,
                            <br>
                            (<br>
                            IIf((Variables!GroupExecutionTime.Value.Subtract(Globals!ExecutionTime).Hours &gt; 0, (Variables!GroupExecutionTime.Value.Subtract(Globals!ExecutionTime).Hours &amp; &quot; hour(s), &quot;, &quot;&quot;) +<br>
                            IIf((Variables!GroupExecutionTime.Value.Subtract(Globals!ExecutionTime).Minutes &gt; 0, (Variables!GroupExecutionTime.Value.Subtract(Globals!ExecutionTime).Minutes &amp; &quot; minute(s), &quot;, 
                            &quot;&quot;) +<br>
                            IIf((Variables!GroupExecutionTime.Value.Subtract(Globals!ExecutionTime).Seconds &gt; 0, (Variables!GroupExecutionTime.Value.Subtract(Globals!ExecutionTime).Seconds &amp; &quot; second(s)&quot;, &quot;&quot;))<br>
                            )
                        </td><td valign="top">Execution time&#58; 1 minute, 10 seconds</td></tr><tr><td valign="top">
                            Page x of y
                        </td><td valign="top">
                            =&quot;Page &quot; + Globals!PageNumber.ToString() + &quot; of &quot; + 
                            Globals!TotalPages.ToString()</td><td valign="top">
                            Page 3 of 10</td></tr></tbody></table>​​​
<br><p></p><p><img alt="footerInDesigner.gif" src="/SiteAssets/reports-do-you-have-a-standard-report-footer/footerInDesigner.gif" style="margin&#58;5px;" /><br>&#160;</p><dd class="ssw15-rteElement-FigureGood">Good Example - Footer in visual studio designer</dd><div><br>&#160;</div><p><br><strong>Warning&#58;</strong> Adding the User who printed it stops all data-driven subscriptions 
   <br>When you try to add the User your data-driven subscriptions will fail with the following error&#58;<br>'The '/GroupHealth' report has user profile dependencies and cannot be run unattended. (rsHasUserProfileDependencies)'. 
   <br>A quick workaround is to add a user function to fallback the error to a nice message, like&#58; &quot;SYSTEM&quot;, 
   </p><p class="ssw15-rteElement-GreyBox"><div dir="ltr"> Public Function UserName()</div><blockquote dir="ltr" style="margin-right&#58;0px;"><div>Try</div><blockquote dir="ltr" style="margin-right&#58;0px;"><div>Return Report.User!UserID</div></blockquote><div dir="ltr">Catch<br></div><blockquote dir="ltr" style="margin-right&#58;0px;"><div dir="ltr">Return &quot;System&quot;<br> </div></blockquote><div dir="ltr">End Try</div></blockquote><div dir="ltr">End Function 
&#160;&#160; </div></p><p>
   <br>Use above function to replace your reference to Report.User!UserID will allow the subscription to work correctly. 
   <br></p>


