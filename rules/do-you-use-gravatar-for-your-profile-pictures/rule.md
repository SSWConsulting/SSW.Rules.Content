---
type: rule
archivedreason: 
title: Do you use Gravatar for your profile pictures?
guid: b790dbfc-fe37-4a4a-992e-c9294620a06b
uri: do-you-use-gravatar-for-your-profile-pictures
created: 2015-03-16T10:17:40.0000000Z
authors: []
related: []
redirects: []

---

To keep profile management simple and make it easier for users to have a consistent experience across applications, you should use [Gravatar](https://en.gravatar.com/) for showing profile images in your application.

Your Gravatar is an image that follows you from site to site appearing beside your name when you do things like comment or post on a blog.

<!--endintro-->

### Setting up Gravatar in your application

It is simple to set up and if you are developing an MVC application, there are even several Nuget packages to make your life easier. The [GravatarHelper](https://www.nuget.org/packages/GravatarHelper) is recommended.

``` aspnet
@Html.GravatarImage("MyEmailAddress@example.com", 80, new { Title = "My Gravatar", Alt = "Gravatar" })
```

Also, check out the [Gravatar API documentation](https://en.gravatar.com/site/implement/images/) for all the options available.

The below short video shows how to get up and running with Gravatar in your ASP.NET MVC application.

`youtube: https://www.youtube.com/embed/rjFjVD9jPIk`
 

