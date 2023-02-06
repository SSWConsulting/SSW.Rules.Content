---
type: rule
title: Do You Use Dev Tunnels to Test Local Builds?
uri: do-you-use-dev-tunnels-to-test-local-builds
authors:
  - title: Daniel Mackay
created: 2023-02-06T01:31:37.930Z
guid: 44219801-42c9-4a90-ac22-5fefcf0cb365
---
Instructions for creating rules can be found at [How to Create Rules](https://github.com/SSWConsulting/SSW.Rules.Content/wiki/How-to-Create-Rules). Follow the steps below and replace the text in this box with your own content.
            
Sometimes we have a need to expose a locally running application over the internet for testing or other purposes.  Dev Tunnels is a new Visual Studio feature that can help us do that.
            
<!--endintro-->

## Use Cases

- Feedback on a locally running application
- Testing of an application on a mobile phone or tablet
- Webhooks: public service needing to make an API call to your local website (e.g. Twillio or Sendgrid webhook)
- Azure SignalR: Get the Azure hosted signal R service to send websocket messages to your local website
- Azure APIM: Use APIM as a gateway that points to a locally running API
- Power Platform Development

## Setup

::: info
Dev Tunnels is currently only available via a preview version of Visual Studio
:::

### Pre-Requisites

- Visual Studio 2022 Preview 15.5
- ASP.NET Core project

### Usage

## Best Practices

## Resources
- [MS Learn - Port Tunneling](https://learn.microsoft.com/en-us/connectors/custom-connectors/port-tunneling)
- [How To - Dev Tunnels](https://learn.microsoft.com/en-us/aspnet/core/test/dev-tunnels?view=aspnetcore-7.0)
- [Dev Tunnels Public Preview](https://devblogs.microsoft.com/visualstudio/public-preview-of-dev-tunnels-in-visual-studio-for-asp-net-core-projects/)

- [Twilio Webhooks](https://www.twilio.com/blog/use-visual-studio-port-tunneling-with-twilio-webhooks)

