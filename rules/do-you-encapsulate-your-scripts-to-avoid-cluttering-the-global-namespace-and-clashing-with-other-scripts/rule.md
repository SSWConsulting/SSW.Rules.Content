---
type: rule
archivedreason: No longer relevant for modern TS and ES era.
title: Do you encapsulate your scripts to avoid cluttering the global namespace and clashing with other scripts?
guid: 3439acb0-c24a-4c79-9543-4afabcf17312
uri: do-you-encapsulate-your-scripts-to-avoid-cluttering-the-global-namespace-and-clashing-with-other-scripts
created: 2015-05-28T05:30:10.0000000Z
authors: []
related: []
redirects: []

---

It's very common to see people creating variables and methods in the global namespace not worrying about how they will behave in conjunction with other libraries and custom codes. Once you have a handful of libraries and several people working on the same project you'll find that a lot of method and variable names will overlap, so if you don't take enough care, you will have your methods and variables overwritten and your page breaking for no apparent reason. 

<!--endintro-->

```
var buttonClicked = false;
function click()
{
     buttonClicked = true;
}
```

::: bad
Bad example - create variables and methods in the global namespace   
:::

In order to avoid your variables and methods to be overwritten, it's best practice to encapsulate them.

```
(function(ssw){
    var buttonClicked = false; //private variable 
    ssw.click = function(){ //public method
    {
        buttonClicked = true;
    }
}(window.SSW = window.SSW || {}));
```

::: good
Good example - the variable and method are now encapsulate and under a distinct namespace
:::

By encapsulating your script using this anonymous function, you can as well pass some parameter to be used within it and again not worrying about being overwritten somewhere else. A very used library is jQuery, simply referred as $ in the code, although it's not common, in some cases you'll see the $ conflicting with some existing library and to avoid that we can pass jQuery as a parameter for this anonymous function then use $ freely inside that context.

```
(function(ssw, $ ){    var buttonClicked = false; //private variable     ssw.click = function() //public method    {        buttonClicked = true;
         $('#id').html('<span>Example</span>');     }}(window.SSW = window.SSW || {},  jQuery ));
```

::: good
Good example - jQuery being passed as parameter of the anonymous function  
:::

Since JavaScript is very forgiving language, you could even redefine the meaning of *undefined* to something like *true*, which would probably make a lot of noise inside your code, to avoid this let's make sure that *undefined* is really *undefined* by completing this pattern this way:



```
(function(ssw,$, undefined ){
    var buttonClicked = false; //private variable 
    ssw.click = function() //public method
    {
        buttonClicked = true;
        $('#id').html('<span>Example</span>');
    }
}(window.SSW = window.SSW || {}, jQuery));  //nothing added as the third parameter
```




::: good
Good example - making sure undefined is really undefined

:::
