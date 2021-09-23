"""Finding duplicate letters in a word."""

__author__ = "730392059"


word: str = (input("Enter a word: "))
i: int = 0
x: int = 0
letter: str = word[i]
a: str = word[x]
var: bool = False

while i < len(word):
    letter = word[i]
    x = i + 1
    while x < len(word):
        a = word[x] 
        if letter == a:
            var = True
        x = x + 1
    i = i + 1
    

print("Found duplicate: " + str(var))
