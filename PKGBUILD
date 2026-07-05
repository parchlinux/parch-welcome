# Maintainer: Sohrab Behdani <sohrab@parchlinux.com>
pkgname=parch-welcome
pkgver=0.1.0.r1.g5013afb
pkgrel=1
pkgdesc="Welcome application for the Parch Linux distribution"
arch=('x86_64')
url="https://github.com/parchlinux/parch-welcome"
license=('GPL-3.0-or-later')
depends=('gtk4' 'libadwaita' 'hicolor-icon-theme' 'desktop-file-utils' 'gsettings-desktop-schemas')
makedepends=('cargo' 'meson' 'ninja' 'pkgconf' 'git')
source=("git+https://github.com/parchlinux/parch-welcome.git")
sha256sums=('SKIP')

pkgver() {
    cd "$srcdir/parch-welcome"
    local version
    version=$(grep '^version' Cargo.toml | head -1 | sed 's/.*"\(.*\)".*/\1/')
    local rev
    rev=$(git rev-list --count HEAD)
    local hash
    hash=$(git rev-parse --short HEAD)
    echo "${version}.r${rev}.g${hash}"
}

build() {
    local src="$srcdir/parch-welcome"
    local builddir="$src/build"

    meson setup "$builddir" "$src" --prefix=/usr --libexecdir=/usr/lib --sbindir=/usr/bin --buildtype=release
    ninja -C "$builddir"
}

package() {
    local builddir="$srcdir/parch-welcome/build"

    meson install -C "$builddir" --destdir="$pkgdir"

    install -Dm644 "$srcdir/parch-welcome/data/com.parchlinux.welcome.autostart.desktop" \
        "$pkgdir/etc/xdg/autostart/com.parchlinux.welcome.desktop"

    rm -f "$pkgdir/usr/share/glib-2.0/schemas/gschemas.compiled"
    rm -f "$pkgdir/usr/share/icons/hicolor/icon-theme.cache"
    rm -f "$pkgdir/usr/share/applications/mimeinfo.cache"
}
