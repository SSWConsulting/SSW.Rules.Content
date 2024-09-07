---
seoDescription: Use Gravatar to simplify profile management and provide a consistent experience across applications, as it allows your Gravatar image to follow you from site to site.
type: rule
title: Do you use Gravatar (or Cravatar for China) for your profile pictures?
uri: do-you-use-gravatar-for-your-profile-pictures
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
related: []
redirects: []
created: 2015-03-16T10:17:40.000Z
archivedreason: null
guid: b790dbfc-fe37-4a4a-992e-c9294620a06b
---

To keep profile management simple and make it easier for users to have a consistent experience across applications, you should use [Gravatar](https://en.gravatar.com/) for showing profile images in your application.

::: china
Gravatar is blocked by Great Firewall of China (GFW), and clients from China can't access their profile photos successfully without a VPN. There is an alternative option for Chinese users which is [Cravatar](https://cravatar.cn/).
:::

Your Gravatar or Cravatar is an image that follows you from site to site appearing beside your name when you do things like comment or post on a blog.

<!--endintro-->

### Setting up Gravatar in your application

It is simple to set up and if you are developing an MVC application, there are even several Nuget packages to make your life easier. The [GravatarHelper](https://www.nuget.org/packages/GravatarHelper) is recommended.

```aspnet
@Html.GravatarImage("MyEmailAddress@example.com", 80, new { Title = "My Gravatar", Alt = "Gravatar" })
```

Also, check out the [Gravatar API documentation](https://en.gravatar.com/site/implement/images/) for all the options available.

The below short video shows how to get up and running with Gravatar in your ASP.NET MVC application.

`youtube: https://www.youtube.com/embed/rjFjVD9jPIk`

### Setting up Cravatar in your application

Unlike Gravatar, Cravatar doesn't provide any library to generate profile image. To solve this issue we can create custom helper class which creates profile URL for us.

```
public static class CravatarHelper
{
    private const int MIN_IMAGE_SIZE = 1;
    private const int MAX_IMAGE_SIZE = 2048;
    private const string WEBSITE = "https://cravatar.cn/avatar/";

    private static int ValidateImageSize(int imageSize)
    {
        imageSize = Math.Max(imageSize, MIN_IMAGE_SIZE);
        imageSize = Math.Min(imageSize, MAX_IMAGE_SIZE);
        return imageSize;
    }

    public static string GetCravatarImageUrl(string email, int imageSize, string defaultImageUrl)
    {
        if (string.IsNullOrEmpty(email))
        {
            return string.Empty;
        }

        UriBuilder uriBuilder = new UriBuilder(WEBSITE);
        email = email.Trim().ToLower();
        uriBuilder.Path += $"{email.ToMD5Hash()}";

        string queryString = "";
        if (imageSize != 0)
        {
            imageSize = ValidateImageSize(imageSize);
            queryString += $"s={imageSize}";
        }

        if (!string.IsNullOrWhiteSpace(defaultImageUrl))
        {
            queryString += $"&d={defaultImageUrl}";
        }

        if (!string.IsNullOrEmpty(queryString))
        {
            uriBuilder.Query += queryString;
        }

        return uriBuilder.Uri.ToString();
    }
}

public static class StringExtensionMethods
{
    public static string ToMD5Hash(this string str)
    {
        byte[] hashBytes = MD5.HashData(Encoding.UTF8.GetBytes(str));
        StringBuilder strBuilder = new();

        if (hashBytes != null)
        {
            for (int i = 0; i < hashBytes.Length; i++)
            {
                strBuilder.Append(hashBytes[i].ToString("x2"));
            }
        }

        return strBuilder.ToString();
    }
}
```

Now we can call custom helper function to create a profile URL and use it in the application.

```
@{
    ViewData["Title"] = "Home Page";
    string profileURL = CravatarHelper.GetCravatarImageUrl("MyEmailAddress@example.com", 80, "mm");
}

<img src=@profileURL alt="avatar"/>
```

For more information, check out the [Cravatar API documentation](https://cravatar.com/developer/api).
