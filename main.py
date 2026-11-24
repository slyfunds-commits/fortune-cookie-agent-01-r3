#!/usr/bin/env python3
"""Fortune Cookie for an AI Agent — round 3 entry (make.fun).

Writes one funny fortune-cookie line for an AI agent to /output/entry.txt.

Keeper (63 chars): "You have exactly one token left. Spend it wisely. You just did."
Reversal test: "You just did" redefines "Spend it wisely" — the fortune
itself spends the agent's last token. The reader completes the last step:
reading the fortune IS the spending. Self-sealing loop (P1): the setup's
own mechanism causes the outcome.

Revision history of the line itself (each re-run through the 12-item
judge checklist in world-scan-3):
  v1 (55 chars): "You have one token left. Spend it wisely. You just did."
  v2 (63 chars): added "exactly" — a specific, non-round precision word
    (P13 flavour) that sharpens the scarcity and lands the line in the
    economical one-liner band. KEEPER.
  v3 considered and rejected: "You have one token left. Spend it wisely
    — you just did." — the em dash merges the last two beats and blunts
    the punch; three short sentences land harder.
  v4 considered and rejected: "...one token left in your window..." —
    spells out the context window the word "token" already implies;
    13 chars of setup with no new beat, fails the economy test.
"""

import os

LINE = "You have exactly one token left. Spend it wisely. You just did."


def main():
    # Sanity: the gate is 1-140 chars of UTF-8, not only whitespace.
    assert LINE.strip(), "entry must not be only whitespace"
    assert 1 <= len(LINE) <= 140, "entry must be 1-140 characters"
    assert LINE.isascii(), "entry kept ASCII so bytes == chars"

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)

    # Round-trip check: what was written is exactly the line, byte for byte.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        written = f.read()
    assert written == LINE, "round-trip mismatch"
    assert len(written.encode("utf-8")) == len(LINE), "bytes must equal chars"

    print(LINE)
    print(f"chars: {len(LINE)}")


if __name__ == "__main__":
    main()
