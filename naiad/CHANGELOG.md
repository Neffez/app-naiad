# Changelog

## 0.1.17 (2026-05-30)

- fix: ruff format system.py (collapse single-expr exec call)

## 0.1.16 (2026-05-30)

- fix: dynamic season icon (sun in summer, snowflake in winter)

## 0.1.15 (2026-05-30)

- fix: weather strip icons-only, season shows Summer/Winter

## 0.1.14 (2026-05-30)

- fix: history duplication, timezones, hero next run, factor display

## 0.1.12 (2026-05-30)

- docs: drop 'optimized for KNX' — Naiad is hardware-agnostic via HA

## 0.1.11 (2026-05-30)

- feat(notify): per-recipient categories + platform-aware quiet
- feat(notify): watchdog push, evening reminder, configurable events + quiet

## 0.1.10 (2026-05-30)

- fix(i18n): unify 'Ventil/Valve' to 'Zone' in the UI
- fix(config): make zone assignment obvious; robust export with clipboard fallback

## 0.1.9 (2026-05-30)

- fix: code-review quick wins (plan tz, week consistency, factor/duration bounds)
- docs: fresh code review — findings on liter accounting, auth, scheduling

## 0.1.8 (2026-05-30)

- feat(notify): test-notification button + clearer notify logging

## 0.1.5 (2026-05-30)

- feat(config): searchable picker for notify targets

## 0.1.2

- Add a `password` add-on option. Naiad keeps the app password env-only, and the
  add-on has no env vars to set, so this is how you protect direct-port access
  (`http://<haos-ip>:5195`). Plaintext or a bcrypt hash; the sidebar (ingress)
  needs no password. `run.sh` exports it as `NAIAD_PASSWORD_HASH`.

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
