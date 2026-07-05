# parch-welcome

Welcome application for the **Parch Linux** distribution.

## Features

- Displays a friendly bilingual (English / Persian) welcome screen on live sessions
- One-click Calamares installer launcher
- Language toggle in the header bar
- Auto-detects Wayland / X11 session type
- Live session detection (hides install button on installed systems)
- Autostarts on live environment boot

## Dependencies

- GTK 4
- libadwaita (>= 1.5)
- Rust (edition 2024)
- Meson / Ninja

## Building

```sh
meson setup build
meson compile -C build
```

## Installing

```sh
meson install -C build
```

## Authors

- **Sohrab Behdani** <sohrab@parchlinux.com> – Maintainer

## License

This project is licensed under the [GPL-3.0-or-later](./LICENCE) License.
