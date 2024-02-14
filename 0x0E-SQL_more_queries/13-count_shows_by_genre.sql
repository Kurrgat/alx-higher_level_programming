-- Select tv_genres.name as genre and count(tv_show_genres.tv_show_id) as number_of_shows from tv_genres left join tv_show_genres tables
SELECT tv_genres.name AS genre, COUNT(tv_show_genres.show_id) AS number_of_shows
FROM tv_genres
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
GROUP BY tv_genres.name
ORDER BY number_of_shows DESC;
