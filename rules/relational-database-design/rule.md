---
type: rule
title: Do you understand relational database design?
uri: relational-database-design
authors:
  - title: Piers Sinclair
    url: https://ssw.com.au/people/piers-sinclair
created: 2023-07-03T05:50:13.555Z
guid: f2383ae4-3e2c-487a-b3ab-14bc89273994
---
Imagine an e-commerce company called Northwind Traders, where thousands of products, multiple sellers, and millions of customers converge. In such a company, the importance of a well-designed database cannot be overstated. Consider the scenario where a customer places an order only to encounter delays and frustration due to data inconsistencies that wrongly indicate an out-of-stock product. To mitigate such chaos, developers rely on relational database design principles, including normalization and entity-relationship diagrams (ERDs). These concepts provide the foundation for a well-structured database with improved data integrity and reduced redundancy, ensuring smooth operations and customer satisfaction.

# Poor database design - The problems

If a database lacks proper structure and organization, many problems can arise. These include:

* **Data Duplication** e.g. If Northwind Traders employee details, like home address, are stored separately in the HR and Payroll departments, an update in one place may not reflect in the other, leading to inconsistencies.
* **Update Anomalies** e.g. If a customer's phone number is stored in multiple places in the database, a change in contact information might not be updated everywhere, causing confusion when attempting to reach them.
* **Insertion Anomalies** e.g. If a database requires a vendor's details when adding a new product, it would be difficult to add a new product if the vendor information isn't available at the time of entry.
* **Deletion Anomalies** e.g. If a customer record is deleted from the database, it might unintentionally delete all associated order records, erasing valuable sales data.

These problems can be mitigated using Entity-Relationship Diagrams (ERDs) and Database Normalization, two critical concepts in database design.

# Database normalization

Database Normalization is a systematic approach to designing databases that reduces redundancy and avoids potential anomalies during data update, deletion, or insertion. This process involves organizing the columns (attributes) and tables (relations) of a database to ensure their dependencies are properly enforced by database integrity constraints.

Normalization is typically carried out through a series of steps called normal forms, each with specific rules:
- First Normal Form (1NF)
- Second Normal Form (2NF)
- Third Normal Form (3NF)

