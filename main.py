"""Unsent: The Micro-Confession Sprint.

Writes one two-part micro-confession to /output/entry.txt:
a To: line naming who it was meant for, and the unsent message
itself, one line written exactly as it was typed, with no
explanation after it. Pure standard library, deterministic.
"""

import os

ENTRY = (
    "To: Ana, my sister\n"
    "I kept the blue sweater you left in my car because giving it "
    "back means admitting you don't live here anymore.\n"
)


def main() -> None:
    # Gate check, mirroring the scorer: UTF-8 text of 1 to 260 chars.
    assert 1 <= len(ENTRY) <= 260, "entry must be 1-260 characters"
    assert ENTRY.strip(), "entry must not be only whitespace"
    output_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
