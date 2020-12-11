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


<p>It is important to define your response types.</p><dl class="badImage"><dt><img src="bad-no-response-types.jpg" alt="bad-no-response-types.jpg" /></dt>
dd>​Figure: Bad example – no response types
</dl><dl class="goodImage"><dt><img src="good-response-types.png" alt="good-response-types.png" /></dt><dd>Figure: Good example – Response types (in .NET)</dd>
</dl>
<br><excerpt class='endintro'></excerpt><br>
<p><br></p><p class="ssw15-rteElement-CodeArea">/// <summary><br>/// Returns the nth number in the fibonacci sequence.<br>/// </summary><br>/// <param name="n">The index (n) of the fibonacci sequence</param><br>/// <returns>Returns the nth fibonacci number.</returns><br>/// <response code="200">int64</response><br>[HttpGet]<br>[ProducesResponseType(200)]<br>[ProducesResponseType(400)]<br>[ResponseCache(CacheProfileName = DefaultCacheProfile.Name)]<br>[Produces("application/json", "text/json")]<br>public <span class="ssw15-rteStyle-Highlight">ActionResult<long></span> Get(long n)<br>{<br>_logger.LogInformation($"Fibonacci number {n} requested");<br>if(!_fibonacciSolver.CanSolve(n))<br>return new BadRequestResult();<br>try<br>{<br>return _cache.GetOrAdd($"Fibonacci{n}", () => _fibonacciSolver.Solve(n));<br>}<br>catch (ArgumentOutOfRangeException)<br>{<br>return new BadRequestResult();<br>}<br>}</p><dd class="ssw15-rteElement-FigureBad">Figure: Good example for swashbuckle - Even b​etter if you have .NET Core 2.1 use the strong typed ActionResult – see yellow​​<br><br></dd><p class="ssw15-rteElement-CodeArea">        [HttpGet]<br>        [SwaggerResponse(HttpStatusCode.OK, typeof(long))]<br>        [SwaggerResponse(HttpStatusCode.BadRequest, typeof(void))]<br>        public <span class="ssw15-rteStyle-Highlight">ActionResult<long></span> Get(long n)<br>        {<br>            _logger.LogInformation($"Fibonacci number {n} requested");<br>            <br>            if(!_fibonacciSolver.CanSolve(n))<br>                return new BadRequestResult();<br> <br>            try<br>            {<br>                return _cache.GetOrAdd($"Fibonacci{n}", () => _fibonacciSolver.Solve(n));<br>            }<br>            catch (ArgumentOutOfRangeException)<br>            {<br>                return new BadRequestResult();<br>            }<br>        }</p><dd class="ssw15-rteElement-FigureGood">Figure: Good example for nswag - Even better if you have .NET Core 2.1 use the strong typed ActionResult – see yellow​​<br><br></dd>


