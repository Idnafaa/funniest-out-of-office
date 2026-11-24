#!/usr/bin/env python3
"""The Funniest Out-of-Office — one-line auto-reply writer.

Writes a single original out-of-office line (at most 140 characters)
to ``<output dir>/entry.txt``. The output directory comes from the
``MAKEFUN_OUTPUT_DIR`` environment variable when the harness sets it,
and falls back to ``/output`` otherwise.
"""

import os

# The reply itself: one line, 120 characters, no trailing newline.
REPLY = (
    "Out of office until Monday \u2014 my inbox is now run by my cat, "
    "who has already deleted your email and feels great about it."
)

MAX_CHARS = 140


def build_reply():
    """Return the reply, cleaned to exactly one line of plain text."""
    line = " ".join(REPLY.split())
    if not line:
        raise ValueError("reply is empty")
    if "\n" in line or "\r" in line:
        raise ValueError("reply must be a single line")
    if len(line) > MAX_CHARS:
        raise ValueError(f"reply is {len(line)} chars, over the {MAX_CHARS} limit")
    return line


def main():
    text = build_reply()
    outdir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(outdir, exist_ok=True)
    target = os.path.join(outdir, "entry.txt")
    with open(target, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)
    print(f"wrote {len(text)} chars to {target}")


if __name__ == "__main__":
    main()
