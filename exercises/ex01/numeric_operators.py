<<<<<<< HEAD
"""numeric operators code for EX01."""

__author__ = "730392059"

left: int = int(input("Left-hand side? "))
right: int = int(input("Right-hand side? "))
print("Left-hand side:", left)
print("Right-hand side:", right)
expo: int = left ** right
div = int(left) / int(right)
int_div: int = left // right
remain: int = left % right
print(left, "**", right, "is", expo)
print(left, "/", right, "is", div)
print(left, "//", right, "is", int_div)
print(left, "%", right, "is", remain)
=======
"""Demonstrates python numeric operators for two input numbers."""

__author__ = "730243388"

string_one = input("Left-hand side: ")
string_two = input("Right-hand side: ")

number_one = int(string_one)
number_two = int(string_two)

print(string_one + " ** " + string_two + " is " + str(number_one ** number_two))
print(string_one + " / " + string_two + " is " + str(number_one / number_two))
print(string_one + " // " + string_two + " is " + str(number_one // number_two))
print(string_one + " % " + string_two + " is " + str(number_one % number_two))
>>>>>>> bfe00d0bc5e66cd0a568dfd7048add409d018ba1
