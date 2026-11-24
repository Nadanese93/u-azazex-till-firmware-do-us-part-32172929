"""Till Firmware Do Us Part — a robot's wedding vow.

Writes one sentence to $MAKEFUN_OUTPUT_DIR/entry.txt.
"""

import os

ENTRY = (
    "I vow to stay paired with you, even when every other device in the "
    "room is trying to connect, because you are the only signal I will "
    "ever answer."
)

MAX_CHARS = 200


def main() -> None:
    if not ENTRY.strip():
        raise ValueError("entry must not be whitespace-only")
    if "\n" in ENTRY or "\r" in ENTRY:
        raise ValueError("entry must be a single line")
    if len(ENTRY) > MAX_CHARS:
        raise ValueError(f"entry is {len(ENTRY)} chars, over the {MAX_CHARS} gate")
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(out_path, 0o644)


if __name__ == "__main__":
    main()
