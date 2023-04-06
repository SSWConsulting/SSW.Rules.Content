---
type: rule
title: Do you have tests for Performance?
uri: have-tests-for-performance
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
  - title: Prem Radhakrishnan
    url: https://www.ssw.com.au/people/prem-radhakrishnan
related: []
redirects:
  - do-you-have-tests-for-performance
created: 2020-03-12T19:58:01.000Z
archivedreason: null
guid: a0b93a9e-1367-4a8c-985a-e46df21db9d1
---
Typically, there are User Acceptance Tests that need to be written to measure the performance of your application. As a general rule of thumb, forms should load in less than 4 seconds. This can be automated with your load testing framework.

<!--endintro-->

**Sample Code:**

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

Some popular open source load testing tools are: 

* [Apache JMeter](https://jmeter.apache.org) - 100% Java application with built in reporting - 6.7k Stars on GitHub
* [k6](https://k6.io/open-source) - Write load tests in javascript - 19.2k Stars on GitHub
* [NBomber](https://github.com/PragmaticFlow/NBomber) - Write tests in C# - 1.8k Stars on GitHub
* [Bombardier](https://github.com/codesenberg/bombardier) - CLI tool for writing load tests - 3.9k stars on GitHub
* [BenchmarkDotNet](https://github.com/dotnet/BenchmarkDotNet) - A powerful benchmarking tool - 8.8k stars on GitHub
