---
type: rule
title: Do you know that you should never throw an exception using System.Exception?
uri: do-you-know-that-you-should-never-throw-an-exception-using-system-exception
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
  - title: Drew Robson
    url: https://ssw.com.au/people/drew-robson
related: []
redirects: []
created: 2013-09-11T21:27:14.000Z
archivedreason: null
guid: d1c0e7ba-09e6-4b89-b2d5-695e47e18064
---

While everyone knows that `catch (Exception ex)` is bad, no one has really noticed that `throw new Exception()` is worse.

`System.Exception` is a very extensive class, and it is inherited by all other exception classes. If you throw an exception with the code `throw new Exception()`, what you need subsequently to handle the exception will be the infamous `catch (Exception ex)`.

<!--endintro-->

As a standard, you should use an exception class with the name that best describes the exception's detail. All exception classes in .NET Framework follow this standard very well. As a result, when you see exceptions like FileNotFoundException or DivideByZeroException, you know what's happening just by looking at the exception's name. The .NET Framework has provided us a comprehensive list of exception classes that we can use. If you really can't find one that is suitable for the situation, then create your own exception class with the name that best describes the exception (e.g.: EmployeeListNotFoundException).

Also, System.ApplicationException should be avoided as well unless it's an exception related to the application. While it's acceptable and should be used in certain cases, be aware that using it broadly will be just as bad as 'throw new Exception()'.

``` cs

public async Task<Unit> Handle(UpdateTodoListCommand request, CancellationToken cancellationToken)
{
        var entity = await _context.TodoLists.FindAsync(request.Id);

        if (entity == null)
        {
                throw new Exception($"Couldn't find a todo list with id: {request.Id}");
        }

        ...
}
```
::: bad
Figure: Bad example - System.Exception is thrown, you now need to read the code to try to work out what is going wrong (hard if it was thrown by code outside of this solution)
:::

``` cs

public async Task<Unit> Handle(UpdateTodoListCommand request, CancellationToken cancellationToken)
{
        var entity = await _context.TodoLists.FindAsync(request.Id);

        if (entity == null)
        {
                throw new NotFoundException(nameof(TodoList), request.Id);
        }

        ...
}
...
public class NotFoundException : Exception
{
        public NotFoundException()
            : base()
        {
        }

        public NotFoundException(string message)
            : base(message)
        {
        }

        public NotFoundException(string message, Exception innerException)
            : base(message, innerException)
        {
        }

        public NotFoundException(string name, object key)
            : base($"Entity \"{name}\" ({key}) was not found.")
        {
        }
    }
```
::: good
Figure: Good example - A specific exception is thrown which you can specifically catch, the message is consistently formatted and a consuming application can understand what was wrong with their request easily
:::