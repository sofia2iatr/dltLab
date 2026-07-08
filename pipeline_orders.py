import dlt
import pandas as pd

@dlt.resource(
    name               = "orders",
    write_disposition  = "merge",
    primary_key        = "order_id"
)
def orders_incremental(
    updated_at = dlt.sources.incremental("order_date", initial_value="2026-01-01")
):
    df = pd.read_csv("files/orders.csv")
    df["order_date"] = pd.to_datetime(df["order_date"]).dt.date.astype(str)
    new_rows = df[df["order_date"] > updated_at.last_value]
    yield new_rows.to_dict(orient="records")

pipeline = dlt.pipeline(
    pipeline_name = "orders_pipeline",
    destination   = "postgres",
    dataset_name  = "raw_bookstore_sofiatr"
)

load_info = pipeline.run(orders_incremental())
print(load_info)