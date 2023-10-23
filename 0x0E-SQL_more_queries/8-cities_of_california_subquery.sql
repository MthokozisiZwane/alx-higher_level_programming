-- 8-cities_of_california_subquery.sql
USE hbtn_0d_usa;
SELECT * FROM cities WHERE state_id = (SELECT id FROM states WHERE name = 'California');

