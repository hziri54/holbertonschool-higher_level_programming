SELECT tv_genres.name
FROM tv_shows
JOIN tv_shows_genres ON tv_shows.id = tv_shows_genres.tv_show_id
JOIN tv_genres ON tv_shows_genres.tv_genre_id = tv_genres.id
WHERE tv_shows.title = 'Dexter'
ORDER BY tv_genres.name ASC;
