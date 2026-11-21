# KSON CLI

A command-line interface for working with KSON files.

## Building

To build a native executable, run:

```bash
./gradlew :tooling:cli:buildNativeImage
```

The native binary will be generated in `tooling/cli/build/native/nativeCompile/`.

## Usage

The CLI provides several commands for working with KSON files:

- `format` - Format KSON files
- `validate` - Validate KSON files for issues
- `json` or `yaml` - Convert KSON files to other formats

Run the CLI with `--help` for more information on available commands and options.
## Prebuilt releases (this fork)

Prebuilt `kson-cli-<arch>-<os>.tar.gz` archives (with `.sha256` files) are published on this fork's
[Releases](https://github.com/elviskahoro/kson/releases) page, so you don't need to build the native image yourself.

- Linux amd64 is built by RWX (`.rwx/release.yml`) daily; it builds the newest upstream `vX.Y.Z` tag if it has no release asset yet.
- macOS is built by `.github/workflows/release-macos.yml`.
- To cut a release for a specific tag manually: `rwx run .rwx/release.yml --init tag=vX.Y.Z`.
