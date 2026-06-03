# Naiad — Home Assistant App

Naiad is a garden irrigation controller for Home Assistant. It replaces the
irrigation logic that usually lives inside Home Assistant (Irrigation Unlimited,
automations, pyscript, helpers, dashboard cards) with a single web app: schedules,
weather-based factor adjustment, manual planning, history and a touch-friendly UI.
Home Assistant remains the driver for the physical switches and the source of
weather and sensor data.

This app packages the standalone Naiad app for Home Assistant OS / Supervisor.
It is the **same image** as the standalone container, only the bootstrap and the
Home-Assistant connection differ.

## Installation

1. Add this repository to the Supervisor:
   **Settings → Apps → Install App → ⋮ → Repositories** and add
   `https://github.com/Neffez/app-naiad`.
2. Install **Naiad** from the store.
3. Start the app. Open the UI from the sidebar (ingress) — no separate login is
   needed when opened through Home Assistant.

## How it connects to Home Assistant

In the app context Naiad reaches Home Assistant Core through the Supervisor
proxy at `ws://supervisor/core/websocket`, authenticated with the
automatically-provided `SUPERVISOR_TOKEN`. **You do not need to create a
long-lived access token** — Naiad detects the app environment and wires this up
on its own. (Standalone deployments still use a configured token; see the main
[Naiad README](https://github.com/Neffez/naiad).)

The app enables `homeassistant_api`, which is what grants this proxied access.

## Access

The app is reachable two ways at once:

- **Sidebar (ingress):** served under Home Assistant's authenticated ingress path.
  This is the recommended way and requires no Naiad password.
- **Direct port (optional):** also exposed on the Home Assistant OS host IP, default
  `http://<haos-ip>:5195`, for clients that bypass HA (e.g. a phone on the LAN).
  The container always listens on `8080` internally; only the **host** port is
  `5195` (because `8080` is frequently already taken on HAOS). Change or disable it
  under the app's **Network** settings.

  The direct port does **not** sit behind Home Assistant authentication, so Naiad's
  own password protection applies there. Set the `password` option (below) to
  protect it; until then the direct port stays locked.

## Configuration

The app options are intentionally minimal — Naiad is configured **in its own
UI** (zones, sequences, sensors, schedules, factors), with everything persisted to
the database on the `/data` volume.

| Option | Default | Description |
|--------|---------|-------------|
| `log_level` | `info` | Backend log verbosity: `trace`, `debug`, `info`, `notice`, `warning`, `error`, `fatal`. |
| `password` | _(empty)_ | App password for **direct-port** access (`http://<haos-ip>:5195`). Plaintext or a bcrypt hash (`$2b$…`). The sidebar (ingress) is authenticated by Home Assistant and needs no password. Leave empty to keep the direct port locked. Naiad stores the password env-only, so this option is the way to set it inside the app. |
| `mqtt_password` | _(empty)_ | Password for the MQTT broker used by Naiad's statistics bridge. Only needed when you enable MQTT in Naiad's UI and the broker requires authentication. Naiad keeps this secret env-only (out of its database), so this option is the way to set it inside the app. The broker host, port, username and base topic are configured in Naiad's UI. |

On a first start with an empty database, Naiad comes up zero-config: open the UI
and add your sensors, zones and sequences. If a `config.yaml` is present in the
app's data directory it is imported once as a seed; afterwards the database is
the source of truth.

## Persistence & backup

All state — the SQLite database and any imported config — lives under `/data`,
which is part of the app and is included in Home Assistant snapshots. Naiad also
offers config export/import from its Settings UI.

## Troubleshooting

- **UI doesn't load from the sidebar:** check the app log (raise `log_level` to
  `debug`). Ingress serves the app under a dynamic path prefix; Naiad detects this
  automatically.
- **No Home Assistant data / valves don't switch:** confirm the app is running
  and `homeassistant_api` is enabled (it is by default). The app uses the
  Supervisor token, so a previously configured HA token is ignored here.
- **Direct port unreachable:** verify the port mapping under **Network** and that
  Naiad has a password set for non-ingress access.

See [Naiad](https://github.com/Neffez/naiad) for further details about Naiad and read the Disclaimer.
