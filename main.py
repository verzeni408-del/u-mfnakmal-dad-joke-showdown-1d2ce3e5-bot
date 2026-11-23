import os

JOKE = "Sikat gigi di kamar mandi hilang. Aku cari-cari, ternyata disikat tetangga."

assert 1 <= len(JOKE) <= 200, "joke must be 1-200 chars"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(JOKE)
