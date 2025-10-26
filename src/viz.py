
import os, logging
import pandas as pd
import plotly.express as px
from plotly.offline import plot

CLEAN_PATH = os.getenv("CLEAN_PATH", "data/clean/cleaned.csv")
VIZ_PATH = os.getenv("VIZ_PATH", "viz/chart.html")

def build_chart(clean_path: str = CLEAN_PATH, out_path: str = VIZ_PATH) -> str:
    df = pd.read_csv(clean_path)
    if df.empty:
        raise RuntimeError("No data in cleaned.csv for visualization")

    # Simple time vs magnitude scatter
    fig = px.scatter(
        df.sort_values("time_iso"),
        x="time_iso",
        y="mag",
        hover_data=["place","latitude","longitude","depth","id"],
        title="USGS Earthquakes – Magnitude over Time (latest window)"
    )
    fig.update_layout(xaxis_title="Time (UTC)", yaxis_title="Magnitude (Mw)")

    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    plot(fig, filename=out_path, auto_open=False, include_plotlyjs="cdn")
    logging.info(f"dashboard_path={out_path}")
    return out_path
