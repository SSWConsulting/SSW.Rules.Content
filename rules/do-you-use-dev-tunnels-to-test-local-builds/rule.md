---
type: rule
title: Do You Use Dev Tunnels to Test Local Builds?
uri: do-you-use-dev-tunnels-to-test-local-builds
authors:
  - title: Daniel Mackay
created: 2023-02-06T01:31:37.930Z
guid: 44219801-42c9-4a90-ac22-5fefcf0cb365
---
Sometimes we have a need to expose a locally running application over the internet for testing or other purposes.  Dev Tunnels is a new Visual Studio feature that can help us do that.

<!--endintro-->

## Use Cases

* Feedback on a locally running application
* Testing of an application on a mobile phone or tablet
* Webhooks: public service needing to make an API call to your local website (e.g. Twilio or Sendgrid webhook)
* Azure SignalR: Get the Azure hosted signal R service to send websocket messages to your local website
* Azure APIM: Use APIM as a gateway that points to a locally running API
* Power Platform Development 

## Setup

::: info
Dev Tunnels is currently only available via Visual Studio Preview 15.5+
:::

### Pre-Requisites

* Visual Studio 2022 Preview 15.5
* ASP.NET Core project

### Usage

1. Enable the Dev Tunnels via Tools | Options:

Image TBC

2. Start your website

3. Open the Dev Tunnels window

Image TBC

4. Create a new Dev Tunnel

Image TBC

5. Configure Dev Tunnel

Image TBC

6. Test Dev Tunnel

## Best Practices

### Tunnel Type
- Private: Testing yourself on mobile device
- Organization: Need feedback from others within the organization
- Public: When the other two options are no possible (.e.g. Web hooks).  In this case I recommend using Temporary tunnels so that the URL is no longer available once you've closed visual studio
 

## Resources

* [MS Learn - Port Tunneling](https://learn.microsoft.com/en-us/connectors/custom-connectors/port-tunneling)
* [How To - Dev Tunnels](https://learn.microsoft.com/en-us/aspnet/core/test/dev-tunnels?view=aspnetcore-7.0)
* [Dev Tunnels Public Preview](https://devblogs.microsoft.com/visualstudio/public-preview-of-dev-tunnels-in-visual-studio-for-asp-net-core-projects/)
* [Twilio Webhooks](https://www.twilio.com/blog/use-visual-studio-port-tunneling-with-twilio-webhooks)