SELECT
    b.genre,
    g.category,
    g.is_fiction,
    COUNT(o.order_id)        AS total_orders,
    SUM(o.quantity)          AS books_sold,
    SUM(o.total_usd)         AS total_revenue,
    AVG(b.rating)            AS avg_rating
FROM {{ ref('stg_orders') }}     o
JOIN {{ ref('stg_books') }}      b USING (book_id)
LEFT JOIN {{ ref('genre_map') }} g USING (genre)
GROUP BY b.genre, g.category, g.is_fiction
ORDER BY total_revenue DESC