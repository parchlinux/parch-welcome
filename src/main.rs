mod i18n;
mod utils;
mod window;

use adw::prelude::*;
use gtk::{gio, glib};

fn main() -> glib::ExitCode {
    utils::setup_environment();

    let resource_data = include_bytes!(concat!(env!("OUT_DIR"), "/com.parchlinux.welcome.gresource"));
    let bytes = glib::Bytes::from_static(resource_data);
    let resource = gio::Resource::from_data(&bytes).expect("Failed to create GResource");
    gio::resources_register(&resource);

    let app = adw::Application::builder()
        .application_id("com.parchlinux.welcome")
        .resource_base_path("/com/parchlinux/welcome")
        .build();

    let quit_action = gio::ActionEntry::builder("quit")
        .activate(|app: &adw::Application, _, _| app.quit())
        .build();

    let about_action = gio::ActionEntry::builder("about")
        .activate(|app: &adw::Application, _, _| {
            let about = adw::AboutDialog::builder()
                .application_name("parch-welcome")
                .application_icon("com.parchlinux.welcome")
                .developer_name("Sohrab Behdani")
                .version("0.1.0")
                .developers(["Sohrab Behdani"])
                .copyright("\u{00a9} 2025 Parch Linux")
                .build();
            if let Some(win) = app.active_window() {
                about.present(Some(&win));
            }
        })
        .build();

    app.add_action_entries([quit_action, about_action]);
    app.set_accels_for_action("app.quit", &["<primary>q"]);

    app.connect_activate(|app| {
        let win = window::WelcomeWindow::create(app);
        win.present();
    });

    app.run()
}
