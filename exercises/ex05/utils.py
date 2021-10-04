"""List utility functions part 2."""

__author__ = "730392059"

# Define your functions below


def only_evens(xs: list[int]) -> list[int]:
    """Function to return only evans."""
    i: int = 0
    while i < len(xs):
        if xs[i] % 2 != 0:
            xs.pop(i)
        i += 1
    return xs


def sub(xs: list[int], x: int, y: int) -> list[int]:
    """Function to return index items."""
    ys: list[int] = []
    i: int = x
    if xs == []:
        return []
    if x >= len(xs):
        return []
    if x < 0:
        i = 0
    if y > len(xs):
        y = len(xs)
    while i <= y - 1:
        ys.append(xs[i])
        i += 1
    return ys


def concat(xs: list[int], ys: list[int]) -> list[int]:
    """Function that adds two lists together."""
    cs: list[int] = []
    i: int = 0
    while i < len(xs):
        cs.append(xs[i])
        i += 1
    i = 0
    while i < len(ys):
        cs.append(ys[i])   
        i += 1
    return cs