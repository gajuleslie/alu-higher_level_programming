-- Creates the table second_table if it does not already exist
CREATE TABLE IF NOT EXISTS second_table (id INT, name VARCHAR(256), score INT);
-- Adds John with a score of 10
INSERT INTO second_table (id, name, score) VALUES (1, 'John', 10);
-- Adds Alex with a score of 3
INSERT INTO second_table (id, name, score) VALUES (2, 'Alex', 3);
-- Adds Bob with a score of 14
INSERT INTO second_table (id, name, score) VALUES (3, 'Bob', 14);
-- Adds George with a score of 8
INSERT INTO second_table (id, name, score) VALUES (4, 'George', 8);
