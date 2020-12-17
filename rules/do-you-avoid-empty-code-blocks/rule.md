---
type: rule
archivedreason: 
title: Do you avoid Empty code blocks?
guid: 87d8d6e4-deba-44bf-a5db-4cc8b2c937b5
uri: do-you-avoid-empty-code-blocks
created: 2018-04-30T22:08:47.0000000Z
authors:
- id: 1
  title: Adam Cogan
related: []

---

Empty Visual C# .NET methods consume program resources unnecessarily. Put a comment in code block if its stub for future application.
Don’t add empty C# methods to your code. If you are adding one as a placeholder for future development, add a comment with a TODO.

Also, to avoid unnecessary resource consumption, you should keep the entire method commented until it has been implemented.


If the class implements an inherited interface method, ensure the method throws NotImplementedException.


<!--endintro-->

public class Example
 {
       public double salary()
       {     
       }
 }


::: bad
Figure: Bad Example - Method is empty

:::


public class Sample
 {
       public double salary()
       {
               return 2500.00;
        }
 }


::: good
Figure: Good Example - Method implements some code

:::


public interface IDemo
 {
       void DoSomethingUseful();
       void SomethingThatCanBeIgnored();
 }
public class Demo : IDemo
 {
       public void DoSomethingUseful()
       {
              // no audit issues
             Console.WriteLine("Useful");
       }
       // audit issues 
      public void SomethingThatCanBeIgnored()
      { 
      } 
 }


::: bad
Figure: Bad Example - No Comment within empty code block
:::


public interface IDemo
 {
       void DoSomethingUseful();
       void SomethingThatCanBeIgnored();
 }
public class Demo : IDemo
 {
       public void DoSomethingUseful()
       {
              // no audit issues
              Console.WriteLine("Useful");
       }
       // No audit issues 
       public void SomethingThatCanBeIgnored() 
       {
              // stub for IDemo interface
       } 
 }


::: good
Figure: Good Example - Added comment within Empty Code block method of interface class
:::
