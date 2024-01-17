-- number by score
-- cat 15-groups.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
SELECT score, COUNT(*) AS number FROM second_table
    GROUP BY score
    ORDER BY number DESC;