---
type: rule
archivedreason: 
title: Do you call AngularJS services from your Kendo datasource?
guid: 1da148fe-4093-419d-b4b0-4cc50f50d36b
uri: do-you-call-angularjs-services-from-your-kendo-datasource
created: 2015-05-05T19:23:00.0000000Z
authors:
- title: Duncan Hunter
  url: https://ssw.com.au/people/duncan-hunter
related: []
redirects: []

---

To keep a good separation of concerns between your AngularJS controllers and your data service layers you should always call an AngularJS service or factory from your Kendo datasource logic.

Many demonstrations show a hard coded string in your Angular controllers calling your API but this means you will be making data API calls from your controllers, which is bad for several reasons:

1. You will end up with many API data calls from different controllers versus all being in your one location
2. Your controllers will be harder to unit test
3. If you want to call the same API endpoint somewhere else in your application you now have two place with this hard coded string, that might need to change in the future
4. If you keep all your data calls in one place your code will be easier to read and you can share business logic for making the API calls within your Angular service or factory, like a common error handling message for failed API calls
5. Finally you can perform actions while the promise is being resolved, like show a spinner animation or log out a message to the user


<!--endintro-->

The bad way to call your API from a Kendo datasource with AngularJS. Notice the hard coded url directly calling the API endpoint.


```
read: { 
    url: "../content/dataviz/js/spain-electricity.json", 
    dataType: "json" 
}
```



::: bad
Bad Example - This hard codes your url endpoint throughout your application 

:::

This is example is in TypeScript and you can see the Kendo data source is calling the getFundAssetPositionChartData function and passing it a promise which when resolved will return the data. This function calls an AngularJS service which then calls the API endpoint. You can also see in the getFundAssetPositionChartData function the ‘this.isLoading = true’ code which is turning the pages spinner feature on and off when the call is resolved, to let the user know it is processing.


```
module app.widgets {    'use strict';
    class AssetAllocationByAssetClassChartController {        isLoading: any;        static $inject = ['app.dataServices.InvestmentReportsService']        constructor(private investmentReportsService: dataServices.InvestmentReportsService) { }
        options = {            series: [{                field: 'AssetStrategyOverallPercent',                categoryField: 'AssetClassName'            }],            seriesDefaults: {                type: 'pie'            },            legend: {                position: 'bottom',                labels: {                    visible: true,                    background: 'transparent',                    template: '#=text # #=value#% '                }            },            dataSource: new kendo.data.DataSource({                transport: {                    read: (promise: any) => {                        this.getFundAssetPositionChartData(promise);                    }                }            })        }        getFundAssetPositionChartData = (promise) => {            this.isLoading = true;            return this.investmentReportsService.fundAssetPosition()                .then((response) => {                    promise.success(                        response.Data.PortfolioAssetPositions[0].AssetClassDetailList                    );                    this.isLoading = false;                });        }    }    Angular.        .module('app.widgets')        .controller('app.widgets.assetAllocationByAssetClassChartController',        AssetAllocationByAssetClassChartController        )}
```





::: good
Good Example - This code passes a promise to a function which calls an AngularJS service to call the API endpoint.  
:::
