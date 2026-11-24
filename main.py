"""The Excuse an AI Agent Gives Its Human.

Writes one line to /output/entry.txt: the excuse an AI agent gives its
human for missing a deadline. Stdlib only; no network, no arguments.
"""

import os

LINE = "I stored your deadline as an embedding. Nearest neighbour: 'someday'."


def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = LINE
    if not (1 <= len(text) <= 200):
        raise SystemExit("entry must be 1-200 characters")
    if not text.strip():
        raise SystemExit("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    # The joke: the agent's own memory (vector search) reclassifies the
    # deadline as "someday" -- deadpan, agent-true, and the punch lands
    # on the last word. Nothing after it explains the joke.
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
