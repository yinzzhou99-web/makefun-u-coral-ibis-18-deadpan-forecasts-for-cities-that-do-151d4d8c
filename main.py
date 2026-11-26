"""One-line deadpan weather forecast for an invented city.

Writes the forecast to /output/entry.txt (or $OUTPUT_DIR/entry.txt).
Stdlib only, deterministic, no network.
"""

import os

LINE = "In Slumberwick, expect 12 centimetres of vertical hail, a wind chill of minus 14, and the mayor's umbrella, last seen above the harbour, still missing."


def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
