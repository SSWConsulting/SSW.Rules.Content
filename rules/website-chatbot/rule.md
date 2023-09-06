---
type: rule
title: Do you know the best chatbot for your website?
uri: website-chatbot
authors:
  - title: Ulysses Maclaren
    url: https://ssw.com.au/people/uly
  - title: Khaled Albahsh
    url: https://www.ssw.com.au/people/khaled-albahsh/
related: null
redirects: null
created: 2023-08-23T03:50:10.000Z
archivedreason: null
guid: 945588b4-8053-41cf-9052-b2f871c4363d
---
A chatbot is a computer program that uses artificial intelligence to engage in text or voice conversations with users, often to answer questions, provide assistance, or automate tasks. In the age of Generative AI, good chatbots have become a necessary part of the User Experience. 

::: img-small
![Figure: A good chatbot in action](chatbot-example.png)
:::

Choosing the right chatbot service for your website can be a challenging task. With so many options available it's essential to find the one that best fits your needs and provides a good experience for your users. But what distinguishes a good chatbot from a great one? It's not just about automated responses; it's about intelligence and efficiency.

<!--endintro-->

### Factors to consider

Here are some key factors to consider.

#### Custom Built vs 3rd Party Service
* Custom built provides more control but incurs high development effort & cost
* Cost per message may be lower in custom built solutions for high volume of traffic

#### Performance

* **Responses**: Smooth and natural responses that answer questions while understanding context.
* **Visual Design**: Aligns with brand aesthetics.
* **Content Tailoring**: Adapts responses to fit brand voice.

#### Development Effort

* **Pre-built Templates**: Speeds up deployment.
* **Drag-and-Drop Builders**: Simplifies creation without coding.
* **Documentation & Support**: Assists in development.

#### Ease of Access

* **Multi-Platform**: Seamless functionality on desktop and mobile.
* **Messaging App Integration**: Works with apps like WhatsApp, Messenger.
* **Language Support**: Multilingual for global reach.

#### Research and Training

* **API Support**: API integration for third-party applications.
* **Data Syncing**: Real-time synchronization for up-to-date responses.

#### Scalability

* **Traffic Management**: Handles varying user traffic levels.
* **Data Storage**: Manages increasing user data.

#### Handling Curveballs

* **Adaptive Responses**: Adjusts to unexpected user inputs.
* **Feedback Loop**: Improves from past interactions.
* **Human Agent Referral**: Transfers smoothly to a human if needed.

#### Resilience to Trick Questions

* **Response Filtering**: Identifies misleading questions.
* **Learning from Mistakes**: Improves trick question handling.  

### Comparing platforms

The first decision is to choose between using a 3rd party chatbot service such as ChatBase/Botpress vs developing your own from scratch using the OpenAI API. The table below gives a summary of how these two options compare.

| Attribute | OpenAI API | 3rd Party | 
| --------- | ---------- | --------- | 
| Development effort and cost | Very High | Low |
| Control | Very High | Moderate |
| Cost to Train | Very Low | Very Low |
| Knowledge Base Limits | Unlimited | Limited but Sufficient |
| Cost per Message | Moderate | High |

Before delving deeper into the comparison it would help to first understand the steps involved in building chatbots using either technology. 

#### Steps to create chatbot using a 3rd Party service
For e.g. in Chatbase you would:
1.	Train the bot by providing links to your web pages or by uploading docs
2.	Craft a pointed prompt to give it instructions on how to respond to the user. For e.g. you can ask it to share URLs to your web pages when appropriate 
3.	Choose a GPT model – GPT-4 highly recommended
4.	Embed an iframe or javascript code provided by the service on your website
5.	Configure the chatbot for features such as a greeting msg, company logo, chat bubble colours, etc.

#### Steps to create chatbot using the OpenAI API
The following provides a very high level description of creating a chatbot from scratch using the OpenAI API. For a more in-depth explanation please watch:
`youtube: https://www.youtube.com/watch?v=9cUciEMUcnA&t=884s`
**Video: Exploring the Capabilities of ChatGPT | Calum Simpson | User Group (132 mins)**

1. Convert your knowledge base into embeddings 
2. Store embeddings and their corresponding text content in a vector database 
3. Setup a server that can do the following
   1. Convert user query into an embedding
   2. Lookup vector database to find embeddings that are closest to the embedding created out of user query
   3. Insert the content corresponding to the matching embeddings into the OpenAI System message
   4. Pass recent user chat history to the OpenAI API
   5. Wait for OpenAI to generate a response. Present the response to the user.
4. Create a chatbot front-end widget

You might be torn between two popular platforms: [Botpress](https://botpress.com/) and [Chatbase](https://www.chatbase.co/). 

`youtube: https://www.youtube.com/watch?v=a1LSk3krUL0`
**Video: Do you know the best chatbot for your website? (8 min)**

|          | GPT Integration                                          | Customization                | Pricing                     |
| -------- | -------------------------------------------------------- | ---------------------------- | --------------------------- |
| Botpress | ❌ Traditional style of workflow and steep learning curve | ✅ Wide range of integrations | ✅ Free to start             |
| Chatbase | ✅ Does everything with prompt engineering                | ✅ Easy customization         | ❌ Limited free plan options |

### Making the right choice

While both platforms offer unique features, Chatbase stands out as the superior choice in most instances. Here's why:

* Chatbase allows easy customization and integration with various tools
* Chatbase's user-friendly interface makes it accessible to a wide range of users. A prompt engineer can setup, tweak and improve the system. No development required
* Botpress lacks the intuitive interface of Chatbase, and is more prone non-sequeter conversation without extensive workflow development and testing

![Figure: Although Botpress seems to have more attention online recently, this may be because it's harder to configure so people are Googling it to help with that](botpress-vs-chatbase.jpg)

When selecting the best chatbot for your website, consider your specific needs and preferences. While Botpress offers a wide range of features, Chatbase's ease of customization, user-friendly interface, and robust GPT integration make it the superior choice for most users. 

Evaluate your requirements and choose the platform that best aligns with your goals.