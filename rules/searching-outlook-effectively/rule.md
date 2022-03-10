---
type: rule
title: Do you know how to search Outlook effectively?
uri: searching-outlook-effectively
authors:
  - title: Ulysses Maclaren
  - title: Piers Sinclair
    url: https://www.ssw.com.au/people/piers-sinclair
created: 2022-03-09T05:28:52.197Z
guid: 77ea51b9-baf8-46c2-9f8a-47f1c07fddc6
---
Some people are really good at using Outlook search to find the emails they need, while others have a hard time. Searching for emails can be a real struggle, sometimes you want to find emails from months ago but you aren't sure exactly what to search for.\
\
Being able to find an email quickly in Outlook is an important skill. So I want to share some tips and tricks I have picked up about how to find that email buried in your inbox...

Note: These tips will also help you in your Google/Bing searches too.  

<!--endintro-->

Let's take an example scenario and see what tips we can use to search. Last month, you got an email in your inbox from your manager Bob about making changes to how you see data in his Northwind website.

### Tip 1: Giving the person I’m talking to focus

You know Bob sent the email, and that it's in your inbox. So the best thing to do first is to limit outlook to only your inbox folder and only emails from Bob. So while in your inbox:

* Change the folder to "Current Folder"
* Search for:

```
from:Bob
```

Note: You can change the folder scoping to fit your specific needs

![Figure: There are several scoping options available](search-scope.png)

### Tip 2: Focus on the person (i.e. to: from: cc: bcc:)

There are many different ways to focus on people. If know that the email was sent to Adam, from Bob, Luke was CCed and Chris was BCCed then:

* Search for:

```
to:Adam from:Bob cc:Luke bcc:Chris
```

### Tip 3: Focus on the subject (i.e. subject:)

If you have a good idea of what the email subject contains, then the "subject:" scope can help a lot. For example, if you know that the email had Northwind and Bob in the subject then:

* Search for:

```
"Subject: Northwind Bob"
```

### Tip 4: Use negatives (i.e. –)

Negatives are a great way to remove results you know definitely won't be relevant. For example, if you know Luke and Adam frequently work with Bob but weren't involved in that email then:

* Search for: 

```
-Luke - Adam
```

Note: Start with a broad search, and then, when you start seeing irrelevant results about invoicing, add -invoice to your search

### Tip 5: Use quotation marks (i.e. “”)

You can search for a direct match in an email using quotation marks. For example, if you know that "days outstanding" was written in the email then:

* Search for:

```
"days outstanding"
```

Note: Particularly useful when using common words but you know they were written in an exact phrase. E.g. “on top of this”

### Tip 6: Combine 2 searches into 1 (i.e. OR)

Sometimes you might know a specific thing was referred to, but aren't sure what terminology was used. For example, let's say you know the email mentioned either "web app" or "website". In that case:

* Search for:

```
"web app" OR website
```

Note: Must be upper case... lowercase “or” won’t work

### Tip 7: Find a file (i.e. hasattachments:yes)

Emails can be filtered to only include ones with attachments. If you know the email has an attachment then:

* Search for:

```
hasattachments:yes
```

### Tip 8: Find a file’s content (i.e. attachment:)

File contents can also be searched. If you know that there was an attachment that contained the text "20/07/2021" then:

* Search for:

```
attachment:"20/07/2021"
```

### Tip 9: Focus on the date received (i.e. received=<>)

You can filter on a specific time period or date. For example, If you know that the email was received after 07/20/2019 then:

* Search for:

```
received>"07/20/2019"
```

Note: Outlook has a heap of other properties that you can filter on.

![Figure: Outlook has a lot of meta data filtering options](email-metadata.png)

**Learn more:** [How to search in Outlook](https://support.microsoft.com/en-us/office/how-to-search-in-outlook-d824d1e9-a255-4c8a-8553-276fb895a8da).