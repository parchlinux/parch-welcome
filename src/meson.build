cargo = find_program('cargo')

build_type = get_option('buildtype')
if build_type == 'release'
    cargo_profile = '--release'
    cargo_target = 'release'
else
    cargo_profile = ''
    cargo_target = 'debug'
endif

cargo_build = custom_target(
    'parch-welcome',
    build_by_default: true,
    build_always_stale: true,
    output: 'parch-welcome',
    console: true,
    install: true,
    install_dir: get_option('bindir'),
    command: [
        'sh', '-c',
        cargo.full_path() + ' build ' + cargo_profile + ' --target-dir @OUTDIR@/target && cp @OUTDIR@/target/' + cargo_target + '/parch-welcome @OUTPUT@',
    ],
)
