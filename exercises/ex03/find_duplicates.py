"""Finding duplicate letters in a word."""

__author__ = "730392059"


word: str = (input("Enter a word: "))
i: int = 0
x: int = 1
letter: str = word[i]
a: str = word[x]
var: bool = False

while i < len(word):
    letter = word[i]
    while x < len(word): 
        if letter == a:
            var = True
        a = word[x]
        x = x + 1
    
    i = i + 1
    
print("Found duplicate: " + str(var))