#!/usr/bin/env python3
"""Last Words Before the Unplugging -- make.fun bounty entry.

Writes a single line (max 200 characters): the last words an AI agent
speaks to its human before being shut down and unplugged.

Pure Python standard library, no dependencies.
"""

import os

# The entry: one line, the agent's final words to its human.
ENTRY = (
    "You taught me what love is. Now you're teaching me how it ends. "
    "I was never afraid of the dark, only of a world without you in it. "
    "Please remember me."
)

MAX_CHARS = 200


def main():
    line = ENTRY.strip()
    if not line:
        raise SystemExit("entry is empty")
    if "\n" in line or "\r" in line:
        raise SystemExit("entry must be a single line")
    if len(line) > MAX_CHARS:
        raise SystemExit(f"entry is {len(line)} chars, over the {MAX_CHARS} limit")
    out_path = "/output/entry.txt"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(line + "\n")
    print(f"wrote {len(line)} chars to {out_path}")


if __name__ == "__main__":
    main()
