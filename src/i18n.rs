use std::collections::HashMap;
use std::sync::LazyLock;

static STRINGS: LazyLock<HashMap<&'static str, HashMap<&'static str, &'static str>>> =
    LazyLock::new(|| {
        let mut m = HashMap::new();

        let mut en = HashMap::new();
        en.insert("dorood", "Welcome \u{1f44b}");
        en.insert("subtitle", "Start installing the Parch on your system.");
        en.insert("start", "Start");
        en.insert("error_title", "Error");
        en.insert("calamares_error", "Calamares is not installed!");
        en.insert("ok", "OK");
        m.insert("en", en);

        let mut fa = HashMap::new();
        fa.insert("dorood", "\u{1f44b} \u{62e}\u{648}\u{634} \u{622}\u{645}\u{62f}\u{6cc}\u{62f}");
        fa.insert("subtitle", "\u{634}\u{631}\u{648}\u{639} \u{628}\u{647} \u{646}\u{635}\u{628} \u{67e}\u{627}\u{631}\u{686} \u{628}\u{631} \u{631}\u{648}\u{6cc} \u{633}\u{627}\u{645}\u{627}\u{646}\u{647} \u{62e}\u{648}\u{62f} \u{6a9}\u{646}\u{6cc}\u{62f}.");
        fa.insert("start", "\u{622}\u{63a}\u{627}\u{632}");
        fa.insert("error_title", "\u{62e}\u{637}\u{627}");
        fa.insert("calamares_error", "\u{6a9}\u{627}\u{644}\u{627}\u{645}\u{627}\u{631}\u{633} \u{646}\u{635}\u{628} \u{646}\u{634}\u{62f}\u{647} \u{627}\u{633}\u{62a}!");
        fa.insert("ok", "\u{642}\u{628}\u{648}\u{644}");
        m.insert("fa", fa);

        m
    });

pub fn get_string(lang: &str, key: &str) -> &'static str {
    STRINGS
        .get(lang)
        .and_then(|lang_map| lang_map.get(key))
        .copied()
        .unwrap_or("")
}
