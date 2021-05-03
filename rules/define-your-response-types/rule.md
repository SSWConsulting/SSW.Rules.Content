---
type: rule
archivedreason: 
title: Do you define your response types?
guid: 35bd658c-dc8c-40ed-843c-1d7bd79e5331
uri: define-your-response-types
created: 2019-05-25T02:12:33.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
- do-you-define-your-response-types

---

It is important to define your response types.

::: bad  
![Figure: Bad example – no response types ](bad-no-response-types.jpg)  
:::

::: good  
![Figure: Good example – Response types (in .NET)](good-response-types.png)  
:::

<!--endintro-->

```cs
/// <summary>
/// Returns the nth number in the fibonacci sequence.
/// </summary>
/// <param name="n">The index (n) of the fibonacci sequence</param>
/// <returns>Returns the nth fibonacci number.</returns>
/// <response code="200">int64</response>
[HttpGet]
[ProducesResponseType(200)]
[ProducesResponseType(400)]
[ResponseCache(CacheProfileName = DefaultCacheProfile.Name)]
[Produces("application/json", "text/json")]
public ActionResult<long> Get(long n)
{
    _logger.LogInformation($"Fibonacci number {n} requested");
    if(!_fibonacciSolver.CanSolve(n))
    {
        return new BadRequestResult();
    }

    try
    {
        return _cache.GetOrAdd($"Fibonacci{n}", () => _fibonacciSolver.Solve(n));
    }
    catch (ArgumentOutOfRangeException)
    {
        return new BadRequestResult();
    }
}
```
::: good
Figure: Good example for swashbuckle - Even better if you have .NET Core 2.1 use the strong typed ActionResult
:::

```cs
[HttpGet]
[SwaggerResponse(HttpStatusCode.OK, typeof(long))]
[SwaggerResponse(HttpStatusCode.BadRequest, typeof(void))]
public ActionResult<long> Get(long n)
{
    _logger.LogInformation($"Fibonacci number {n} requested");
    
    if(!_fibonacciSolver.CanSolve(n))
    {
        return new BadRequestResult();
    }

    try
    {
        return _cache.GetOrAdd($"Fibonacci{n}", () => _fibonacciSolver.Solve(n));
    }
    catch (ArgumentOutOfRangeException)
    {
        return new BadRequestResult();
    }
}
```
::: good
Figure: Good example for nswag - Even better if you have .NET Core 2.1 use the strong typed ActionResult
:::
