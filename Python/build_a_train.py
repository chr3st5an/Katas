"""https://www.codewars.com/kata/60398a8c64b9d5000d84f6a9

Your job is to return the amount of metal needed to build
the train. You are given a string. The string will look
something like this:

str = 'A________'

Where the 'A' is a type of a locomotive and "_ " is a
coach after the train.

RULES:

A = 15 pieces of metal

B = 10 pieces of metal

C = 7 pieces of metal

D = 8 pieces of metal

The coaches take 5 pieces of metal to make(for each).

###EXAMPLE###

train('A_') = 20, 15 for A type, and 5 for coach

The value is supposed to be an integer

All translations and edits welcome!
"""
def train(train: str) -> int:
    return sum({"A": 15, "B": 10, "C": 7, "D": 8, "_": 5}[char] for char in train)
