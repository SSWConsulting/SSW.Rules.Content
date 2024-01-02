---
type: rule
title: Do you normalize your database?
uri: database-normalization
authors:
  - title: Piers Sinclair
    url: https://ssw.com.au/people/piers-sinclair
related:
  - relational-database-design
  - erds
created: 2023-07-06T11:50:13.555Z
guid: a23003ee-765a-4abf-84e7-5a52df5e5e50
---
Database Normalization is a systematic approach to designing databases that reduces redundancy and avoids potential anomalies during data update, deletion, or insertion. This process involves organizing the columns (attributes) and tables (relations) of a database to ensure their dependencies are properly enforced by database integrity constraints.

<!--endintro-->

Normalization is typically carried out through a series of steps called normal forms, each with specific rules:
- First Normal Form (1NF)
- Second Normal Form (2NF)
- Third Normal Form (3NF)

There are [further normal forms](https://en.wikipedia.org/wiki/Database_normalization), and the theory constantly evolves, but these 3 are the bare minimum required for database design.

`youtube: https://youtu.be/J-drts33N8g`

**Video: Database normalization explained**

# Normal forms explained - the example of a library checkout system

Consider a library checkout system where each row in the table represents a book-borrowing transaction.

We might start with an unnormalized data set that looks like this:

**Transaction table**

| BorrowerName | Books                                           |
| ------------ | ----------------------------------------------- |
| John Doe     | "1984, Harry Potter"                            |
| Sarah Smith  | "To Kill a Mockingbird, The Catcher in the Rye" |
| John Doe     | "Moby Dick", "Pride and Prejudice"              |

## 1st Normal Form (1NF)

1st normal form means ensuring:

* Each record is unique
* Each table cell contains a single value
* All values are atomic - meaning no values can be split into smaller parts

### Ensuring each record is unique

The first thing to do is make sure each record is unique. We can assign a unique transaction identifier for each book borrowing transaction.

**Transaction table**

| TransactionID | BorrowerName | Books                                           |
| ------------- | ------------ | ----------------------------------------------- |
| 1             | John Doe     | "1984, Harry Potter"                            |
| 2             | Sarah Smith  | "To Kill a Mockingbird, The Catcher in the Rye" |
| 3             | John Doe     | "Moby Dick", "Pride and Prejudice"              |

### Ensuring each cell contains a single value

Next, the cells in the table need to contain only 1 value. This concept can be applied by breaking up the "Books" field so that each cell contains a single value. 

**Transaction table**

| TransactionID | BorrowerName | Book                     |
| ------------- | ------------ | ------------------------ |
| 1             | John Doe     | "1984"                   |
| 2             | John Doe     | "Harry Potter"           |
| 3             | Sarah Smith  | "To Kill a Mockingbird"  |
| 4             | Sarah Smith  | "The Catcher in the Rye" |
| 5             | John Doe     | "Moby Dick"              |
| 6             | John Doe     | "Pride and Prejudice"    |

### Ensuring all values are atomic

Lastly, all values must be atomic to ensure that the data is in the smallest form possible without losing its meaning. For example, in the Transaction table, the "BorrowerName" field can be split into "FirstName" and "LastName", however the "Book" cannot because "To Kill" and "a Mockingbird" would not make sense separately.

**Transaction table**

| TransactionID | FirstName | LastName | Book                     |
| ------------- | --------- | -------- | ------------------------ |
| 1             | John      | Doe      | "1984"                   |
| 2             | John      | Doe      | "Harry Potter"           |
| 3             | Sarah     | Smith    | "To Kill a Mockingbird"  |
| 4             | Sarah     | Smith    | "The Catcher in the Rye" |
| 5             | John      | Doe      | "Moby Dick"              |
| 6             | John      | Doe      | "Pride and Prejudice"    |

Now the table is in 1st Normal Form (1NF). It has unique records, each cell contains a single value, and all values are atomic.

## 2nd Normal Form (2NF)

2nd normal form means ensuring:

* Database is already in 1NF
* Every non-primary key attribute is fully functionally dependent on all parts of the primary key

Let's examine the data to see how we can change it into 2NF:

* FirstName and LastName don't change based on TransactionID, meaning they aren't functionally dependent on TransactionID. For example, John Doe could borrow books 10 times, but his name would always stay the same. 
* Book can change for each TransactionID, so it functionally depends on TransactionID. For example, John Doe could borrow different books in all 10 transactions.

Therefore we need to split FirstName and LastName into a new table. Since that table identifies the person borrowing the books, we could call it "Borrower". We also need to introduce a BorrowerID to ensure it is uniquely identified as per 1NF.

**Transaction table**

| TransactionID | BorrowerID | Book                     |
| ------------- | ---------- | ------------------------ |
| 1             | 1          | "1984"                   |
| 2             | 1          | "Harry Potter"           |
| 3             | 2          | "To Kill a Mockingbird"  |
| 4             | 2          | "The Catcher in the Rye" |
| 5             | 1          | "Moby Dick"              |
| 6             | 1          | "Pride and Prejudice"    |

**Borrower table**

| BorrowerID | FirstName | LastName |
| ---------- | --------- | -------- |
| 1          | John      | Doe      |
| 2          | Sarah     | Smith    |

## 3rd Normal Form (3NF)

3rd normal form means ensuring:

* Database is already in 2NF
* Every non-primary key attribute directly depends on the primary key, not any other non-key attribute

Let's imagine that we wanted to introduce a genre to the table. Our data might look like this:

**Transaction table**

| TransactionID | BorrowerID | Book                     | Genre              |
| ------------- | ---------- | ------------------------ | ------------------ |
| 1             | 1          | "1984"                   | Dystopian          |
| 2             | 1          | "Harry Potter"           | Fantasy            |
| 3             | 2          | "To Kill a Mockingbird"  | Historical Fiction |
| 4             | 2          | "The Catcher in the Rye" | Coming-of-Age      |
| 5             | 1          | "Moby Dick"              | Romance            |
| 6             | 1          | "Pride and Prejudice"    | Adventure          |

It looks ok here, but what if John decided to borrow "To Kill a Mockingbird"? The Genre would be repeated as follows:

**Transaction table**

| TransactionID | BorrowerID | Book                     | Genre              |
| ------------- | ---------- | ------------------------ | ------------------ |
| 1             | 1          | "1984"                   | Dystopian          |
| 2             | 1          | "Harry Potter"           | Fantasy            |
| 3             | 2          | "To Kill a Mockingbird"  | Historical Fiction |
| 4             | 2          | "The Catcher in the Rye" | Coming-of-Age      |
| 5             | 1          | "Moby Dick"              | Romance            |
| 6             | 1          | "Pride and Prejudice"    | Adventure          |
| 7             | 1          | "To Kill a Mockingbird"  | Historical Fiction |

So to fix it, Book needs to become a separate table.

**Transaction table**

| TransactionID | BorrowerID | BookID |
| ------------- | ---------- | ------ |
| 1             | 1          | 1      |
| 2             | 1          | 2      |
| 3             | 2          | 3      |
| 4             | 2          | 4      |
| 5             | 1          | 6      |
| 6             | 1          | 5      |
| 7             | 1          | 3      |

**Book table**

| BookID | Book                     | Genre              |
| ------ | ------------------------ | ------------------ |
| 1      | "1984"                   | Dystopian          |
| 2      | "Harry Potter"           | Fantasy            |
| 3      | "To Kill a Mockingbird"  | Historical Fiction |
| 4      | "The Catcher in the Rye" | Coming-of-Age      |
| 5      | "Pride and Prejudice"    | Romance            |
| 6      | "Moby Dick"              | Adventure          |

# Summary
Database Normalization is a method of ensuring a relational database conforms to good design principles. Normal Forms are definitions for different levels as you progress through normalization.

The use of these tools helps improve data integrity and reduce data redundancy.

# Further Study
* Microsoft Office's Troubleshoot Access Database Normalization Description: https://learn.microsoft.com/en-us/office/troubleshoot/access/database-normalization-description
