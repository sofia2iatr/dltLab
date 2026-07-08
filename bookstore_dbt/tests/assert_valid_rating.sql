SELECT *
FROM {{ ref('stg_books') }}
WHERE rating < 0 OR rating > 5