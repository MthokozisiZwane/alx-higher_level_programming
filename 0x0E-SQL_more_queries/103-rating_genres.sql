-- 103-rating_genres.sql
USE hbtn_0d_tvshows_rate;
SELECT tv_genres.name, SUM(rating) AS rating_sum
FROM tv_genres
LEFT JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
LEFT JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
LEFT JOIN show_ratings ON tv_shows.id = show_ratings.show_id
GROUP BY tv_genres.name
ORDER BY rating_sum DESC;

