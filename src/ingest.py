
import os, sys, json, time, logging
from typing import Tuple, Optional
import pandas as pd
import requests
from dotenv import load_dotenv

load_dotenv(override=True)

USGS_URL = os.getenv("USGS_URL", "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_hour.geojson")
RAW_DIR = os.getenv("RAW_DIR", "data/raw")

def fetch_geojson(url: str = USGS_URL, timeout: int = 30) -> dict:
    resp = requests.get(url, timeout=timeout)
    logging.info(f"source_url={url} http_status={resp.status_code}")
    resp.raise_for_status()
    return resp.json()

def to_dataframe(geojson: dict) -> pd.DataFrame:
    feats = geojson.get("features", [])
    rows = []
    for f in feats:
        props = f.get("properties", {}) or {}
        geom = f.get("geometry", {}) or {}
        coords = geom.get("coordinates", [None, None, None])
        row = {
            "id": f.get("id"),
            "time": props.get("time"),
            "updated": props.get("updated"),
            "mag": props.get("mag"),
            "place": props.get("place"),
            "type": props.get("type"),
            "status": props.get("status"),
            "tsunami": props.get("tsunami"),
            "sig": props.get("sig"),
            "longitude": coords[0] if len(coords) > 0 else None,
            "latitude": coords[1] if len(coords) > 1 else None,
            "depth": coords[2] if len(coords) > 2 else None,
        }
        rows.append(row)
    return pd.DataFrame(rows)

def save_raw_snapshot(geojson: dict, raw_dir: str = RAW_DIR) -> str:
    os.makedirs(raw_dir, exist_ok=True)
    stamp = time.strftime("%Y%m%d_%H%M%S")
    path = os.path.join(raw_dir, f"usgs_{stamp}.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(geojson, f)
    return path

def ingest() -> pd.DataFrame:
    gj = fetch_geojson()
    raw_path = save_raw_snapshot(gj)
    logging.info(f"raw_snapshot_path={raw_path}")
    df = to_dataframe(gj)
    logging.info(f"rows_in={len(df)}")
    return df
