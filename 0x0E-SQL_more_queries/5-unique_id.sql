-- create table 
-- cat 5-unique_id.sql | mysql -hlocalhost -uroot -p 
CREATE TABLE IF NOT EXISTS unique_id (id INT DEFAULT 1 UNIQUE, name VARCHAR(256));