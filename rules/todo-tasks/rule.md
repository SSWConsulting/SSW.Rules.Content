---
seoDescription: Documenting "TODO" tasks ensures ideas and missing content are tracked, making it easier to prioritize and complete tasks.
type: rule
title: Do you document "TODO" tasks?
uri: todo-tasks
authors:
  - title: Adam Cogan
    url: https://www.ssw.com.au/people/adam-cogan
  - title: Matt Wicks
    url: https://www.ssw.com.au/people/matt-wicks
  - title: Matt Goldman
    url: https://www.ssw.com.au/people/matt-goldman
  - title: Daniel Mackay
    url: https://www.ssw.com.au/people/daniel-mackay
related:
  - do-you-make-todo-items-in-red
created: 2021-08-09T23:00:41.371Z
guid: 1f5d6f06-e69f-4306-9601-df6640bd5caa
---

It's common to add a `TODO` comment to some code you're working on, either because there's more work to be done here or because you've spotted a problem that will need to be fixed later. But how do you ensure these are tracked and followed up?

<!--endintro-->

We add a `TODO` comment to our code when we have either identified or introduced [technical debt](/technical-debt) as a way of showing other developers that there's work to be done here. It could be finishing the implementation of a feature, or it could be fixing a bug which (hypothetically) is limited in scope and therefore deprioritized. That's all well and good if another developer happens to be looking at that code and sees the comment, but if nobody looks at the code, then the problem could potentially never be fixed.

```cs
public class UserService(ApplicationDbContext context) : IUserService
{
    public async Task<UserDto> GetUserByEmailAsync(string emailAddress, CancellationToken cancellationToken = default)
    {
        var dbUser = await context.Users
          .AsNoTracking()
          .FirstOrDefaultAsync(u => u.Email == emailAddress, cancellationToken);

        // TODO: handle null user if not found
        return new UserDto
        {
            Id          = dbUser.Id,
            Name        = dbUser.Name,
            Email       = dbUser.Email,
            TenantId    = dbUser.TenantId.ToString()
        }
    }
}
```
::: bad
Bad example - There is problematic code here, and while the comment is useful as it immediately alerts developers to the problem, but it is not tracked anywhere
:::

Just like with any other technical debt, it's critical to ensure that it is captured on the backlog. When you add a `TODO` in your code, it should _always_ be accompanied by a link to the PBI.

```cs
public class UserService(ApplicationDbContext context) : IUserService
{
    public async Task<UserDto> GetUserByEmailAsync(string emailAddress, CancellationToken cancellationToken = default)
    {
        var dbUser = await context.Users
          .AsNoTracking()
          .FirstOrDefaultAsync(u => u.Email == emailAddress, cancellationToken);

        // TODO: handle null user if not found. See: https://github.com/SSWConsulting/SSWSockDarner/issues/324
        return new UserDto
        {
            Id          = dbUser.Id,
            Name        = dbUser.Name,
            Email       = dbUser.Email,
            TenantId    = dbUser.TenantId.ToString()
        }
    }
}
```
::: good
Good example - The `TODO` is tracked on the backlog, so the developers and the Product Owner have visibility of the problem and can plan and prioritise accordingly
:::

::: info
**Tip:** If you are reviewing a Pull Request and you spot a `TODO` without a link to a PBI, you should either create the PBI and update the code (Good Samaritan) or request the change before approving and merging the code.
:::
