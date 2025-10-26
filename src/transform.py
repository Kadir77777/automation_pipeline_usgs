
import pandas as pd
import logging

def transform(df: pd.DataFrame) -> pd.DataFrame:
    # Convert epoch ms → ISO8601 strings
    def ms_to_iso(ms):
        try:
            return pd.to_datetime(int(ms), unit="ms", utc=True).isoformat()
        except Exception:
            return None

    df = df.copy()
    df["time_iso"] = df["time"].apply(ms_to_iso)
    df["updated_iso"] = df["updated"].apply(ms_to_iso)
    # Lightweight, keep essential columns in a stable order
    cols = ["id","time_iso","updated_iso","mag","place","latitude","longitude","depth","type","status","tsunami","sig"]
    out = df[cols].drop_duplicates(subset=["id"])
    logging.info(f"rows_out={len(out)}")
    return out
