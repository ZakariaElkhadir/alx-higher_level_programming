-- remove low score from table
-- cat 10-top_score.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
DELETE FROM second_table
    WHERE score <= 5;