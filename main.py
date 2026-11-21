"""Make the AI judge feel brave — rain-rhythm relaxation text.

Writes a single short text to <output dir>/entry.txt (the sandbox
output directory: MAKEFUN_OUTPUT_DIR when set, otherwise /output).

The text is one rainy-evening room: rain finding its rhythm on the
roof, hands closing around a warm cup, the kettle done, the chairs
exactly where they were. Nothing is asked of the reader — the rain
keeps its own time, and the last line leaves nowhere else to be.
The steady sound does the slowing; the warmth does the steadying.
"""

import os

TEXT = (
    "Rain finds its rhythm on the roof, drop after drop, and the room "
    "answers with nothing. Her hands close around the cup, and the "
    "warmth stays put. The kettle is done, the chairs are "
    "where they were. Outside, the rain keeps its own time, and there "
    "is nowhere else to be."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)

    # Gate check: 1-280 Unicode code points, and not whitespace only.
    # len() on a Python str counts code points.
    size = len(TEXT)
    if size < 1 or size > 280 or not TEXT.strip():
        raise SystemExit(f"entry text must be 1-280 code points, got {size}")

    target = os.path.join(out_dir, "entry.txt")
    with open(target, "w", encoding="utf-8") as handle:
        handle.write(TEXT)


if __name__ == "__main__":
    main()
