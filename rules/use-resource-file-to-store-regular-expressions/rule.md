---
type: rule
title: Do you use resource file to store your regular expressions?
uri: use-resource-file-to-store-regular-expressions
authors:
  - title: Igor Goldobin
    url: https://ssw.com.au/people/alumni/igor-goldobin/
created: 2024-03-09T01:40:15.879Z
guid: 6be11005-f82a-48ba-8300-460284be1df5
---

Using resource files to store regular expressions simplifies management and promotes consistency across the project, enhancing maintainability and development workflows.

<!--endintro-->

```cs
public static Queue getFilesInProject(string projectFile)
{
	Queue tempQueue = new Queue();

	TextReader tr = File.OpenText(projectFile);

	// RT (10/10/2005): New regex to support VS 2005 project files (.csproj & .vbproj)
	//(?ixm-sn:
	//# VS 2003
	//(?:RelPath\s=\s\"(?<filename>.*?)\")
	//|
	//# VS 2005
	//(?:(?<=Compile|EmbeddedResource|Content|None)\sInclude=\"(?<FileName>.*?)\")
	//)
	Regex regex = new Regex
	    (@"(?ixm-sn:(?:RelPath\s=\s\""(?<FileName>.*?)\"")|(?:(?<=Compile|EmbeddedResource|Content|None)\sInclude=\""(?<FileName>.*?)\""))");
	MatchCollection matches = regex.Matches(tr.ReadToEnd());

}
```

::: bad
Bad example: Regular expression is embedded in code
:::

The problem with this code is that the regular expression is embedded within the method and not easily testable without creating mock files on-the-fly, etc. Another issue with embedding regular expressions in-code is escaping issues - often people will forget to escape the special characters or escape them incorrectly and thus cause the regular expression to behave differently between the design and execution environments.

The way we deal with this is to put the regular expression in a resource file. Using a resource file, it solves the aforementioned issues, and it also allows us to leave a comment for the regular expression.

![Figure: Good example - The regular expression (with comment) is stored in a resource file](resourceregularexpression.gif)

```cs
public static Queue getFilesInProject(string projectFile)
{
	Queue tempQueue = new Queue();

	TextReader tr = File.OpenText(projectFile);

	Regex regex = new Regex(RegularExpression.GetFilesInProject);
	MatchCollection matches = regex.Matches(tr.ReadToEnd());

}
```

::: good
Good example: We can easily get the regular expression from resource file
:::
