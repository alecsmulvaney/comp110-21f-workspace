"""Practice with dictionaries."""

__author__ = "730392059"

# Define your functions below


def invert(x: dict[str, str]) -> dict[str, str]:
    """Function that inverts keys and values."""
    y: dict[str, str] = {x[key]: key for key in x}
    w: list[str] = []
    for key in x:
        w.append(x[key])
    i: int = 0
    while i < len(w) - 1:
        c = i + 1
        if w[i] == w[c]:
            raise KeyError("Duplicate input key detected")
        i += 1
    return y


def favorite_color(x: dict[str, str]) -> str:
    """Function that finds the favorite color."""
    color_count: dict[str, int] = {}
    for key in x:
        color_count[x[key]] = 0
    for key in x:
        if x[key] in color_count:
            color_count[x[key]] += 1
    counter: int = 0
    color: str = ""
    for key in color_count:
        if counter < color_count[key]:
            counter = color_count[key]
    for key in color_count:
        if color_count[key] == counter:
            color = key
            return color
    return ""


def count(x: list[str]) -> dict[str, int]:
    """Function that finds count of each input."""
    y: dict[str, int] = {}
    i: int = 0
    while i < len(x):
        if x[i] in y:
            y[x[i]] = y[x[i]] + 1
        else:
            y[x[i]] = 1
        i += 1
    return y
