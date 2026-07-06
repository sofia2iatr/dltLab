SELECT
    order_id,
    customer_id,
    book_id,
    quantity,
    total::NUMERIC(10,2)    AS total_usd,
    order_date::DATE        AS ordered_on
FROM {{ source('raw', 'orders') }}
WHERE total > 0