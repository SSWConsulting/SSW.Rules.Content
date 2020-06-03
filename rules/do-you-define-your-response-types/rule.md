---
type: rule
title: Do you define your response types?
uri: do-you-define-your-response-types
created: 2019-05-25T02:12:33.0000000Z
authors:
- id: 1
  title: Adam Cogan

---



<span class='intro'> <p>It is important to define your response types.</p><dl class="badImage"><dt><img src="/PublishingImages/bad-no-response-types.jpg" alt="bad-no-response-types.jpg" /></dt>
dd&gt;​Figure&#58; Bad example – no response types
</dl><dl class="goodImage"><dt><img src="/PublishingImages/good-response-types.png" alt="good-response-types.png" /></dt><dd>Figure&#58; Good example – Response types (in .NET)</dd>
</dl> </span>

<p><br></p><p class="ssw15-rteElement-CodeArea">/// &lt;summary&gt;<br>/// Returns the nth number in the fibonacci sequence.<br>/// &lt;/summary&gt;<br>/// &lt;param name=&quot;n&quot;&gt;The index (n) of the fibonacci sequence&lt;/param&gt;<br>/// &lt;returns&gt;Returns the nth fibonacci number.&lt;/returns&gt;<br>/// &lt;response code=&quot;200&quot;&gt;int64&lt;/response&gt;<br>[HttpGet]<br>[ProducesResponseType(200)]<br>[ProducesResponseType(400)]<br>[ResponseCache(CacheProfileName = DefaultCacheProfile.Name)]<br>[Produces(&quot;application/json&quot;,&#160;&quot;text/json&quot;)]<br>public&#160;<span class="ssw15-rteStyle-Highlight">ActionResult&lt;long&gt;</span> Get(long&#160;n)<br>&#123;<br>_logger.LogInformation($&quot;Fibonacci number &#123;n&#125; requested&quot;);<br>if(!_fibonacciSolver.CanSolve(n))<br>return&#160;new&#160;BadRequestResult();<br>try<br>&#123;<br>return&#160;_cache.GetOrAdd($&quot;Fibonacci&#123;n&#125;&quot;, () =&gt; _fibonacciSolver.Solve(n));<br>&#125;<br>catch&#160;(ArgumentOutOfRangeException)<br>&#123;<br>return&#160;new&#160;BadRequestResult();<br>&#125;<br>&#125;</p><dd class="ssw15-rteElement-FigureBad">Figure&#58; Good example for swashbuckle - Even b​etter if you have .NET Core 2.1 use the strong typed ActionResult – see yellow​​<br><br></dd><p class="ssw15-rteElement-CodeArea">&#160; &#160; &#160; &#160; [HttpGet]<br>&#160; &#160; &#160; &#160; [SwaggerResponse(HttpStatusCode.OK, typeof(long))]<br>&#160; &#160; &#160; &#160; [SwaggerResponse(HttpStatusCode.BadRequest, typeof(void))]<br>&#160; &#160; &#160; &#160; public <span class="ssw15-rteStyle-Highlight">ActionResult&lt;long&gt;</span> Get(long n)<br>&#160; &#160; &#160; &#160; &#123;<br>&#160; &#160; &#160; &#160; &#160; &#160; _logger.LogInformation($&quot;Fibonacci number &#123;n&#125; requested&quot;);<br>&#160; &#160; &#160; &#160; &#160; &#160;&#160;<br>&#160; &#160; &#160; &#160; &#160; &#160; if(!_fibonacciSolver.CanSolve(n))<br>&#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; return new BadRequestResult();<br>&#160;<br>&#160; &#160; &#160; &#160; &#160; &#160; try<br>&#160; &#160; &#160; &#160; &#160; &#160; &#123;<br>&#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; return _cache.GetOrAdd($&quot;Fibonacci&#123;n&#125;&quot;, () =&gt; _fibonacciSolver.Solve(n));<br>&#160; &#160; &#160; &#160; &#160; &#160; &#125;<br>&#160; &#160; &#160; &#160; &#160; &#160; catch (ArgumentOutOfRangeException)<br>&#160; &#160; &#160; &#160; &#160; &#160; &#123;<br>&#160; &#160; &#160; &#160; &#160; &#160; &#160; &#160; return new BadRequestResult();<br>&#160; &#160; &#160; &#160; &#160; &#160; &#125;<br>&#160; &#160; &#160; &#160; &#125;</p><dd class="ssw15-rteElement-FigureGood">Figure&#58; Good example for nswag - Even better if you have .NET Core 2.1 use the strong typed ActionResult – see yellow​​<br><br></dd>


