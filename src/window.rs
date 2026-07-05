use std::cell::RefCell;
use std::rc::Rc;

use adw::prelude::*;

use crate::i18n;
use crate::utils;

pub struct WelcomeWindow;

impl WelcomeWindow {
    pub fn create(application: &adw::Application) -> adw::ApplicationWindow {
        let win = adw::ApplicationWindow::builder()
            .application(application)
            .default_width(800)
            .default_height(600)
            .resizable(false)
            .title("Welcome")
            .build();

        let lang = Rc::new(RefCell::new(String::from("en")));

        let toolbar_view = adw::ToolbarView::new();

        let header_bar = adw::HeaderBar::new();
        let toggle_button = gtk::Button::builder()
            .icon_name("preferences-desktop-locale-symbolic")
            .css_classes(["flat"])
            .build();
        header_bar.pack_start(&toggle_button);
        toolbar_view.add_top_bar(&header_bar);

        let status_page = adw::StatusPage::builder()
            .icon_name("com.parchlinux.welcome")
            .title(i18n::get_string("en", "dorood"))
            .description(i18n::get_string("en", "subtitle"))
            .build();

        let start_button = gtk::Button::builder()
            .label(i18n::get_string("en", "start"))
            .css_classes(["pill", "suggested-action"])
            .halign(gtk::Align::Center)
            .build();

        status_page.set_child(Some(&start_button));

        if !utils::is_live_session() {
            start_button.set_visible(false);
        }

        toolbar_view.set_content(Some(&status_page));
        win.set_content(Some(&toolbar_view));

        {
            let lang = lang.clone();
            let status_page = status_page.clone();
            let start_button = start_button.clone();
            toggle_button.connect_clicked(move |_| {
                let new_lang = if *lang.borrow() == "en" { "fa" } else { "en" };
                *lang.borrow_mut() = String::from(new_lang);

                status_page.set_title(i18n::get_string(new_lang, "dorood"));
                status_page.set_description(Some(i18n::get_string(new_lang, "subtitle")));
                start_button.set_label(i18n::get_string(new_lang, "start"));
            });
        }

        {
            let lang = lang.clone();
            let win = win.clone();
            start_button.connect_clicked(move |_| {
                if utils::is_calamares_installed() {
                    let _ = std::process::Command::new("sudo")
                        .args(["-E", "/etc/calamares/launch.sh"])
                        .spawn();
                    if let Some(app) = win
                        .application()
                        .and_then(|a| a.downcast::<adw::Application>().ok())
                    {
                        app.quit();
                    }
                } else {
                    let lang = lang.borrow();
                    let dialog = adw::AlertDialog::builder()
                        .heading(i18n::get_string(&lang, "error_title"))
                        .body(i18n::get_string(&lang, "calamares_error"))
                        .build();
                    dialog.add_response("OK", i18n::get_string(&lang, "ok"));
                    dialog.set_default_response(Some("OK"));
                    dialog.set_close_response("OK");
                    dialog.present(Some(&win));
                }
            });
        }

        win
    }
}
