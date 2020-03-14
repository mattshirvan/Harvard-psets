-- SELECT ROUND(AVG(rating), -2) FROM ratings WHERE (SELECT year FROM movies WHERE year = 2012);

SELECT printf("%.2f", AVG(rating)) FROM ratings WHERE (SELECT year FROM movies WHERE year = 2012);



