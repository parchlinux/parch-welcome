use std::path::Path;

pub fn setup_environment() {
    unsafe {
        std::env::set_var("LIBGL_DEBUG", "quiet");
    }

    if std::env::var("GDK_BACKEND").is_err() {
        let session = std::env::var("XDG_SESSION_TYPE")
            .unwrap_or_default()
            .to_lowercase();
        let backend = match session.as_str() {
            "wayland" => "wayland",
            "x11" => "x11",
            _ => "wayland,x11",
        };
        unsafe {
            std::env::set_var("GDK_BACKEND", backend);
        }
    }
}

pub fn is_calamares_installed() -> bool {
    let path = std::env::var("PATH").unwrap_or_default();
    for dir in std::env::split_paths(&path) {
        if dir.join("calamares").exists() {
            return true;
        }
    }
    false
}

pub fn is_live_session() -> bool {
    let markers = [
        "/run/archiso",
        "/run/archiso/bootmnt",
        "/run/live/medium",
        "/cdrom",
    ];
    if markers.iter().any(|m| Path::new(m).exists()) {
        return true;
    }

    let user = std::env::var("USER")
        .unwrap_or_default()
        .to_lowercase();
    matches!(user.as_str(), "liveuser" | "parch")
}
