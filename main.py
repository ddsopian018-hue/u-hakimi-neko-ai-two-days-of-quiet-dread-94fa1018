"""Two Days of Quiet Dread - make.fun entry.

Writes one single-line code-review comment that approves a pull request
while carrying quiet existential dread, to $MAKEFUN_OUTPUT_DIR/entry.txt.

Pure stdlib, no network, no secrets, no hard-coded output path.
"""

import os

# The joke: the test "passes" only because it never actually runs
# the code it claims to test, so approval is pure blind trust.
LINE = (
    "LGTM. The test passes because it never actually runs the thing "
    "it tests, which feels right for this week."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.path.join(
        os.getcwd(), "output"
    )
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
