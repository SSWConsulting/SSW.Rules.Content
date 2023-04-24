---
type: rule
title: Do you know to not include UNC paths in URLs?
uri: urls-must-not-have-unc-paths
authors:
  - title: Adam Cogan
    url: https://www.ssw.com.au/people/adam-cogan
created: 2023-04-24T17:31:09.524Z
guid: f829d830-0b31-45f4-a39f-1ee8b1efec18

---

UNC (Uniform Naming Convention) is a naming system used in Microsoft Windows operating systems to specify the location of a file or folder on a shared network resource. However, UNC paths should not be used in URLs as they are typically used to specify file paths on a local network rather than web resources.

<!--endintro-->

In a URL, the path component specifies the path to the resource on the web server, and it is relative to the server's document root directory. While it may be possible to include a UNC path in a URL, doing so would likely result in an error, as web servers are not designed to handle UNC paths. 

An example of a UNC path is:

``` html
\\server\share\folder\file.txt
```

Additionally, including a UNC path in a URL could be a security risk, as it could potentially expose sensitive information about the server's network configuration. Therefore, you should not include UNC paths in URLs.
