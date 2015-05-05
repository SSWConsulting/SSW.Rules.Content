---
type: rule
title: Do you call AngularJS services from your Kendo datasource?
uri: do-you-call-angularjs-services-from-your-kendo-datasource
created: 2015-05-05T19:23:00.0000000Z
authors:
- id: 44
  title: Duncan Hunter

---



<span class='intro'> <p class="p1"></p><p class="p1">To keep a good separation of concerns between your AngularJS controllers and your data service layers you should always call an AngularJS service or factory from your Kendo datasource logic.</p><p class="p1">Many demonstrations show a hard coded string in your Angular controllers calling your API but this means you will be making data API calls from your controllers, which is bad for several reasons&#58;</p><ol class="ol1"><li class="li1">You will end up with many API data calls from different controllers versus all being in your one location</li><li class="li1">Your controllers will be harder to unit test</li><li class="li1">If you want to call the same API endpoint somewhere else in your application you now have two place with this hard coded string, that might need to change in the future</li><li class="li1">If you keep all your data calls in one place your code will be easier to read and you can share business logic for making the API calls within your Angular service or factory, like a common error handling message for failed API calls</li><li class="li1">Finally you can perform actions while the promise is being resolved, like show a spinner animation or log out a message to the user</li></ol> </span>

<p>​<span style="line-height&#58;1.6;">The bad way to call your API from a Kendo datasource with AngularJS. Notice the hard coded url directly calling the API endpoint.</span></p><p class="ssw15-rteElement-CodeArea">transport&#58; &#123; 
   <br>read&#58; &#123; 
   <br>url&#58; &quot;../content/dataviz/js/spain-electricity.json&quot;, 
   <br>dataType&#58; &quot;json&quot; 
   <br>&#125; 
   <br>&#125;, </p><dd class="ssw15-rteElement-FigureBad">Bad Example -​&#160;This hard codes your url endpoint throughout your application&#160;​​<br></dd><p class="p6"> 
   <span class="s1">This is example is in TypeScript and you can see the Kendo data source is calling the </span>getFundAssetPositionChartData function and passing it a promise which when resolved will return the data. This function calls an AngularJS service which then calls the API endpoint. You can also see in the getFundAssetPositionChartData function the ‘this.isLoading = true’ code which is turning the pages spinner feature on and off when the call is resolved, to let the user know it is processing.​</p><p class="ssw15-rteElement-CodeArea">
<code>module app.widgets &#123;
<br>'use strict';
<br><br>class AssetAllocationByAssetClassChartController &#123;
<br>        isLoading&#58; any;
<br><br>static $inject = ['app.dataServices.InvestmentReportsService']
<br>constructor(
<br>private investmentReportsService&#58; <br>dataServices.InvestmentReportsService
<br>) &#123;&#125;

        <br><br>options = &#123;
<br>series&#58; [&#123;
<br>field&#58; 'AssetStrategyOverallPercent',
<br>                categoryField&#58; 'AssetClassName'
<br>&#125;],
<br>seriesDefaults&#58; &#123;
<br>type&#58; 'pie'
<br>&#125;,
<br>legend&#58; &#123;
<br>position&#58; 'bottom',
<br>labels&#58; &#123;
<br>visible&#58; true,
<br>background&#58; 'transparent',
<br>template&#58; '#=text #  #=value#% '
<br>&#125;<br>&#125;,
<br>dataSource&#58; new kendo.data.DataSource(&#123;
<br>transport&#58; &#123;
<br>read&#58; (promise&#58; any) =&gt; &#123;
                        <br>this.getFundAssetPositionChartData(promise);
<br>&#125;
<br>&#125;<br>&#125;)
<br>&#125;
<br><br>getFundAssetPositionChartData = (promise) =&gt; &#123;
<br>this.isLoading = true;
<br>return this.investmentReportsService.fundAssetPosition()
<br>.then((response) =&gt; &#123; promise.success(
  <br>response.Data.PortfolioAssetPositions[0].AssetClassDetailList
<br>);
<br>this.isLoading = false;
<br>&#125;);
<br>&#125;
<br>&#125;
<br><br>Angular.
<br>.module('app.widgets')
 <br>.controller('app.widgets.assetAllocationByAssetClassChartController',
 <br>AssetAllocationByAssetClassChartController <br>)</code></p><dd class="ssw15-rteElement-FigureGood">Good Example -&#160;This code passes a promise to a function which calls an AngularJS service to call the API endpoint.​</dd>


