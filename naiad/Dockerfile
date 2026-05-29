# The add-on runs the published multi-arch Naiad app image directly; Docker pulls
# the architecture-matching variant from the manifest, so a single FROM covers
# amd64 and aarch64. The add-on layers only the Supervisor bootstrap on top, so one
# image powers both the standalone container and the Home Assistant add-on.
FROM ghcr.io/neffez/naiad:latest

# Persist the SQLite database (and an optional config.yaml seed) on the mapped
# /data volume the Supervisor provides.
ENV NAIAD_DATA_DIR=/data \
    NAIAD_CONFIG=/data/config.yaml

# Supervisor injects SUPERVISOR_TOKEN and proxies Core at ws://supervisor/core/websocket;
# the backend detects this automatically (resolve_ha_connection). No LLAT needed.
COPY run.sh /run.sh
RUN chmod a+x /run.sh

CMD ["/run.sh"]
