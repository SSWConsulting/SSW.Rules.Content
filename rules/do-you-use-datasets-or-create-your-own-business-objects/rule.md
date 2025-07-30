---
seoDescription: In .NET, you can pass data through layers using either DataSets or custom business objects.
type: rule
title: Do you use DataSets or create your own business objects?
uri: do-you-use-datasets-or-create-your-own-business-objects
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan/
created: 2014-03-14T05:36:00.000Z
guid: d4123a64-239a-4251-9a22-1ba31e85b690
---

In .NET, there are 2 ways to pass data through the layers of your application. You can:

<!--endintro-->

* Use DataSet objects, OR
* Write your own custom business objects

There are 2 very different opinions on this matter amongst .NET developers:

✅ Pros of **DataSet** object:

* **Code Generation** - Strongly typed **DataSet** objects can be created automatically in Visual Studio. Custom business objects must be laboriously coded by hand.
* **CRUD functionality DataSets** - When used with data adapters, can provide CRUD (Create, Read, Update, Delete) support. You must manually implement this functionality with custom business objects.
* **Concurrency** - Support for concurrency is part of the **DataSet** object. Again, you must implement this yourself in a custom business object.
* **Data binding** - It is difficult and time-consuming to write custom business objects that are compatible with data binding. The **DataSet** object is designed for data binding.

✅ Pros of **Custom Business** objects:

* **Better performance** - The **DataSet** object is a very heavy object and is memory-intensive. In contrast custom business objects are always much more efficient. Business objects are usually faster when manipulating data, or when custom sorting is required.
* Business objects allow you to combine data storage (NOT data access) and business logic (e.g. validation) in the one class. If you use **DataSet** objects, these must be in separate classes.

### The Case for Business Objects

Usually, it is recommended to choose datasets as it is believed you get more for free. However, all the the features you get in the dataset can be manually coded up in business objects.

E.g. For business objects you must manually code up the bindings, with datasets however you may use the designer for binding straight after designing the dataset. This layer should be code generated - so it doesn't matter much.

In Visual Studio, binding to business objects is supported in which case we might be swayed to use business objects.

**Exception: Real complex forms say 500,000 lines of C# code**

Datasets are a tool for representing relational data in an object oriented world. They are also slower across networks. Datasets are fantastic for maintenance forms (an editable grid with a couple of checkboxes and text boxes and a save button), but terrible for real complex forms. In a complicated scenario you might have a Customer object. An Order form has a reference to this customer object that it uses to display. When a process is run on the Customer invoked from the Order, you can simply pass a reference to the customer, and if something changes, fire an event back to the Order. If datasets were used, you would be either passing datasets around (which some may say is not very safe, or good OO) or pass an ID around and have the process load the data again.

Also it appears.NET 2.0's BindingList makes binding extremely easy along with IEditableObject. But in most cases, you don't even need to implement these.

Rocky Lhotka appeared on a [.NET Rocks! episode](https://www.dotnetrocks.com/details/66) and they had a big discussion of Business Objects versus DataSets. The use of either must change on a case by case basis. Datasets do allow you to get more for free, but if one day management decide you need to do something a little out of the ordinary, there will be problems. In contrast, business objects take longer to write (this can be minimized with a good code generator and custom templates), but stand the test of time much better than Datasets.
