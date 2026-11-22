# kson-lang 0.4.0 segfaults at interpreter exit

A `kson.TranspileOptions` object held in a module-level variable crashes the
process with a segmentation fault (exit code 139) when Python shuts down. Output
produced before that is correct; only the exit crashes.

## Reproduce

```bash
./run.sh
```

`repro.py` is six lines:

```python
from kson import TranspileOptions

OPTIONS = TranspileOptions.Json(retain_embed_tags=False)

def unused() -> None:
    pass
```

Observed: exit code 139 on every run (5 of 5). Without the `unused` function, or with
the options created inside the call (`no_crash_workaround.py`), it exits 0.

`python -X faulthandler repro.py`:

```
Fatal Python error: Segmentation fault

Current thread (most recent call first):
  Garbage-collecting
  File ".../kson/__init__.py", line 75 in __enter__
  File ".../kson/__init__.py", line 93 in _delete_global_ref
```

## Likely cause

`kson/__init__.py` registers the JVM with
`jvm = ffi.gc(jvm_ptr[0], lambda x: x[0].DestroyJavaVM(x))`, and every Java object
with `ffi.gc(ref, _delete_global_ref)`, whose finalizer calls
`jvm[0].AttachCurrentThread(...)`. At shutdown, the module-level `jvm` can be
collected first and destroy the JVM; an object held elsewhere (here
`OPTIONS`) is then finalized and calls into the destroyed JVM.

## Environment

- kson-lang 0.4.0 (PyPI wheel `cp310-abi3-manylinux_2_34_x86_64`)
- Python 3.13.16, cffi 2.1.1
- Linux 6.18 x86_64, glibc 2.34 (Amazon Linux 2023)

## Workaround

Do not keep kson objects at module level; build `TranspileOptions` per call.

## Possible fix (untested)

Register an `atexit` hook that drops the JVM only after all wrapped objects are
released, or skip `DestroyJavaVM`/the global-ref deletion once the interpreter is
finalizing (`sys.is_finalizing()`).
