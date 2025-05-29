---
type: rule
title: Do you avoid using “any”?
seoDescription: Avoid using "any" to ensure type safety and avoid runtime
  errors, instead use "unknown" and leverage TypeScript's benefits such as
  intellisense and compile-time checks.
uri: avoid-using-any
authors:
  - title: Steve Leigh
    url: https://ssw.com.au/people/steve-leigh
related: []
redirects:
  - do-you-avoid-using-any
created: 2016-04-28T19:32:36.000Z
archivedreason: null
guid: aec54975-ddf2-421c-ae6d-0964f7e02b0b
---


TypeScript’s any keyword is a blessing and a curse. It is a type that can be anything, where every possible property and method exists and also returns any. It can be casted to and from anything and is how you tell the compiler to get out of your way.

However, it’s easy to use it as a crutch, and as a result, miss out on handy intellisense, refactoring support and compile-time safety – the main benefits of TypeScript!

<!--endintro-->

If you're trying to write more type-safe code, it's generally recommended to use "unknown" instead of "any" wherever possible, as it forces you to perform type checks and can help catch errors earlier in the development process.

There are two main problems with using "any" in Typescript:

**Runtime errors** - Using "any" effectively tells the compiler to treat the code you're writing as if it were written in JavaScript rather than Typescript. This is dangerous because it allows you to push code with potential runtime errors into production. These errors would ordinarily cause the Typescript compilation to fail, catching bugs before they ever reach a staging environment.

``` typescript
// The type of "person" would ordilarily match the initial assignment assignment
// because we're using "any" the implicit type is not used

let person : any = {
  name: {
    first: "foo",
    last: "bar",
  },
}

// Typescript would ordinarily flag this as a type error
// however, "any" allows strings to be assigned to objects

person = "Bob Northwind"

// This will successfully compile into JavaScript, resulting in a runtime error

console.log(person.name.first)

```

**Code maintainability** - Maintaining a large TypeScript code base where "any" is used frequently can be an absolute nightmare. Imagine you have a recurring object in your code base representing a person, with properties like "fName" and "lName". Now suppose you're using "any" as the input argument for all methods that work with this object. What happens when you want to rename "fName" to "firstName"? You’d have to do a find and replace across the entire code base, hoping that no other objects have properties with the same name.

::: bad
![Figure: Bad example – You can pass anything into this method, so you get a bad output at run time (“undefined undefined”)](any-bad.png)
:::

::: good
![Figure: Good example – Using types means you get errors and intellisense support](any-good.png)
:::

If you have ESLint enabled in your project, you can enable the [`no-explicit-any`](https://typescript-eslint.io/rules/no-explicit-any/) rule to provide useful lint warnings or errors to ensure the `any` type is not used in the project.
