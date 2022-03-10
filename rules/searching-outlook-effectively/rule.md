---
type: rule
title: Do you know how to search effectively in Outlook?
uri: searching-outlook-effectively
authors:
  - title: Ulysses Maclaren
created: 2022-03-09T05:28:52.197Z
guid: 77ea51b9-baf8-46c2-9f8a-47f1c07fddc6
---
Being able to find an email quickly in Outlook is an important skill, and many of the following techniques will also help you in your Google/Bing searches too.  

<!--endintro-->

Let's take an example scenario and see what tips we can use to search. Last month, you got an email in your inbox from your manager Bob about making changes to how you see data in his Northwind App.

### Tip 1: Giving the person I’m talking to focus

You know Bob sent the email, and that it's in your inbox. So the best things to do first is to limit outlook to only your inbox folder and only emails from Bob. So while in your inbox:

* Change the folder to "Current Folder"
* Search for:
```
From:Bob
```
### Tip 2: Focus on the person (i.e. to: from: cc: bcc:)

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

### Tip 5: Use quotation marks (i.e. “”)

You can search for a direct match in an email using quotation marks. For example, if you know that "days outstanding" was written in the email then:

* Search for:
```
"days outstanding"
```

### Tip 6: Combine 2 searches into 1 (i.e. OR)

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
Dates are a useful way to filter. If you know that an email was received after 07/20/2019 then:

* Search for:
```
received>"07/20/2019"
```
