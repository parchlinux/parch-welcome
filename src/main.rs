use std::process::Command;

use slint::ComponentHandle;
slint::include_modules!();

fn main() {
    let appwindow = App::new().unwrap();
    appwindow.global::<Globals>().on_close(move || {
        std::process::exit(0);
    });
    appwindow.global::<Globals>().on_openUrl(move |url| {
        let _ = open::that(url.as_str());
    });
    appwindow.global::<Globals>().on_startInstaller(move || {
        let _ = Command::new("sudo").arg("-E").arg("/etc/calamares/launch.sh").spawn();
    });
    let _ = appwindow.run();
}
