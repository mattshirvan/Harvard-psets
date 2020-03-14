SELECT movies.title AS title
FROM movies
JOIN stars ON movies.id = stars.movie_id
JOIN people ON people.id = stars.person_id
WHERE name IN ('Helena Bonham Carter', 'Johnny Depp')
GROUP BY title
HAVING COUNT(stars.movie_id) > 1;

-- the last two lines I saw on stack exchange, otherwise all mine :)