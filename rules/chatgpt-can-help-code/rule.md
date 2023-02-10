---
type: rule
title: Do you use ChatGPT to help you code?
uri: chatgpt-can-help-code
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
  - title: Piers Sinclair
    url: https://www.ssw.com.au/people/piers-sinclair
  - title: Calum Simpson
    url: https://www.ssw.com.au/people/calum-simpson
  - title: Harry Ross
    url: https://www.ssw.com.au/people/harry-ross
created: 2023-02-09T08:31:54.821Z
guid: 499bd550-d8c3-448d-a307-06e6a762efb3
---
ChatGPT is an extremely useful tool for software developers as it has been trained to understand how code functions. It will provide an invaluable alternative to StackOverflow, being a great resource to help developers troubleshoot.

ChatGPT can be used for:

* Detecting bugs in your code
* Solving compile time or runtime errors
* Generating code based on a text description 
* Explaining how a piece of code works
* Translating code to a different language (e.g. Python code to C#)
* Minimising generation of boilerplate (e.g. JSON to C# classes)
* Helping automate the code refactoring process
* Helping perform code reviews

::: info
**Warning:** Ensure you double check code integrity before deploying to production!
:::

![Figure: Asking ChatGPT to explain this code](chatgpt-code-prompt.png)

![Figure: ChatGPT explains the code](chatgpt-code-response.png)

### Try it yourself, copy and paste this into [ChatGPT](https://chat.openai.com)

``` markup
What does this code do?
[HttpPut("{id}")]
public async Task<IActionResult> MoveRight(string id)
{
	try
	{
		if (await _legalApiDbContext.ParaLefts.Where(a => a.ParaId == id).CountAsync() != 0)
		{
			ParaLeft toDelete = _legalApiDbContext.ParaLefts.Where(para => para.ParaId == id).First();
			_legalApiDbContext.ParaRights.Add(new ParaRight { ParaId = id });
			_legalApiDbContext.ParaLefts.Remove(toDelete);
			await _legalApiDbContext.SaveChangesAsync();
			return Ok();
		} else
		{
			return StatusCode(StatusCodes.Status404NotFound);
		}
	}
	catch (SqlException err)
	{
		_logger.LogError(err.Message);
		return StatusCode(StatusCodes.Status500InternalServerError);
	}
}
```
