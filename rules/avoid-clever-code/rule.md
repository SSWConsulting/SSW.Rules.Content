---
type: rule
title: Tech Debt - Do you avoid 'clever' code?
uri: avoid-clever-code
authors:
  - title: Luke Parker
    url: https://ssw.com.au/people/luke-parker
related:
  - technical-debt
created: 2022-05-13T10:19:05.000Z
archivedreason: null
guid: ec1a95c9-e313-4dcb-99e9-a7a02d93567e
---

### What is Clever Code?

Clever Code comes in several forms. The desired form is solving a complex problem, in a simple way. The Clever Code that causes tech debt, is when code is written in a way to use the language features to look 'smart', while making it difficult for developers to read.

<!--endintro-->

```
var totalMoved = sortedChannels.Where((channel, i) => channel.Position != i).Count();
```

::: bad
Bad example - Smart code, that could be even simpler! (Although, not bad by any means)
:::

```
var totalMoved = 0;

for (var i = 0; i < sortedChannels.Count; i++)
{
    var channel = sortedChannels[i];

    if (channel.Position != i)
    {
        totalMoved++
    }
}
```

::: good
Good example - Simple code, while it has more lines, it is easier to read!
:::

### When is Simple Code Bad?

Let's take a moment to digest this more generic example:

```
[ProducesResponseType(StatusCodes.Status404NotFound)]
[ProducesResponseType(StatusCodes.Status204NoContent)]
[HttpDelete("{id:guid}")]
public async Task<IActionResult> Delete(Guid id)
{
    var model = await _context.Styles.FirstOrDefaultAsync(x => x.Id == id);

    if (model is null)
    {
        return NotFound();
    }

    _context.Styles.Remove(model);
    await _context.SaveChangesAsync();

    return NoContent();
}
```

At first glance, this is pretty simple - almost what you would find on an intro to EF Core & ASP.NET Core Web API on the Microsoft documentation!

As code scales, sometimes we need to write more 'clever' code, to abstract away concerns (like data access, or application logic).

So depending on the context, this is both good & bad code at the same time!
