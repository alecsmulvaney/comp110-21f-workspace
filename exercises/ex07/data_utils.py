"""Utility functions."""

__author__ = "730392059"

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a table."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)

    file_handle.close()
    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oreinted table to a colum oriented table."""
    result: dict[str, list[str]] = {}

    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)
    return result


def head(xs: dict[str, list[str]], n: int) -> dict[str, list[str]]:
    """Some function for data wrangling tables."""
    z: dict[str, list[str]] = {}
    for keys in xs:
        i: int = 0
        if n >= len(xs[keys]):
            return xs
        values: list[str] = []
        while i < n:
            values.append(xs[keys][i])
            i += 1
        z[keys] = values
    return z


def select(xs: dict[str, list[str]], ys: list[str]) -> dict[str, list[str]]:
    """Function to select certain columns."""
    z: dict[str, list[str]] = {}
    i: int = 0
    while i < len(ys):
        z[ys[i]] = xs[ys[i]]
        i += 1
    return z


def concat(xs: dict[str, list[str]], ys: dict[str, list[str]]) -> dict[str, list[str]]:
    """Function to combine two peieces of data."""
    z: dict[str, list[str]] = {}
    for key in xs:
        z[key] = xs[key]
    for key in ys:
        if key in z:
            z[key] += ys[key]
        else:
            z[key] = ys[key] 
    return z


def count(xs: list[str]) -> dict[str, int]:
    """Function to count frequency of values."""
    z: dict[str, int] = {}
    i: int = 0
    while i < len(xs):
        if xs[i] in z:
            z[xs[i]] += 1
        else:
            z[xs[i]] = 1
        i += 1
    return z
