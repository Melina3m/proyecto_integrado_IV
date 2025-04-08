SELECT
    oc.customer_state,
    SUM(oop.payment_value) AS Revenue
FROM olist_customers oc
LEFT JOIN olist_orders oo 
    ON oc.customer_id = oo.customer_id
LEFT JOIN olist_order_payments oop 
    ON oo.order_id = oop.order_id
WHERE oo.order_status = 'delivered'
  AND oo.order_delivered_customer_date IS NOT NULL
GROUP BY oc.customer_state
ORDER BY Revenue DESC
LIMIT 10;