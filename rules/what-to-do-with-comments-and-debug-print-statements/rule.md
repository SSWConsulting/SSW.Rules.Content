---
type: rule
archivedreason: 
title: Comments - Do you know what to do with comments and Debug.Print statements
guid: cebb6d03-5254-4e76-b6ac-5e0f62c8e9f8
uri: what-to-do-with-comments-and-debug-print-statements
created: 2018-04-25T18:12:19.0000000Z
authors:
- title: Adam Cogan
  url: https://ssw.com.au/people/adam-cogan
related: []
redirects:
- comments-do-you-know-what-to-do-with-comments-and-debug-print-statements

---

When you create comments in your code, it is better to document why you've done something a certain way than to document how you did it. The code itself should tell the reader what is happening, there's no need to create "how" comments that merely restate the obvious unless you're using some technique that won't be apparent to most readers.

<!--endintro-->

What do you do with your print statements? Sometimes a programmer will place print statements at critical points in the program to print out debug statements for either bug hunting or testing. After the testing is successful, often the print statements are removed from the code. This is a bad thing to do.

Debugging print statements are paths that show where the programmer has been.  **They should be commented out, but the statements should be left in the code in the form of comments.** Thus, if the code breaks down later, the programmers (who might not remember or even know the program to start with), will be able to see where testing has been done and where the fault is likely to be - i.e., elsewhere.



```
private void Command0_Click() {
    rst.Open("SELECT * FROM Emp") // Open recordset with employee records
    // Debug.Print("Got " + intCount + " results");
    if (intCount > 1000) {
         // Debug.Print("too many records - returning early");
        return;
    } else  {
    .....processing code
}
```




::: bad
Bad Example - Debug code has just been commented out

:::



```
private void Command0_Click() {
    rst.Open("SELECT * FROM Emp")
    // Count will exceed 1,000 during eighteenth century    // leap years, which we aren't prepared to handle.
    if (intCount > 1000) {
        return
    } else  {
    .....processing code
}
```




::: good
Good Example - the debug commands have been rafactored into meaningful comments for the next developer

:::
