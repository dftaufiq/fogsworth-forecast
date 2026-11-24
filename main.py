#!/usr/bin/env python3
"""Charm the Commuter: Forecast a City That Isn't.

Writes one line of weather forecast (140 characters at most) for a city
that does not exist to /output/entry.txt.

The line: a broadcast-style forecast for Fogsworth with a 2-beat structure
— forecast setup, then a reveal in the final clause (the 7:40 train waits
because the conductor overslept too). Deterministic: no input, no network,
no environment, no randomness. The same bytes every run.
"""

import os

LINE = (
    "In Fogsworth, fog till eight, then clear skies, 14\u00b0 \u2014 "
    "the 7:40 train waits two extra minutes, "
    "because the conductor overslept too."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = LINE
    assert 1 <= len(text) <= 140, f"line is {len(text)} chars, must be 1-140"
    assert text.strip(), "line must not be only whitespace"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
