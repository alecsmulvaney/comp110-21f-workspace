"""Program that outputs one of at least four random, good fortunes."""

<<<<<<< HEAD
__author__ = "730392059"
=======
__author__ = "730243388"
>>>>>>> bfe00d0bc5e66cd0a568dfd7048add409d018ba1

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


# Begin your solution here...
<<<<<<< HEAD
print("Your fortune cookie says...")
fortune_number = randint(1, 4)
if fortune_number == 1:
    print("A great person from your past with find you soon!")
else:
    if fortune_number == 2:
        print("You will find something you love ealry in life!")
    if fortune_number == 3:
        print("You're life will be filled with joy!")
    if fortune_number == 4:
        print("Money and power will be drawn to you!")
=======

rand_int: int = randint(0, 3)
print("Your fortune cookie says...")
if (rand_int == 0):
    print("you will get married")
elif (rand_int == 1):
    print("you should take a nap")
elif (rand_int == 2):
    print("you need therapy")
else:
    print("you will meet a new friend tommorow")
>>>>>>> bfe00d0bc5e66cd0a568dfd7048add409d018ba1
print("Now, go spread positive vibes!")
