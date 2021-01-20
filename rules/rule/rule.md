---
type: rule
archivedreason:
title: Example Rule
guid:
uri: rule
created: 2021-01-20T05:06:33.0000000Z
authors: []
related:

---

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 
Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

<!--endintro-->

## This is a heading 2
Lorem ipsum dolor sit amet. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
Duis aute irure dolor in reprehenderit in voluptate [this is a link](https://ssw.com.au/rules/rule) dolore eu fugiat nulla pariatur. 
Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

### This is a heading 3
Lorem ipsum dolor sit amet, consectetur adipiscing elit, [this is an external link](http://www.google.com/), sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 
Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

#### This is a heading 4 and below is a blockquote
> Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer posuere erat a ante.  
>                                   - Someone famous in Source Title

#### Lists
* This is the first item of an unordered list
* This is the second item of an unordered list
* This is the third item of an unordered list
   * This is the first item of an unordered list inside another
   * This is the second item of an unordered list inside another
      1. This is the first item of an ordered list inside an unordered list
      1. This is the second item of an ordered list inside an unordered list 
   
&nbsp;  

1. This is the first item of an ordered list
1. This is the second item of an ordered list
1. This is the third item of an ordered list
   * This is the first item of an unordered list inside an ordered list
   * This is the second item of an unordered list inside an ordered list
      1. This is the first item of an ordered list inside another
      1. This is the second item of an ordered list inside another

  
### Boxes

::: greybox  
This is a &lt;figure&gt; using the class "greybox" with a &lt;div&gt; and no &lt;p&gt; inside - Only text straight in the div. <mark>These words</mark> are surrounded by a &lt;mark&gt;.
:::

#### Boxes with captions

::: greybox  
This is a example of a grey box  
:::  
::: bad  
Figure: Bad greybox
:::

::: greybox  
This is a example of a grey box  
:::  
**Figure: Normal greybox**

::: greybox  
This is a example of a grey box  
:::  
::: good  
Figure: Good greybox
:::

#### Other boxes

::: highlight  
This is a &lt;div&gt; using the class "highlight". If used in a &lt;p&gt; it won't get the border and paddings.  
:::

::: info  
This is a &lt;div&gt; using the class "info". Works the same as using a &lt;p&gt; . Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation.  
:::

::: china  
This is a &lt;div&gt; using the class "china". Works the same as using a &lt;p&gt; . Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.  
:::

::: todo  
This is a &lt;div&gt; using the class "todo". Works the same as using a &lt;p&gt; . Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco.  
:::

### Codes
```
This is a piece of code using <code>
```

```javascript
let iceCream = 'chocolate';
if(iceCream === 'chocolate') {
  alert('Yay, I love chocolate ice cream!');    
} else {
  alert('Awwww, but chocolate is my favorite...');    
}
```
**Figure: Javascript code block**

### Videos
Check out this video - it's responsive!  
`youtube: https://www.youtube.com/embed/0ugMkda9IBw`

### Images
::: bad  
![Figure: Bad figure](https://images.unsplash.com/photo-1542014740373-51ad6425eb7c?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1000&q=80)
:::

![Figure: Normal figure](https://images.unsplash.com/photo-1513677785800-9df79ae4b10b?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1000&q=80)

::: ok  
![Figure: OK figure](https://images.unsplash.com/photo-1478998674531-cb7d22e769df?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1000&q=80)
:::

::: good  
![Figure: Good figure](https://images.unsplash.com/photo-1491472253230-a044054ca35f?ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&q=80)
:::

![Figure: How a smaller image (400px) works with long caption. Full screen on mobile, real width on larger screens](https://images.unsplash.com/photo-1528820454441-189cd70a6c3c?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=400&q=80)

![Figure: Short caption](https://images.unsplash.com/photo-1528820454441-189cd70a6c3c?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=400&q=80)

