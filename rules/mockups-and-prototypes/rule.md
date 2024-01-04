---
type: rule
title: Do you know when to create mockups and prototypes?
uri: mockups-and-prototypes
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
  - title: Jayden Alchin
    url: https://www.ssw.com.au/people/jayden-alchin
  - title: Geordie Robinson
    url: https://ssw.com.au/people/geordie-robinson
related:
  - storyboards
redirects:
  - visual-design-specifications
created: 2023-09-04T07:37:31.732Z
guid: 2b8c7067-4d59-49b2-a448-4b746b11383a
---
:::  info
**Note:** Some people might use the term storyboarding when they are actually talking about mockups or prototypes. For information on storyboarding, check [The Storyboarding Rule](/storyboards)
:::

Mockups and prototypes are both design artifacts used in the software development process, but they serve different purposes and have different levels of fidelity. Many user requirements can be best encapsulated in visual mockups/prototypes.

A **design mockup** is typically created early in the design process to provide a rough visual overview of the user interface. They are static and do not include interactive elements or functionalities.

Mockups can become interactive and functional representation, also know as **design prototype** over time. They are more advanced and closer to the final product, allowing for user testing, feedback, and iteration.

<!--endintro-->

There are 3 types of mockup or prototype, use depends on the specific goals and the stage of the project:

1. **Low-fidelity Mockups (aka Wireframes)**
2. **High-fidelity Mockups**
3. **Interactive  Prototypes**

Often it's best to start with a low-fidelity mockup to get across a concept or rough storyboard. Then complete a high-fidelity mockup to communicate the look and feel, and if time permits create an interactive prototype.

### Low-fidelity Mockups

Creating a low-fidelity design mockup can be achieved through various methods including wireframes, paper prototypes, and other similar techniques. It can be valuable to have the Product Owner on call when creating a low-fidelity mockup to get immediate feedback and direction.

Start by identifying the key features and functionality that the product should have. This will help you focus your efforts and ensure that your mockup accurately represents your intended product.

::: good
![Figure: Good Example - A hand-drawn mockup. Nice and quick for early concept design](handdrawnui.jpg)
:::

Then create a basic wireframe of your design. A wireframe is a visual representation of the layout and structure of your website or app. You can create digital wireframes using tools like Figma, Adobe XD, or Sketch. Alternatively, you can use paper and pencil to sketch out a rough wireframe by hand. Add details to your wireframe by adding boxes and labels for different features and elements (e.g. buttons, input fields, and images).

::: good
![Figure: Good example – Example of wireframes (created in Figma)](figma_wireframe_app_screenshot.png)
:::

Once your low-fidelity design mockup has been approved, you can use it as a reference point for creating a high-fidelity mockup.

### High-fidelity Mockups

A high-fidelity mockup is a more detailed version of a design that includes visual design elements such as typography, colors, and images. It is created using specialized design tools and takes more time to create than a low-fidelity mockup.

::: info
**Warning:** Don't go down the track of giving a customer a few concepts (on some projects we gave 2 or 3 completely different concepts by different designers). This leads to too much mixing and matching when they see them.
:::

::: good
![Figure: Good example – High fidelity mockup for SSW Rewards App - recommended as quick to update when changes are requested](high-fedelity-ui.png)
:::

Use a design tool such as Figma to create high-fidelity mockups of a website or app's interface. This should include more consideration of UX and detailed UI elements such as buttons, forms, icons, and typography.

:::  info
**Incorporate branding:** It's important to incorporate the brand's visual identity into the design of a product! This should include the brand's given color scheme, typography, and logo at a minimum.
:::

### Interactive Prototypes

To make a mockup more realistic and accurate to the end product, add interactivity to it. This includes consideration of how different elements will respond to user input, such as on-hover effects or the styling of visited links.

`youtube: https://www.youtube.com/embed/-d6zNGeF59M`

### What are the best tools?

* [Figma](https://www.figma.com) (Recommended)
* [Sketch](https://www.sketchapp.com) (Mac Only and for UX designers)
* [Moqups](https://moqups.com) (HTML5 based App)
* [Balsamiq](https://balsamiq.com)
* [UXPin](http://uxpin.com) (more sophisticated, helps you create responsive designs)

### Tips

::: greybox

Here are some more hot tips on using mockups for specification analysis:

* It is best to have a designer, developer, and customer work together
* Mock-ups should follow [interface rules](/rules-to-better-interfaces-general-usability-practices)
* Get the mockups [physically initialed](/tasks-do-you-know-to-ensure-that-relevant-emails-are-attached-to-tasks), especially if you are performing a fixed-price contract. Yes, paperless is great - but not in this case
* If you can't get mockups initialed, then page by page approval over email is the 2nd best option
* Write the related business rules at the bottom of each screen - to be turned into unit tests

:::
