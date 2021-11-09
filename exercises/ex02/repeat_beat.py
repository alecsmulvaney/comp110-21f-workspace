"""Repeating a beat in a loop."""

<<<<<<< HEAD
__author__ = "730392059"


# Begin your solution here...
beat: str = input("What beat do you want to repeat?")
times: int = int(input("How many times do you want to repeat it?"))
space: str = " "
if times <= 0:
    print("No beat...")
while times > 0:
    print((beat + space) * (times - 1) + beat)
    times = times - times
=======
__author__ = "730243388"


# Begin your solution here...
beat: str = input("What beat do you want to repeat? ")
number: int = int(input("How many times do you want to repeat it? "))
i: int = 0
if (number < 1):
    print("No beat...")
else:
    print_beat = beat
    while (i < number - 1):
        print_beat += "" + beat

    print(print_beat)
>>>>>>> bfe00d0bc5e66cd0a568dfd7048add409d018ba1
