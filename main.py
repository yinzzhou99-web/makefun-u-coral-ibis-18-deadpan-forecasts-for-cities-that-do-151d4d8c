"""One-line deadpan weather forecast for an invented city.

Writes the forecast to /output/entry.txt (or $OUTPUT_DIR/entry.txt).
Stdlib only, deterministic, no network.
"""

import os

LINE = "In Grimblesnatch, expect 41 centimetres of sideways rain, a low of minus 9, and one confused seagull circling the town hall until Thursday."


def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
