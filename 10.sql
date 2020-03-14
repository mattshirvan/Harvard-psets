SELECT people.name AS name
FROM people
JOIN directors ON people.id = directors.person_id
JOIN movies ON movies.id = directors.movie_id
WHERE (SELECT ratings.rating AS rating FROM ratings WHERE rating >= 9.0);