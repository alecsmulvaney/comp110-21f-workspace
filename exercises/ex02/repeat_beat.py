"""Repeating a beat in a loop."""

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
