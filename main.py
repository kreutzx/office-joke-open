"""Entrypoint for the office-joke-open make.fun entry.

Writes the one-line office joke to /output/entry.txt, with a trailing newline.
"""

from pathlib import Path

ENTRY_TEXT = (
    "Our 15-minute stand-up has met every day for 3 years. "
    "It now lasts 45 minutes, has its own agenda, and nobody stands."
)


def main() -> None:
    # The entry is exactly one line.
    out = Path("/output")
    out.mkdir(parents=True, exist_ok=True)
    (out / "entry.txt").write_text(ENTRY_TEXT + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
