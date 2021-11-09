"""examples of imports."""

from lessons import helpers

print(helpers.powerful(2, 4))
print(helpers.THE_ANSWER)
print(f"imports.py: {__name__}")

from lessons import helpers as hp
print(hp.THE_ANSWER)