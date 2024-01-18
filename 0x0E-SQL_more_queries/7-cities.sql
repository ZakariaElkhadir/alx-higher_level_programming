-- create database and table
-- cat 7-cities.sql | mysql -hlocalhost -uroot -p
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE cities (
    id INT AUTO_INCREMENT NOT NULL PRIMARY KEY UNIQUE,
    state_id INT NOT NULL,
    FOREIGN KEY (state_id) REFERENCES states (id)
)