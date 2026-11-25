"""Dad Joke Showdown entry — writes one dad joke to /output/entry.txt."""

import os

JOKE = (
    "My daughter asked why I wear a belt and suspenders. "
    "I said, 'In case one of them lets me down.'"
)


def write_entry():
    """Write the dad joke to the output file, creating the folder first."""
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE + "\n")


def main():
    write_entry()


if __name__ == "__main__":
    main()
