---
type: rule
title: Do you track QR codes' data for your own URLs in Google Analytics?
uri: track-qr-code-data-in-ga
authors:
  - title: Camilla Rosa Silva
    url: https://www.ssw.com.au/people/cammy
created: 2023-05-11T01:26:19.889Z
guid: dd810edd-10ea-4b6f-af61-02f2bcf40b46
---
To ensure you are tracking the traffic taken to your website from a QR code, it's important to add UTM parameters to the URLs you are using to create your QR codes.

This will allow you to see users, bounce rate, sessions, events, conversions and more in Google Analytics.

> The UTM parameters in a URL identify the campaign that refers traffic to a specific website, and attributes the browser's website session and the sessions after that until the campaign attribution window expires to it. The parameters can be parsed by analytics tools and used to populate reports.
>
> Source: [Wikipedia](https://en.wikipedia.org/wiki/UTM_parameters#:~:text=The%20UTM%20parameters%20in%20a,and%20used%20to%20populate%20reports.)

**Important:** this only works for your own domain or domains that you have access to in your Google Analytics account.  

<!--endintro-->

[Google's Campaign URL Builder](https://ga-dev-tools.google/campaign-url-builder/) is a free tool that allows you to easily add campaign parameters to URLs so you can measure [Custom Campaigns](https://support.google.com/analytics/answer/1033863) in Google Analytics.

![Figure: Google will provide you with a campaign URL, ready to track all the relevant data you need](google-utm-generator.png)