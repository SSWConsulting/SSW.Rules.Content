---
type: rule
archivedreason:
title: Do you know how to use Observables
guid: ba7e787d-85d2-4a70-8635-7007d32312b8
uri: use-observables
created: 2024-09-29T09:00:33.0000000Z
authors: 
  - title: Jeoffrey Fischer
    url: https://ssw.com.au/people/jeoffrey-fischer
related:
- why-angular-is-great
redirects: []

---

Observables are a fundamental concept in Angular, enabling developers to manage asynchronous data streams efficiently.
This rule explores what observables are, how to use them effectively in your applications, and provides practical examples to enhance your understanding.

<!--endintro-->

## What are Observables?

Imagine you're in a busy coffee shop, and you’ve ordered your favorite drink.
Instead of waiting at the counter for it to be prepared, the barista hands you a special buzzer.
This buzzer will light up and vibrate when your drink is ready, allowing you to continue chatting with friends or reading a book without interruption.
In this scenario, the coffee order process is an analogy for observables in Angular.

Observables are like this buzzer.
They are a way to handle asynchronous data streams, allowing your application to react to changes over time without blocking the main thread.
Just like the buzzer informs you only when your drink is ready, observables notify your application when new data is available, enabling efficient management of asynchronous events.  

## How to use Observables  

### Creating Observables  

You can create observables in several ways, including using the Observable constructor or Angular’s built-in HttpClient for handling HTTP requests.
Here’s how to create a simple observable:  

```typescript  
import { Observable } from 'rxjs';  

const myObservable = new Observable(subscriber => {  
  subscriber.next('Hello, world!');  
  subscriber.complete();  
});  
```  

### Subscribing to Observables  

To receive data from an observable, you need to subscribe to it.
This is like waiting for your buzzer to alert you.
Here’s an example of subscribing to the observable created above:  

```typescript  
myObservable.subscribe({  
  next(value) {  
    console.log(value); // Output: Hello, world!  
  },  
  complete() {  
    console.log('Completed!');  
  }  
});  
```  

### Using Observables in Angular Services  

In Angular, observables are often used in services, especially for making HTTP requests.
Here’s how you might use Angular’s HttpClient to get data from an API:  

```typescript  
import { HttpClient } from '@angular/common/http';  
import { Injectable } from '@angular/core';  
import { Observable } from 'rxjs';  
  
@Injectable({  
  providedIn: 'root'  
})  
export class DataService {  
  constructor(private http: HttpClient) {}  
  
  getData(): Observable<any> {  
    return this.http.get('https://api.example.com/data');  
  }  
}  
```  

### Using the AsyncPipe in Templates  

To display data from an observable in your component’s template, you can use the AsyncPipe.
This automatically subscribes and unsubscribes to the observable for you, simplifying your code:  

```html  
<div *ngIf="dataService.getData() | async as data">  
  <p>{{ data }}</p>  
</div>
```  

## Examples of Observables  

Here are some common use cases and examples of observables in Angular:  

### Fetching Data from an API

Using observables to handle HTTP requests allows you to manage asynchronous data fetching effortlessly:  

```typescript  
this.dataService.getData().subscribe(data => {  
  console.log('Fetched data:', data);  
});  
```  

### Listening to User Inputs  

You can use observables to react to user inputs, such as typing in a search box:  

```typescript  
import { Subject } from 'rxjs';  
import { debounceTime, distinctUntilChanged } from 'rxjs/operators';  
  
searchTerm = new Subject<string>();  
  
this.searchTerm.pipe(  
  debounceTime(300),  
  distinctUntilChanged()  
).subscribe(term => {  
  console.log('Searching for:', term);  
});  
```  

### Handling Events  

Observables can also be used to manage events, such as clicks:  

```typescript  
fromEvent(document, 'click').subscribe(event => {  
  console.log('Document clicked:', event);  
});  
```  

### Combining Multiple Observables  

You can combine multiple observables using operators like combineLatest or forkJoin:  

```typescript  
import { forkJoin } from 'rxjs';  
  
forkJoin([this.service1.getData(), this.service2.getData()]).subscribe(results => {  
  console.log('Combined results:', results);  
});  
```  

Observables are a powerful tool in Angular for managing asynchronous data streams, much like the buzzer that alerts you when your coffee is ready.
By understanding how to create, subscribe to, and use observables effectively, you can build responsive and efficient Angular applications that handle data seamlessly.
Embrace the power of observables and take your Angular skills to the next level!
