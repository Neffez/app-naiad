# Changelog

## 0.1.0

- Initial Home Assistant add-on packaging for Naiad (Phase 6c).
- Ingress sidebar entry plus an optional direct host port (default `5195`).
- Connects to Home Assistant Core through the Supervisor proxy with the
  auto-provided `SUPERVISOR_TOKEN` — no long-lived access token required.
- Persists the SQLite database and optional config seed on the `/data` volume.
- `log_level` option mapped to the backend logger.
