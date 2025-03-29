WITH DistinctOrders AS (
  SELECT 
    o.order_id,
    o.customer_id,
    o.order_delivered_customer_date,
    p.payment_value
  FROM olist_orders o
  JOIN olist_order_payments p ON o.order_id = p.order_id
  WHERE o.order_status = 'delivered'
    AND o.order_delivered_customer_date IS NOT NULL
    AND strftime('%Y', o.order_delivered_customer_date) IN ('2016','2017','2018')
  GROUP BY o.order_id, o.customer_id, o.order_delivered_customer_date
),
MonthlyRevenue AS (
  SELECT 
    strftime('%m', order_delivered_customer_date) AS month_no,
    strftime('%Y', order_delivered_customer_date) AS year,
    SUM(payment_value) AS monthly_total
  FROM DistinctOrders
  GROUP BY month_no, year
)
SELECT
  month_no,
  CASE month_no
    WHEN '01' THEN 'Jan'
    WHEN '02' THEN 'Feb'
    WHEN '03' THEN 'Mar'	
    WHEN '04' THEN 'Apr'
    WHEN '05' THEN 'May'
    WHEN '06' THEN 'Jun'
    WHEN '07' THEN 'Jul'
    WHEN '08' THEN 'Aug'
    WHEN '09' THEN 'Sep'
    WHEN '10' THEN 'Oct'
    WHEN '11' THEN 'Nov'
    WHEN '12' THEN 'Dec'
  END AS month,
  COALESCE(ROUND(MAX(CASE WHEN year = '2016' THEN monthly_total END), 2), 0.00) AS "Year2016",
  COALESCE(ROUND(MAX(CASE WHEN year = '2017' THEN monthly_total END), 2), 0.00) AS "Year2017",
  COALESCE(ROUND(MAX(CASE WHEN year = '2018' THEN monthly_total END), 2), 0.00) AS "Year2018"
FROM MonthlyRevenue
GROUP BY month_no
ORDER BY month_no;