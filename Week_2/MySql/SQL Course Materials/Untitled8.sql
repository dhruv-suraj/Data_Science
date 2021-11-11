-- SELECT order_id,first_name
-- FROM orders
-- INNER JOIN customers ON orders.customer_id=customers.customer_id
SELECT *
FROM order_items
INNER JOIN products ON order_items.product_id=products.product_id