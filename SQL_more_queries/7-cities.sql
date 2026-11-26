-- Creates the database hbtn_0d_usa if it does not already exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- Selects the database hbtn_0d_usa
USE hbtn_0d_usa;
-- Creates the table states if it does not already exist, for the foreign key
CREATE TABLE IF NOT EXISTS states (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, name VARCHAR(256) NOT NULL);
-- Creates the table cities if it does not already exist
CREATE TABLE IF NOT EXISTS cities (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, state_id INT NOT NULL, name VARCHAR(256) NOT NULL, FOREIGN KEY (state_id) REFERENCES states(id));
