WITH delivery_times AS (
    SELECT
        JULIANDAY(oo.order_delivered_customer_date) - JULIANDAY(oo.order_purchase_timestamp) AS real_time,
        JULIANDAY(oo.order_estimated_delivery_date) - JULIANDAY(oo.order_purchase_timestamp) AS estimated_time,
        STRFTIME('%m', oo.order_purchase_timestamp) AS month_no,
        CASE STRFTIME('%m', oo.order_purchase_timestamp)
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
        END AS month,
        STRFTIME('%Y', oo.order_purchase_timestamp) AS year_date
    FROM olist_orders oo
    WHERE oo.order_status = 'delivered'
      AND oo.order_delivered_customer_date IS NOT NULL
)
SELECT
    dt.month_no,
    dt.month,
    AVG(CASE WHEN dt.year_date = '2016' THEN dt.real_time END) AS Year2016_real_time,
    AVG(CASE WHEN dt.year_date = '2017' THEN dt.real_time END) AS Year2017_real_time,
    AVG(CASE WHEN dt.year_date = '2018' THEN dt.real_time END) AS Year2018_real_time,
    AVG(CASE WHEN dt.year_date = '2016' THEN dt.estimated_time END) AS Year2016_estimated_time,
    AVG(CASE WHEN dt.year_date = '2017' THEN dt.estimated_time END) AS Year2017_estimated_time,
    AVG(CASE WHEN dt.year_date = '2018' THEN dt.estimated_time END) AS Year2018_estimated_time
FROM delivery_times dt
GROUP BY dt.month_no, dt.month
HAVING dt.month_no IS NOT NULL
ORDER BY dt.month_no;