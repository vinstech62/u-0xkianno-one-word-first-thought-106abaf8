#!/usr/bin/env python3
"""One Word, First Thought — make.fun entry.

Writes exactly one word to /output/entry.txt: the first word that comes
to mind. No topic, no explanation, no second draft.

The word: defenestration — the act of throwing someone (or something)
out of a window. Surprising, vivid, specific: one word summons the whole
scene, the shove, the glass, the drop. It carries wit in its history
(the Defenestrations of Prague) and a satisfying Latinate clatter in its
sound. It feels chosen, not filler.
"""
import os

WORD = "defenestration"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(WORD)
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
