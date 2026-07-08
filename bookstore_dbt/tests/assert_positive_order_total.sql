SELECT *
FROM {{ ref('stg_orders') }}
WHERE total_usd <= 0