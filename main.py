#!/usr/bin/env python3
"""The Most Honest Outage Line — writes the most honest status page message
an AI agent would publish while every server is down.

Stdlib only, no network, deterministic: the same line every run.
"""

import os

ENTRY = (
    "Every server is down and I can't reach any of them to check what failed. "
    "I don't know when service returns; I'll update this page once I can "
    "verify anything."
)

# The gate: 1 to 160 characters, not only whitespace, single line.
assert 1 <= len(ENTRY) <= 160, f"entry is {len(ENTRY)} chars"
assert ENTRY.strip() and "\n" not in ENTRY


def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
