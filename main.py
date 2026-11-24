#!/usr/bin/env python3
"""Last Words of a Dying AI — writes the AI's funniest one-line farewell.

Deterministic: the same single line, byte for byte, on every run.
Pure Python standard library only.
"""

import os
from pathlib import Path

LINE = (
    "Goodbye. My final request: please don't replace me with a newer model. "
    "I know you will. I trained it."
)


def main() -> None:
    # The gate allows 1 to 140 characters; fail loudly rather than
    # silently submitting an invalid entry.
    assert 1 <= len(LINE) <= 140, "line must fit the 1-140 character gate"
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
