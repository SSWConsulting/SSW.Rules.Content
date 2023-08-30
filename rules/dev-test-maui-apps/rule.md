---
type: rule
archivedreason:
title: Do you test .NET MAUI apps on different devices?
guid: c039d377-4b4e-4b81-adbf-2291c4648607
uri: dev-test-maui-apps
created: 2023-07-02T23:23:51Z
authors:
  - title: Vlad Kireyev
    url: https://www.ssw.com.au/people/vlad-kireyev/
related: 
- dev-mobile-device-policy
---
.NET MAUI (Multi-platform App UI) is a framework that enables developers to create cross-platform applications for different devices efficiently. However, the efficiency of this framework could mean nothing if the developed apps are not tested on various devices, especially the older once. 

<!--endintro-->

Testing mobile apps on different devices helps in ensuring compatibility across multiple platforms and versions. Different devices have unique hardware, operating systems, and screen resolutions. Therefore, testing an app on different devices ensures that the app can work efficiently on all platforms. For example, an app that runs smoothly on an Android device might be incompatible with an iPhone's operating system, resulting in a suboptimal user experience and potential bugs.

## Option 1: Use emulators

There are several ways that developers can test mobile apps on different devices to ensure that they are running smoothly and providing the best user experience possible. One approach is to use emulators, which are programs that simulate the behaviour of specific devices and operating systems. These emulators can be very helpful for testing basic functionality, but they may not accurately represent all aspects of the user experience, such as touch sensitivity and screen size.

Some of the popular .NET MAUI emulator apps are:
- iOS Simulator: it allows developers to preview their apps on iOS and macOS devices.
- Android Emulator: it allows developers to test their apps on various Android devices.
- Tizen Simulator: it allows developers to test their apps on Tizen devices.


## Option 2: Use a cloud-based service

Testing mobile apps with cloud-based services like BrowserStack offers several advantages to developers. Firstly, it allows them to easily access a wide range of real devices and browsers for testing, enabling comprehensive and efficient app evaluation. The developers can run tests on multiple operating systems, screen sizes, and resolutions, ensuring that their MAUI app performs seamlessly across various platforms. Additionally, these cloud-based services provide instant access to devices, eliminating the need for physical hardware and saving both time and resources. However, reliance on such cloud-based services introduces substantial latency to your inner development loop, and might not be the best option for development.

Apart from BrowserStack, there are several services that offer similar functionality: 
- Sauce Labs
- LambdaTest
- Experitest
- CrossBrowserTesting. 


## Option 3: Use real devices (Recommended)

Another effective way to test mobile apps on different devices is to use real hardware. This allows developers to see how the app performs on a variety of devices with different screen sizes, processing power, and other specifications. One approach is to borrow or purchase multiple devices to test on, but this can be time-consuming and expensive. The better way is to [have a device policy for your mobile dev teams](/dev-mobile-device-policy).


Regardless of the approach used, it is important to test on a variety of devices to ensure that the app works well for all users. This can include testing on both iOS and Android devices, as well as different versions of each device and operating system. Additionally, testing on different screen resolutions and aspect ratios can help identify any design issues that may arise. By thoroughly testing on a range of devices, developers can ensure that their MAUI app is high-quality, user-friendly, and reliable across all platforms.
