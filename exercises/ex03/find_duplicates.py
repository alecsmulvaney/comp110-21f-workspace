"""Finding duplicate letters in a word."""

<<<<<<< HEAD
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
=======
__author__ = "123456789"

word: str = input("Enter a word: ")

i: int = 0
duplicate: bool = False
while (i < len(word)):
    j: int = i + 1
    while(j < len(word)):
        if (word[i] == word[j]):
            duplicate = True
        j += 1
    i += 1

print("Found duplicate: " + str(duplicate))
>>>>>>> bfe00d0bc5e66cd0a568dfd7048add409d018ba1
