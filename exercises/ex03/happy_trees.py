"""Drawing forests in a loop."""

__author__ = "730392059"

# The string constant for the pine tree emoji
TREE: str = '\U0001F332'

depth: int = int(input("How deep do you want? "))
print("Depth:", depth)
depthtwo: int = depth
while depth > 0:
    print((TREE) * (depthtwo - depth + 1))
    depth = depth - 1
