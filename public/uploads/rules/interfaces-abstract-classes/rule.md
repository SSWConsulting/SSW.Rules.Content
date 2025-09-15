---
seoDescription: Interfaces and abstract classes provide a clear overview of code structure and behavior without delving into implementation details.
type: rule
title: Reading Source Code - Do you understand the importance of interfaces and
  abstract classes?
uri: interfaces-abstract-classes
authors:
  - title: Luke Mao
    url: https://www.ssw.com.au/people/luke-mao
  - title: Andrew Harris
    url: https://www.ssw.com.au/people/andrew-harris
  - title: Matt Wicks
    url: https://www.ssw.com.au/people/matt-wicks
related:
  - read-source-code
created: 2023-07-01T00:00:00.000Z
guid: dc2f25d6-46b4-4917-8328-70459c7f8165
---

When embarking on understanding a new codebase, it's crucial to identify the components that offer the most insight with the least effort. Interfaces and Abstract Classes stand out as the pillars that uphold the structure and behavior of the code, providing a clear overview without delving into the intricate details of implementation.

<!--endintro-->

`youtube: https://youtu.be/9j-uECGrqSI`

**Video: How to Read Source Code: Interfaces and abstract classes | Luke Mao | SSW Rules (6 min)**

### Why interfaces and abstract classes are important

Interfaces and abstract classes provide 2 main insights by helping you know:

- Data structures and their relationships​
- What functionality a class can provide

### What is an interface?

An interface defines properties and methods that a class must implement. It only provides the method signatures without any implementation details.​

Imagine we have objects of different shapes, such as circles and rectangles. Each shape can have its own color. Also, all shapes have an area that can be calculated. However, the calculation changes depending on the type of shape. For example, a circle calculates area using PI and radius, while a rectangle uses the width and height.​

So, we can define an interface called `Shape`:

```typescript
interface Shape {
  color: string;
  area(): number;
}
```

It declares a property called color and a method called area. The specific implementation will be inside the `Circle` and `Rectangle` class.​

#### Circle class

```typescript
class Circle implements Shape {
  color: string;
  radius: number;

  constructor(color: string, radius: number) {
    this.color = color;
    this.radius = radius;
  }

  area(): number {
    return Math.PI * this.radius * this.radius;
  }
}
```

#### Rectangle class

```typescript
class Rectangle implements Shape {
  color: string;
  width: number;
  height: number;

  constructor(color: string, width: number, height: number) {
    this.color = color;
    this.width = width;
    this.height = height;
  }

  area(): number {
    return this.width * this.height;
  }
}
```

These implementations can then be instantiated separately depending on the kind of shape that is needed.

```typescript
const circle = new Circle("red", 10);
console.log(circle.color); // outputs "red"
console.log(circle.area()); // outputs "314.1592653589793"

const rectangle = new Rectangle("blue", 5, 10);
console.log(rectangle.color); // outputs "blue"
console.log(rectangle.area()); // outputs "50"
```

Its important to note that you can get interfaces wrong. For example you could not use interfaces or you could over use interfaces

```typescript
interface Animal {
  eat(): void;
}

interface Mammal extends Animal {
  breathe(): void;
}

interface Dog extends Mammal {
  bark(): void;
}

interface Bulldog extends Dog {
  snore(): void;
}
```

::: bad
Figure: Bad Example - When you over abstract, it becomes harder to find the right place to add new methods
:::

The role of the interface is to reduce coupling. For example, if you need to change how the area is calculated for a rectangle but not for a circle, you can do so without affecting how the circle behaves. It also improves scalability. Every time a new shape is added, there is already a set of well-defined methods, making it easier to add the new class.​

Interfaces are contracts that dictate what a class can do without specifying how it does it. They are crucial in defining behavior and ensuring consistency across different implementations.

### What is an abstract class?

An abstract class is a class that cannot be instantiated and serves as a blueprint for creating derived classes. It's similar to an interface but allows you to provide fully implemented methods, not just method declarations.​ A class that uses an abstract class is known as a concrete class.

Imagine various payment methods, such as bank transfer and credit card payment. ​

We can define an abstract class called Payment:

```typescript
abstract class Payment {
  amount: number;

  constructor(amount: number) {
    this.amount = amount;
  }

  abstract processPayment(): void;

  receipt(): void {
    console.log(`Payment of $${this.amount} has been processed.`);
  }
}
```

It's similar to an interface. It defines a property called `amount` and a method called `processPayment`. `processPayment` will change depending on the payment method. There is also a `receipt` method, and unlike the `processPayment` method, it should be the same for all kinds of payment methods. This `receipt` method can be directly implemented in an abstract class but not in an interface.​

This abstract class would then be used to define different types of payments, such as Bank Transfer or Credit Card Payment:

#### Bank Transfer class

```typescript
class BankTransfer extends Payment {
  processPayment(): void {
    console.log(`Processing a bank transfer of $${this.amount}`);
  }
}
```

#### Credit Card Payment class

```typescript
class CreditCardPayment extends Payment {
  processPayment(): void {
    console.log(`Processing a credit card payment of $${this.amount}`);
  }
}
```

These implementations can then be instantiated separately depending on the kind of payment that is needed.

```typescript
const bankTransfer = new BankTransfer(512);
bankTransfer.processPayment(); // Processing a bank transfer of $512
bankTransfer.receipt(); // Payment of $512 has been processed.

const creditCardPayment = new CreditCardPayment(1024);
creditCardPayment.processPayment(); // Processing a credit card payment of $1024
creditCardPayment.receipt(); // Payment of $1024 has been processed.
```

The primary purpose of abstract classes is to solve code reuse problems. If we don't use a Payment abstract class here, the `BankTransfer` and `CreditCardPayment` classes will have duplicate receipt methods.​

### When to focus on interfaces and abstract classes

The best time to read interfaces and abstract classes is:

- After understanding the business problem
- Before diving into implementation details

### Other Benefits

There more benefits to using interfaces and abstract classes such as in Unit Testing which you can read [here](https://www.mehulkar.com/blog/2015/05/unit-testing-interface-vs-implementation/)

### Conclusion

Knowing when and how to read interfaces and abstract classes streamlines your learning process and equips you with a framework to understand the broader system architecture and its components.
