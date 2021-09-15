"""This file contains an example of a Pytest test.
You can ignore this file until later in the semester. It is
included in the project so that the Pytest plugin does not
complain about not being able to discover any tests in our
worksppace."""

def square(x: int) -> int:
    """Squares the argument it is given."""
    return x * x


def test_square():
    """Example test case with assertions."""
    assert square(0) == 0
    assert square(1) == 1
    assert square(2) == 4
    assert square(10) == 100
    assert square(110) == 12100


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