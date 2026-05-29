# Changelog

## 0.1.1

- Remove the custom AppArmor profile: it blocked the Python interpreter from
  loading `libpython3.12.so.1.0`, so the add-on failed to start.
- Run the published image directly via a hardcoded `FROM` and drop `build.yaml`
  (clears the Supervisor's build.yaml-deprecation warning); the multi-arch manifest
  still selects the matching architecture.

## 0.1.0

- Initial Home Assistant add-on packaging for Naiad (Phase 6c).
- Ingress sidebar entry plus an optional direct host port (default `5195`).
- Connects to Home Assistant Core through the Supervisor proxy with the
  auto-provided `SUPERVISOR_TOKEN` — no long-lived access token required.
- Persists the SQLite database and optional config seed on the `/data` volume.
- `log_level` option mapped to the backend logger.
