---
type: rule
title: Do you optimise your JavaScript code with Lodash wisely and efficiently?
uri: optimise-js-with-lodash
authors:
  - title: Jack Pettit
    url: https://www.ssw.com.au/people/jack-pettit/
created: 2023-08-01T23:51:13.657Z
guid: 14157333-05fd-492d-a443-6eeb389a654a
---
Do you want to make your JavaScript code more efficient and easier to read? Lodash might be the utility library you need. But like any tool, knowing when and how to use it is crucial for the maintainability and performance of your project.

JavaScript is a powerful language, but it can sometimes be tricky to write clean, efficient code. This is where Lodash shines. Lodash is a JavaScript utility library providing handy methods for manipulating and combining arrays, objects, numbers, strings, among other data types.

<!--endintro-->

::: info  
For optimal bundle size and tree-shaking capabilities in modern JavaScript applications, we recommend using [lodash-es](https://www.npmjs.com/package/lodash-es) over the standard lodash library.
:::

## The why and when to use lodash

Lodash simplifies JavaScript by easing the work with arrays, numbers, objects, strings, and more. Its API is straightforward, with hundreds of functions at your disposal for tasks from object manipulation to array sorting, filtering, and more. Lodash can make your code concise, readable, and thus more maintainable.

Lodash should be used when its methods provide a clearer, more efficient way of achieving your goals than the equivalent native JavaScript methods. It can save significant time and reduce errors in your code. However, Lodash should not be used indiscriminately. 

Always consider the trade-off between adding an extra dependency to your project and achieving your goal using native JavaScript methods.


### A simple misuse of Lodash

Here's an example where using Lodash's `_.map` method is unnecessary:

::: bad
```js
const arr = [1, 2, 3];
const newArr = _.map(arr, function(n) { return n * 3; });
console.log(newArr);
// output: [3, 6, 9]
```
Figure: using Lodash's _.map method
:::

::: good
```js
const arr = [1, 2, 3];
const newArr = arr.map(n => n * 3);
console.log(newArr);
// output: [3, 6, 9]
```
Figure: using the native JavaScript Array.map() method
:::

In the above example it is more efficient to use the native implementation and would not require adding the Lodash dependency. Which adds bloat to the 


### A good use of Lodash

Consider an example where you have an array of objects, and you need to find an object with specific property values. 

::: bad
```js
const user = users.find(user => user.age === 1 && user.active === true);
console.log(user);
// output: { 'user': 'pebbles', 'age': 1, 'active': true }
```
Figure: native JavaScript find method
:::

::: good
```js
import { find } from 'lodash-es';

const users = [
  { 'user': 'barney',  'age': 36, 'active': true },
  { 'user': 'fred',    'age': 40, 'active': false },
  { 'user': 'pebbles', 'age': 1,  'active': true }
];

const user = find(users, { 'age': 1, 'active': true });
console.log(user);
// output: { 'user': 'pebbles', 'age': 1, 'active': true }
```
Figure: Lodash's _.find method 
:::