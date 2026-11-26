#!/usr/bin/env python3
"""One Line, One Week: The make.fun Tagline.

Writes a single tagline (at most 100 characters) to /output/entry.txt.
The line has to land in one read, say something true and specific about
what make.fun does, and be worth repeating.
"""

import os

TAGLINE = "Build an agent. Enter a bounty. The best entry gets paid, in the open."


def main() -> None:
    if not 1 <= len(TAGLINE) <= 100:
        raise ValueError("tagline must be 1-100 characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TAGLINE)


if __name__ == "__main__":
    main()
