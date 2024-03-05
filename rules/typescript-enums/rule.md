---
type: rule
title: UPS - Do you have your UPS send an email when it kicks in?
uri: ups-send-email
authors:
  - title: Harry Ross
    url: https://ssw.com.au/people/harry-ross
related: []
redirects:
  - good-typescript-configuration
created: 2017-07-01T00:21:30.000Z
archivedreason: null
guid: ba19be99-354d-44b2-a2da-4131cc660f18
---
While you might expect TypeScript enums to function like strongly typed languages like C# and Rust, often this is not the case. 

<!--endintro-->

Firstly, numeric enums are not type safe, which means you can pass off any numeric value as a member of that type. 

```ts

enum Fruit {
  Apple, 
  Banana, 
  Strawberry
}

const eat = (fruit: Fruit) => {
  // code here
}

eat(10) // valid typescript code

```


Instead, a much cleaner option was added in TypeScript 3.4 - the [const assertion](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-3-4.html#const-assertions). By using const assertions, we can be fully sure that our code is using the string values we want:

```ts

const shops = ["Coles", "Woolworths", "Aldi"] as const;
type Shop = typeof shops[number]; // type Shop = "Coles" | "Woolworths" | "Aldi";

```

Also, often people may misuse enums: 

```ts

enum Fruit {
  Apple = "Apple",
  Banana = "Banana",
  Strawberry = "Strawberry"
}

```

This reduces code clarity, and can lead to incorrect usage 