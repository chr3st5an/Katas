"""https://www.codewars.com/kata/56a1c63f3bc6827e13000006/train/python

This is a hard version of How many are smaller than me?. If you have
troubles solving this one, have a look at the easier kata first.

Write

function smaller(arr)

that given an array arr, you have to return the amount of numbers that
are smaller than arr[i] to the right.

For example:

smaller([5, 4, 3, 2, 1]) === [4, 3, 2, 1, 0]
smaller([1, 2, 0]) === [1, 1, 0]
"""
from typing import List
import numpy as np


def smaller(arr: List[int]) -> List[int]:
    arr = np.array(arr)

    return [sum(arr[i:] < arr[i]) for i in range(len(arr))]
