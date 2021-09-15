"""Finding duplicate letters in a word."""

__author__ = "730392059"


word: str = (input("Enter a word: "))
count: int = len(word)
last = word[count - 1]
i = 0
x = 1
letter = word[i]
a = word[x]


while count > 0:
    while a != last: 
        if letter == a:
            t = str("True") 
        x = x + 1
    count = count - 1
    i = i + 1
    x = i + 1

    

if t == "True":
    print("True")
else:
    print("False")


print(a)