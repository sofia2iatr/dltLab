{% snapshot snap_books %}

{{
  config(
    target_schema = 'snapshots_sofiatr',
    unique_key    = 'book_id',
    strategy      = 'check',
    check_cols    = ['rating', 'available']
  )
}}

SELECT
    book_id,
    title,
    author_id,
    genre,
    rating,
    available
FROM {{ source('raw', 'books') }}

{% endsnapshot %}