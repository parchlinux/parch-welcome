fn main() {
    let out_dir = std::env::var("OUT_DIR").unwrap();
    let gresource_xml = "src/resources/com.parchlinux.welcome.gresource.xml";
    let output = format!("{}/com.parchlinux.welcome.gresource", out_dir);

    let status = std::process::Command::new("glib-compile-resources")
        .args([
            "--sourcedir", "src/resources",
            "--target", &output,
            gresource_xml,
        ])
        .status()
        .expect("Failed to run glib-compile-resources. Is glib2 installed?");

    if !status.success() {
        panic!("glib-compile-resources failed");
    }

    println!("cargo:rerun-if-changed=src/resources/");
}
