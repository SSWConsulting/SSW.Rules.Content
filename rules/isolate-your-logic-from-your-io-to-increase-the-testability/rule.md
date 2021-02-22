---
type: rule
archivedreason: 
title: Do you isolate your logic from your IO to increase the testability?
guid: 71aa799a-2b10-4e38-9798-789e24a4ba6a
uri: isolate-your-logic-from-your-io-to-increase-the-testability
created: 2020-03-12T22:19:47.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
- do-you-isolate-your-logic-from-your-io-to-increase-the-testability

---

If your method is consists of logic and IO, we recommend you isolate them to increase the testability of the logic.
Take this for example (and see how we refactor it):


<!--endintro-->



```
public static List<string> GetFilesInProject(string projectFile)
{
 List<string> files = new List<string>();
 TextReader tr = File.OpenText(projectFile);
 Regex regex = RegexPool.DefaultInstance[RegularExpression.GetFilesInProject];
 MatchCollection matches = regex.Matches(tr.ReadToEnd());
 tr.Close();
 string folder = Path.GetDirectoryName(projectFile);
 foreach (Match match in matches)
 {
 string filePath = Path.Combine(folder, match.Groups["FileName"].Value);
 if (File.Exists(filePath))
 {
 files.Add(filePath);
 }
 }
 return files;
}
```




::: bad
Bad - The logic and the IO are coded in a same method

:::

While this is a small concise and fairly robust piece of code, it still isn't that easy to unit test. Writing a unit test for this would require us to create temporary files on the hard drive, and probably end up requiring more code than the method itself.

If we start by refactoring it with an overload, we can remove the IO dependency and extract the logic further making it easier to test:



```
public static List<string> GetFilesInProject(string projectFile)
{
 string projectFileContents;
 using (TextReader reader = File.OpenText(projectFile))
 {
 projectFileContents = reader.ReadToEnd();
 reader.Close();
 }
 string baseFolder = Path.GetDirectoryName(projectFile);
 return GetFilesInProjectByContents(projectFileContents, baseFolder, true);
}
public static List<string> GetFilesInProjectByContents(string projectFileContents, string baseFolder, bool checkFileExists)
{
 List<string> files = new List<string>();
 Regex regex = RegexPool.DefaultInstance[RegularExpression.GetFilesInProject];
 MatchCollection matches = regex.Matches(projectFileContents);
 foreach (Match match in matches)
 {
 string filePath = Path.Combine(baseFolder, match.Groups["FileName"].Value);
 if (File.Exists(filePath) || !checkFileExists)
 {
 files.Add(filePath);
 }
 }
 return files;
}
```




::: good
Good - The logic is now isolated from the IO

:::

The first method (GetFilesInProject) is simple enough that it can remain untested. We do however want to test the second method (GetFilesInProjectByContents). Testing the second method is now too easy:



```
[Test]
public void TestVS2003CSProj()
{
 string projectFileContents = VSProjects.VS2003CSProj;
 string baseFolder = @"C:\NoSuchFolder";
 List<string> result = CommHelper.GetFilesInProjectByContents(projectFileContents, baseFolder, false);
 Assert.AreEqual(15, result.Count);
 Assert.AreEqual(true, result.Contains(Path.Combine(baseFolder, "BaseForm.cs")));
 Assert.AreEqual(true, result.Contains(Path.Combine(baseFolder, "AssemblyInfo.cs")));
}
[Test]
public void TestVS2005CSProj()
{
 string projectFileContents = VSProjects.VS2005CSProj;
 string baseFolder = @"C:\NoSuchFolder";
 List<string> result = CommHelper.GetFilesInProjectByContents(projectFileContents, baseFolder, false);
 Assert.AreEqual(6, result.Count);
 Assert.AreEqual(true, result.Contains(Path.Combine(baseFolder, "OptionsUI.cs")));
 Assert.AreEqual(true, result.Contains(Path.Combine(baseFolder, "VSAddInMain.cs")));
}
```




::: good
Good - Different test cases and assertions are created to test the logic

:::
