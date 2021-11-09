"""example of functions imported elsewhere."""


def powerful(x: float, n: float) -> float:
    """raises x to the power of n."""
    return x ** n

THE_ANSWER: int = 42

r: dict[str, int] = {}

r["foo"] = 110


print(r)