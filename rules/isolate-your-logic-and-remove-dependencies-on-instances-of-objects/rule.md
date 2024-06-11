---
seoDescription: Isolate complex logic evaluations and remove dependencies on instances of objects to improve testability and maintainability.
type: rule
title: Do you isolate your logic and remove dependencies on instances of objects?
uri: isolate-your-logic-and-remove-dependencies-on-instances-of-objects
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
  - title: Daniel Mackay
    url: https://ssw.com.au/people/daniel-mackay
related: []
redirects:
  - do-you-isolate-your-logic-and-remove-dependencies-on-instances-of-objects
created: 2020-03-12T22:04:06.000Z
archivedreason: null
guid: 9f7792d8-fdb1-4e9b-926f-0cfccf25b87d
---

If there are complex logic evaluations in your code, we recommend you isolate them and write unit tests for them.

<!--endintro-->

Take this for example:

```cs
while ((ActiveThreads > 0 || AssociationsQueued > 0) && (IsRegistered || report.TotalTargets <= 1000 )
 && (maxNumPagesToScan == -1 || report.TotalTargets < maxNumPagesToScan) && (!CancelScan))
```

**Figure: This complex logic evaluation can't be unit tested**

Writing a unit test for this piece of logic is virtually impossible - the only time it is executed is during a scan and there are lots of other things happening at the same time, meaning the unit test will often fail and you won't be able to identify the cause anyway.

We can update this code to make it testable though.

Update the line to this:

```cs
while (!HasFinishedInitializing (ActiveThreads, AssociationsQueued, IsRegistered,
 report.TotalTargets, maxNumPagesToScan, CancelScan))
```

**Figure: Isolate the complex logic evaluation**

We are using all the same parameters - however, now we are moving the actual logic to a separate method.

Now create the method:

```cs
private static bool HasFinishedInitializing(int ActiveThreads, int AssociationsQueued, bool IsRegistered,
 int TotalAssociations, int MaxNumPagesToScan, bool CancelScan)
{
 return (ActiveThreads > 0 || AssociationsQueued > 0) && (IsRegistered || TotalAssociations <= 1000 )
 && (maxNumPagesToScan == -1 || TotalAssociations < maxNumPagesToScan) && (!CancelScan);
}
```

**Figure: Function of the complex logic evaluation**

The critical thing is that everything the method needs to know is passed in, it mustn't go out and get any information for itself and mustn't rely on any other objects being instantiated. In Functional Programming this is called a "Pure Function". A good way to enforce this is to make each of your logic methods static. They have to be completely self-contained.

The other thing we can do now is actually go and simplify / expand out the logic so that it's a bit easier to digest.

```cs
public class Initializer
{
    public static bool HasFinishedInitializing(
        int ActiveThreads,
        int AssociationsQueued,
        bool IsRegistered,
        int TotalAssociations,
        int MaxNumPagesToScan,
        bool CancelScan)
    {
        // Cancel
        if (CancelScan)
            return true;


        // Only up to 1000 links if it is not a registered version
        if (!IsRegistered && TotalAssociations > 1000)
            return true;


        // Only scan up to the specified number of links
        if (MaxNumPagesToScan != -1 && TotalAssociations > MaxNumPagesToScan)
            return true;


        // Not ActiveThread and the Queue is full
        if (ActiveThreads <= 0 && AssociationsQueued <= 0)
            return true;


        return false;
    }
}
```

**Figure: Simplify the complex logic evaluation**

The big advantage now is that we can unit test this code easily in a whole range of different scenarios!

```cs
public class InitializerTests
{
    [Theory()]
    [InlineData(2, 20, false, 1200, -1, false, true)]
    [InlineData(2, 20, true, 1200, -1, false, false)]
    public void Initialization_Logic_Should_Be_Correctly_Calculated(
        int activeThreads,
        int associationsQueued,
        bool isRegistered,
        int totalAssociations,
        int maxNumPagesToScan,
        bool cancelScan,
        bool expected)
    {
        // Act
        var result = Initializer.HasFinishedInitializing(activeThreads, associationsQueued, isRegistered, totalAssociations, maxNumPagesToScan, cancelScan);

        // Assert
        result.Should().Be(expected, "Initialization logic check failed");
    }
}
```

**Figure: Write a unit test for complex logic evaluation**
