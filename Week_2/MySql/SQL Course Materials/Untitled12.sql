SELECT *
FROM orders o
JOIN customer c
	ON o.customer_id=c.customer_id