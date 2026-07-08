import psycopg2

conn = psycopg2.connect(
    host     = "localhost",
    port     = 5434,
    dbname   = "itc6050",
    user     = "itc6050",
    password = "itc6050"
)
conn.autocommit = True

with conn.cursor() as cur:
    cur.execute("""
        DELETE FROM raw_bookstore_sofiatr.orders a
        USING raw_bookstore_sofiatr.orders b
        WHERE a.order_id = b.order_id
          AND a.ctid < b.ctid;
    """)
    print(f"Διαγράφηκαν {cur.rowcount} διπλότυπες γραμμές")

conn.close()