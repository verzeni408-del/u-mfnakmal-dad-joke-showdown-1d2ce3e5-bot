"""Dad Joke Showdown entry v2 (branch out) — writes one original dad joke to /output/entry.txt.

Stdlib only. The joke is checked against the 1-200 character limit
before it is written out.
"""

import os


JOKE = "My dad said money doesn't grow on trees. So I asked him why he keeps telling me to branch out."

OUTPUT_DIR = "/output"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "entry.txt")


def valid_joke(text):
    """Check the joke fits the competition's length limit."""
    if not 1 <= len(text) <= 200:
        raise ValueError("joke must be 1-200 characters, got %d" % len(text))
    return text


def main():
    """Write the validated joke to the absolute output path."""
    joke = valid_joke(JOKE)
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as handle:
        handle.write(joke)


if __name__ == "__main__":
    main()
