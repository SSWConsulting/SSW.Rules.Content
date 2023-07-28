---
type: rule
archivedreason: 
title: Do you send Control4 notifications to a Slack channel?
guid: 0222a672-083e-4b07-81d6-90467a6fafbd
uri: do-you-send-control4-notifications-to-a-slack-channel
created: 2017-11-03T01:04:53.0000000Z
authors:
- title: Greg Harris
  url: https://ssw.com.au/people/greg-harris
related: []
redirects: []

---

Are you tired of missing important Control4 notifications? Fear not! We have a solution for you. By using the "Incoming Webhook" integration in Slack, you can receive Control4 notifications directly in Slack. 📣💬

<!--endintro-->

To set up Control4 notifications in Slack, follow these steps:

1. Open Slack and go to your desired channel or create a new one dedicated to Control4 notifications 📢
2. Click on the channel name and select "Add apps" from the dropdown menu 🔌
3. Search for "Incoming Webhooks" and click on the app to install it 
4. Configure the webhook by providing a name for it and selecting the channel where you want the notifications to appear 📝
5. Copy the generated webhook URL. This will be used to send Control4 notifications to Slack 

::: good
![Figure: Good example - Slack Integration window](slackintegration.jpg)
:::

1. In your Control4 system, navigate to the Composer software and open your project
2. Configure the "Generic TCP command" by providing the necessary details, such as the Web address and Post Data

   - **Web Address:** Your Slack Webhook URL e.g. `https://hooks.slack.com/services/Taaqw3H6/B7RMC66yBV/GvA3IEIrpZgy4nqssddsaa`
   - **Post Data:** The message contents (payload) to be delivered to Slack  e.g. `{"text":":key:Reception Door Success"}`
  
3. Save the TCP command settings and test it out by triggering a Control4 event that will execute the TCP command 🚨

::: good
![Figure: Good example - Setting up a Generic TCP Command in Composer](composerintegration.jpg)
:::

That's it! Now you'll be able to send Control4 notifications to Slack using the generic TCP command in Control4 Composer. 🙌

::: good
![Figure: Good example - You can send any kinds of notifications to Slack](slacknotification.jpg)
:::

Remember, using the "Incoming Webhook" integration in Slack and the generic TCP command in Control4 Composer is a powerful combination for seamless notification integration. It keeps everyone in the loop and makes collaboration a breeze! 🤝
