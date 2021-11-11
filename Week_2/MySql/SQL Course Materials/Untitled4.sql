-- SELECT *
-- FROM customers
-- WHERE last_name LIKE "b%"
-- WHERE last_name LIKE "b__y"
-- WHERE last_name regexp "field"
-- %is basicaly for any letters
-- _single charachter
SELECT *
FROM customers
-- WHERE address LIKE "%TRAIL%" OR 
-- 	  address LIKE "%AVENUE%"
      
WHERE phone LIKE "%9"