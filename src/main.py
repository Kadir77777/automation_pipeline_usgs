
import os, sys, time, logging
from ingest import ingest
from validate import validate
from transform import transform
from store import append_store, write_clean
from viz import build_chart

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
)

def main():
    start = time.time()
    try:
        df = ingest()
        df = validate(df)
        clean = transform(df)
        write_clean(clean)
        append_store(clean)
        build_chart()
        dur = round(time.time() - start, 2)
        logging.info(f"run_status=success duration_sec={dur}")
    except Exception as e:
        dur = round(time.time() - start, 2)
        logging.error(f"run_status=failed duration_sec={dur} error={e}")
        raise

if __name__ == "__main__":
    main()
