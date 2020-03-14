SELECT movies.title AS title
FROM movies
JOIN stars ON movies.id = stars.movie_id
JOIN people ON people.id = stars.person_id
WHERE people.name = 'Chadwick Boseman'
ORDER BY (SELECT ratings.rating AS rating FROM ratings) DESC
LIMIT 5;