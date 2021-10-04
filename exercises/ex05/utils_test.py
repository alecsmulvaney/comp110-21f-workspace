"""Unit tests for list utility functions."""

# TODO: Uncomment the below line when ready to write unit tests
# from exercises.ex05.utils import only_evens, sub, concat

__author__ = "730392059"

from exercises.ex05.utils import only_evens
from exercises.ex05.utils import sub
from exercises.ex05.utils import concat


def test_only_evens() -> None:
    """Testing only evens."""
    xs: list[int] = [2, 4, 5, 6]
    ys: list[int] = [3, 4, 5, 6]
    assert only_evens(xs) == [2, 4, 6]
    assert only_evens(xs) == [2, 4, 4]
    assert only_evens(ys) == [4, 4, 4]


def test_only_evens_two() -> None:
    """Testing only evens."""
    xs: list[int] = [2, 4, 5, 6]
    ys: list[int] = [3, 4, 5, 6]
    assert only_evens(xs) == [2, 4, 6]
    assert only_evens(xs) == [2, 5, 4]
    assert only_evens(ys) == [4, 3, 4]


def test_only_evens_three() -> None:
    """Testing only evens."""
    xs: list[int] = [2, 4, 5, 6]
    ys: list[int] = [3, 4, 5, 6]
    assert only_evens(xs) == [2, 5, 6]
    assert only_evens(xs) == [2, 7, 4]
    assert only_evens(ys) == [4, 8, 4]


def test_sub() -> None:
    """Testing sub function."""
    xs: list[int] = [2, 4, 5, 6]
    x: int = 1
    y: int = 3
    z: int = 4
    assert sub(xs, x, y) == [2, 4, 6]
    assert sub(xs, x, y) == [2, 4, 5]
    assert sub(xs, x, z) == [2, 4, 5, 6]


def test_sub_two() -> None:
    """Testing sub function."""
    xs: list[int] = [2, 4, 6, 6]
    x: int = 1
    y: int = 3
    z: int = 4
    assert sub(xs, x, y) == [2, 4, 6]
    assert sub(xs, x, y) == [2, 3, 5]
    assert sub(xs, x, z) == [2, 4, 5, 6]


def test_sub_three() -> None:
    """Testing sub function."""
    xs: list[int] = [2, 4, 5, 3]
    x: int = 2
    y: int = 3
    z: int = 4
    assert sub(xs, x, y) == [2, 4, 6]
    assert sub(xs, x, y) == [2, 4, 5]
    assert sub(xs, x, z) == [2, 4, 5, 6]


def test_concat() -> None:
    """Testing concat function."""
    xs: list[int] = [2, 4, 5, 6]
    ys: list[int] = [3, 4, 5, 6]
    zs: list[int] = [2, 4, 5, 5]
    assert concat(xs, ys) == [2, 4, 5, 6, 3, 4, 5, 6]
    assert concat(xs, ys) == [2, 4, 4]
    assert concat(ys, zs) == [4, 4, 4]


def test_concat_two() -> None:
    """Testing concat function."""
    xs: list[int] = [2, 4, 5, 6]
    ys: list[int] = [3, 4, 5, 6]
    zs: list[int] = [2, 4, 5, 5]
    assert concat(xs, ys) == [2, 3, 5, 6, 3, 4, 5, 6]
    assert concat(xs, ys) == [2, 5, 4]
    assert concat(ys, zs) == [4, 5, 4]


def test_concat_three() -> None:
    """Testing concat function."""
    xs: list[int] = [2, 4, 6, 6]
    ys: list[int] = [3, 4, 6, 6]
    zs: list[int] = [2, 4, 6, 5]
    assert concat(xs, ys) == [2, 3, 5, 6, 3, 4, 5, 6]
    assert concat(xs, ys) == [2, 5, 4]
    assert concat(ys, zs) == [4, 5, 4]