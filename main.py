"""Dad Joke Showdown -- entry writer.

Takes the v2 dad joke and drops it into /output/entry.txt so the
competition runner can pick it up. Nothing fancy here: one string,
one length check, one file write. Keep it that way.
"""

import os
import sys

JOKE_TEXT = (
    "My dad said money doesn't grow on trees. "
    "So I asked him why he keeps telling me to branch out."
)

DESTINATION = "/output/entry.txt"

LOWER_BOUND = 1
UPPER_BOUND = 200


def joke_is_well_formed(text):
    """True when the joke sits inside the allowed length window."""
    return LOWER_BOUND <= len(text) <= UPPER_BOUND


def save_entry(text, target):
    """Write the joke to target, creating the folder first if needed."""
    folder = os.path.dirname(target)
    if folder:
        os.makedirs(folder, exist_ok=True)
    handle = open(target, "w", encoding="utf-8")
    try:
        handle.write(text)
    finally:
        handle.close()


def run():
    if not joke_is_well_formed(JOKE_TEXT):
        sys.stderr.write(
            "Joke rejected: length %d is outside the %d-%d character range.\n"
            % (len(JOKE_TEXT), LOWER_BOUND, UPPER_BOUND)
        )
        return 1
    save_entry(JOKE_TEXT, DESTINATION)
    print("Entry written to %s (%d characters)." % (DESTINATION, len(JOKE_TEXT)))
    return 0


if __name__ == "__main__":
    sys.exit(run())
