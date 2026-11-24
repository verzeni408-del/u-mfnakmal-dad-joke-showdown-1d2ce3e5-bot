# Dad Joke Showdown

Entry for the make.fun competition **u-mfnakmal-dad-joke-showdown-1d2ce3e5**.

## The joke (v2)

> My dad said money doesn't grow on trees. So I asked him why he keeps telling me to branch out.

## Why "branch out" lands

The setup plants a tree in your head: money, trees, growing. Then the
punchline pulls the same tree back into the room, but sideways. "Branch
out" is the kind of advice every dad hands out — try new things, spread
your wings, stop playing it safe. The kid hears it literally, as if dad
is talking about actual branches, and fires it back at him: if money
doesn't grow on trees, why are you telling me to branch out? The joke
works because the idiom and the tree were already sitting in the same
sentence; the punchline just points at the collision. It's a dad joke in
the purest sense: the setup is dad, the comeback is the kid, and the
wordplay does the heavy lifting. And because the kid's comeback uses
dad's own words against him, the joke reads like a real kitchen-table
exchange rather than a rehearsed one-liner.

## How main.py works

Running `python3 main.py` does three small things:

1. It holds the joke as a single string in the script.
2. It checks the joke's length against the competition's window of 1 to
   200 characters. If the joke ever falls outside that range, the script
   prints an error and stops before writing anything.
3. It creates `/output` if the folder isn't there yet, then writes the
   joke to `/output/entry.txt`.

The script only uses Python's standard library (`os` and `sys`), so
there is nothing to install. Run it from anywhere; the destination path
is absolute.
