---
type: rule
title: Do you know how to narrow down which Azure service to use?
uri: choose-azure-services
authors:
  - title: Piers Sinclair
    url: https://www.ssw.com.au/people/piers-sinclair
created: 2022-06-16T07:33:51.366Z
guid: 00777476-6f6f-4bb8-b583-ca2a4a4ffbd6
---
Getting application architecture right is super hard and often choosing the wrong architecture at the start of a project causes immense pain further down the line when the limitations start to become apparent.

[Azure has 100s of offerings](https://azure.microsoft.com/services) and it can be hard to know what the right services are to choose for any given application.

However, there are a few questions that [Azure MVP Barry Luijbregts has come up with](https://github.com/bmaluijb/HowIChooseMyAzureServices/blob/master/How%20I%20choose%20which%20services%20to%20use%20in%20Azure.pdf) to help narrow down the right services for each business case. 
            
<!--endintro-->

`youtube: https://www.youtube.com/watch?v=ZpK_lv6HJkQ`

There are 2 overarching questions to ask when building out Azure architecture:

# 1. How do you run your app?
There are heaps of models on offer in Azure for running your app. So, to choose the right one you need to break this question down into 3 further parts:

## 1.1 How much control do I need?
There are many different levels of control that can be provided. From a VM which provides complete control over every aspect to an out-of-the-box solution which provides very little control.

Keep in mind, that the more control you have, the more maintenance will be required meaning more costs. It is crucial to find the suite spot for control vs maintenance costs, really think about if the extra control gained is actually necessary.

* Infrastructure as a Service (IaaS)
   * Consumer responsible for everything beyond the hardware

     e.g. Azure VM, AKS
* Platform as a Service (PaaS)
   * Consumer responsible for App configuration, building the app and server configuration
     
     e.g. Azure App Service
* Logic as a Service (LaaS)
   * Consumer responsible for App configuration and building the app
     
     e.g. Azure Functions, Azure Logic Apps

* Software as a Service (SaaS)
   * Consumer responsible for only App configuration

## 1.2 Where do I need the app to run?
Choosing where to run your app 

* Azure 
* On-Premises
* Other Clouds e.g. AWS, Netlify, GitHub Pages
* Hybrid

## 1.3 How often does the app need to run?
Evaluating how often an app needs to run is crucial for determining the right costing model. A website or app that needs to be available 24/7 is suited to a different payment model than something which is called infrequently as a scheduled job that runs once a day.

There are 2 models:

* Runs Occasionally
   * Serverless (Pay per execution) e.g. Azure Functions, Azure Logic Apps
* Runs all the time
   * Classic (Pay per month) e.g. Azure App Service, Azure VM, AKS

# 2. How do you store your data?

## 2.1 What will I use the data for?
The first question is what is the purpose of the data. Data that is used for everyday apps has very different storage requirements to data that is used for complex reporting.

So data can be put into 2 categories:

* Online Transaction Processing (OLTP)
    * For general application usage e.g. storing customer data, invoice data, user data etc
* Online Analytical Processing (OLAP)
    * For data analytics e.g. reporting

## 2.2 What type of data am I going to store?
Data comes in many shapes and forms. For example, it might have been normalized into a fixed structure or it might come with variable structure.

Classify it into 2 categories:

* Relational data e.g. a fully normalized database
* Unstructured data e.g. document data, graph data, key/value data

# Example Scenario
These questions can be applied to any scenario, but here is one example:

Let's say you have an auctions website running a React SPA and a scheduled job that runs daily, picks up all the customer data and puts it into a database for reporting. 

## Where to run the app

The customer doesn't need fine tuned control but does need to configure some server settings for the website.
The app needs to run in Azure
The scheduled job runs occasionally (once a day) while the website needs to be up all the time.

So the best choices here might be
* An Azure App Service for the website since it is a PaaS offering that provides server configuration and constant availability
* An Azure function for the scheduled Job since it only runs occasionally and no server configuration is necessary

## How to store the data



