SELECT
    o.order_id,
    o.customer_id,
    o.ordered_on,
    o.quantity,
    o.total_usd,
    b.title                 AS book_title,
    b.genre,
    b.rating,
    a.author_name,
    a.nationality
FROM {{ ref('stg_orders') }}  o
JOIN {{ ref('stg_books') }}   b USING (book_id)
JOIN {{ ref('stg_authors') }} a USING (author_id)