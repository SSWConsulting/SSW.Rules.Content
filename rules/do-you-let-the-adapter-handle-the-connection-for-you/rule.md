---
type: rule
archivedreason: 
title: Do you let the adapter handle the connection for you?
guid: 9b01cc5c-33b7-4f14-a1ed-9392b8d229df
uri: do-you-let-the-adapter-handle-the-connection-for-you
created: 2009-04-29T07:35:13.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
- title: Ryan Tee
  url: https://ssw.com.au/people/ryan-tee
  noimage: true
related: []
redirects: []

---

Did you know if you are using DataSets throughout your application (not data readers) then you don't need to have any code about connection opening or closing.

Some say it is better to be explicit. However the bottom line is less code is less bugs.

<!--endintro-->


``` dotnet
try
  {
     cnn.Open();
     adapter.Fill(dataset);
  }
  catch (SQLException ex)
  {
     MessageBox.Show(ex.Message);
  }
  finally
  {
     //I'm in the finally block so that I always get called even if the fill fails.
     cnn.Close();
  }
```
::: bad
Bad code - The connection code is not needed            
:::

```
try
  {
     adapter.Fill(dataset);
  }
  catch (SQLException ex)
  {
     MessageBox.Show(ex.Message);
  }
```
::: good
Good code - letting the adapter worry about the connection
:::

**Note:** A common comment for this rule is... "Please tell users to explicitly open and close connection - even when the .NET Framework can do for them" 

The developers who prefer the first (more explicit) code example give the following reasons:

* Explicit Behaviour is always better. Code maintainability. Explicit code is more understandable than implicit code. Don't make your other developers have to look up the fact that data adapters automatically maintain the state of your connection for them.
* Consistency (or a lack of) - not all Framework classes are documented to behave like this. For example, the IDBCommand.ExecuteNonQuery() will throw an exception if the connection isn't open (it might be an interface method, but interface exceptions are documented as a strong guideline for all implementers to follow). The SqlCommand help doesn't mention anything further about this fact, but considering it's an inherited class, it would be fair to expect it to behave the same way. A number of the other methods don't make mention of connection state, making it difficult to know which basket to put your eggs into...
* Developer Awareness - it's healthy for the developer to be aware that they have a resource that needs to be handled properly. If they learn that they don't need to open and close connections here, then when they move onto using other resource types where this isn't the case then many errors may be produced. For example, when using file resources, the developer is likely to need to pass and open stream and needs to remember to close any such streams properly before leaving the function.
* Efficiency (sort of) - In a lot of code it will often populate more than one object at a time so that if I only open the connection once, execute multiple fills or commands, then close, then it'll be more clear about what the intent of the developer. If we left it to the framework, it's likely that the connection will be opened and closed multiple times; which despite it being really cheap to open out of the connection pool it will be slightly (itty bitty bit) more efficient but I think the explicit commands will demonstrate more clearly the intention of the developer.

Bottom line - I wont be swayed - but it is a controversial one. People who agree with me include:

* Ken Getz
* Paul Sheriff
* Bill Vaughan
* George Doubinski

People who don't:

* Chris Kinsman
* Richard Campbell
* Paul Reynolds

Microsoft's online guide to [Improving ADO.NET performance](http&#58;//www.ssw.com.au/ssw/Redirect/MSDN_ADO.htm) to see their opinion and other tips.

**One final note:** This argument is a waste of time... With code generators developing most of the Data Access layer of the application, the errors, if any, will be long gone and the developer is presented with higher level of abstraction that allows him/her to concentrate on more important things rather than mucking around with connections. Particularly considering that, when we start using the Provider model from Whidbey, it won't even be clear whether you're talking to SQL Server or to an XML file.
