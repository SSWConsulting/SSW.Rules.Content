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

Azure has 100s of offerings and it can be hard to know what the right services are to choose for any given application.

However, there are a few questions you can ask yourself to help narrow down the right services for each business case. 
            
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
* Platform as a Service (PaaS)
   * Consumer responsible for App configuration, building the app and server configuration
* Logic as a Service (LaaS)
   * Consumer responsible for App configuration and building the app
* Software as a Service (SaaS)
   * Consumer responsible for only App configuration

## 1.2 Where do I need the app to run?
* Azure 
* On-Premises
* Other Clouds e.g. AWS, Netlify, GitHub Pages
* Hybrid

## 1.3 How often does the app need to run?

* Occasionally
   * Serverless (Pay per execution)
* All the time
   * Classic (Pay per month)

## 1.4 Examples

### Scenario #1 

### Scenario #2

# 2. How do you store your data?

## 2.1 What will I use the data for?
* Online Transaction Processing (OLTP)
    * For general application usage e.g. storing customer data, invoice data, user data etc
* Online Analytical Processing (OLAP)
    * For data analytics e.g. reporting

## 2.2 What type of data am I going to store?
* Relational data e.g. a fully normalized database
* Unstructured data e.g. document data, graph data, key/value data

## 2.3 Examples

### Scenario #1 

### Scenario #2
