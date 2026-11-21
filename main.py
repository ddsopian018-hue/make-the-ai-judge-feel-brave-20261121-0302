"""Make the AI judge feel brave — slow-rhythm relaxation text.

Writes one short text to <output dir>/entry.txt (the sandbox output
directory: MAKEFUN_OUTPUT_DIR when set, otherwise /output).

The text is a single concrete dusk scene — a gate left open, a cooling
kettle, a dog asleep on the step — written so the reading itself slows
down: short plain sentences, soft sounds, nothing commanded. The courage
is shown, never instructed: nothing in the scene needs deciding, the
light stays a little longer, and the evening keeps its pace.
"""

import os

TEXT = (
    "Dusk settles slow over the low wall, and the gate stands open on "
    "its hinges. The kettle ticks as it cools. A dog sleeps with his "
    "chin on the step, one ear up, one ear down. Nothing tonight needs "
    "deciding. The light stays a little longer, and the evening keeps "
    "its pace."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)

    # Self-check against the gate: 1-280 Unicode code points, not only
    # whitespace (len() on a str counts code points).
    code_points = len(TEXT)
    if code_points < 1 or code_points > 280 or not TEXT.strip():
        raise SystemExit(
            f"entry text must be 1-280 code points, got {code_points}"
        )

    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
