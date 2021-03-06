# 0x0D. SQL - Introduction

## Resources:books:
Read or watch:
* [What is Database & SQL?](https://intranet.hbtn.io/rltoken/khEqMKp1PHvKpfO18d4fLQ)
* [A Basic MySQL Tutorial](https://intranet.hbtn.io/rltoken/qrONF5FZPsRxRJ2FkLVPcg)
* [Basic SQL statements: DDL and DML](https://intranet.hbtn.io/rltoken/ibCYnC9CDgZg5NQQvccBWw)
* [Basic queries: SQL and RA](https://intranet.hbtn.io/rltoken/yelYhpf7l0FcRIPCVfnMLw)
* [SQL technique: functions](https://intranet.hbtn.io/rltoken/3aQcovOE-clrD8yIfxFE9Q)
* [SQL technique: subqueries](https://intranet.hbtn.io/rltoken/lTXnq6pdk59x2h_Y-q0-Hg)
* [What makes the big difference between a backtick and an apostrophe?](https://intranet.hbtn.io/rltoken/R--kAkehyaawZFY4m1inxQ)
* [MySQL Cheat Sheet](https://intranet.hbtn.io/rltoken/aGZu7ulJpbbKcDhcz49yrg)
* [MySQL 5.7 SQL Statement Syntax](https://intranet.hbtn.io/rltoken/XrqR4oh6zsk0eOKoTgkA3Q)

---
## Learning Objectives:bulb:
What I learned from this project:

* What’s a database
* What’s a relational database
* What does SQL stand for
* What’s MySQL
* How to create a database in MySQL
* What does DDL and DML stand for
* How to CREATE or ALTER a table
* How to SELECT data from a table
* How to INSERT, UPDATE or DELETE data
* What are subqueries
* How to use MySQL functions

---

## Tasks

* **0. List databases**
  * [0-list_databases.sql](./0-list_databases.sql): MySQL script that lists all databases.

* **1. Create a database**
  * [1-create_database.sql](./1-create_database.sql): MySQL script that creates the database `hbtn_0c_0`.

* **2. Delete a database**
  * [2-remove_databases.sql](./2-remove_databases.sql): MySQL script that deletes the database `hbtn_0c_0`.

* **3. List tables**
  * [3-list_tables.sql](./3-list_tables.sql): MySQL script that lists all tables.

* **4. First table**
  * [4-first_table.sql](./4-first_table.sql): MySQL script that creates a table `first_table`.

* **5. Full description**
  * [5-full_table.sql](./5-full_table.sql): MySQL script that prints the full description of the table `first_table`.

* **6. List all in table**
  * [6-list_values.sql](./6-list_values.sql): MySQL script that lists all rows of the table `first_table`.

* **7. First add**
  * [7-insert_value.sql](./7-insert_value.sql): MySQL script that inserts a new row in the table `first_table`.

* **8. Count 89**
  * [8-count_89.sql](./8-count_89.sql): MySQL script that displays the number records with `id = 89` in the table `first_table`.

* **9. Full creation**
  * [9-full_creation.sql](./9-full_creation.sql): MySQL script that creates and fills a table `second_table` and add some rows.

* **10. List by best**
  * [10-top_score.sql](./10-top_score.sql): MySQL script that lists the `score` and `name` of all records of the table `second_table` in order of descending `score`.

* **11. Select the best**
  * [11-best_score.sql](./11-best_score.sql): MySQL script that lists the `score` and `name` of all records with a `score >= 10` in the table `second_table` in order of descending score.

* **12. Cheating is bad**
  * [12-no_cheating.sql](./12-no_cheating.sql): MySQL script that updates the score of Bob to 10 the table `second_table`.

* **13. Score too low**
  * [13-change_class.sql](./13-change_class.sql): MySQL script that removes all records with a `score <= 5` in the table `second_table`.

* **14. Average**
  * [14-average.sql](./14-average.sql): MySQL script that computes the average `score` of all records in the table `second_table`.

* **15. Number by score**
  * [15-groups.sql](./15-groups.sql): MySQL script that lists the `score` and number of records with the same score in the table `second_table` in order of descending count.

* **16. Say my name**
  * [16-no_link.sql](./16-no_link.sql): MySQL script that lists the `score` and `name` of all records in the table `second_table` in order of descending `score`. Does not display rows without a `name` value.
  
---

## Author
* **Estephania Calvo Carvajal** - [EstephaniaCalvoC](https://github.com/EstephaniaCalvoC)