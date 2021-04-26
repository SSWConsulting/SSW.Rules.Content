---
type: rule
archivedreason: IE7 is no longer supported
title: Do you avoid using "inherit" value of style.display?
guid: a99dd941-f70a-4aa6-8526-fd2ee1b547c7
uri: do-you-avoid-using-inherit-value-of-style-display
created: 2010-12-02T10:35:22.0000000Z
authors: []
related: []
redirects:
- do-you-avoid-using-＂inherit＂-value-of-style-display

---

The property value “inherit” of style.display is not recognized by IE7 and IE7 compatibility mode. So if you use this value in Javascript, it will cause script error in IE7 and IE7 compatibility like: 
             "Message: Could not get the display property. Invalid argument." 
 So to make your Javascript and CSS style more compatible and avoid using "inherit" value of style.display:  
<!--endintro-->


```
divLoading.style.display = "inherit";
```

          Bad code - inherit property             

```
divLoading.style.display = "block";
```

          Good code - block property
