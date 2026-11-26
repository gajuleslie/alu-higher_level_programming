# SQL - More Queries

This project covers MySQL users and privileges, constraints (`NOT NULL`,
`UNIQUE`, `PRIMARY KEY`, `FOREIGN KEY`), subqueries, and joins (`INNER JOIN`,
`LEFT JOIN`) across multiple tables.

Each `.sql` file is meant to be piped into the `mysql` client. When a database
name is required, it is passed as an argument of the `mysql` command, e.g.:

```bash
cat 9-cities_by_state_join.sql | mysql -hlocalhost -uroot -p hbtn_0d_usa
```

Tasks 10-16 use the `hbtn_0d_tvshows` dump, which must be imported first:

```bash
echo "CREATE DATABASE hbtn_0d_tvshows;" | mysql -hlocalhost -uroot -p
curl "https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" -s | mysql -hlocalhost -uroot -p hbtn_0d_tvshows
```

## Tasks

### 0. My privileges!
`0-privileges.sql` lists the grants of `user_0d_1` and `user_0d_2` on
`localhost`.

### 1. Root user
`1-create_user.sql` creates `user_0d_1` (password `user_0d_1_pwd`) with all
privileges on the server.

### 2. Read user
`2-create_read_user.sql` creates the database `hbtn_0d_2` and `user_0d_2`
(password `user_0d_2_pwd`) with only `SELECT` on that database.

### 3. Always a name
`3-force_name.sql` creates `force_name` with a `NOT NULL` name column.

### 4. ID can't be null
`4-never_empty.sql` creates `id_not_null` with `id` defaulting to 1.

### 5. Unique ID
`5-unique_id.sql` creates `unique_id` with a unique `id` defaulting to 1.

### 6. States table
`6-states.sql` creates `hbtn_0d_usa` and its `states` table, with an
auto-incremented primary key and a non-null name.

### 7. Cities table
`7-cities.sql` creates `hbtn_0d_usa`, `states` (needed by the foreign key) and
`cities`, whose `state_id` references `states.id`.

### 8. Cities of California
`8-cities_of_california_subquery.sql` lists California's cities using a
subquery instead of `JOIN`, sorted by city id.

### 9. Cities by States
`9-cities_by_state_join.sql` lists each city with its state name using a join.

### 10. Genre ID by show
`10-genre_id_by_show.sql` lists shows that have at least one linked genre.

### 11. Genre ID for all shows
`11-genre_id_all_shows.sql` lists all shows, displaying `NULL` for shows
without a genre.

### 12. No genre
`12-no_genre.sql` lists only the shows without a linked genre.

### 13. Number of shows by genre
`13-count_shows_by_genre.sql` counts linked shows per genre, sorted by the
count descending.

### 14. My genres
`14-my_genres.sql` lists the genres of the show Dexter.

### 15. Only Comedy
`15-comedy_only.sql` lists all Comedy shows.

### 16. List shows and genres
`16-shows_by_genre.sql` lists all shows with their genre names (`NULL` when
absent).
