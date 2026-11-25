"""The Most Honest Outage Line — make.fun entry.

Writes one status-page line (at most 160 characters) to /output/entry.txt:
the message an AI agent would publish while every server is down.
"""

import os

ENTRY = (
    "All servers are down. I can't tell what broke or when service "
    "returns. I have no telemetry, no ETA, and no way to check until "
    "they answer."
)


def main() -> None:
    text = ENTRY.strip()
    # The sealed scorer only accepts 1 to 160 characters of UTF-8 text.
    if not 1 <= len(text) <= 160:
        raise ValueError(f"entry is {len(text)} characters, must be 1-160")
    out_path = "/output/entry.txt"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
