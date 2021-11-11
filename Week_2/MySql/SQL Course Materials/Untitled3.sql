-- SELECT *
-- FROM customers
-- WHERE points>=1000 AND points<=3000--
-- WHERE points BETWEEN 1000 AND 3000
SELECT *
FROM customers
WHERE birth_date BETWEEN "1-1-1990" AND "1-1-2000"