#!/usr/bin/env sh
set -e

# Map the add-on option `log_level` to Naiad's LOG_LEVEL env var. The Supervisor
# writes the chosen options to /data/options.json. We default to "info" if the file
# or key is missing, and uppercase it for Python's logging level names.
OPTIONS_FILE="/data/options.json"
LOG_LEVEL="info"
if [ -f "${OPTIONS_FILE}" ]; then
    LOG_LEVEL="$(python -c "import json; print(json.load(open('${OPTIONS_FILE}')).get('log_level', 'info'))" 2>/dev/null || echo info)"
fi
LOG_LEVEL="$(echo "${LOG_LEVEL}" | tr '[:lower:]' '[:upper:]')"
export LOG_LEVEL

echo "[naiad] starting Home Assistant add-on (LOG_LEVEL=${LOG_LEVEL})"

# WORKDIR /app is inherited from the base image, where the naiad package lives.
exec uvicorn naiad.main:app --host 0.0.0.0 --port 8080
