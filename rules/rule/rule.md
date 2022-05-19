---
type: rule
title: Example Rule + Markdown Cheatsheet
uri: rule
authors:
  - title: Christian Morford-Waite
    url: https://ssw.com.au/people/christian-morford-waite
  - title: Sebastien Boissiere
    url: https://ssw.com.au/people/sebastien-boissiere
  - title: Tiago Araujo
    url: https://ssw.com.au/people/tiago-araujo
related:
  - do-you-understand-the-value-of-consistency
created: 2021-01-20T05:06:33.000Z
archivedreason: null
guid: 55db32aa-0718-4868-995c-673d8dd69f62
---

This is an example rule to show you what is possible for a rule. 
Below you will see everything you need to create an awesome page. 

<!--endintro-->

# This is a heading 1
Lorem ipsum dolor sit amet. Ut enim ad minim veniam, quis nostrud exercitation. qui officia deserunt mollit anim id est laboru.
Duis aute [this is a link](https://ssw.com.au/rules/rule) dolore  nulla [this is an external link](http://www.google.com/) pariatur. 
Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborumsunt in culpa qui officia.

## This is a heading 2
### This is a heading 3
#### This is a heading 4 
##### This is a heading 5
###### This is a heading 6 and below is a blockquote
> Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer posuere erat a ante.  
>                                   - Someone famous in Source Title

#### Unordered List
* This is the first item of an unordered list
* This is the second item of an unordered list
* This is the third item of an unordered list
   * This is the first item of an unordered list inside another
   * This is the second item of an unordered list inside another
      1. This is the first item of an ordered list inside an unordered list
      2. This is the second item of an ordered list inside an unordered list 

#### Ordered List
1. This is the first item of an ordered list
2. This is the second item of an ordered list
3. This is the third item of an ordered list
   * This is the first item of an unordered list inside an ordered list
   * This is the second item of an unordered list inside an ordered list
      1. This is the first item of an ordered list inside another
      2. This is the second item of an ordered list inside another

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

::: codeauditor
This is a &lt;div&gt; using the class "codeauditor". Works the same as using a &lt;p&gt; . Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.  
:::

::: todo  
This is a &lt;div&gt; using the class "todo". Works the same as using a &lt;p&gt; . Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco.  
:::

### Code

```
This is a piece of code in a code block
```
::: bad  
Figure: Bad Example - This isn't actual code  
:::  

See this [json file](https://unpkg.com/gatsby-remark-vscode@1.0.3/lib/grammars/manifest.json) for all supported languages and their aliases we can use in Rules. See below for some examples:

```javascript
let iceCream = 'chocolate';
if(iceCream === 'chocolate') {
  alert('Yay, I love chocolate ice cream!');    
} else {
  alert('Awwww, but chocolate is my favorite...');    
}
```
**Figure: Javascript code block**


```sql
IF EXISTS (SELECT 1 FROM 
               INFORMATION_SCHEMA.TABLES 
           WHERE 
               TABLE_TYPE='BASE TABLE' AND 
               TABLE_NAME='Employees'
           ) 
    ALTER TABLE [dbo].[Employees]( …… ) ON [PRIMARY] 
ELSE 
    CREATE TABLE [dbo].[Employees]( …… ) ON [PRIMARY]
```
**Figure: SQL code block**


```cs
public class MyClass
{
    public string  myField = string.Empty;

    public MyClass()
    {
    }

    public void MyMethod(int parameter1, string parameter2)
    {
        Console.WriteLine("First Parameter {0}, second parameter {1}", 
                                                    parameter1, parameter2);
    }

    public int MyAutoImplementedProperty { get; set; }

    private int myPropertyVar;
    
    public int MyProperty
    {
        get { return myPropertyVar; }
        set { myPropertyVar = value; }
    } 
}
```
**Figure: C Sharp code block**


```cpp
#include <iostream>
using namespace std;

int main() 
{    
    cout << "Size of char: " << sizeof(char) << " byte" << endl;
    cout << "Size of int: " << sizeof(int) << " bytes" << endl;
    cout << "Size of float: " << sizeof(float) << " bytes" << endl;
    cout << "Size of double: " << sizeof(double) << " bytes" << endl;

    return 0;
}
```
**Figure: C++ code block**


```json
{
    "glossary": {
        "title": "example glossary",
	"GlossDiv": {
        "title": "S",
	"GlossList": {
        	"GlossEntry": {
			"ID": "SGML",
			"SortAs": "SGML",
			"GlossTerm": "Standard Generalized Markup Language",
			"Acronym": "SGML",
			"Abbrev": "ISO 8879:1986",
			"GlossDef": {
				"para": "A meta-markup language, used to create markup languages such as DocBook.",
				"GlossSeeAlso": ["GML", "XML"]
			},
			"GlossSee": "markup"
		}
            }
        }
    }
}
```
**Figure: JSON code block**

```markdown
*This text will be italic*
_This will also be italic_

**This text will be bold**
__This will also be bold__

_You **can** combine them_
```
**Figure: Markdown code block**


### Twitter Card Embed  
`oembed: https://twitter.com/MrHinsh/status/24123713864`

To add a twitter card, copy the link of the tweet then add it to the rule with backticks on each side like this.
```markdown
`oembed: https://twitter.com/MrHinsh/status/24123713864`
```

You can also add a good or bad caption to embeded tweets e.g.
```markdown
`oembed: https://twitter.com/MrHinsh/status/24123713864`

::: good
Figure: My embedded tweet
:::
```

### Email Template  
::: email-template  
|          |     |
| -------- | --- |
| To:      | XXX |
| Cc:      | YYY |
| Bcc:     | ZZZ |
| Subject: | This is the subject |  
::: email-content  

### Hi XXX,  
[Email content]    

:::  
:::  
::: good  
Figure: Good Example - Nice email template  
:::

#### Code for Email Template

```
::: email-template  
|          |     |
| -------- | --- |
| To:      | XXX |
| Cc:      | YYY |
| Bcc:     | ZZZ |
| Subject: | This is the subject |  
::: email-content  

### Hi XXX,  
[Email content]    

:::  
:::  
::: good  
Figure: Good Example - Nice email template  
:::
```

### Organisation Only Content  
::: hidden  
e7d15b01-2a21-4e0f-bc71-c09e5d356cbc-7947936  
:::  

::: hidden  
bfb265e3-644e-4cbe-b17c-4d378b014809-7947936  
:::  

### Videos
Check out this video - it's responsive!  
`youtube: https://www.youtube.com/embed/0ugMkda9IBw`

Adding a video is similar to a tweet:
```md
`youtube: https://www.youtube.com/embed/0ugMkda9IBw`
```

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

::: img-small  
![Figure: Small Normal figure](https://images.unsplash.com/photo-1513677785800-9df79ae4b10b?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1000&q=80)
:::

::: img-medium  
![Figure: Medium Normal figure](https://images.unsplash.com/photo-1513677785800-9df79ae4b10b?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1000&q=80)
:::

::: img-large  
![Figure: Large Normal figure](https://images.unsplash.com/photo-1513677785800-9df79ae4b10b?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1000&q=80)
:::

![Figure: How a smaller image (400px) works with long caption. Full screen on mobile, real width on larger screens](https://images.unsplash.com/photo-1528820454441-189cd70a6c3c?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=400&q=80)

![Figure: Short caption](https://images.unsplash.com/photo-1528820454441-189cd70a6c3c?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=400&q=80)

![Figure: Relative image - in the same folder as the rule](earth_from_space.jpg)


### Horizontal Rules
---
***
___

### Text decoration

**bold** or **bold**  
_italic_ or _italic_  
**combined bold and _italic_**  
~~strikethrough~~  

### Tables
&nbsp; 

| Tables        |      Are      |   Cool |
| ------------- | :-----------: | -----: |
| col 3 is      | right-aligned | \$1600 |
| col 2 is      |   centered    |   \$12 |
| zebra stripes |   are neat    |    \$1 |

&nbsp; 

| Markdown | Less      | Pretty     |
| -------- | --------- | ---------- |
| _Still_  | `renders` | **nicely** |
| 1        | 2         | 3          |

#### Code for tables

```
| Tables        |      Are      |   Cool |
| ------------- | :-----------: | -----: |
| col 3 is      | right-aligned | \$1600 |
| col 2 is      |   centered    |   \$12 |
| zebra stripes |   are neat    |    \$1 |
```
---

### Links

[I'm an inline-style link](https://www.google.com)  

[I'm an inline-style link with title](https://www.google.com "Google's Homepage")  

[I'm a reference-style link][arbitrary case-insensitive reference text]  

[You can use numbers for reference-style link definitions][1]   
Or leave it empty and use the [link text itself].  

URLs and URLs in angle brackets will automatically get turned into links.  

http://www.example.com or <http://www.example.com> and sometimes example.com (but not on Github, for example).  

Some text to show that the reference links can follow later.

[arbitrary case-insensitive reference text]: https://www.mozilla.org  
[1]: http://slashdot.org  
[link text itself]: http://www.reddit.com

**Note:** We use [icons on files' links to not to surprise users](/use-icons-to-not-surprise-users).
