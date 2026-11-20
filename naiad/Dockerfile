# The add-on runs the published multi-arch Naiad app image directly; Docker pulls
# the architecture-matching variant from the manifest, so a single FROM covers
# amd64 and aarch64. The add-on layers only the Supervisor bootstrap on top, so one
# image powers both the standalone container and the Home Assistant add-on.
#
# Pinned to the add-on version (the Supervisor passes it as BUILD_VERSION; the
# release workflow keeps add-on and app versions in lockstep). With `:latest` the
# installed app version depended on when the add-on was (re)built, and a cached
# `latest` layer could keep serving an old app after an add-on update.
ARG BUILD_VERSION=latest
FROM ghcr.io/neffez/naiad:${BUILD_VERSION}

# Persist the SQLite database (and an optional config.yaml seed) on the mapped
# /data volume the Supervisor provides.
ENV NAIAD_DATA_DIR=/data \
    NAIAD_CONFIG=/data/config.yaml

# Supervisor injects SUPERVISOR_TOKEN and proxies Core at ws://supervisor/core/websocket;
# the backend detects this automatically (resolve_ha_connection). No LLAT needed.
COPY run.sh /run.sh
RUN chmod a+x /run.sh

CMD ["/run.sh"]
