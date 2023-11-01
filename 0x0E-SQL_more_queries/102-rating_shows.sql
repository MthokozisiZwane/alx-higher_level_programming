-- 102-rating_shows.sql
SELECT tv_shows.title, SUM(rating) AS rating_sum
FROM tv_shows
LEFT JOIN show_ratings ON tv_shows.id = show_ratings.show_id
GROUP BY tv_shows.title
ORDER BY rating_sum DESC;

