"""Dad Joke Showdown entry: writes one dad joke to /output/entry.txt."""

import os

JOKE = "I told my suitcase there would be no vacation this year. Now I'm dealing with emotional baggage."

# The rules allow 1-200 characters; keep the joke inside that limit.
assert 1 <= len(JOKE) <= 199, "joke must fit in 200 characters including the newline"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE + "\n")


if __name__ == "__main__":
    main()
