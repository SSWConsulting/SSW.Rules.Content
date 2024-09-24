---
type: rule
title: Do you have tests for Performance?
uri: have-tests-for-performance
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
  - title: Prem Radhakrishnan
    url: https://www.ssw.com.au/people/prem-radhakrishnan
  - title: Yazhi Chen
    url: https://www.ssw.com.au/people/yazhi-chen
related: []
redirects:
  - do-you-have-tests-for-performance
created: 2020-03-12T19:58:01.000Z
archivedreason: null
guid: a0b93a9e-1367-4a8c-985a-e46df21db9d1
---
Typically, there are User Acceptance Tests that need to be written to measure the performance of your application. As a general rule of thumb, forms should load in less than 4 seconds. This can be automated with your load testing framework.

<!--endintro-->

#### Sample Code

``` cs
import http from 'k6/http';

export const options = {
  thresholds: {
    http_req_duration: ['p(100)<4000'], // 100% of requests should be below 4000ms
  },
};

export default function () {
  http.get('https://test-api.k6.io/public/mainpage');
}

```

**Figure: This code uses k6 to test that the MainPage loads in under 4 seconds**

Sometimes, during performance load testing, it becomes necessary to simulate traffic originating from various regions to comprehensively assess system performance. This allows for a more realistic evaluation of how the application or system responds under diverse geographical conditions, reflecting the experiences of users worldwide. 

**Sample Code:**

``` cs
import http from 'k6/http';
import { check, sleep } from 'k6';

export const options = {
  vus: 25, //simulates 25 virtual users
  duration: "60s", //sets the duration of the test
  ext: { //configuring Load Impact, a cloud-based load testing service.
    loadimpact: {
      projectID: 3683064,
      name: "West US - 25 vus",
      distribution: {
        distributionLabel1: { loadZone: 'amazon:us:palo alto', percent: 34 },
        distributionLabel2: { loadZone: 'amazon:cn:hong kong', percent: 33 },
        distributionLabel3: { loadZone: 'amazon:au:sydney', percent: 33 },
      },
    },
  },
  summaryTrendStats: ['avg', 'min',  'max', 'p(95)', 'p(99)', 'p(99.99)'],
};

export default function () {
  const baseUrl = "https://my.sugarlearning.com";
  const httpGetPages = [
    baseUrl,
    baseUrl + "/api/Leaderboard/GetLeaderboardSummary?companyCode=SSW",
    baseUrl + "/api/v2/admin/modules?companyCode=SSW"
  ]; 

  const token = ''; //set the token here
  const params = {
    headers: {
      'Content-Type' : 'application/json',
      Authorization: "Bearer " + token
    }
  }; 

  for (const page of httpGetPages){
    const res = http.get(page, params);
    check(res, {
      'status was 200': (r) => r.status === 200
    });
    sleep(1);
  };   
}
```
**Figure: This code uses k6 to test several endpoints by simulating traffic from different regions**

::: good  
![Figure: Good example - Output the result of simulating traffic from West US to K6 Cloud](run-script-with-k6-cloud.png)  
:::

Some popular open source load testing tools are: 

* [Apache JMeter](https://jmeter.apache.org) - 100% Java application with built in reporting - 6.7k Stars on GitHub
* [k6](https://k6.io/open-source) - Write load tests in javascript - 19.2k Stars on GitHub
* [NBomber](https://github.com/PragmaticFlow/NBomber) - Write tests in C# - 1.8k Stars on GitHub
* [Bombardier](https://github.com/codesenberg/bombardier) - CLI tool for writing load tests - 3.9k stars on GitHub
* [BenchmarkDotNet](https://github.com/dotnet/BenchmarkDotNet) - A powerful benchmarking tool - 8.8k stars on GitHub
