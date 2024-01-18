-- lists all shows contained in hbtn_0d_tvshows
-- cat 12-no_genre.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows

SELECT c.title, s.genre_id
FROM tv_shows c
LEFT JOIN tv_show_genres s ON c.id = s.show_id
WHERE s.genre_id IS NULL
ORDER BY c.title, s.genre_id ASC;
