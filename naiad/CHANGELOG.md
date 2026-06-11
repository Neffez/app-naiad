# Changelog

## 0.6.12 (2026-06-11)

- feat: add decision log answering why a run watered or was skipped

## 0.6.11 (2026-06-10)

- add mqtt controls

## 0.6.10 (2026-06-10)

- added codereview.md and future_improvements.md
- added parity tests
- several fixes and improvements, added wind-abort after configurable time
- make npm step more robust

## 0.6.9 (2026-06-10)

- fixed several bugs and refactoring

## 0.6.8 (2026-06-10)

- fixed several bugs and refactoring

## 0.6.7 (2026-06-06)

- refactor: address code review of the settings rework
- feat(settings): reset watering factors to their base defaults
- refactor(frontend): unify config & settings into a sectioned settings area

## 0.6.6 (2026-06-04)

## 0.6.5 (2026-06-04)

## 0.6.4 (2026-06-04)

## 0.6.3 (2026-06-03)

- feat: add mqtt password

## 0.6.2 (2026-06-03)

- refactor: make OpenAPI the frontend API contract source

## 0.6.1 (2026-06-03)

- fix: improve ci, do not track static files

## 0.6.0 (2026-06-03)

- fix: formatting

## 0.5.25 (2026-06-03)

- fix: formatting

## 0.5.24 (2026-06-03)

- feat: add water balance rain mode and MQTT factor sensors`

## 0.5.22 (2026-06-02)

- feat: make tomorrow's rain peak opt-in via peak_tomorrow setting
- feat: scale rain factor to the day's peak forecast, not the latest reading

## 0.5.21 (2026-06-02)

- fix: fix test

## 0.5.19 (2026-06-02)

- fix: fix ruff formatting

## 0.5.18 (2026-06-02)

- fix: missing import, added test

## 0.5.17 (2026-06-02)

- fix: several codereview fixes

## 0.5.16 (2026-06-02)

- fix: ci and several codereview fixes

## 0.5.15 (2026-06-02)

- feat: per-zone staircase-timer support and durable valve-close retry
- docs: added AGENT.md

## 0.5.14 (2026-06-02)

- feat(frontend): surface query-load errors + tokenize repeated rgba literals (L-7)

## 0.5.13 (2026-06-02)

- fix(a11y): address code-review findings in dialog/toast/infotip
- a11y(frontend): add accessibility across components, pages and dialogs

## 0.5.12 (2026-06-01)

- refactor(frontend): remove unused EmergencyStop component
- docs: mark Low-item cleanup (L-4/L-5/L-6/L-7 a11y) in code review
- a11y(frontend): give icon-only buttons accessible names
- refactor(backend): throttle token writes, dedupe master switch + timestamp parsing

## 0.5.11 (2026-06-01)

- docs: mark M-3 progress in code review (query keys, Config split, history)
- refactor(frontend): fetch config once for the history table
- refactor(frontend): split Config.tsx into cohesive modules
- refactor(frontend): centralize React Query keys
- docs: rewrite code review with findings and work log
- refactor: remove dead driver code, bound HA fan-out, English MQTT names
- fix: close forward_header auth fail-open and config-import reload race

## 0.5.10 (2026-06-01)

- feat: expose notification queue_max_hours in the config UI
- feat: persist the notification queue so it survives restarts
- feat: queue notifications during HA outages and re-deliver on reconnect

## 0.5.9 (2026-06-01)

- fix: don't ignore README.md in .dockerignore (no inline comments)

## 0.5.6 (2026-06-01)

- Enhance README with image and introduction update

## 0.5.5 (2026-06-01)

- add mobile showcase

## 0.5.4 (2026-06-01)

- Added screenshots and gif for showcase

## 0.5.3 (2026-06-01)

- fix: hardcoded german strings

## 0.5.2 (2026-06-01)

- Add release badge to README

## 0.5.0 (2026-06-01)

- feat: allow parallel runs

## 0.4.5 (2026-06-01)

- feat: improve dashboard viewing run time and upcoming runs
- feat: add zone live status to dashboard

## 0.4.4 (2026-06-01)

- fix: bound upcoming-runs list height to viewport so it scrolls

## 0.4.3 (2026-06-01)

- chore: add CODEOWNERS requiring owner review

## 0.4.1 (2026-06-01)

- fix: let upcoming-runs list fill available card height before scrolling

## 0.4.0 (2026-06-01)

- fix: keep manual adjustment editor open while using steppers

## 0.3.7 (2026-06-01)

- fix: keep manual adjustment editor open while using steppers

## 0.3.6 (2026-06-01)

- fix: keep manual adjustment editor open while using steppers

## 0.3.5 (2026-06-01)

- fix: keep manual adjustment editor open while using steppers

## 0.3.4 (2026-06-01)

- fix: avoid nested scroll trap for upcoming runs on mobile
- feat: make upcoming runs list scrollable on vertical overflow

## 0.3.2 (2026-06-01)

- feat: make sequence card accent colors configurable

## 0.3.1 (2026-06-01)

- feat: manual adjustment override on dashboard

## 0.3.0 (2026-06-01)

- ci: run frontend vitest tests on every CI pass

## 0.2.13 (2026-05-31)

- refactor: drop redundant i18n defaultValue fallbacks
- fix: use English defaults for i18n fallback strings

## 0.2.12 (2026-05-31)

- feat: show sensor inputs in adjustment tooltips
- feat: dashboard UX improvements

## 0.2.11 (2026-05-31)

- fix: alignment

## 0.2.10 (2026-05-31)

- docs: update README.md

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
