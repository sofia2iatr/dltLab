SELECT
    author_id,
    name AS author_name,
    nationality,
    born AS birth_year
FROM {{ source('raw', 'authors') }}