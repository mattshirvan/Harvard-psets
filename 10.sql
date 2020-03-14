-- SELECT people.name AS name
-- FROM people
-- JOIN directors ON people.id = directors.person_id
-- JOIN movies ON movies.id = directors.movie_id
-- WHERE (SELECT rating FROM ratings WHERE rating >= 9.0);

SELECT people.name AS name
FROM people
JOIN directors ON people.id = directors.person_id
JOIN movies ON movies.id = directors.movie_id
WHERE movie_id IN (SELECT ratings.movie_id FROM ratings WHERE rating >= 9.0);