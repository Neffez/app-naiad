#!/usr/bin/env sh
set -e

# The Supervisor writes the chosen add-on options to /data/options.json. Read them
# with a tiny Python helper (jq isn't in the base image) and map them to the env
# vars Naiad expects.
OPTIONS_FILE="/data/options.json"

read_option() {
    # read_option <key> <default>
    if [ -f "${OPTIONS_FILE}" ]; then
        python -c "import json,sys; print(json.load(open('${OPTIONS_FILE}')).get('${1}', '${2}'))" 2>/dev/null || echo "${2}"
    else
        echo "${2}"
    fi
}

# log_level → LOG_LEVEL (uppercased for Python's logging level names).
LOG_LEVEL="$(read_option log_level info)"
LOG_LEVEL="$(echo "${LOG_LEVEL}" | tr '[:lower:]' '[:upper:]')"
export LOG_LEVEL

# password → NAIAD_PASSWORD_HASH. Naiad keeps the app password out of its database
# (env-only); in the add-on there are no env vars to set, so this option is how you
# protect the direct port. The value may be plaintext or a bcrypt hash ($2b$...) —
# Naiad accepts both. Left empty: the sidebar still works via HA ingress trust, but
# the direct port stays locked until a password is set.
PASSWORD="$(read_option password "")"
if [ -n "${PASSWORD}" ]; then
    export NAIAD_PASSWORD_HASH="${PASSWORD}"
    echo "[naiad] app password configured from add-on options"
fi

# mqtt_password → MQTT_PASSWORD. Naiad keeps the MQTT broker password out of its
# database (env-only), so this option is how you set it inside the add-on. Only
# relevant when the MQTT statistics bridge is enabled in Naiad's UI.
MQTT_PASSWORD="$(read_option mqtt_password "")"
if [ -n "${MQTT_PASSWORD}" ]; then
    export MQTT_PASSWORD
    echo "[naiad] MQTT password configured from add-on options"
fi

echo "[naiad] starting Home Assistant add-on (LOG_LEVEL=${LOG_LEVEL})"

# WORKDIR /app is inherited from the base image, where the naiad package lives.
exec uvicorn naiad.main:app --host 0.0.0.0 --port 8080
