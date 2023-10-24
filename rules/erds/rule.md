---
type: rule
title: Do you visualize your database with an ERD?
uri: erds
authors:
  - title: Piers Sinclair
    url: https://ssw.com.au/people/piers-sinclair
related:
  - relational-database-design
  - database-normalization
created: 2023-07-06T11:50:13.555Z
guid: 1c41b0f4-2cdf-4fad-8354-769ab02385ff
---
Relational databases are complicated, and understanding the entire architecture of a database can be difficult when expressed solely in words. That's where Entity Relationship Diagrams (ERDs) come in. ERDs are a way of visualizing the relationships between different entities and their cardinality. 

<!--endintro-->

`youtube: https://www.youtube.com/watch?v=6uwuNRUUimY`

**Video: ERDs explained**

# Cardinality

Cardinality is a crucial concept within entity relationship modeling which refers to the number of instances of an entity that can be associated with each instance of another entity. Defining cardinality helps people understand the nature of relationships.

The cardinality of relationships can be one-to-one, one-to-many, or many-to-many.

* **One-to-One**: Each instance of entity A can be associated with one instance of entity B, and vice versa.
  * e.g. each employee in a company has one employee ID, and each employee ID is associated with one employee.
* **One-to-Many**: Each instance of entity A can be associated with multiple instances of entity B, but each instance of entity B is associated with only one instance of entity A.
  * e.g. one author can write many books, but each book is written by one author.
* **Many-to-Many**: Each instance of entity A can be associated with multiple instances of entity B, and vice versa.
  * e.g. a student can enrol in multiple courses, and multiple students can take a course.

## Optionality
In addition to the above relationship types, each side of the relationship may be optional. Let's examine the case of an airline company which tracks Pilots and Completed Flights.
- 1 Flight must always have at least one Pilot
- 1 Pilot can have 0, 1 or many Flights (they may have 0 if they have been recently hired)

So in this case, the Pilot having Flights is optional.

## Handling Many-to-Many - Practical Example - Student Courses
Many-to-many relationships require special handling to ensure that the relationships and their data can be stored accurately in the database. An associative entity (also known as a joining table) handles this by converting the many-to-many relationship into two one-to-many relationships.

Let's imagine a university that wants to track students and courses. In this example, 1 student has many courses, and 1 course has many students, meaning it has a many-to-many relationship.

### ❌ Bad Example - Architecting the schema to have 1 table

The bad way to architect the schema for this scenario is using a single table. This method results in lots of repeated data.

**StudentCourses Table**

| FirstName | LastName  | CourseName | Instructor    |
| --------- | --------- | ---------- | ------------- |
| Alice     | Smith     | Math       | Prof. Smith   |
| Alice     | Smith     | English    | Prof. Johnson |
| Bob       | Northwind | Math       | Prof. Smith   |

### ✅ Good Example - Architecting the schema to have 3 tables

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

# Visualization

Note how wordy it was to illustrate the many-to-many relationship in the StudentCourses example. Now imagine that database expands to have 10 more tables. It would quickly become hard to keep track of everything. This problem is what ERDs solve.

An ERD helps quickly display all the relationships in a database at a glance. Let's see what it looks like for StudentCourses:

![Figure: Student Courses ERD](studentcourseserd.png)

In this example, Students, Courses and StudentCourses are represented via the rectangles. Meanwhile, their relationships are shown via the lines between the rectangles. You can see the cardinality indicated by what is called [Crow's foot notation](https://en.wikipedia.org/wiki/Entity%E2%80%93relationship_model#Crow's_foot_notation). 

# Summary
ERDs are a fantastic tool for visualizing a database at a glance. Through using this tool, developers can ensure they have a solid understanding of how data in the database is related and identify any problems quickly and easily.

# Further Study
* Lucidchart's ER Diagrams page: https://www.lucidchart.com/pages/er-diagrams
