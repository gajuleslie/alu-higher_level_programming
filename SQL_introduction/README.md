# SQL - Introduction

This project introduces MySQL and basic SQL statements: DDL (creating and
dropping databases and tables) and DML (inserting, selecting, updating and
deleting data), plus aggregation and sorting.

Each `.sql` file is meant to be piped into the `mysql` client. When a database
name is required, it is passed as an argument of the `mysql` command, e.g.:

```bash
cat 10-top_score.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
```

## Tasks

### 0. List databases
`0-list_databases.sql` lists all databases on the server (`SHOW DATABASES;`).

### 1. Create a database
`1-create_database_if_missing.sql` creates `hbtn_0c_0` if it does not exist.

### 2. Delete a database
`2-remove_database.sql` drops `hbtn_0c_0` if it exists.

### 3. List tables
`3-list_tables.sql` lists all tables of the current database.

### 4. First table
`4-first_table.sql` creates `first_table` (`id INT`, `name VARCHAR(256)`) if it
does not exist.

### 5. Full description
`5-full_table.sql` prints the full creation statement of `first_table` using
`SHOW CREATE TABLE` (without `DESCRIBE` or `EXPLAIN`).

### 6. List all in table
`6-list_values.sql` lists all rows and columns of `first_table`.

### 7. First add
`7-insert_value.sql` inserts the row `id = 89, name = 'Best School'` into
`first_table`.

### 8. Count 89
`8-count_89.sql` counts the records in `first_table` with `id = 89`.

### 9. Full creation
`9-full_creation.sql` creates `second_table` (`id`, `name`, `score`) if needed
and inserts the four records for John, Alex, Bob and George.

### 10. List by best
`10-top_score.sql` lists `score` and `name` from `second_table`, ordered by
descending score.

### 11. Select the best
`11-best_score.sql` lists `score` and `name` for scores of at least 10, ordered
by descending score.

### 12. Cheating is bad
`12-no_cheating.sql` sets Bob's score to 10, using only his name.

### 13. Score too low
`13-change_class.sql` deletes all records with a score of 5 or less.

### 14. Average
`14-average.sql` computes the average score as the column `average`.

### 15. Number by score
`15-groups.sql` counts records per score (column `number`), sorted by count
descending.

### 16. Say my name
`16-no_link.sql` lists `score` and `name` for records that have a name, ordered
by descending score.
