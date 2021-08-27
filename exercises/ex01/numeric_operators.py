"""numeric operators code for EX01"""

__author__ = "730392059"

left: int = int(input("Left-hand side? "))
right: int = int(input("Right-hand side? "))
print("Left-hand side:", left)
print("Right-hand side:", right)
expo: int = left ** right
div: int = left / right
int_div: int = left // right
remain: int = left % right
print(left, "**", right, "is", expo)
print(left, "/", right, "is", div)
print(left, "//", right, "is", int_div)
print(left, "%", right, "is", remain)
