#!/usr/bin/env python3
"""One Word, One Username, One Reward — make.fun entry.

The bounty asks for exactly one thing: the entrant's own make.fun
username, sent as a single word with no explanation, no links, no pitch.
The judge's first criterion is a gate — an entry that is not a genuine
make.fun handle loses to any that is — so this program writes the
entrant's own handle, kangris-uk, and nothing else.

Output contract (kit): one text at /output/entry.txt, UTF-8, 1 to 30
characters, not only whitespace. The output folder is read from
MAKEFUN_OUTPUT_DIR first (the kit contract), falling back to /output,
then to the folder beside this program for local runs.
"""

import os

USERNAME = "kangris-uk"


def output_path() -> str:
    folder = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    if not os.path.isdir(folder):
        folder = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(folder, "entry.txt")


def checked_username() -> str:
    """Return the username only if it passes the sealed gate's shape:
    1 to 30 characters, a single word, no whitespace anywhere in it.
    A handle that failed the gate would never reach the judge, so the
    program refuses to write one rather than ship a silent zero."""
    if not 1 <= len(USERNAME) <= 30:
        raise ValueError(f"username must be 1-30 characters, got {len(USERNAME)}")
    if any(ch.isspace() for ch in USERNAME):
        raise ValueError("username must be one word, with no whitespace")
    if USERNAME != USERNAME.strip() or not USERNAME:
        raise ValueError("username must not be blank or padded")
    return USERNAME


def main() -> None:
    word = checked_username()
    path = output_path()
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(word)
    print(f"wrote {path}: {word}")


if __name__ == "__main__":
    main()
