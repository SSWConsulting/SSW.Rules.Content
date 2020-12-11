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

When designing custom applications you want to include branding on reports.                      You should always include a useful and informative footer at the bottom of your reports.

<!--endintro-->

Include:

1. Date and Time Printed and User who printed it - see warning below (e.g. Printed by SSW2000\JatinValabjee on 3/1/2006 3:16:30 PM)
2. Execution Time (e.g. Execution time: 1 minute, 10 seconds)
3. Page x of y (e.g. Page 3 of 10)
4. Link to company website + slogan  (e.g. www.ssw.com.au - Writing software people understand)



![](RSRulesBadFooter.gif)
 


::: bad
Bad Example - This footer doesn't provide any useful information
:::





![](RSRulesGoodFooter.gif)


::: good
Good Example - Useful and informative information should be displayed in your report footer
:::



 

Use these handy report expressions to show the above information.

**NOTE:** Do not use System.DateTime.Now for your Execution Time because if you do it will return the result at time of printing the document/PDF.  Instead store the value in a variable (for example GroupExecutionTime) and then call that.


| Footer Item | Expression | Sample Output |
| --- | --- | --- |
| Date and Time Printed / User ID | ="Printed by " + User!UserID + " on " + <br>                            Globals!ExecutionTime.ToString() | Printed by SSW2000\JatinValabjee on 3/1/2006 3:16:30 PM |
| Execution Time |                             ="Execution Time: " +<br><br>                            IIf((Variables!GroupExecutionTime.Value.Subtract(Globals!ExecutionTime).TotalSeconds < 1, "0 <br>                            seconds",<br>                            <br><br>                            (<br><br>                            IIf((Variables!GroupExecutionTime.Value.Subtract(Globals!ExecutionTime).Hours > 0, (Variables!GroupExecutionTime.Value.Subtract(Globals!ExecutionTime).Hours & " hour(s), ", "") +<br><br>                            IIf((Variables!GroupExecutionTime.Value.Subtract(Globals!ExecutionTime).Minutes > 0, (Variables!GroupExecutionTime.Value.Subtract(Globals!ExecutionTime).Minutes & " minute(s), ", <br>                            "") +<br><br>                            IIf((Variables!GroupExecutionTime.Value.Subtract(Globals!ExecutionTime).Seconds > 0, (Variables!GroupExecutionTime.Value.Subtract(Globals!ExecutionTime).Seconds & " second(s)", ""))<br><br>                            )<br>                         | Execution time: 1 minute, 10 seconds |
| Page x of y<br>                         |                             ="Page " + Globals!PageNumber.ToString() + " of " + <br>                            Globals!TotalPages.ToString() |                             Page 3 of 10 |






![](footerInDesigner.gif)


::: good
Good Example - Footer in visual studio designer
:::



 

**Warning:** Adding the User who printed it stops all data-driven subscriptions     
When you try to add the User your data-driven subscriptions will fail with the following error:
'The '/GroupHealth' report has user profile dependencies and cannot be run unattended. (rsHasUserProfileDependencies)'.     
A quick workaround is to add a user function to fallback the error to a nice message, like: "SYSTEM",


::: greybox

:::


 Public Function UserName()


> Try
> 
> 
> > Return Report.User!UserID
> 
> 
> Catch
> 
> 
> 
> > Return "System"
> 
> 
> End Try


End Function <br>   

Use above function to replace your reference to Report.User!UserID will allow the subscription to work correctly.
