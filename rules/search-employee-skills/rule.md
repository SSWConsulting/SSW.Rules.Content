---
type: rule
title: Do you know how to search employee skills? (Extending AD vs SharePoint vs
  Dynamics 365 CRM)
uri: search-employee-skills
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
  - title: Jean Thirion
    url: https://ssw.com.au/people/jean-thirion
  - title: Piers Sinclair
    url: https://ssw.com.au/people/piers-sinclair
related:
  - do-you-know-what-are-the-sharepoint-features-our-customers-love
redirects:
  - extending-AD
created: 2021-07-30T05:06:33.000Z
archivedreason: null
guid: d641a712-b67f-40dc-8251-4b933afb487a
---
`youtube: https://www.youtube.com/watch?v=fhnatho4nSg`

AD has all your users e.g. Bob, Mary, Jane...

SharePoint also has all your users, plus you can extend this information using the UserProfile Service – https://docs.microsoft.com/en-us/sharepoint/manage-user-profiles

The beauty of this is that if everyone has updated their skills, it is wonderfully searchable.

<!--endintro-->

![Figure: SharePoint People Search – Notice the Skills coming from UserProfile Service (aka UPS)](extending-ad-1.png)

![Figure: Mockup - Improved SharePoint People Search Results](mockup-extending-ad-3.jpg)

SharePoint has an Admin UI to manage User Profiles

![Figure: User Profile UI in your SharePoint Admin Centre – generally this is not needed the Delve out of the box experience works for your organisation](extending-ad-2.png)

[Delve](https://support.microsoft.com/en-us/office/what-is-delve-1315665a-c6af-4409-a28d-49f8916878ca) is a cool product with a nice UI that is essentially a portal onto the User Profiles.

![Figure: Delve profile – Click on “Update Profile” to write data back to SharePoint User Profile Service](extending-ad-3.png)

Where it all falls down...

What if your people’s skills are stored in another system such as Dynamics 365 CRM or Salesforce ?

![Figure: People’s skills are often stored in Dynamics 365 CRM or Salesforce](extending-ad-4.png)

You can use PowerShell and SharePoint PNP libraries to programmatically interact with the SharePoint UserProfile service. This process allows you to sync skills across systems with a custom solution:

![Figure: Powershell - Reading skills from UserProfile](extending-ad-5.png)

![Figure: Powershell - Adding “Blazor” to Jean’s skill list](extending-ad-6.png)

OpenSearch is another solution, using the OpenSearch protocol you can [add external data sources to your SharePoint search results](https://docs.microsoft.com/en-us/sharepoint/search/understanding-result-sources-for-search)

#### Suggestions to Microsoft:

**#1 Help me better sync my Dynamics 365 CRM data with the SharePoint user profile service**

This should be a simple SharePoint connector so this piece of PowerShell glue is not required 👌\
E.g. CRM user skills to User Profile properties

**#2 Help me make Dynamics 365 CRM data searchable from SharePoint search**

If not using a connector, we should be able to easily index and search through Dynamics 365 CRM data.
This is essentially just calling a different API.

**#3 Help me customise SharePoint search results**

If you don’t want either of those options (i.e. you users’ skills are stored somewhere else), we should be able to change the search results UI.\
E.g. Search for people here: https://ssw.com.au/people

![Figure: The SharePoint Search should let you add links like in this image](sharepointuxforpeopleandbookedindays.png)

**[\#4 Help me search for user entities in Dynamics 365 CRM](https://experience.dynamics.com/ideas/idea/?ideaid=b5daa141-90f5-eb11-ba5e-0003ff457d0a)**

There should be a global user search that goes across all entities in Dynamics 365 CRM.

![Figure: Searching User + Skill doesn’t yield any result although this skill is associated to the user](extending-ad-7.png)
