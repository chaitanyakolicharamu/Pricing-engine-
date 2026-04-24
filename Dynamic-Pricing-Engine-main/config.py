
import pandas as pd
import os

SERP_API_KEY = "your api key from serpapi.com"   # free at serpapi.com

CITY_LAT  = 39.0997
CITY_LON  = -94.5786

FAIRNESS_LAMBDA = 0.3
PRICE_STEP      = 500.0    # bigger step for real electronics prices

_csv_path = os.path.join(os.path.dirname(__file__), "products.csv")
_df       = pd.read_csv(_csv_path)

# Rename your_price → base_price so rest of code works
if "your_price" in _df.columns:
    _df = _df.rename(columns={"your_price": "base_price"})

PRODUCTS  = _df.to_dict("records")
MIN_PRICE = min(p["min_price"]  for p in PRODUCTS)
MAX_PRICE = max(p["max_price"]  for p in PRODUCTS)
BASE_PRICE = PRODUCTS[0]["base_price"]
