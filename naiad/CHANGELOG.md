# Changelog

## 0.2.9 (2026-05-31)

- fix: formatting

## 0.2.8 (2026-05-31)

- fix: deleted zones will now also be removed from the sequence references

## 0.2.7 (2026-05-31)

- feat: improved number fields

## 0.2.6 (2026-05-31)

- fix: proper favicon
- feat: i18n for notifications, "en" is now default for language
- fix: sort starlette imports to satisfy ruff I001
- fix: add missing type annotations to _SPAStaticFiles.get_response

## 0.2.5 (2026-05-31)

- fix: sort starlette imports to satisfy ruff I001
- fix: add missing type annotations to _SPAStaticFiles.get_response

## 0.2.4 (2026-05-31)

- fix: fix routing
- feat: add login throttling (M-1) and skip runs at factor 0% (M-2)
- fix: resolve low-risk review findings (rain-vs-paused, docs, design tokens)
- docs: refresh code review and README against current implementation

## 0.2.3 (2026-05-31)

- feat: add login throttling (M-1) and skip runs at factor 0% (M-2)
- fix: resolve low-risk review findings (rain-vs-paused, docs, design tokens)
- docs: refresh code review and README against current implementation

## 0.2.1 (2026-05-31)

- fix: use appropriate emojis

## 0.2.0 (2026-05-31)

- style: apply ruff format
- feat: publish irrigation statistics to Home Assistant over MQTT

## 0.1.31 (2026-05-31)

- feat: schedule and run individual zones, not just sequences

## 0.1.30 (2026-05-31)

- fix: remove unused type-ignore in history delete
- feat: drag-and-drop reordering of dashboard sequence and zone cards

## 0.1.29 (2026-05-31)

- test: fix peer dependency resolution for Vitest
- test: add Vitest frontend test suite

## 0.1.28 (2026-05-31)

- feat: add API endpoints to clear sequence overrides

## 0.1.27 (2026-05-31)

- feat: add history deletion with confirmation and 30-day cleanup

## 0.1.26 (2026-05-30)

- fix: move notify targets setting to notifications section
- fix(frontend): keep frame-ancestors input from overflowing its card

## 0.1.25 (2026-05-30)

- fix: resolve frontend ESLint errors and npm peer-dep conflict

## 0.1.24 (2026-05-30)

- feat: remove emergency stop button from dashboard

## 0.1.23 (2026-05-30)

- fix(frontend): portal settings tooltips and drop duplicate notification settings

## 0.1.22 (2026-05-30)

- feat: confirm before stopping a run or skipping a scheduled run

## 0.1.21 (2026-05-30)

- feat: fall back to yesterday's recorded max temperature
- style: apply ruff format to test_factors.py
- feat: irrigation UX fixes and improvements

## 0.1.20 (2026-05-30)

- feat: friendly schedule picker (weekdays + times) instead of raw cron

## 0.1.18 (2026-05-30)

- feat: add per-target test notification button in notify target config

## 0.1.19 (2026-05-30)

- refactor: remove duplicate rain/temperature factor settings from Anlagenkonfiguration

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
