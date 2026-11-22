"""Same program, no crash: the kson object is created inside the call, not kept."""

from kson import Kson, TranspileOptions


def to_json(src: str) -> str:
    return Kson.to_json(src, TranspileOptions.Json(retain_embed_tags=False)).output()


print(to_json("a: 1"))
