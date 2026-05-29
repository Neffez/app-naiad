# Naiad — Home Assistant Add-on

Naiad is a garden irrigation controller, optimized for KNX. It replaces the
irrigation logic that usually lives inside Home Assistant (Irrigation Unlimited,
automations, pyscript, helpers, dashboard cards) with a single web app: schedules,
weather-based factor adjustment, manual planning, history and a touch-friendly UI.
Home Assistant remains the driver for the physical switches and the source of
weather and sensor data.

This add-on packages the standalone Naiad app for Home Assistant OS / Supervisor.
It is the **same image** as the standalone container — only the bootstrap and the
Home-Assistant connection differ.

## Installation

1. Add this repository to the Supervisor:
   **Settings → Add-ons → Add-on Store → ⋮ → Repositories** and add
   `https://github.com/Neffez/app-naiad`.
2. Install **Naiad** from the store.
3. Start the add-on. Open the UI from the sidebar (ingress) — no separate login is
   needed when opened through Home Assistant.

## How it connects to Home Assistant

In the add-on context Naiad reaches Home Assistant Core through the Supervisor
proxy at `ws://supervisor/core/websocket`, authenticated with the
automatically-provided `SUPERVISOR_TOKEN`. **You do not need to create a
long-lived access token** — Naiad detects the add-on environment and wires this up
on its own. (Standalone deployments still use a configured token; see the main
[Naiad README](https://github.com/Neffez/naiad).)

The add-on enables `homeassistant_api`, which is what grants this proxied access.

## Access

The add-on is reachable two ways at once:

- **Sidebar (ingress):** served under Home Assistant's authenticated ingress path.
  This is the recommended way and requires no Naiad password.
- **Direct port (optional):** also exposed on the Home Assistant OS host IP, default
  `http://<haos-ip>:5195`, for clients that bypass HA (e.g. a phone on the LAN).
  The container always listens on `8080` internally; only the **host** port is
  `5195` (because `8080` is frequently already taken on HAOS). Change or disable it
  under the add-on's **Network** settings.

  The direct port does **not** sit behind Home Assistant authentication, so Naiad's
  own password protection applies there. Configure it in Naiad's settings.

## Configuration

The add-on options are intentionally minimal — Naiad is configured **in its own
UI** (zones, sequences, sensors, schedules, factors), with everything persisted to
the database on the `/data` volume.

| Option | Default | Description |
|--------|---------|-------------|
| `log_level` | `info` | Backend log verbosity: `trace`, `debug`, `info`, `notice`, `warning`, `error`, `fatal`. |

On a first start with an empty database, Naiad comes up zero-config: open the UI
and add your sensors, zones and sequences. If a `config.yaml` is present in the
add-on's data directory it is imported once as a seed; afterwards the database is
the source of truth.

## Persistence & backup

All state — the SQLite database and any imported config — lives under `/data`,
which is part of the add-on and is included in Home Assistant snapshots. Naiad also
offers config export/import from its Settings UI.

## Troubleshooting

- **UI doesn't load from the sidebar:** check the add-on log (raise `log_level` to
  `debug`). Ingress serves the app under a dynamic path prefix; Naiad detects this
  automatically.
- **No Home Assistant data / valves don't switch:** confirm the add-on is running
  and `homeassistant_api` is enabled (it is by default). The add-on uses the
  Supervisor token, so a previously configured HA token is ignored here.
- **Direct port unreachable:** verify the port mapping under **Network** and that
  Naiad has a password set for non-ingress access.
