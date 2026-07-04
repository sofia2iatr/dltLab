# pipeline_orders_api.py
import dlt
import json

@dlt.resource(
    name              = "orders",
    write_disposition = "append",
    primary_key       = "order_id"
)
def orders_from_api(
    updated_at = dlt.sources.incremental("order_date", initial_value="2026-01-01")
):
    with open("files/orders_api.json") as f:
        orders = json.load(f)

    for order in orders:
        if order["order_date"] > updated_at.last_value:
            yield order

pipeline = dlt.pipeline(
    pipeline_name = "orders_api_pipeline",
    destination   = "postgres",
    dataset_name  = "raw_bookstore_sofiatr"
)

load_info = pipeline.run(orders_from_api())
print(load_info)