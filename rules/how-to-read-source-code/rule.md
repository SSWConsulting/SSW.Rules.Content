---
type: rule
title: Do you know how to read source code?
uri: how-to-read-source-code
authors:
  - title: Luke Mao
    url: https://www.ssw.com.au/people/luke-mao
  - title: Andrew Harris
    url: https://www.ssw.com.au/people/andrew-harris
  - title: Matt Goldman
    url: https://www.ssw.com.au/people/matt-goldman
redirects:
  - do-you-know-how-to-read-source-code
created: 2022-09-12T14:44:28.666Z
guid: 1b706f91-a99c-49a6-9ae8-72d2026abc11
---
First of all, you need to have the following prerequisites so that you can read the code smoothly afterwards.

1. **Basic knowledge** - Knowledge of relevant languages ​​and underlying technologies.
2. **Software function** - You must know what the software does, what features it has, and what configurations it has. You need to read the user manual first, then let the software run, and feel it for yourself.
3. **Relevant documentation** - Read the relevant internal documents, Readme or Release Notes, Design or Wiki. These documents can let you understand all aspects of the software. If your software doesn't have documentation, then you can only count on the original author of the software still alive and willing to communicate.
4. **The structure of the code** - You need to know what is the function of each directory. If the program you want to read is organized under some standard framework, such as the [Clean Architecture](https://github.com/jasontaylordev/CleanArchitecture). Then congratulations, the code is not difficult to read.

Next, you need to understand what parts of the code of this software are made up of. Below is a list for reference.

1. **Interface/abstract definition** - Any code will have many interfaces or abstract definitions, which describe the data structures or business entities that the code needs to deal with and the relationships between them. It is very important to understand these relationships.
2. **Module adhesive layer** - A lot of our code is used to glue code, such as middleware, Promises pattern, Callback, proxy and delegation, dependency injection and so on. The gluing techniques between these code modules are very important. Because they will split the code that would otherwise be straightforward, making it difficult for you to understand their relationships.
3. **Business Process** - This is how the code runs. In the beginning, we don't want to go into the details. But we need to figure out at a high level what the entire business process looks like. And in this process, how data is passed and processed. Generally speaking, we need to draw program flow charts.
4. **Detailed implementation** - After understanding the above three aspects, you will have a general understanding of the framework and logic of the entire code. At this point, you can dive into the details and start reading the code for the specific implementation. In general, you need to know the following facts, which will help you find the key points when reading the code.
    - **Code logic** - The code has two kinds of logic. One is business logic. The other is control logic. You need to separate these two kinds of logic. The reason why many code bases are confusing is that these two kinds of logic are mixed.
    - **Error handling** - According to the [Pareto principle](https://en.wikipedia.org/wiki/Pareto_principle), 20% of the code is normal logic and the other 80% of the code is dealing with various errors. Therefore, when you read the code, you can completely delete or comment out all the error-handling code, which will leave a clean and simple code with normal logic. By eliminating distracting factors, the code can be read more efficiently.
    - **Data processing** - As long as you look carefully, you will find that a lot of our code is there to manipulate data. They are long and boring. You can ignore them since they are not the main logic.
    - **Important algorithm** - Generally speaking, there will be many important algorithms in our code. It is not necessarily a sorting or search algorithm. But maybe some other core algorithms, such as index table algorithms, globally unique identifier algorithms, information recommendation algorithms, statistical algorithms, etc. These relatively hardcore algorithms can be very hard to read, but they tend to be the most technical parts.
    - **Low-level interaction** - Some code interacts with the underlying system, generally with the operating system. Therefore, reading this kind of code usually requires some low-level technical knowledge. Otherwise, it is difficult to read.
5. **Runtime debugging** - Most of the time, you don't know what happened unless the code is running. So we let the code run, and then analyse the log or use breakpoints to debug it. Seeing the code in action is a great way to understand it.

To sum up, the way to read the code is as follows:

-   Generally use a top-down, general to detail reading method called "Peeling the Onion".
-   Drawing is necessary. Such as program flow chart, call sequence diagram, module organization diagram, etc.
-   Categorize code logic and eliminate the noise. So the main logic will be clearer.
-   Debugging and tracing the code is the best way to understand what's going on in the code's execution.
