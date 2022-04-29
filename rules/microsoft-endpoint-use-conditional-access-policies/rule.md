---
type: rule
title: Do you use conditional access policies?
uri: microsoft-endpoint-use-conditional-access-policies
authors:
  - title: Warwick Leahy
created: 2022-04-13T01:19:59.907Z
guid: deadd754-b7c5-4564-8e44-234642690769
---
Did you know that you can stop your users from logging into any of your Azure or Office365 resources based on the location they are in?  What about the types of devices that they can connect from or only allowing connections that use MFA? These things are all possible to restrict.

This seriously limits the attack surface and also helps to stop compromised devices and accounts from being used.

<!--endintro-->

::: bad 

![Figure: Bad example no locations setup](locationsbadexample.png)

:::

## Configure locations

First you need to add any locations that you require for an office. 

1. Go to https://endpoint.microsoft.com | Endpoint security | Conditional Access | Named locations
2. Click "+ Countries location and add required countries

   ![Figure: Add a location](locations1.png)
3. Add as many as you require for your users to access

   ![Figure: Every location that your users work from](locationsadded.png)

## Configure policies

Now configure some policies to implement these rules

1. Go to Go to https://endpoint.microsoft.com | Endpoint security | Conditional Access | Policies
2. Select New policy | Create new policy

   ![Figure: Add a conditional access policy](conditionalaccess2.png)
3. Give it a name then select Cloud apps or actions | Select All cloud apps

   ![Figure: Add all cloud apps](conditionalaccess3.png)
4. Select Conditions | Locations 
   Then set configure to yes and Include to "Any location"

   ![Figure: Choose any location](conditionalaccess4.png)
5. On Exclude choose Selected locations and then exclude your workers countries (i.e. Australia) 

 **Note this must be done this way as the user must not meet a block access rule ever if they are to login**

![Figure: Exclude good locations](conditionalaccess5.png)

6. Now select block access for this rule

   ![Figure: Block access](conditionalaccess6.png)

   ## Create a grant rule
7. Similarly create a rule that applies to all cloud apps as above
8. This will be exactly the same as the above rule except that you should not have conditions and should Grant access with MFA

   ![Figure: Add a grant with MFA](conditionalaccess7.png)