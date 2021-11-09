"""Drawing forests in a loop."""

__author__ = "730392059"

# The string constant for the pine tree emoji
TREE: str = '\U0001F332'

<<<<<<< HEAD
depth: int = int(input("How deep do you want? "))
print("Depth:", depth)
depthtwo: int = depth
while depth > 0:
    print((TREE) * (depthtwo - depth + 1))
    depth = depth - 1
=======
depth: int = int(input("Depth: "))

i: int = 0
duplicate: bool = False
while (i < depth):
    j: int = 0
    tree: str = ""
    while(j < i + 1):
        tree += TREE
        j += 1
    print(tree)
    i += 1
>>>>>>> bfe00d0bc5e66cd0a568dfd7048add409d018ba1
