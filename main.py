"""Write the One-Liner Marathon entry using only the standard library."""

import os
from pathlib import Path
import sys


JOKE = "The CEO said to bring our whole selves to work, so I invited his second family to the Christmas party. Attendance corrected."


def main() -> int:
    try:
        output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
        output_dir.mkdir(parents=True, exist_ok=True)
        (output_dir / "entry.txt").write_text(JOKE, encoding="utf-8")
    except (OSError, ValueError) as error:
        # Invalid path values and ordinary filesystem failures use the same CLI error path.
        print(f"Cannot write entry.txt: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
