---
type: rule
title: Passwords - Do you know that Transforms and Substitutions don’t offer
  much protection?
uri: password-complexities
authors:
  - title: Matt Goldman
created: 2022-03-17T05:10:04.385Z
guid: eaaed5d1-b812-4b31-9a10-8a69e7a2ddd5
---
Complexity requirements are valuable in that they offer a little protection, but not as much as you think. Attackers generally use 2 methods to get people’s passwords: brute force, and social engineering (see rule:…)

<!--endintro-->

Brute force means they try different combinations until they find one that works. But before trying random combinations, they start with well-known lists of words called dictionaries and rainbow tables, and the whole process is automated. Using cheap scalable cloud hosting, attackers can try billions of combinations in seconds.

When people see complexity requirements in password rules, they usually do 1 or both of 2 things: transforms and substitutions.

Transforms are when you ‘transform’ a dictionary word in some way, like changing password to password1 or password123.

Substitutions are when you substitute one character for another, like changing password to p@55w0rd.

The problem with these rules is that the majority of people use similar transforms and substitutions, so the dictionaries and rainbow tables that attackers use are filled with what are called well-known transforms and substitutions. This means that p@55w0rd, password1, password123, and many other variations are in their dictionaries, and therefore offer no more protection that the actual word itself.

It's not worth the effort trying to get clever with these: if you can think of a transform or substitution, it’s almost certainly already on the books.

If you are using complexity, a better approach is to come up with a reusable, easily remembered scheme of your own. For example, inserting !#@ between every 3rd letter which would yield pas!#@wor!#@d is significantly better than p@55w0rd.

Password1

❌Bad example

Password123

❌Bad example

P@55w0rd

❌Bad example

Pas!#@wor!#@d

✔Better example (but DON’T use the word password!)

