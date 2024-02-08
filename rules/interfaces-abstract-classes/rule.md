---
type: rule
title: Reading Source Code - Do you understand the importance of Interfaces and Abstract Classes?
uri: interfaces-abstract-classes
authors:
  - title: Luke Mao
    url: https://www.ssw.com.au/people/luke-mao
created: 2023-07-01T00:00:00.000Z
guid: dc2f25d6-46b4-4917-8328-70459c7f8165
---

When embarking on understanding a new codebase, it's crucial to identify the components that offer the most insight with the least effort. Interfaces and Abstract Classes stand out as the pillars that uphold the structure and behavior of the code, providing a clear overview without delving into the intricate details of implementation.

<!--endintro-->

`youtube: https://youtu.be/9j-uECGrqSI`

**Video: How to Read Source Code: Interfaces and Abstract Classes | Luke Mao | SSW Rules (6 min)**

### Why Interfaces and Abstract Classes are important
Interfaces and Abstract classes provide 2 main insights by helping you:
- Know data structures and their relationships​
- Know what functionality a class can provide

### What is an Interface?

An interface defines properties and methods that a class must implement. It only provides the method signatures without any implementation details.​

Imagine we have objects of different shapes, such as circles and rectangles. Each shape can have its own color. Also all shapes have area and that area can be calculated. But the calculation changes depending on the type of shape. For example, a circle calculates area using PI and radius while a rectangle uses the width and height.​

So we can define an interface called Shape. It declares a property called color and a method called area. The specific implementation will be inside the Circle and Rectangle class.​

The role of the interface is to reduce coupling. For example, if you need to change how area is calculated for a rectangle but not for a circle, you can do so without affecting how the circle behaves. It also improves scalability. Every time a new shape is added, there is already a set of well-defined methods making it easier to add the new class.​

Interfaces are contracts that dictate what a class can do without specifying how it does it. They are crucial in defining behavior and ensuring consistency across different implementations.

### What is an Abstract Classes?

An abstract class is a class that cannot be instantiated and serves as a blueprint for creating derived classes. It's similar to an interface but also allows you to provide fully implemented methods, not just method declarations.​

Imagine we have various payment methods, such as bank transfer and credit card payment. ​

We can define an abstract class called Payment. It's similar to an interface. It defines a property called amount and a method called processPayment. processPayment changes depending on the payment method. There is also a receipt method and unlike the processPayment method. It should be the same for all kinds of payment methods. This can be directly implemented in the abstract class, but not in an interface.​

The main purpose of abstract class is to solve the code reuse problem. If we don’t use Payment abstract class here, BackTransfer and CreditCardPayment classes will end up having duplicate receipt methods.​

### When to Focus on Interfaces and Abstract Classes
The best time to read interfaces and abstract classes is:
- After understanding the business problem​
- Before diving into implementation details

### Conclusion
Knowing when and how to read interfaces and abstract classes not only streamlines your learning process but also equips you with a framework to understand the broader system architecture and its components.

