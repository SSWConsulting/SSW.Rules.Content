---
type: rule
title: Do you write your Angular 1.x directives in TypeScript?
uri: do-you-write-your-angular-1x-directives-in-typescript
created: 2016-01-11T01:10:43.0000000Z
authors:
- id: 46
  title: Danijel Malik
- id: 44
  title: Duncan Hunter
- id: 15
  title: Mark Liu

---



<span class='intro'> <p>​​​​​​​​​​​​​​Angular 1.x directives are awesome and they help you reuse your code base by being able to drop directives (aka reuasable HTML elements)&#160;into several pages without having to duplicate your code base.​</p> </span>

​<style>
li.L0, li.L1, li.L2, li.L3, li.L5, li.L6, li.L7, li.L8 {
list-style-type:decimal !important;
}
</style> 
<div><div class="rulesummarycontenttop"><p class="p1" style="font-family&#58;'segoe ui', verdana, arial, helvetica, sans-serif;margin-bottom&#58;0px;">
         <span style="line-height&#58;20px;">Writing&#160;</span>your AngularJS 1.x directives&#160;in Typescript will help in the following ways&#58;</p><ol class="p1" style="margin-bottom&#58;0px;"><li>
            <font face="segoe ui, verdana, arial, helvetica, sans-serif"> 
               <span style="line-height&#58;13.8667px;">​You will more easily migrate to Angular2 which is written in TypeScript<br></span></font></li><li>
            <font face="segoe ui, verdana, arial, helvetica, sans-serif"> 
               <span style="line-height&#58;13.8667px;">Your code will be more robust with compile time checking avoiding errors you might miss or not see till you run the application in the browser.</span></font></li><li>
            <font face="segoe ui, verdana, arial, helvetica, sans-serif"> 
               <span style="line-height&#58;13.8667px;">You can more easily manage your code by reusing directives and not duplicating code.</span></font></li><li>
            <font face="segoe ui, verdana, arial, helvetica, sans-serif"> 
               <span style="line-height&#58;13.8667px;">If you keep your DDO (Directive Definition Object) seperate to your directive controller logic you can avoid using $scope and further be ready to migrate to Angular2. You can also reuse the directive controller with other parts of your application.</span></font><span style="line-height&#58;13.8667px;font-family&#58;'segoe ui', verdana, arial, helvetica, sans-serif;">&#160;</span></li></ol><div>
         <font face="segoe ui, verdana, arial, helvetica, sans-serif"> 
            <span style="line-height&#58;13.8667px;"> 
               <br></span></font></div><div>
         <font face="segoe ui, verdana, arial, helvetica, sans-serif"> 
            <span style="line-height&#58;13.8667px;">Writing Angular 1.x directives in Typescript can be a challenge with only a few examples available online. Most examples of Angular 1.x directives are in JavaScript and converting them to TypeScript versions means you need to have a good understanding of how it all works. Many examples that are available online do it a little differently from each other.&#160;</span></font></div><h3 class="ssw15-rteElement-H3">​​HTML</h3><p class="ssw15-rteElement-GreyBox">​​​&lt;current-value&gt;&lt;/current-value​&gt;<br></p><h3 class="ssw15-rteElement-H3">​Typescript<br></h3></div><pre class="prettyprint linenums">   module app.widgets &#123;
    'use strict';

    class CurrentValueDirectiveController &#123;
        amount&#58; number;

        static $inject = ['investmentReportsService'];
        constructor(private investmentReportsService&#58; app.dataServices.InvestmentService) &#123;
        &#125;

        setCurrentValue() &#123;
            this.investmentReportsService.investmentSummary(this.amount)
                .then((response) =&gt; &#123;
                    this.currentValue = response.Data.TotalMarket;
                &#125;);
        &#125;
    &#125;​

    function CurrentValueDirective()&#58; ng.IDirective &#123;
        return &#123;
            restrict = 'E';
            templateUrl = 'app/widgets/currentValue/currentValue.directive.html';
            controller = CurrentValueDirectiveController;
            controllerAs = 'currentValueDirCtrl';
            bindToController = true;
            scope = &#123;
                amount&#58; '='
            &#125;
        &#125;
    &#125;

    angular
        .module('app.widgets')
        .directive('currentValue', CurrentValueDirective);
&#125;​
</pre><p>​​</p></div>


