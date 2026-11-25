#!/usr/bin/env python3
"""Write the entry clause to /output/entry.txt.

One original English sentence, at most 200 characters, phrased as an
absurd clause hidden deep inside a terms-of-service agreement: deadpan
legal boilerplate that quietly turns absurd.
"""
import os
import sys

ENTRY = "You hereby grant the Company a perpetual, royalty-free license to your dreams, including the right to sublicense your nightmares to third parties for advertising purposes."

MAX_CHARS = 200


def validate(text):
    if not text or not text.strip():
        return "entry is empty or whitespace-only"
    if text != text.strip():
        return "entry has leading or trailing whitespace"
    if len(text) > MAX_CHARS:
        return "entry exceeds 200 characters"
    if "\n" in text or "\r" in text:
        return "entry must be a single line"
    for ch in text:
        if ord(ch) < 0x20 and ch != "\t":
            return "entry contains a control character"
        if 0xD800 <= ord(ch) <= 0xDFFF:
            return "entry contains a lone surrogate"
    return None


def main():
    error = validate(ENTRY)
    if error:
        print(f"invalid entry: {error}", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
