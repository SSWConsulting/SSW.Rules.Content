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
   Insert Pic 3
2. Select New policy | Create new policy
   Insert Pic 4
3. Select Cloud apps or actions | Select All cloud apps
   Insert Pic 5
4. Select Conditions | Locations 
   Then set configure to yes and Include to "Any location"
5. On exclude