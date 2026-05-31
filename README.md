<div align="center">
  <img src="naiad/logo.svg" alt="Naiad" width="420">

  **Home Assistant app repository for Naiad, the garden irrigation controller.**
</div>


---

This repository packages [**Naiad**](https://github.com/Neffez/naiad) as a Home
Assistant add-on. It is the *same image* as the standalone Naiad container. Only
the bootstrap and the Home Assistant connection differ.

## Add this repository

**Settings → Apps → Install App → ⋮ → Repositories**, then add:

```
https://github.com/Neffez/app-naiad
```

[![Open your Home Assistant instance and show the add add-on repository dialog with a specific repository URL pre-filled.](https://my.home-assistant.io/badges/supervisor_add_addon_repository.svg)](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2FNeffez%2Fapp-naiad)

Then install **Naiad** from the store and start it. Open it from the sidebar. No
login is required through Home Assistant ingress.

## What you get

- **Ingress sidebar entry** — opens Naiad inside Home Assistant, pre-authenticated.
- **No long-lived token needed** — the add-on reaches Home Assistant Core through
  the Supervisor proxy (`ws://supervisor/core/websocket`) with the auto-provided
  `SUPERVISOR_TOKEN`.
- **Optional direct port** (`http://<haos-ip>:5195` by default) for LAN clients that
  bypass Home Assistant. Toggle or remap it in the add-on's Network settings.
- **Persistent storage** on the add-on `/data` volume (SQLite + optional config
  seed), included in Home Assistant snapshots.

See [`naiad/DOCS.md`](naiad/DOCS.md) for full add-on documentation.

## Documentation

Full README and documentation in the [**Naiad**](https://github.com/Neffez/naiad) repositry. 

## Architecture

The add-on tracks the published Naiad image from `ghcr.io/neffez/naiad` built by the naiad repo CI. Backend support for the HA app context
(Supervisor connection detection) lives in the [naiad](https://github.com/Neffez/naiad) repository.

## License

[MIT](LICENSE) — Copyright (c) 2026 Neffez.

---

<sub>Naiads are the freshwater nymphs of Greek mythology — spirits of springs, brooks and fountains. A fitting patron for a tool that decides when and how much water to send into a garden.</sub>
