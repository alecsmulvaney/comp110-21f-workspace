<<<<<<< HEAD
"""relational operators code for EX01."""

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
=======
"""Demonstrates python relational operators for two number inputs."""

__author__ = "730243388"

string_one = input("Left-hand side: ")
string_two = input("Right-hand side: ")

number_one = int(string_one)
number_two = int(string_two)

print(string_one + " < " + string_two + " is " + str(number_one < number_two))
print(string_one + " >= " + string_two + " is " + str(number_one >= number_two))
print(string_one + " == " + string_two + " is " + str(number_one == number_two))
print(string_one + " != " + string_two + " is " + str(number_one != number_two))
>>>>>>> bfe00d0bc5e66cd0a568dfd7048add409d018ba1
