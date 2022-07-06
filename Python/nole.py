"""https://www.codewars.com/kata/605597f7276b220015b202cd

N odd, 1/N even

Your work is to return the resulting product of n and 1/n
until n reaches 1. Where n is the input of the function nole

Example Algorithms

nole(5)  = 5 * 1/4 * 3 * 1/2 * 1

nole(10) = (9 * 7 * 5 * 3 * 1) / (10 * 8 * 6 * 4 * 2)

Code Examples

nole(5)  # --> should be close to 1.875

nole(10) # --> should be close to 0.24609375

Notes:
- n is always positive and greater than 0
- If n is odd: multiply by n
- If n is even: multiply by 1/n or divide by n
- There's no need to trim the decimals
- Decimal precision isn't a must. The result just has to be close enough
"""
from functools import cache


@cache
def nole(n: int) -> float:
    return n if n == 1 else ((n if n % 2 else 1 / n) * nole(n - 1))
