# 0x0E. SQL - More queries 

## Resources:books:
Read or watch:
* [How To Create a New User and Grant Permissions in MySQL](https://intranet.hbtn.io/rltoken/u4h2MXcCQfadszlRMQy-gw)
* [How To Use MySQL GRANT Statement To Grant Privileges To a User](https://intranet.hbtn.io/rltoken/ztrEKQexfEDtZ-8EUsG70Q)
* [MySQL constraints](https://intranet.hbtn.io/rltoken/LBrFqCMm9N9woTX7sS7e0g)
* [SQL technique: subqueries](https://intranet.hbtn.io/rltoken/YYpPtkqFeKSCsAU4Y_y3Og)
* [Basic query operation: the join](https://intranet.hbtn.io/rltoken/npLCp3WasK0SUSUQqCF25A)
* [SQL technique: multiple joins and the distinct keyword](https://intranet.hbtn.io/rltoken/GmRLMhkY-pPvjcpzyDvmRg)
* [SQL technique: join types](https://intranet.hbtn.io/rltoken/ryjyRRN7696rJV0maP03Xw)
* [SQL technique: union and minus](https://intranet.hbtn.io/rltoken/L7Fi5w8GZG5MSdQZ19e88g)
* [MySQL Cheat Sheet](https://intranet.hbtn.io/rltoken/V9vpLbtkFwV4EZYoiz2NBA)
* [The Seven Types of SQL Joins](https://intranet.hbtn.io/rltoken/ySKSdhFeMDddea07XrDzeQ)
* [MySQL Tutorial](https://intranet.hbtn.io/rltoken/-uqP0a89xUl3SsmV_ZtxRA)
* [SQL Style Guide](https://intranet.hbtn.io/rltoken/jn4SHgwVtOJF0LQYPEIs-g)
* [MySQL 5.7 SQL Statement Syntax](https://intranet.hbtn.io/rltoken/YjNAE7DcadDbT_a7iI0sYw)

---
## Learning Objectives:bulb:
What I learned from this project:

* How to create a new MySQL user
* How to manage privileges for a user to a database or table
* What’s a PRIMARY KEY
* What’s a FOREIGN KEY
* How to use NOT NULL and UNIQUE constraints
* How to retrieve datas from multiple tables in one request
* What are subqueries
* What are JOIN and UNION

---

* **0. My privileges!**
  * [0-privileges.sql](./0-privileges.sql): MySQL script that lists all privileges of the users `user_0d_1` and `user_0d_2`.

* **1. Root user**
  * [1-create_user.sql](./1-create_user.sql): MySQL script that creates the user `user_0d_1` with all privileges and password `user_0d_1_pwd`.

* **2. Read user**
  * [2-create_read_user.sql](./2-create_read_user.sql): MySQL script that creates the database `hbtn_0d_2` and user `user_0d_2` with password `user_0d_2_pwd` with only SELECT privilege on the database `hbtn_0d_2`.

* **3. Always a name**
  * [3-force_name.sql](./3-force_name.sql): MySQL script that creates the table `force_name`.


* **4. ID can't be null**
  * [4-never_empty.sql](./4-never_empty.sql): MySQL script that creates the table `id_not_null`.

* **5. Unique ID**
  * [5-unique_id.sql](./5-unique_id.sql): MySQL script that creates the table `unique_id`.

* **6. States table**
  * [6-states.sql](./6-states.sql): MySQL script that creates the database `hbtn_0d_usa` with a table `states`.


* **7. Cities table**
  * [7-cities.sql](./7-cities.sql): MySQL script that creates the database `hbtn_0d_usa` with a table `cities`.

* **8. Cities of California**
  * [8-cities_of_california_subquery.sql](./8-cities_of_california_subquery.sql):
  MySQL script that lists all the cities of California that can be found in the
  database `hbtn_0d_usa`, ordered by ascending city id.

* **9. Cities by States**
  * [9-cities_by_state_join.sql](./9-cities_by_state_join.sql): MySQL script that lists all cities contained in the database `hbtn_0d_usa`, ordered by ascending city id.

* **10. Genre ID by show**
  * [10-genre_id_by_show.sql](./10-genre_id_by_show.sql): MySQL script that lists all shows contained in `hbtn_0d_tvshows` that have at least one genre linked, in order of ascending `tv_shows.title` and `tv_show_genres genre_id`.

* **11. Genre ID for all shows**
  * [11-genre_id_all_shows.sql](./11-genre_id_all_shows.sql): MySQL script that lists all shows contained
  in the database `hbtn_0d_tvshows`, in order of ascending `tv_shows.title` and `tv_show_genres.genre_id`. If a show does not have a genre, displays `NULL`.
<!--
* **12. No genre**
  * [12-no_genre.sql](./12-no_genre.sql): MySQL script that lists all shows contained in
  `hbtn_0d_tvshows` without a genre linked, in order of ascending `tv_shows.title` and `tv_show_genres.genre_id`.

* **13. Number of shows by genre**
  * [13-count_shows_by_genre.sql](./13-count_shows_by_genre.sql): MySQL script that lists all genres from
  `hbtn_0d_tvshows` and displays the number of shows linked to each, in order of descending number of shows linked.
  * Does not display a genre if it has no linked shows.

* **14. My genres**
  * [14-my_genres.sql](./14-my_genres.sql): MySQL script that uses the `hbtn_0d_tvshows` database
  to list all genres of the show Dexter, in order of ascending genre name.

* **15. Only Comedy**
  * [15-comedy_only.sql](./15-comedy_only.sql): MySQL script that lists all comedy shows in the
  database `hbtn_0d_tvshows`, in order of ascending show title.

* **16. List shows and genres**
  * [16-shows_by_genre.sql](./16-shows_by_genre.sql): MySQL script that lists all shows, and all genres
  linked to that show, from the database `hbtn_0d_tvshows`, in order of ascending show title and genre name.

* **17. Not my genre**
  * [100-not_my_genres.sql](./100-not_my_genres.sql`) MySQL script that uses the `hbtn_0d_tvshows`
  database to list all genres not linked to the show Dexter, in order of ascending genre name.

* **18. No Comedy tonight!**
  * [101-not_a_comedy.sql](./101-not_a_comedy.sql): MySQL script that lists all shows without the
  genre comedy in the database `hbtn_0d_tvshows`, in order of ascending show title.

* **19. Rotten tomatoes**
  * [102-rating_shows.sql](./102-rating_shows.sql): MySQL script that lists all shows from
  `hbtn_0d_tvshows_rate` by their rating, in order of descending rating.

* **20. Best genre**
  * [103-rating_genres.sql](./103-rating_genres.sql): MySQL script that lists all genres in the
  database `hbtn_0d_tvshows_rate` by their rating, in order of descending rating.
-->
---

## Author
* **Estephania Calvo Carvajal** - [EstephaniaCalvoC](https://github.com/EstephaniaCalvoC)