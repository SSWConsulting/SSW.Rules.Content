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

`youtube: jjMbPt_H3RQ`
**Video: Enums considered harmful (9 mins)**

While TypeScript enums provide a lot of useful type safety both at runtime, it's very important to consider that there may be cleaner options. 

```ts
enum Fruits {
    Apple, Pear, Strawberry
}
```

Becomes this when compiled:

```js
var fruits;
(function (Fruits) {
    Fruits[Fruits["Apple"] = 0] = "Apple";
    Fruits[Fruits["Pear"] = 1] = "Pear";
    Fruits[Fruits["Strawberry"] = 2] = "Strawberry";
})(Fruits || (Fruits = {}));
```

However, this makes it hard to loop over the keys of the enum, as when you run `Object.keys(Fruits)` you would get the following array returned:

```ts
["0", "1", "2", "Apple", "Pear", "Strawberry"] 
```

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



```ts

enum Fruit {
  Apple = "Apple",
  Banana = "Banana",
  Strawberry = "Strawberry"
}

enum Fruit2 {
  Banana = "Banana",
  Blueberry = "Blueberry"
}

functionHere(Fruit2.Banana); // invalid if this function is expecting Fruit

```


Instead, a much cleaner option is by using [const assertions](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-3-4.html#const-assertions). By using const assertions, we can be fully sure that our code is using the string values we want:

```ts

const shops = ["Coles", "Woolworths", "Aldi"] as const;
type Shop = typeof shops[number]; // type Shop = "Coles" | "Woolworths" | "Aldi";

```

Or, if we are using an object instead of an array the same concept applies:


```tsx
const icons = {
  sun: () => <Sun />
  moon: () => <Moon />
} as const

type Icon = keyof icons; // "sun" | "moon" union type

```

