"""Dad Joke Showdown entry — writes one original dad joke to /output/entry.txt.

Stdlib only. The joke is validated to be within the 1-200 character limit
before it is written out.
"""

from pathlib import Path


PUNCHLINE = "Sikat gigi di kamar mandi hilang. Aku cari-cari, ternyata disikat tetangga."

DESTINATION = Path("/output") / "entry.txt"


def check_length(text: str) -> str:
    """Return the joke unchanged when its length is inside the allowed range."""
    size = len(text)
    if size < 1 or size > 200:
        raise ValueError(f"joke length {size} is outside the 1-200 range")
    return text


def main() -> None:
    """Validate the joke, then write it to the absolute output path."""
    joke = check_length(PUNCHLINE)
    DESTINATION.parent.mkdir(parents=True, exist_ok=True)
    DESTINATION.write_text(joke, encoding="utf-8")


if __name__ == "__main__":
    main()
