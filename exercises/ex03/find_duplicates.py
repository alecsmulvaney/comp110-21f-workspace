"""Finding duplicate letters in a word."""

__author__ = "730392059"


word: str = (input("Enter a word: "))
count: int = len(word)
last = word[count - 1]
i = 0
x = 1
letter = word[i]
a = word[x]
var: bool = False

while i < len(word):
    while x < len(word): 
        if letter == a:
            var = True   
        x = x + 1
    i = i + 1

print("Found duplicate: " + str(var))
