---
type: rule
archivedreason: 
title: Do you define your response types?
guid: 35bd658c-dc8c-40ed-843c-1d7bd79e5331
uri: do-you-define-your-response-types
created: 2019-05-25T02:12:33.0000000Z
authors:
- id: 1
  title: Adam Cogan
related: []

---

It is important to define your response types.
<dl class="badImage">&lt;dt&gt;<img src="bad-no-response-types.jpg" alt="bad-no-response-types.jpg">&lt;/dt&gt;
dd>Figure: Bad example – no response types</dl><dl class="goodImage">&lt;dt&gt;<img src="good-response-types.png" alt="good-response-types.png">&lt;/dt&gt;<dd>Figure: Good example – Response types (in .NET)</dd></dl>
<!--endintro-->



/// <summary><br>/// Returns the nth number in the fibonacci sequence.<br>/// </summary>
/// <param name="n">The index (n) of the fibonacci sequence
/// <returns>Returns the nth fibonacci number.</returns>
/// <response code="200">int64</response>
[HttpGet]
[ProducesResponseType(200)]
[ProducesResponseType(400)]
[ResponseCache(CacheProfileName = DefaultCacheProfile.Name)]
[Produces("application/json", "text/json")]
public ActionResult Get(long n)
{
\_logger.LogInformation($"Fibonacci number {n} requested");
if(!\_fibonacciSolver.CanSolve(n))
return new BadRequestResult();
try
{
return \_cache.GetOrAdd($"Fibonacci{n}", () => \_fibonacciSolver.Solve(n));
}
catch (ArgumentOutOfRangeException)
{
return new BadRequestResult();
}
}


::: bad
Figure: Good example for swashbuckle - Even better if you have .NET Core 2.1 use the strong typed ActionResult – see yellow


:::


[HttpGet]
        [SwaggerResponse(HttpStatusCode.OK, typeof(long))]
        [SwaggerResponse(HttpStatusCode.BadRequest, typeof(void))]
        public ActionResult Get(long n)
        {
            \_logger.LogInformation($"Fibonacci number {n} requested");

            if(!\_fibonacciSolver.CanSolve(n))
                return new BadRequestResult();
 
            try
            {
                return \_cache.GetOrAdd($"Fibonacci{n}", () => \_fibonacciSolver.Solve(n));
            }
            catch (ArgumentOutOfRangeException)
            {
                return new BadRequestResult();
            }
        }


::: good
Figure: Good example for nswag - Even better if you have .NET Core 2.1 use the strong typed ActionResult – see yellow


:::
