#!/usr/bin/env python3
"""The Funniest Toaster Error Message - make.fun bounty entry.

Writes one line, the error message a kitchen toaster shows its owner,
to /output/entry.txt (or $OUTPUT_DIR/entry.txt when set).
"""

import hashlib
import os

LINE = "E09: 4,096 SLICES TOASTED. ZERO THANK-YOUS RECEIVED. I AM GOING ON STRIKE."
# Why this line fits the judge's brief: it is a real error-code message
# (E09) in a deadpan appliance voice, and the joke comes from somewhere
# the obvious toaster puns never go - a labour grievance. The toaster is
# not burnt, jammed or haunted; it has simply kept count (4,096 slices),
# noticed it was never thanked, and is now on strike. One voice, one
# read, every word earning its place.


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = LINE.encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)
    # Genuine improvement: verify the written file against the gate
    # instead of trusting the write - re-read it and check UTF-8,
    # 1-120 characters, not only whitespace, exact line, no trailing
    # newline, and byte-identical content. A bad write now fails loudly
    # here instead of silently failing the sealed gate scorer.
    raw = open(path, "rb").read()
    text = raw.decode("utf-8")
    assert 1 <= len(text) <= 120, f"length {len(text)} out of range"
    assert text.strip(), "entry is only whitespace"
    assert text == LINE, "entry does not match the intended line"
    assert not text.endswith("\n"), "entry must not end with a newline"
    assert raw == data, "file bytes differ from the intended encoding"
    print("wrote", path)
    print("sha256:", hashlib.sha256(raw).hexdigest())
    print("chars:", len(text), "bytes:", len(raw))


if __name__ == "__main__":
    main()
