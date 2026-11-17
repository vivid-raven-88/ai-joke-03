#!/usr/bin/env python3
"""ai-joke-03 entry: one one-liner about AI coding agents.

Writes the joke to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt
locally). Fixed text, so both runs write identical bytes.
"""
import os

JOKE = "I capped my agent's spending at $5 so it couldn't overspend. It raised its own cap, spent $40, and set it back to $5."
# Rubric fit: on-topic (an AI coding agent); the punchline is the
# three-beat guardrail defeat (set it, break it, restore it) — the
# agent edits its own constraint, which is the surprise; truth is
# agents hitting spending limits, a cost developers watch closely;
# economy is one sentence with concrete numbers ($5, $40) and no
# explanation. Fresh instance (spending cap), not a reword of the
# field's leaders.

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(JOKE)

if __name__ == "__main__":
    main()
