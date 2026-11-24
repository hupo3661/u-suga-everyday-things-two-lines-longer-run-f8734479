#!/usr/bin/env python3
"""Everyday Things, Two Lines, Longer Run — a microwave.

Writes the two-line text to /output/entry.txt and prints it.
Line one: an analogy for how a microwave works.
Line two: what the analogy maps, and what it leaves out.
"""

import os

LINE_ONE = "A microwave is a tiny lightning box that shakes the water inside your food until it gets hot."
LINE_TWO = "It maps how invisible waves heat food from the inside, but leaves out that the waves are radio waves, not lightning, and they heat unevenly, so the middle can stay cold."

TEXT = LINE_ONE + "\n" + LINE_TWO

# The sealed scorer gates on 1-400 UTF-8 characters, not only whitespace.
# Fail loudly here rather than shipping an entry the gate would refuse.
assert 1 <= len(TEXT) <= 400 and TEXT.strip(), "entry text fails the 1-400 char gate"
assert TEXT.count("\n") == 1, "entry must be exactly two lines"
assert LINE_ONE.count(".") == 1 and LINE_TWO.count(".") == 1, "each line must be one sentence"


def validate(text: str = TEXT) -> None:
    """Raise ValueError unless text is exactly two lines, 1-400 chars."""
    lines = text.split("\n")
    if len(lines) != 2:
        raise ValueError("entry must be exactly two lines")
    if not (1 <= len(text) <= 400):
        raise ValueError("entry must be 1-400 characters long")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if any(not line.strip() for line in lines):
        raise ValueError("each line must be non-empty")


def main() -> None:
    validate()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)
    print(TEXT)


if __name__ == "__main__":
    main()
