---
type: rule
title: Do you know how LINQ has evolved?
uri: how-linq-has-evolved
authors:
  - title: Bryden Oliver
    url: https://www.ssw.com.au/people/bryden-oliver
  - title: Adam Cogan
    url: https://www.ssw.com.au/people/adam-cogan
created: 2021-12-13T16:14:34.287Z
guid: 77170593-5069-45ee-baf1-318356e37efa
---
How LINQ has evolved:

<!--endintro-->

### In .NET 1.1 - ArrayLists

**(System.Collections)**

ArrayList - Implements the IList interface using an array whose size is dynamically increased as required.

Example:

```cs
ArrayList greeks = new ArrayList();
    greeks.Add("Alexopoulos");
    greeks.Add("Gianopoulos");
    greeks.Add("Michaelides");
 
    //and
    ArrayList names = new ArrayList();
    foreach(string g in greeks)
    {
        if(g.IndexOf(“opoulos”) > -1)
        {
            names.Add(g);
        }
    }
```

### In .NET 2.0 -Generic Lists - enforces type, more OO, reduce code if different types

**(System.Collections.Generic)**

List \<T\>: IList - The List class is the generic equivalent of the ArrayList class. It implements the IList generic interface using an array whose size is dynamically increased as required.

Example:

```cs
List<string> greeks = new List<string>();
greeks.Add("Alexopoulos");
greeks.Add("Gianopoulos");
greeks.Add("Michaelides");
 
//and
List<string> names = new List<string>();
foreach(string g in greeks)
{
    if(g.Contains(“opoulos”))
    {
        names.Add(g);
    }
}  
```

### In .NET 3.5 - nicer to query

**(System.Linq)**

```cs
IQueryable<out T> : IEnumerable<T>, 
         IQueryable, IEnumerable
```

The IQueryable<T> interface is intended for implementation by query providers. This interface inherits the IEnumerable<T> interface so that if it represents a query, the results of that query can be enumerated. Enumeration forces the expression tree associated with an IQueryable object to be executed.

```cs
List<string> greeks = new List<string>();
greeks.Add("Alexopoulos");
greeks.Add("Gianopoulos");
greeks.Add("Michaelides");
 
//and
IEnumerable<string> opoulos = greeks.Where(x => x.Contains(“opoulos”));
```

### In .NET 4.0 (thread safe)

**(System.Collections.Concurrent)**

(The System.Collections.Concurrent namespace provides several thread-safe collection classes that should be used in place of the corresponding types in the System.Collectionsand System.Collections.Generic namespaces whenever multiple threads are accessing the collection concurrently.)

```cs
public class ConcurrentBag<T> : IProducerConsumerCollection<T>, 
         IEnumerable<T>, ICollection, IEnumerable
 
Represents a thread-safe, unordered collection of objects.
 
    // Demonstrates: 
    //      ConcurrentBag<T>.Add() 
    //      ConcurrentBag<T>.IsEmpty 
    //      ConcurrentBag<T>.TryTake() 
    //      ConcurrentBag<T>.TryPeek() 
    static void Main()
    {
        // Construct and populate the ConcurrentBag
        ConcurrentBag<string> cb = new ConcurrentBag<string>();
        cb.Add("Alexopoulos");
        cb.Add("Gianopoulos");
        cb.Add("Michaelides");
 
        // Consume the items in the bag 
        int item;
        while (!cb.IsEmpty)
        {
            if (cb.TryTake(out item))
                Console.WriteLine(item);
            else
                Console.WriteLine("TryTake failed for non-empty bag");
        }
 
        // Bag should be empty at this point 
        if (cb.TryPeek(out item))
            Console.WriteLine("TryPeek succeeded for empty bag!");
    }
```

### In .NET 4.5 (casting backwards - read only)

**(System.Collections.Generic)**

```cs
public class List : IList, ICollection, 
         IList, ICollection, IReadOnlyList, IReadOnlyCollection, IEnumerable, 
         IEnumerable
```

The Microsoft .NET Framework 4.5 includes the IReadOnlyList, IReadOnlyDictionary and IReadOnlyCollection generic interfaces. The main benefit is that the new interfaces are covariant, except for IReadOnlyDictionary. This means that you can use a derived type as the generic parameter, when passing in a collection into a method that's defined for a base type. If you have a Dog class, for example, that derives from Animal, you can have a method that accepts an IReadOnlyList<Animal> and pass it an IReadOnlyList<Dog>.

```cs
public class Greek : Person
{
..
}
 
List greeks = new List()
{
    new Greek() { LastName  = "Alexopoulos" },
    new Greek () { LastName = "Gianopoulos" },
    new Greek () { LastName  = "Michaelides" },
};
// IReadOnlyList supports covariance
IReadOnlyList<Person> people = greeks;
Person first = people[0];
```
