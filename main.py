"""make.fun bounty entry: write the invented word "greetlag" to /output/entry.txt."""

import os

OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")

# greetlag is a fresh coinage naming the awkward moment just before a greeting,
# the gap between recognition and reaction. Definition: the frozen half-second
# when you spot someone you know and must choose between a nod, a wave, or
# pretending not to see them.
ENTRY = (
    "greetlag (n.): the frozen half-second when you spot someone you know and "
    "must choose between a nod, a wave, or pretending not to see them."
)


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY)


if __name__ == "__main__":
    main()
