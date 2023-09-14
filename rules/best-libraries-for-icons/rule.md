---
type: rule
archivedreason: 
title: Do you use the best libraries for icons?
guid: a18dd243-d1ab-4a1a-bcc3-53ee3bc96e06
uri: best-libraries-for-icons
created: 2014-06-18T05:00:53.0000000Z
authors:
- title: Ben Cull
  url: https://ssw.com.au/people/ben-cull
- title: Drew Robson
  url: https://ssw.com.au/people/drew-robson
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: Jayden Alchin
  url: https://ssw.com.au/people/jayden-alchin
related: 
- enforce-the-text-meaning-with-icons-and-emojis
- use-icons-to-not-surprise-users
redirects:
- do-you-use-font-awesome-for-icons
- do-you-use-the-best-libraries-for-icons

---

When building a web application, you may eventually need icons somewhere in the UI. In the past this was done with images (e.g. png, jpg) which can create a lot of resource management, inconsistency, and other pain.

<!--endintro-->

##Why you should use icons, not images

- **Scalability:** Icon fonts are vector-based, which means they can be scaled up or down in size without losing quality. This is particularly important for responsive web design, where icons need to adapt to different screen sizes and resolutions. Image files, however, become pixelated and lose quality when scaled.
- **Adaptability:** The customization of icon color, size, and other properties is quick and easy using simple CSS. This removes any need to create new image files for icon variants or states.
- **Consistency:** Using a single icon library makes it effortless to maintain a consistent design language across your website or product.
- **Cross-browser compatibility:** Complete support across all modern browsers means icon fonts are reliable and render in a predictable, consistent way across different platforms and devices.
- **Accessibility:** Icons can be made accessible to screen readers by using ARIA roles and labels. Doing so ensures that users with disabilities can understand their meaning.
- **SEO:** Search engines can index text-based content more effectively than images. Using icons with proper semantic HTML can improve the SEO of your website, as search engines can understand and index that content.
- **Faster loading:** Icon fonts reduce the number of HTTP requests to the server. Fewer requests means faster load timing. In addition, even a small collection of image files can take a large amount of space. Icon font files are much smaller and make icon load times almost a non-issue.

If you _absolutely_ must use images for icons (e.g. complex custom icons) use svg files. These vector-based images function closer to an icon font, being similar in scalability, adaptability, and customization.

::: bad  
![Figure: Bad example - Using images as icons generates a lot of pain](23-06-2014 11-20-02 AM.png)  
:::

::: good  
![Figure: Good example - A 5x scaled paper plane icon on the web](18-06-2014 2-33-45 PM.png)  
:::

##Awesome icon libraries

- You can quickly and easily get set up with [Bootstrap icons](https://icons.getbootstrap.com/) with or without using Bootstrap itself. Many consider this icon library timeless, but there is another popular icon library to challenge it...
- [Font Awesome](https://fontawesome.com/) provides scalable vector icons that can be fully customized with CSS and many are completely free for commercial use. This library is especially great if you need a wide selection of generic icons in a hurry. You can also purchase a pro license to access an extended collection of variations like thin, sharp, and duotone icons. 
- See [Google material icons and symbols](https://fonts.google.com/icons) for another huge set of variable icons. These icons can be customized right down to their line weight and roundness or sharpness.
- If you are using Azure, there's an awesome icon collection with several [Azure icons for you to use](http://code.benco.io/icon-collection/). Instead of browsing individually, you can also download the entire up-to-date set from the [Azure Architecture Center](https://learn.microsoft.com/en-us/azure/architecture/icons/#icon-terms).
- If you need Microsoft icons, see [Fluent iconography](https://fluent2.microsoft.design/iconography). 
- There are many more awesome icon libraries, including open-source community projects like [Lucide](https://lucide.dev/).
