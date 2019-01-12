---
type: rule
title: Do you know when to implement IDisposable?
uri: do-you-know-when-to-implement-idisposable
created: 2019-01-11T23:59:37.0000000Z
authors: []

---



<span class='intro'> ​If you access unmanaged resources (e.g. files, database connections etc.) in a class, you should implement&#160;IDisposable and overwrite the Dispose method to allow you to control when the memory is freed.&#160; If not, this responsibility is left to the garbage collector&#160;to free the memory when the object containing the unmanaged resources is finalised.&#160; This means the memory will be unnecessarily consumed by resources which are no longer required, which can lead to inefficient performance and potentially running out of memory altogether.<br> </span>

<p class="ssw15-rteElement-CodeArea">​​public class MyClass<br>&#123;<br> &#160; private File myFile = File.Open(...); // This is an unmanaged resource<br>&#125;<br><br>//elsewhere in project&#58;<br>private void useMyClass()<br>&#123;<br>&#160; var myClass = new MyClass();<br>&#160; &#160;/*<br>&#160; ​​Here we are using an unmanaged resource without disposing of it, meaning it will hang around in memory unnecessarily&#160;until the&#160; &#160;garbage collector finalises it<br>&#160; */<br> &#125;<br> </p><dd class="ssw15-rteElement-FigureBad">​​Figure&#58; Bad example - Using unmanaged resources without disposing of them when we are done​<br></dd><p class="ssw15-rteElement-P">​<br></p><p class="ssw15-rteElement-CodeArea">public class MyClass &#58; IDisposable<br>&#123;<br>&#160; private File myFile&#160;= new File.Open(...);&#160;// This is an unmanaged resource<br><br>​&#160; public void Dispose()<br>&#160; &#123;<br>&#160; &#160; myFile.Dispose(); // Here we dispose of the unmanaged resource<br>&#160; &#160; GC.SuppressFinalize(this); // Preventing a redundant garbage collector finalize call<br>&#160; &#125;<br>&#125;<br></p><dd class="ssw15-rteElement-FigureGood">​​Figure&#58; Good example - Implementing IDisposable​ allows you to dispose of the unmanaged resources deterministically to maximise efficiency<br></dd><p class="ssw15-rteElement-P"><br></p><p class="ssw15-rteElement-P">Now we&#160;can use the &quot;using&quot; statement to automatically dispose the class&#160;when you are finished with it.&#58;<br></p><p class="ssw15-rteElement-CodeArea">​​private void useClass()<br>&#123;<br>&#160; using (var myClass = new MyClass())<br>&#160; &#123;<br>&#160; &#160;&#160;// do stuff with myClass here...<br>&#160; &#125;&#160; // myClass.Dispose() is automatically run at the end of the using block<br>&#125;<br></p><dd class="ssw15-rteElement-FigureGood">​​Figure&#58; Good example - With the using statement, the unmanaged resources are disposed of as soon as we are finished with them<br></dd><p><br></p><p> 
   <a href="https&#58;//msdn.microsoft.com/en-us/library/system.idisposable.dispose.aspx">See here</a> for more details.​<br></p>


