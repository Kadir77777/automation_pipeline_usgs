
#!/usr/bin/env bash
set -euo pipefail
REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$REPO_DIR"
LOCKFILE=".pipeline.lock"
exec 9>"$LOCKFILE"
if ! flock -n 9; then
  echo "[WARN] $(date -Is) another run is in progress; exiting."
  exit 0
fi
if [ -f ".venv/bin/activate" ]; then source .venv/bin/activate; fi
mkdir -p logs data/raw data/clean viz
STAMP="$(date +%Y%m%d_%H%M%S)"
LOGFILE="logs/run_${STAMP}.log"
echo "[INFO] $(date -Is) cron start" | tee -a "$LOGFILE"
set +e
python src/main.py >> "$LOGFILE" 2>&1
RC=$?
set -e
if [ $RC -ne 0 ]; then
  echo "[ERROR] $(date -Is) pipeline failed with code $RC" | tee -a "$LOGFILE"
  exit $RC
fi
echo "[INFO] $(date -Is) cron end OK" | tee -a "$LOGFILE"
