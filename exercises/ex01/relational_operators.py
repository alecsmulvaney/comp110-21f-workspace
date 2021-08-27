"""relational operators code for EX01"""

__author__ = "730392059"

left: int = int(input("Left-hand side? "))
right: int = int(input("Right-hand side? "))
print("Left-hand side:", left)
print("Right-hand side:", right)
less: int = left < right
great_equal: int = left >= right
equal: int = left == right
not_equal: int = left != right
print(left, "<", right, "is", less)
print(left, ">=", right, "is", great_equal)
print(left, "==", right, "is", equal)
print(left, "!=", right, "is", not_equal)