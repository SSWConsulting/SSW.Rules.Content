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


<p>It is important to define your response types.</p><dl class="badImage"><dt><img src="bad-no-response-types.jpg" alt="bad-no-response-types.jpg" /></dt>
dd&gt;​Figure: Bad example – no response types
</dl><dl class="goodImage"><dt><img src="good-response-types.png" alt="good-response-types.png" /></dt><dd>Figure: Good example – Response types (in .NET)</dd>
</dl>
<br><excerpt class='endintro'></excerpt><br>
<p><br></p><p class="ssw15-rteElement-CodeArea">/// &lt;summary&gt;<br>/// Returns the nth number in the fibonacci sequence.<br>/// &lt;/summary&gt;<br>/// &lt;param name="n"&gt;The index (n) of the fibonacci sequence&lt;/param&gt;<br>/// &lt;returns&gt;Returns the nth fibonacci number.&lt;/returns&gt;<br>/// &lt;response code="200"&gt;int64&lt;/response&gt;<br>[HttpGet]<br>[ProducesResponseType(200)]<br>[ProducesResponseType(400)]<br>[ResponseCache(CacheProfileName = DefaultCacheProfile.Name)]<br>[Produces("application/json", "text/json")]<br>public <span class="ssw15-rteStyle-Highlight">ActionResult&lt;long&gt;</span> Get(long n)<br>{<br>_logger.LogInformation($"Fibonacci number {n} requested");<br>if(!_fibonacciSolver.CanSolve(n))<br>return new BadRequestResult();<br>try<br>{<br>return _cache.GetOrAdd($"Fibonacci{n}", () =&gt; _fibonacciSolver.Solve(n));<br>}<br>catch (ArgumentOutOfRangeException)<br>{<br>return new BadRequestResult();<br>}<br>}</p><dd class="ssw15-rteElement-FigureBad">Figure: Good example for swashbuckle - Even b​etter if you have .NET Core 2.1 use the strong typed ActionResult – see yellow​​<br><br></dd><p class="ssw15-rteElement-CodeArea">        [HttpGet]<br>        [SwaggerResponse(HttpStatusCode.OK, typeof(long))]<br>        [SwaggerResponse(HttpStatusCode.BadRequest, typeof(void))]<br>        public <span class="ssw15-rteStyle-Highlight">ActionResult&lt;long&gt;</span> Get(long n)<br>        {<br>            _logger.LogInformation($"Fibonacci number {n} requested");<br>            <br>            if(!_fibonacciSolver.CanSolve(n))<br>                return new BadRequestResult();<br> <br>            try<br>            {<br>                return _cache.GetOrAdd($"Fibonacci{n}", () =&gt; _fibonacciSolver.Solve(n));<br>            }<br>            catch (ArgumentOutOfRangeException)<br>            {<br>                return new BadRequestResult();<br>            }<br>        }</p><dd class="ssw15-rteElement-FigureGood">Figure: Good example for nswag - Even better if you have .NET Core 2.1 use the strong typed ActionResult – see yellow​​<br><br></dd>


