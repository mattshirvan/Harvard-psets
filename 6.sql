-- SELECT ROUND(AVG(rating), -2) FROM ratings WHERE (SELECT year FROM movies WHERE year = 2012);

SELECT AVG(rating) FROM ratings WHERE ratings.movie_id IN (SELECT id FROM movies WHERE year = 2012);



