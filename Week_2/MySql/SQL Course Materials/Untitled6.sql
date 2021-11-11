-- SELECT *
-- FROM customers
-- ORDER BY state,first_name   -- ->assending
-- ORDER BY state DESC,first_name -- DESC ->descending
-- order by is for sorting
SELECT *
FROM order_items
WHERE order_id = 2
ORDER BY quantity * unit_price DESC
