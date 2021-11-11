-- CREATE TABLE orders_archive AS
-- SELECT * FROM orders
INSERT INTO orders_archive
SELECT *
FROM orders
WHERE order_date < '2019-01-01'