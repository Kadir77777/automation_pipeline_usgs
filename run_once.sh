
#!/usr/bin/env bash
set -euo pipefail
REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$REPO_DIR"
if [ -f ".venv/bin/activate" ]; then source .venv/bin/activate; fi
mkdir -p logs data/raw data/clean viz
STAMP="$(date +%Y%m%d_%H%M%S)"
LOGFILE="logs/run_${STAMP}.log"
echo "[INFO] $(date -Is) starting one-shot run" | tee -a "$LOGFILE"
python src/main.py 2>&1 | tee -a "$LOGFILE"
echo "[INFO] $(date -Is) finished one-shot run" | tee -a "$LOGFILE"
