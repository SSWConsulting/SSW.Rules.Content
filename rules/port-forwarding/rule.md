---
type: rule
title: Do you use port forwarding to test local builds?
uri: port-forwarding
authors:
  - title: Daniel Mackay
    url: https://ssw.com.au/people/daniel-mackay
created: 2023-02-06T01:31:37.930Z
guid: 44219801-42c9-4a90-ac22-5fefcf0cb365
redirects: 
 - do-you-use-dev-tunnels-to-test-local-builds
---
Sometimes we have a need to expose a locally running application over the internet for testing or other purposes. Dev Tunnels is a new port forwarding feature in Visual Studio that can help us do that.

<!--endintro-->

## Use Cases

* Feedback on a locally running application
* Testing of an application on a mobile phone or tablet
* Webhooks: public service needing to make an API call to your local website (e.g. Twilio or Sendgrid webhook)
* Azure SignalR: Get the Azure hosted signal R service to send websocket messages to your local website
* Azure APIM: Use APIM as a gateway that points to a locally running API
* Power Platform: Debug Power Platform by running your API locally

## Options

* [Dev Tunnels](https://learn.microsoft.com/en-us/aspnet/core/test/dev-tunnels?view=aspnetcore-7.0) (Recommended)
* [ngrok](https://ngrok.com)
* [TunnelTo](https://tunnelto.dev)
* [Packet Riot](https://packetriot.com)

## Dev Tunnels Setup

::: info
Dev Tunnels is currently only available via Visual Studio 2022 15.5+
:::

### Pre-Requisites

* Visual Studio 2022 15.5+
* ASP.NET Core project

### Usage

1. Enable the Dev Tunnels via **Tools | Options | Environment | Preview Features**:

   ![Figure: Enabling Dev Tunnels](screen1.png)
2. Open the Dev Tunnels window via **View | Other Windows | Dev Tunnels**
3. Create and configure a new Dev Tunnel:

   ![Figure: Configuring a Dev Tunnel](screen2.png)
4. Run the website
5. Get the public URL via **Dev Tunnels | Tunnel URL**:

   ![Figure: Finding the Dev Tunnel URL](screen4.png)
6. Confirm you can browse your site via the public URL:

   ![Figure: Testing the Dev Tunnel on desktop](screen3.png)
7. Confirm you can browse via a mobile:

   ::: img-medium
   ![Figure: Testing the Dev Tunnel on mobile](screen5.png)
   :::

## Best Practices on Access Types

* Private: Ideal if you are testing yourself on mobile device
* Organization (Recommended): Ideal if you need feedback from others within the organization
* Public: For when the other two options are not possible (e.g. Web hooks). In this case it is recommend to use Temporary tunnels so that the URL is no longer available once you've closed visual studio

## Resources

* [MS Learn - Port Tunneling](https://learn.microsoft.com/en-us/connectors/custom-connectors/port-tunneling)
* [How To - Dev Tunnels](https://learn.microsoft.com/en-us/aspnet/core/test/dev-tunnels?view=aspnetcore-7.0)
* [Dev Tunnels Public Preview](https://devblogs.microsoft.com/visualstudio/public-preview-of-dev-tunnels-in-visual-studio-for-asp-net-core-projects)
* [Twilio Webhooks](https://www.twilio.com/blog/use-visual-studio-port-tunneling-with-twilio-webhooks)
