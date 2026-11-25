"""Monday Morning Punchlines — a make.fun entry.

Prints exactly one joke about Monday mornings, no longer than 200
characters.
"""

LINE = (
    "Monday morning is just Friday's confidence coming home to find "
    "its stuff out on the lawn."
)


def build_line() -> str:
    line = LINE
    assert len(line) <= 200, f"line too long: {len(line)} chars"
    assert "\n" not in line
    return line


if __name__ == "__main__":
    print(build_line())
