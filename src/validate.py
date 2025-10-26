
import pandas as pd
import logging

def validate(df: pd.DataFrame) -> pd.DataFrame:
    before = len(df)
    df = df.dropna(subset=["id", "time"])
    df = df[df["mag"].fillna(0).between(-1.0, 12.0)]
    df = df[df["latitude"].between(-90, 90, inclusive="both")]
    df = df[df["longitude"].between(-180, 180, inclusive="both")]
    after = len(df)
    logging.info(f"rows_valid={after} rows_dropped={before - after}")
    return df
