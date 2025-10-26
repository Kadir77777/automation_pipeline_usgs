
import os, logging
import pandas as pd

DATA_STORE = os.getenv("DATA_STORE", "data/data_store.csv")
CLEAN_PATH = os.getenv("CLEAN_PATH", "data/clean/cleaned.csv")

def append_store(clean_df: pd.DataFrame) -> None:
    # Append new rows to data_store dedup by id
    os.makedirs(os.path.dirname(DATA_STORE), exist_ok=True)
    if os.path.exists(DATA_STORE):
        existing = pd.read_csv(DATA_STORE)
        merged = pd.concat([existing, clean_df], ignore_index=True)
        merged = merged.drop_duplicates(subset=["id"]).sort_values("time_iso")
    else:
        merged = clean_df.sort_values("time_iso")

    merged.to_csv(DATA_STORE, index=False)
    logging.info(f"rows_appended_store={len(merged)} store_path={DATA_STORE}")

def write_clean(clean_df: pd.DataFrame) -> None:
    os.makedirs(os.path.dirname(CLEAN_PATH), exist_ok=True)
    clean_df.to_csv(CLEAN_PATH, index=False)
    logging.info(f"cleaned_path={CLEAN_PATH}")
