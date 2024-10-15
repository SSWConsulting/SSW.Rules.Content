---
seoDescription: Developing a chatbot from scratch using OpenAI API requires significant expertise and upfront costs. Compare options with Chatbase, Botpress, or build your own custom solution for more control over AI model training and system messages.
type: rule
title: Do you know the best chatbot for your website?
uri: website-chatbot
authors:
  - title: Ulysses Maclaren
    url: https://ssw.com.au/people/ulysses-maclaren
  - title: Khaled Albahsh
    url: https://www.ssw.com.au/people/khaled-albahsh/
  - title: Manu Gulati
    url: https://www.ssw.com.au/people/manu-gulati
related: null
redirects: null
created: 2023-08-23T03:50:10.000Z
archivedreason: null
guid: 945588b4-8053-41cf-9052-b2f871c4363d
---

A chatbot is a computer program that uses artificial intelligence to engage in text or voice conversations with users, often to answer questions, provide assistance, or automate tasks. In the age of generative AI, good chatbots have become a necessary part of the user experience.

::: good img-small
![Figure: Good example - A good chatbot in action](chatbot-example.png)
:::

Choosing the right chatbot service for your website can be a challenging task. With so many options available it's essential to find the one that best fits your needs and provides a good experience for your users. But what distinguishes a good chatbot from a great one? Here are some factors to consider.

<!--endintro-->

### Factors to consider

##### Development Effort/Cost

* **Custom Built vs 3rd Party Service**: Custom built provides more control but incurs high development effort & cost - usually 3rd party solutions are cheaper up front
* **Pre-built/Drag-and-Drop Builders**: Simplifies creation without coding
* **Documentation & Support**: Bad documentation can make a simple product hard to use - incurring more costs

##### Performance

* **Responses**: Smooth and natural responses that answer questions while understanding context
* **Visual Design**: Aligns with brand aesthetics
* **Content Tailoring**: Adapts responses to fit brand voice

##### Research and Training

* **API Support**: API integration if you might want to use it in other applications
* **Data Syncing**: How often does it refresh it data from your website?

##### Scalability

* **Traffic Management**: Handles varying user traffic levels
* **Data Storage**: Manages increasing user data
* **Knowledge Base** There is usually a limit in 3rd party chatbots e.g. Chatbase provides you 11M characters, which roughly equates to ~3500 pages of text

##### Handling Curveballs

* **Adaptive Responses**: Adjusts to unexpected user inputs
* **Feedback Loop**: Improves from past interactions
* **Human Agent Referral**: Transfers smoothly to a human if needed
* **Response Filtering**: Is not tricked by misleading questions

### Comparing platforms

The first decision is to choose between using a 3rd party chatbot service (e.g. ChatBase or Botpress) vs developing your own from scratch using a large language model API (e.g. OpenAI API).

| Factor                      | Directly from an API (e.g. OpenAI) | 3rd Party              |
| --------------------------- | ---------- | ---------------------- |
| Development effort and cost | Very High  | Low                    |
| Control                     | Very High  | Moderate               |
| Cost to Train               | Very Low   | Very Low               |
| Knowledge Base Limits       | Unlimited  | Limited but Sufficient |
| Cost per Message            | Moderate   | High                   |

Before delving deeper into the comparison it would help to first understand the steps involved in building chatbots using either technology.

### Using a 3rd Party service

After creating your account and starting a new project, you should:

1. Choose the best large language model – e.g. in 2023 you'd choose GPT-4
2. Craft a pointed prompt to give it instructions on how to respond to the user. For e.g. you can ask it to share URLs to your web pages when appropriate
3. Train the bot by providing links to your web pages or by uploading docs
4. Configure the chatbot for features such as a greeting msg, company logo, chat bubble colours, etc.
5. Embed an iframe or javascript code provided by the service on your website

### Creating a chatbot using an API (e.g. OpenAI API)

The following provides a very high level description of creating a chatbot from scratch using the OpenAI API. For a more in-depth explanation please watch:
`youtube: https://www.youtube.com/watch?v=9cUciEMUcnA&t=884s`
**Video: Exploring the Capabilities of ChatGPT | Calum Simpson | User Group (132 mins)**

1. Convert your knowledge base into embeddings
2. Store embeddings and their corresponding text content in a vector database
3. Set up a server that can do the following
   1. Convert user query into an embedding
   2. Lookup vector database to find embeddings that are closest to the embedding created out of user query
   3. Insert the content corresponding to the matching embeddings into the OpenAI System message
   4. Pass recent user chat history to the OpenAI API
   5. Wait for OpenAI to generate a response. Present the response to the user.
4. Create a chatbot front-end widget

As you can see, developing a chatbot from scratch using the OpenAI API requires significant development effort and expertise. 3rd party chatbots on the other hand are much easier to program and embed on your website. As a rough estimate assume it will take a developer 20 days to build a custom chatbot - or $20K up front (assuming the developer costs $1000/day. Assuming a $399/month subscription of Chatbase on the other hand, it would take the custom solution over 4 years just to break even.

However, custom built chatbots provide a lot more control in how you train the AI model, what content you match the user query with, and what system message you provide the GPT engine to respond to a user’s query. You don’t get this level of control with 3rd party chatbots. The backend of custom built solutions can also be leveraged to serve multiple chatbots supporting completely different use cases. For e.g. one chatbot could provide basic company info to visitor’s on the company website, while a second chatbot could help employees find info on the company Intranet.

Cost to train the chatbot on your knowledge base is very inexpensive in both options. For example, you can train a chatbot on ~3000 pages for less than $1 USD using the OpenAI Embeddings model.

#### Chatbase vs Botpress - 2 popular solutions

If you decide to go with a 3rd party service, you might be torn between 2 popular platforms: [Botpress](https://botpress.com/) and [Chatbase](https://www.chatbase.co/).

`youtube: https://www.youtube.com/watch?v=a1LSk3krUL0`
**Video: Do you know the best chatbot for your website? (8 min)**

|          | GPT Integration                                           | Customization                 | Pricing                      |
| -------- | --------------------------------------------------------- | ----------------------------- | ---------------------------- |
| Botpress | ❌ Traditional style of workflow and steep learning curve | ✅ Wide range of integrations | ✅ Free to start             |
| Chatbase | ✅ Does everything with prompt engineering                | ✅ Easy customization         | ❌ Limited free plan options |

##### Making the right choice

While both platforms offer unique features, Chatbase stands out as the superior choice in most instances. Here's why:

* Easier customization and integration with various tools
* Chatbase's user-friendly interface makes it accessible to a wide range of users. A prompt engineer can setup, tweak and improve the system. No development required
* Botpress lacks the intuitive interface of Chatbase, and without extensive workflow development and testing, will fail in conversations
