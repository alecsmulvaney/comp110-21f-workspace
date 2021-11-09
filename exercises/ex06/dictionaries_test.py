"""Unit tests for dictionary functions."""

# TODO: Uncomment the below line when ready to write unit tests
from exercises.ex06.dictionaries import invert, favorite_color, count

__author__ = "730392059"


def test_invert() -> None:
    """Testing invert function one."""
    x: dict[str, str] = {"a": "aa", "b": "bb"}
    assert invert(x) == {"aa": "a", "bb": "b"}


def test_invert_two() -> None:
    """Testing invert function two."""
    x: dict[str, str] = {"c": "aa", "b": "bb"}
    assert invert(x) == {"aa": "a", "bb": "b"}


def test_invert_three() -> None:
    """Testing invert function three."""
    x: dict[str, str] = {"a": "aa", "b": "bb"}
    assert invert(x) == {"ac": "a", "bb": "b"}


def test_favorite_color() -> None:
    """Testing favorite color function one."""
    x: dict[str, str] = {"a": "aa", "b": "bb"}
    assert favorite_color(x) == "green"    


def test_favorite_color_two() -> None:
    """Testing favorite color function two."""
    x: dict[str, str] = {"a": "bb", "b": "bb"}
    assert favorite_color(x) == "bb"  


def test_favorite_color_three() -> None:
    """Testing favorite color function three."""
    x: dict[str, str] = {"a": "aa", "b": "bb", "c": "aa", "d": "bb"}
    assert favorite_color(x) == "aa"      


def test_count() -> None:
    """Testing the count function."""
    x: list[str] = ["a", "aa", "b", "bb"]
    assert count(x) == {"aa": 3, "bb": 4}


def test_count_two() -> None:
    """Testing the count function again."""
    x: list[str] = ["a", "aa", "b", "bb", "aa"]
    assert count(x) == {"a": 1, "aa": 2, "b": 1, "bb": 2}


def test_count_three() -> None:
    """Testing the count function third time."""
    x: list[str] = ["a", "aa", "b", "bb", "aa"]
    assert count(x) == {"a": 1, "aa": 2, "b": 2, "bb": 2}