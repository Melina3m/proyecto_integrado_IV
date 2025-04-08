SELECT
    pcnt.product_category_name_english AS Category,
    COUNT(DISTINCT ooi.order_id) AS Num_order,
    SUM(oop.payment_value) AS Revenue
FROM olist_order_items ooi
JOIN olist_products op 
    ON op.product_id = ooi.product_id
JOIN product_category_name_translation pcnt 
    ON op.product_category_name = pcnt.product_category_name
JOIN olist_orders oo 
    ON ooi.order_id = oo.order_id
JOIN olist_order_payments oop 
    ON oo.order_id = oop.order_id
WHERE oo.order_status = 'delivered'
  AND oo.order_delivered_customer_date IS NOT NULL
  AND pcnt.product_category_name IS NOT NULL
GROUP BY Category
ORDER BY Revenue DESC
LIMIT 10;