There are [further normal forms](https://en.wikipedia.org/wiki/Database_normalization), and the theory constantly evolves, but these 3 are the bare minimum required for database design.

`youtube: https://youtu.be/J-drts33N8g`

**Video: Database normalization explained**

## Normal forms explained - the example of a library checkout system

Consider a library checkout system where each row in the table represents a book-borrowing transaction.

We might start with an unnormalized data set that looks like this:

**Transaction table**

| BorrowerName | Books                                           |
| ------------ | ----------------------------------------------- |
| John Doe     | "1984, Harry Potter"                            |
| Sarah Smith  | "To Kill a Mockingbird, The Catcher in the Rye" |
| John Doe     | "Moby Dick", "Pride and Prejudice"              |

### 1st Normal Form (1NF)

1st normal form means ensuring:

* Each record is unique
* Each table cell contains a single value
* All values are atomic - meaning no values can be split into smaller parts

#### Ensuring each record is unique

The first thing to do is make sure each record is unique. We can assign a unique transaction identifier for each book borrowing transaction.

**Transaction table**

| TransactionID | BorrowerName | Books                                           |
| ------------- | ------------ | ----------------------------------------------- |
| 1             | John Doe     | "1984, Harry Potter"                            |
| 2             | Sarah Smith  | "To Kill a Mockingbird, The Catcher in the Rye" |
| 3             | John Doe     | "Moby Dick", "Pride and Prejudice"              |

#### Ensuring each cell contains a single value

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

#### Ensuring all values are atomic

Lastly, all values must be atomic. This state can be achieved by splitting the "BorrowerName" field into "FirstName" and "LastName".

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

### 2nd Normal Form (2NF)

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

### 3rd Normal Form (3NF)

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

# Entity relationship diagrams (ERDs)

ERDs are a way of visualizing the relationships between different entities and their cardinality. 

`youtube: https://www.youtube.com/watch?v=6uwuNRUUimY`

**Video: ERDs explained**


## Cardinality

Cardinality is a crucial concept within entity relationship modeling which refers to the number of instances of an entity that can be associated with each instance of another entity. Defining cardinality helps people understand the nature of relationships.

The cardinality of relationships can be one-to-one, one-to-many, or many-to-many.

* **One-to-One**: Each instance of entity A can be associated with one instance of entity B, and vice versa.
  * e.g. each employee in a company has one employee ID, and each employee ID is associated with one employee.
* **One-to-Many**: Each instance of entity A can be associated with multiple instances of entity B, but each instance of entity B is associated with only one instance of entity A.
  * e.g. one author can write many books, but each book is written by one author.
* **Many-to-Many**: Each instance of entity A can be associated with multiple instances of entity B, and vice versa.
  * e.g. a student can enrol in multiple courses, and multiple students can take a course.

### Optionality
In addition to the above relationship types, each side of the relationship may be optional. Let's examine the case of an airline company which tracks Pilots and Completed Flights
- 1 Flight must always have at least one Pilot
- 1 Pilot can have 0, 1 or many Flights (they may have 0 if they have been recently hired)

So in this case, the Pilot having Flights is optional

### Handling Many-to-Many - Practical Example - Student Courses
Many-to-many relationships require special handling to ensure that the relationships and their data can be stored accurately in the database. An associative entity (also known as a joining table) handles this by converting the many-to-many relationship into two one-to-many relationships.

Let's imagine a university that wants to track students and courses. In this example, 1 student has many courses, and 1 course has many students, meaning it has a many-to-many relationship.

#### ❌ Bad Example - Architecting the schema to have 1 table

The bad way to architect the schema for this scenario is using a single table. This method results in lots of repeated data.

**StudentCourses Table**

| FirstName | LastName  | CourseName | Instructor    |
| --------- | --------- | ---------- | ------------- |
| Alice     | Smith     | Math       | Prof. Smith   |
| Alice     | Smith     | English    | Prof. Johnson |
| Bob       | Northwind | Math       | Prof. Smith   |

#### ✅ Good Example - Architecting the schema to have 3 tables

A better way to architect the schema for this scenario is to break it into 3 tables with 2 relationships. Now the data is properly normalized and we can track which students do which courses, and any extra details such as when the student starts the course.

**Students Table**

Contains the student data

| StudentID | Name  | LastName  |
| --------- | ----- | --------- |
| 1         | Alice | Smith     |
| 2         | Bob   | Northwind |

**Courses Table**

Contains the course data

| CourseID | CourseName | Instructor    |
| -------- | ---------- | ------------- |
| 1        | Math       | Prof. Smith   |
| 2        | English    | Prof. Johnson |

**StudentCourses Table**

Contains the data about which students are taking which courses

| StudentID | CourseID |
| --------- | -------- |
| 1         | 1        |
| 1         | 2        |
| 2         | 1        |

**Relationship 1 - Students and StudentCourses**
- 1 Student has many StudentCourses
- 1 StudentCourse has 1 Student

**Relationship 1 - Courses and StudentCourses**
- 1 Course has many StudentCourses
- 1 StudentCourse has 1 Course 

## Visualization

Note how wordy it was to illustrate the many-to-many relationship in the StudentCourses example. Now imagine that database expands to have 10 more tables. It would quickly become hard to keep track of everything. This problem is what ERDs solve.

An ERD helps quickly display all the relationships in a database at a glance. Let's see what it looks like for StudentCourses:

![Figure: Student Courses ERD](studentcourseserd.png)

In this example, Students, Courses and StudentCourses are represented via the rectangles. Meanwhile, their relationships are shown via the lines between the rectangles. You can see the cardinality indicated by what is called [Crow's foot notation](https://en.wikipedia.org/wiki/Entity%E2%80%93relationship_model#Crow's_foot_notation).  

# Summary

Database normalization and ERDs are the core tools needed to perform good relational database design. If misapplied, it can have disastrous consequences with far-reaching effects. For example, once you start putting data into a table, it becomes significantly harder to fix since you now have a data migration problem. That's why getting database design right the first time is vital.

# Further Study

There's a lot to cover in database design. Here's some additional study material:

* Lucidchart's ER Diagrams page: https://www.lucidchart.com/pages/er-diagrams
* Microsoft Office's Troubleshoot Access Database Normalization Description: https://learn.microsoft.com/en-us/office/troubleshoot/access/database-normalization-description
