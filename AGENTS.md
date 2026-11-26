# Agent notes

## Running RWX releases

- Run: `rwx run .rwx/release.yml --init tag=vX.Y.Z`, then `rwx results --wait <run-id>`.
- Auth is via env var. A bare `rwx run` fails with `403 Forbidden`. This fork's org is `elviskahoro`, so use:
  `RWX_ACCESS_TOKEN=$RWX_ACCESS_TOKEN_ELVISKAHORO rwx run ...`
  (`RWX_ACCESS_TOKEN_MARCHILI` is a different org; don't use it here.)
- Check `env | grep RWX` first. Don't ask the user for a token or conclude you're blocked.
- An explicit tag forces a rebuild and re-uploads assets with `--clobber`.
