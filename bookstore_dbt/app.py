import streamlit as st
import pandas as pd
import psycopg2

# --- Connection using secrets.toml ---
conn = psycopg2.connect(
    host     = st.secrets["postgres"]["host"],
    port     = st.secrets["postgres"]["port"],
    dbname   = st.secrets["postgres"]["dbname"],
    user     = st.secrets["postgres"]["user"],
    password = st.secrets["postgres"]["password"]
)

SCHEMA = "dbt_dev_sofiatr"   # change to your schema

st.title("Bookstore Sales Dashboard")

# --- Revenue by genre (from agg_sales_by_genre mart) ---
st.header("Revenue by Genre")
df_genre = pd.read_sql(f"""
    SELECT genre, category, total_orders, books_sold, total_revenue, avg_rating
    FROM {SCHEMA}.agg_sales_by_genre
    ORDER BY total_revenue DESC
""", conn)

st.bar_chart(df_genre.set_index("genre")["total_revenue"])
st.dataframe(df_genre)

# --- Top authors by revenue ---
st.header("Top Authors by Revenue")
df_authors = pd.read_sql(f"""
    SELECT
        author_name,
        COUNT(*)        AS total_orders,
        SUM(total_usd)  AS total_revenue
    FROM {SCHEMA}.fct_orders
    GROUP BY author_name
    ORDER BY total_revenue DESC
    LIMIT 10
""", conn)

st.bar_chart(df_authors.set_index("author_name")["total_revenue"])
st.dataframe(df_authors)

# --- All orders ---
st.header("All Orders")
df_orders = pd.read_sql(f"""
    SELECT order_id, ordered_on, book_title, author_name, genre, quantity, total_usd
    FROM {SCHEMA}.fct_orders
    ORDER BY ordered_on DESC
""", conn)

st.dataframe(df_orders)

conn.close()