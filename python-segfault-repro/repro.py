"""Minimal reproduction: kson-lang segfaults at interpreter exit.

A `TranspileOptions` kept in a module-level variable is finalized after the JVM has
been destroyed, so its finalizer calls into a dead JVM.
"""

from kson import TranspileOptions

OPTIONS = TranspileOptions.Json(retain_embed_tags=False)  # lives until shutdown


def unused() -> None:  # any function definition makes the crash deterministic
    pass
