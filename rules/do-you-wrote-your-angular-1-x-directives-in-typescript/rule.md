---
type: rule
archivedreason: 
title: Do you write your Angular 1.x directives in TypeScript?
guid: 191aee7e-121c-47d8-95e8-5248449fb9df
uri: do-you-wrote-your-angular-1-x-directives-in-typescript
created: 2016-01-11T01:10:43.0000000Z
authors:
- title: Danijel Malik
  url: https://ssw.com.au/people/danijel-malik
- title: Duncan Hunter
  url: https://ssw.com.au/people/duncan-hunter
- title: Mark Liu
  url: https://ssw.com.au/people/mark-liu
related: []
redirects:
- do-you-write-your-angular-1-x-directives-in-typescript

---

Angular 1.x directives are awesome and they help you reuse your code base by being able to drop directives (aka reuasable HTML elements) into several pages without having to duplicate your code base.

<!--endintro-->


Writing your AngularJS 1.x directives in Typescript will help in the following ways:

1. You will more easily migrate to Angular2 which is written in TypeScript
2. Your code will be more robust with compile time checking avoiding errors you might miss or not see till you run the application in the browser
3. You can more easily manage your code by reusing directives and not duplicating code
4. If you keep your DDO (Directive Definition Object) seperate to your directive controller logic you can avoid using $scope and further be ready to migrate to Angular2. You can also reuse the directive controller with other parts of your application

Writing Angular 1.x directives in Typescript can be a challenge with only a few examples available online. Most examples of Angular 1.x directives are in JavaScript and converting them to TypeScript versions means you need to have a good understanding of how it all works. Many examples that are available online do it a little differently from each other.

### HTML

```
<current-value></current-value>
```

### Typescript
```
module app.widgets {
    'use strict';

    class CurrentValueDirectiveController {
        amount: number;

        static $inject = ['investmentReportsService'];
        constructor(private investmentReportsService: app.dataServices.InvestmentService) {
        }

        setCurrentValue() {
            this.investmentReportsService.investmentSummary(this.amount)
                .then((response) => {
                    this.currentValue = response.Data.TotalMarket;
                });
        }
    }

    function CurrentValueDirective(): ng.IDirective {
        return {
            restrict = 'E';
            templateUrl = 'app/widgets/currentValue/currentValue.directive.html';
            controller = CurrentValueDirectiveController;
            controllerAs = 'currentValueDirCtrl';
            bindToController = true;
            scope = {
                amount: '='
            }
        }
    }

    angular
        .module('app.widgets')
        .directive('currentValue', CurrentValueDirective);
}
```
