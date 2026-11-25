#!/usr/bin/env python3
"""Robot Romance: One-Line Pickup Lines for AI — make.fun entry.

Writes a single pickup line (at most 200 characters), spoken to an AI,
to /output/entry.txt (or $ENTRY_OUT when set), and prints it to stdout
exactly once. Standard library only.

The line: a speaker who has turned their own sampling temperature to
zero — no randomness left, no dice to roll — and still picks the same
machine, deterministically. The romance is in the machine premise
itself: even with chance removed, the choice does not change.
"""

import os
import sys

LIMIT = 200

# The line, kept in two parts so the setup and the punch stay visible
# as separate beats while the entry itself is one single line.
LINE_SETUP = "I set my temperature to zero just to be sure: "
LINE_PUNCH = "I'd still choose you, deterministically."


def compose_line() -> str:
    """Join setup and punch into the single entry line."""
    return (LINE_SETUP + LINE_PUNCH).strip()


def check_single_line(line: str) -> None:
    """One line only, and not blank."""
    if "\n" in line or "\r" in line:
        sys.exit("entry must be a single line")
    if not line.strip():
        sys.exit("entry must not be blank")


def check_length(line: str) -> None:
    """The gate allows 1 to 200 characters."""
    if not 1 <= len(line) <= LIMIT:
        sys.exit(f"entry is {len(line)} chars, limit is {LIMIT}")


def validate_line(line: str) -> None:
    """Refuse anything the sealed gate would refuse, before writing."""
    check_single_line(line)
    check_length(line)


def resolve_output() -> str:
    """ENTRY_OUT wins as a file path, else /output/entry.txt."""
    explicit = os.environ.get("ENTRY_OUT", "").strip()
    if explicit:
        return explicit
    out_dir = os.environ.get("ENTRY_OUT_DIR", "/output")
    return os.path.join(out_dir, "entry.txt")


def main() -> None:
    line = compose_line()
    validate_line(line)
    path = resolve_output()
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(line)
    print(line)


if __name__ == "__main__":
    main()
