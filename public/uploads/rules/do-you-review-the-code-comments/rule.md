---
seoDescription: Code comments should be used judiciously to clarify code intentions and avoid unnecessary duplication of information.
type: rule
archivedreason:
title: Do you review the code comments?
guid: 4a1ae65e-893e-44cd-a37b-9b914909b291
uri: do-you-review-the-code-comments
created: 2012-04-01T09:31:34.0000000Z
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
  - title: Damian Brady
    url: https://ssw.com.au/people/damian-brady
related: []
redirects: []
---

Comments can be useful for documenting code but should be used properly. Some developers like seeing lots of code comments and some don't.

<!--endintro-->

Some tips for including comments in your code are:

1. Comments aren't always the solution.  Sometimes it's better to refactor the comments into the actual method name. If your method needs a comment to tell a developer what it does, then the method name is probably not very clear.
2. Comments should never say **\*what\*** the code does, it should say **\*why\*** the code does it.  Any decent developer can work out what a piece of code does.
3. Comments can also be useful when code is missing.  For example, why there is no locking code around a thread-unsafe method.

// returns the Id of the first customer with the matching last name
public int GetResult(string lastname)
{
    // get the first matching customer from the repository
    return repository.Customer.First(c =&gt; c.LastName.StartsWith(lastname));
} Figure: Bad Example - The first comment is only valuable because the method is poorly named, while the second describes \*what\* is happening, not \*why\*public int GetFirstCustomerWithLastName(string lastname)
{
    // we use StartsWith because the legacy system sometimes padded with spaces
    return repository.Customer.First(c =&gt; c.LastName.StartsWith(lastname));
}Figure: Good Example - The method has been renamed so no comment is required, and the comment explains \*why\* the code has been written in that way
