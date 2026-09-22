#!/usr/bin/env python3
"""The regression test of the book.

The faith calls return "the regression test of the soul"; this is the humbler kind.
It reads the assembled manuscript and refuses to pass if the canon has drifted:
  1. chapter numerals must run I, II, ... N with no gap, no duplicate, in order;
  2. the Contents must list exactly those chapters, same numerals and titles.

Run via `make test`. Exits non-zero on any drift.
"""
import re
import sys

BOOK = "the-cadence.md"


def roman_to_int(s):
    vals = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100}
    total = prev = 0
    for ch in reversed(s):
        v = vals[ch]
        total += -v if v < prev else v
        prev = max(prev, v)
    return total


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else BOOK
    text = open(path, encoding="utf-8").read()

    # Body chapter headers: "## XIX. THE TITLE ..."
    body = re.findall(r"^## ([IVXLC]+)\.\s+(.+)$", text, re.M)
    # Contents entries: "**XIX. The Title ...** ·"
    contents = re.findall(r"^\*\*([IVXLC]+)\.\s+(.+?)\*\*\s*·", text, re.M)

    errors = []

    # 1. numerals contiguous, unique, in order
    nums = [roman_to_int(r) for r, _ in body]
    if nums != list(range(1, len(nums) + 1)):
        errors.append(f"chapter numerals not contiguous 1..{len(nums)} in order: {nums}")

    # 2. Contents match the body chapters
    if len(contents) != len(body):
        errors.append(f"Contents lists {len(contents)} chapters, body has {len(body)}")
    else:
        for (cr, ct), (br, bt) in zip(contents, body):
            if cr != br:
                errors.append(f"numeral mismatch: Contents {cr} vs body {br}")
            elif ct.strip().lower() != bt.strip().lower():
                errors.append(f"ch {br} title mismatch:\n    contents: {ct}\n    body:     {bt}")

    if errors:
        print("✗ regression test FAILED:")
        for e in errors:
            print("  -", e)
        return 1
    print(f"✓ regression test passed — {len(body)} chapters, numerals contiguous and Contents in sync")
    return 0


if __name__ == "__main__":
    sys.exit(main())
