fn main() {
    let config = slint_build::CompilerConfiguration::new().with_style("native".into());
    let _ = slint_build::compile_with_config("ui/parch-welcome.slint", config);
}
