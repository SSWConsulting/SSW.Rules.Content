---
type: rule
title: Do you have a device policy for your mobile dev teams?
uri: dev-mobile-device-policy
authors:
  - title: Matt Goldman
    url: https://ssw.com.au/people/matt-goldman
related: []
created: 2023-04-21T04:57:29.000Z
archivedreason: null
guid: 08b5d785-9475-43ee-b4b7-d5f1fd6c0561
---
Lack of access to physical devices for testing can significantly impact mobile development. Issues can arise that you don't know about until UAT. Do you know the best way to mitigate this and avoid spiraling development costs?

<!--endintro-->

Mobile development is acutely prone to the "works on my machine" problem. Features that work on an emulator or simulator may not work as expected when running on a physical device, or features that work on iOS may not work on Android, or vice versa.
    
It's important to ensure that features and UI work as expected on the devices that your end users will be running the app on.

:::info
**Tip** Ensure that testing on at least one physical device on each OS you are targeting is part of your [definition of done](/definition-of-done).
:::

You need to choose the right option to ensure that all team members have access to the required devices without incurring unnecessary expenses.

## Option 1: Developers use their own devices

The easiest approach is just to let your developers use their own devices for testing. This can work well at the start but leads to problems if you divide your work between devs with access to different devices.

:::greybox
1. Developer A works on Feature 1. They test it on their Android phone, it works, so they open a PR and merge it.
2. Developer B works on Feature 2. They test it on their iOS phone, it works, so they open a PR and merge it.
3. At the end of the Sprint, a build is sent to testers for UAT.
4. Feature 1 doesn't work on iOS, and Feature 2 doesn't work on Android.
:::

## Option 2: Use a cloud based service

Cloud based options like BrowserStack are awesome, as they give access to a range of devices that can be used for testing.
    
Using something like BrowserStack is not a good option for development, as it introduces substantial latency to your inner development loop.
    
However, it is an awesome tool for testing and can be incorporated into your release cycle, as an [automated test tool](https://www.browserstack.com/app-automate).

## Option 3: Create a device policy

Having test devices available to your developers is the best option to ensure they can test their work on the hardware and OSes that your clients will need.

**Note:** If your client requires a _specific_ device or a _specific_ hardware version for you to test on, they should supply these to your development team.

You will need to create your policy according to your organization's needs, but the following high-level steps are usually applicable to everyone:

1. For each project, identify the minimum number of physical devices required to support all the necessary features and functionality.
2. Create a device sharing policy that outlines the process for reserving and using devices, ensuring that all team members have access to the devices they need.
3. Encourage team members to purchase their own devices that are compatible with the projects they work on. The company can provide a partial reimbursement or a stipend for the purchase of the device.
4. Utilize device emulators and simulators to test apps on devices that are not physically available to the team.
5. Regularly review and update the list of supported devices to reflect changes in the market.

:::info
**Important:** It's essential to register your devices in your company's [asset catalogue](/label-your-assets) and enrol them in your [MDM solution](/implementing-intune).
:::
