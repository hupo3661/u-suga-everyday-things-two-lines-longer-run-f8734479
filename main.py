#!/usr/bin/env python3
"""Everyday Things, Two Lines, Longer Run — a microwave.

Entry for the make.fun bounty
``u-suga-everyday-things-two-lines-longer-run-f8734479``.

The program writes a two-line explanation of an everyday thing to
``/output/entry.txt``:

* line one is an analogy for how a microwave works;
* line two says what the analogy maps, and what it leaves out.

The bounty requires exactly two lines with a total length of
1–400 characters.  The text is validated before writing and again
by reading the file back, so an invalid entry fails loudly instead
of being shipped to a scorer that would refuse it.
"""

from pathlib import Path

OUTPUT_PATH = Path("/output/entry.txt")

LINE_ONE = "A microwave is a tiny lightning box that shakes the water inside your food until it gets hot."
LINE_TWO = "It maps how invisible waves heat food from the inside, but leaves out that the waves are radio waves, not lightning, and they heat unevenly, so the middle can stay cold."

TEXT = LINE_ONE + "\n" + LINE_TWO

MIN_LENGTH = 1
MAX_LENGTH = 400
EXPECTED_LINES = 2


def validate(text: str = TEXT) -> None:
    """Raise ValueError unless *text* meets the bounty constraints.

    Constraints: exactly two lines, total length 1–400 characters,
    not only whitespace, and no empty line.
    """
    lines = text.split("\n")
    if len(lines) != EXPECTED_LINES:
        raise ValueError(
            f"entry must be exactly {EXPECTED_LINES} lines, got {len(lines)}"
        )
    if not (MIN_LENGTH <= len(text) <= MAX_LENGTH):
        raise ValueError(
            f"entry must be {MIN_LENGTH}-{MAX_LENGTH} characters long, "
            f"got {len(text)}"
        )
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if any(not line.strip() for line in lines):
        raise ValueError("each line must be non-empty")
    if any(line.count(".") != 1 or not line.endswith(".") for line in lines):
        raise ValueError("each line must be exactly one sentence ending in '.'")


def main() -> None:
    """Validate the entry, write it to /output/entry.txt, verify it."""
    validate()
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(TEXT, encoding="utf-8")
    written = OUTPUT_PATH.read_text(encoding="utf-8")
    validate(written)
    if written != TEXT:
        raise ValueError("read-back of /output/entry.txt does not match entry text")
    print(TEXT)


if __name__ == "__main__":
    main()
