"""List utility functions."""

__author__ = "730392059"


# TODO: Implement your functions here.

def all(intlist: list[int], number: int) -> bool:
    """Function to determine if a list and number are all the same."""  
    if intlist == []:
        return False
    i: int = 0
    while i < len(intlist):
        if intlist[i] != number:
            return False
        else:
            i += 1
        
    return True


def is_equal(intlist: list[int], secondlist: list[int]) -> bool:
    """Function to determine is two lists are equal or not."""
    i: int = 0
    if len(intlist) != len(secondlist):
        return False
    while i < len(intlist) and len(secondlist):
        if intlist[i] != secondlist[i]:
            return False
        else:
            i += 1
    return True


def max(numbers: list[int]) -> int:
    """Function to find largest number without max function."""
    if len(numbers) == 0:
        raise ValueError("max() arg is an empty List")
    i: int = 0
    larger = numbers[i]
    while i < len(numbers):
        if larger < numbers[i]:
            larger = numbers[i]
        i += 1
    return larger
