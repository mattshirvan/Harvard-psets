SELECT people.name AS name
FROM people
JOIN stars ON people.id = stars.person_id
JOIN movies ON movies.id = stars.movie_id
WHERE stars.movie_id = (SELECT movies.id FROM movies JOIN stars ON movies.id = stars.movie_id 
JOIN people ON people.id = stars.person_id WHERE name = (SELECT people.name FROM people WHERE (name = 'Kevin Bacon' AND  birth = 1958))) AND name NOT IN ('Kevin Bacon');