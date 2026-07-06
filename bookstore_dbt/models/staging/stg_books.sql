SELECT
    book_id,
    title,
    author_id,
    genre,
    year AS published_year,
    CAST(rating AS NUMERIC(3,1)) AS rating,
    available
FROM {{ source('raw', 'books') }}
WHERE title IS NOT NULL