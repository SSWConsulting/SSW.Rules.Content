---
type: rule
archivedreason: The class [no-longer exists in Bootstrap 4](https://getbootstrap.com/docs/4.5/components/forms/#form-controls)
title: Do you use the CSS class "form horizontal" to arrange your fields and labels?
guid: 5c2ca49f-b126-4f96-a4a0-f3126e91c195
uri: use-css-class-form-horizontal-to-arrange-fields-and-labels
created: 2014-09-08T20:59:34.0000000Z
authors:
- title: Drew Robson
  url: https://ssw.com.au/people/drew-robson
related: 
- how-to-align-your-form-labels
- do-you-know-how-to-arrange-forms
redirects:
- do-you-use-the-css-class-＂form-horizontal＂-to-arrange-your-fields-and-labels
- do-you-use-the-css-class-form-horizontal-to-arrange-your-fields-and-labels

---

You should align labels **next** to the inputs on medium and large displays and **above** inputs on small and extra-small displays.

<!--endintro-->

Bootstrap makes this easy. Use the css class **form-horizontal** on your html form for it to use this behaviour by default.

```html
<form class="form-horizontal">
  <div class="form-group">
    <label for="inputEmail3" class="col-sm-2 control-label">Email</label>
      <div class="col-sm-10">
        <input type="email" class="form-control" id="inputEmail3" placeholder="Email">
      </div>
  </div>
  <div class="form-group">
    <label for="inputPassword3" class="col-sm-2 control-label">Password</label>
      <div class="col-sm-10">
        <input type="password" class="form-control" id="inputPassword3" placeholder="Password">
      </div>
  </div>
</form>
```

**Figure: Example html using Bootstrap to get the above behaviour**

See [https://getbootstrap.com/docs/3.4/css/#forms-horizontal](https://getbootstrap.com/docs/3.4/css/#forms-horizontal) for more information.
