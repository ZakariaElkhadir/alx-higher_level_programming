--lists all genres from hbtn_0d_tvshows
-- cat 13-count_shows_by_genre.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows

SELECT c.name AS genre, COUNT(*) AS number_of_shows FROM tb_genres c
	JOIN tv_show_genres ON c.id = s.genre_id
GROUP BY c.name
ORDER BY number_of_shows DESC;
