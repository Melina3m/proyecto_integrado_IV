SELECT 
    order_status, COUNT(*) AS "Ammount" 
FROM olist_orders 
GROUP BY order_status;