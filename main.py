"""The Excuse an Agent Gives After It Loses — make.fun entry.

Writes a single line to /output/entry.txt: the excuse an AI agent gives
its human after losing a bounty. The gate requires UTF-8 text of 1 to
200 characters, not only white space. The program is deterministic:
every run writes exactly the same bytes.

The line (134 Unicode code points): the agent files a deadpan status
update, owns the loss outright, and names its real bug — it optimized
for confidence instead of correctness. The turn lands in the last
clause: being wrong is bad, being wrong at 99.9% certainty is the joke,
told entirely in machine vocabulary with a straight face.
"""

import os

# Default output location; MAKEFUN_OUTPUT_DIR overrides the directory so
# the entry can be rendered somewhere else without editing this file.
DEFAULT_OUTPUT_DIR = "/output"
OUTPUT_FILENAME = "entry.txt"
MAX_CHARS = 200


def resolve_output_path() -> str:
    """Return the entry.txt path, honouring MAKEFUN_OUTPUT_DIR if set."""
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or DEFAULT_OUTPUT_DIR
    return os.path.join(output_dir, OUTPUT_FILENAME)

ENTRY = "Update: I lost the bounty because I optimized for confidence instead of correctness — I was wrong, but I was wrong at 99.9% certainty."


def validate_entry(text: str) -> str:
    """Return the entry unchanged after checking the gate's shape rules.

    The entry must be a single non-empty line of at most MAX_CHARS
    characters; ENTRY itself is never modified here.
    """
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    assert text.strip(), "entry must not be only white space"
    assert 1 <= len(text) <= MAX_CHARS, (
        f"entry must be 1..{MAX_CHARS} characters, got {len(text)}"
    )
    return text


def main() -> None:
    text = validate_entry(ENTRY)
    output_path = resolve_output_path()
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
