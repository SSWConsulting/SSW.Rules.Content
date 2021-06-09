---
type: rule
archivedreason: 
title: Do you know when to mockup your API?
guid: eee9e703-e6bd-40f8-9f65-8a12a3d92f8d
uri: do-you-know-when-to-mockup-your-apis
created: 2021-05-11T22:00:01.0000000Z
authors:
- title: William Liebenberg
  url: https://ssw.com.au/people/william-liebenberg
- title: Bryden Oliver
  url: https://ssw.com.au/people/bryden-oliver
related: 
- do-you-know-how-to-brand-your-api-portal
- do-you-know-the-best-tools-to-manage-apis
redirects:
- do-you-know-when-to-mockup-your-apis

---

Designing your API up front can be very useful where you have a significant amount of backend development to complete before there is sufficient functionality for front end development to easily commence.

<!--endintro-->

Rather than waiting for the backend to be complete, the APIs can be agreed on up front. Tools like Azure API Management then allow you to mock up the APIs with sample data, allowing the front end development to commence much sooner.

This can result in valuable feedback on the API and backend functionality much earlier in your development lifecycle. The key benefit is being able to present the frontend to stakeholders for feedback really early.

Watch Adam Cogan and William Liebenberg discuss the benefits.

`youtube: https://youtu.be/rNyOALskc_U`

## Steps to create and test a mocked API endpoint

To complete the following steps, you need to create an instance of Azure API Management in your subscription.

> TIP: If you have Azure Credits, the Developer (NO SLA) edition is the cheapest option to test most of the features offered by API Management.

### Step 1 - Create Blank API

1. Select **Blank API**

![](images/step1-create-blank-api.png)
Figure: Create a blank API

## Step 2 - Describe your API

![](images/step2-describe-your-api.png)
Figure: Describe your API

1. Click **Create**

## Step 3 - Add an Operation

1. Select your API from the API list
2. Click **Add operation**
3. Specify the Display name, Name and URL of your operation 

![](images/step3-add-operation.png)
Figure: Adding a new Operation

## Step 4 - Add response

1. Click **Add response**
2. Select the appropriate response code (e.g 200 OK)

![](images/step4-add-response.png)
Figure: Add a response

## Step 5 - Add representation

1. Specify the **Content Type** as `application/json`
2. Specify the **Sample** as `{ "data": "fake" }`
3. Click **Save**
  
![](images/step5-add-represtntation.png)
Figure: Add a representation for your response with fake data

![](images/step5-operation-done.png)
Figure: Operation added successfully

## Step 6 - Add Mock Response Policy

1. Click **Add policy**
2. Select **Mock responses**

![](images/step6-add-mock-response-policy.png)
Figure: Add the Mock Response policy

## Step 7 - Choose response

1. Choose the response representation to return as a Mock (e.g. `200 OK, application/json`)
2. Click **Save**

![](images/step7-choose-response-representation.png)
Figure: Choose the response representation

## Step 8 - Test your Mocked API

1. Make sure your API is selected
2. Click the **Test** tab
3. Click the FakeData operation
4. Note the "Mocking is enabled" notice
5. Click **Send**

![](images/step8-test-mock-api.png)
Figure: Testing the mocked api operation

## Step 9 - Inspect Mocked API response

1. Notice the 200 OK status code
2. Notice the fake data response in the message body

![](images/step9-inspect-mocked-api-reponse.png)
Figure: Response from the mocked operation

## Step 10 - Call your API using a REST Client

1. Add a new `GET` request to your REST Client
2. Specify the API Uri such as `https://william-ssw.azure-api.net/data`
3. Add the subscription header `Ocp-Apim-Subscription-Key` and value
     - you can copy the value directly from the operation HTTP Request section
     - or, from the API Management service | Subscriptions blade
4. **SEND** your request
5. Verify the `200 OK` response and the mocked data

![](images/step10-call-from-rest-client.png)
Figure: Calling our Data API from a REST Client

## Conclusion

Mocking API responses is awesome! You are able to quickly add mocked responses for all your API endpoints without even having a real backend implementation, and your front-end application can make REAL API calls. 
