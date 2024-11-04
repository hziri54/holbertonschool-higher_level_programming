-- A script that lists all Comedy shows in the databaseg.
SELECT tv_shows.title 
FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
JOIN tv_genres ON tv_genres.id = tv_shows_genre_id
WHERE tv_genres.name = "Comedy"
ORDER BY tv_shows.title ASC;
