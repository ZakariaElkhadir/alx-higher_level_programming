-- lists all shows contained in the data ...
-- cat 11-genre_id_all_shows.sql | sudo mysql -hlocalhost -uroot -p hbtn_0d_tvshows

SELECT c.title, s.genre_id FROM hbtn_0d_tvshows
LEFT JOIN tv_show_genres s ON c.id = s.show_id
ORDER BY c.title, s.genre_id ASC;
