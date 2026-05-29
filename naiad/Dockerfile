ARG BUILD_FROM
FROM ${BUILD_FROM}

# BUILD_FROM is the published multi-arch Naiad app image (see build.yaml). We add
# only the add-on bootstrap on top, so a single image powers both the standalone
# container and the Home Assistant add-on.

# Persist the SQLite database (and an optional config.yaml seed) on the mapped
# /data volume the Supervisor provides.
ENV NAIAD_DATA_DIR=/data \
    NAIAD_CONFIG=/data/config.yaml

# Supervisor injects SUPERVISOR_TOKEN and proxies Core at ws://supervisor/core/websocket;
# the backend detects this automatically (resolve_ha_connection). No LLAT needed.
COPY run.sh /run.sh
RUN chmod a+x /run.sh

CMD ["/run.sh"]
