"""Counting letters in a string."""

__author__ = "730392059"


# Begin your solution here...
letter: str = input("What letter do you want to seach for?:")
word: str = input("Enter a word:")
i: int = 0
count: int = 0
while i < len(word):
    if word[i] == letter:
        count = count + 1
    i = i + 1
print("Count: ", count)
