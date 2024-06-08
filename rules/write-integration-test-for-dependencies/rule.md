---
type: rule
title: Do you write Integration Test for Dependencies - e.g. DLLs?
uri: write-integration-test-for-dependencies
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
  - do-you-write-integration-test-for-dependencies-e-g-dlls
created: 2020-03-11T21:59:13.000Z
archivedreason: We now use NuGet to manage dependencies
guid: 62615da5-6ce6-4f6d-b236-88cc2c918f93
---

Dependant code is code that relies on other factors like methods and classes inside a separate DLL. Because of the way the .NET works assemblies are loaded as required by the program (this is what we call the JIT compiler). Thus, when a DLL goes astray, you will only find out at run time when you run a form/function that uses that DLL. These run time errors can occur when you have not packaged DLLs in your release or if the versions are incompatible. Such errors cause the following exceptions:

<!--endintro-->

* An unhandled exception ("System.IO.FileNotFoundException") occurred in SSW.NETToolkit.exe.
* System.IO.FileLoadException The located assembly's manifest definition with name 'SSW.SQLDeploy.Check' does not match the assembly reference.


These errors can be fixed by writing a integration test to check all referenced assemblies in a project.

Sample code:



```cs
[Test]
public void ReferencedAssembliesTest()
{
 // Get the executing assembly
 Assembly asm = Assembly.GetExecutingAssembly();
 // Get the assemblies that are referenced
 AssemblyName[] refAsms = asm.GetReferencedAssemblies();
 // Loop through and try to load each assembly
 foreach( AssemblyName refAsmName in refAsms)
 {
 try
 {
 Assembly.Load(refAsmName);
 	}
 catch(FileNotFoundException)
 {
 // Missing assembly
 Assert.Fail(refAsmName.FullName + " failed to load");
 }
 }
}
```


 **Figure: This code is a unit test for checking that all referenced assemblies are able to load.**
