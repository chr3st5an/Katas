"""https://www.codewars.com/kata/610c8308ed5ee4003279d112

You are given a dictionary:

Example: {"firstName": "John", "lastName": "Doe"}

Your job is to create a function snake_casify that receives
a dictionary as a parameter. The function should convert all
the keys in the dictionary to snake_case format, and return
that new dictionary.

snake_casify({"firstName": "John", "lastName": "Doe"}) == {"first_name": "John", "last_name": "Doe"}
"""
from typing import Dict
import re


def snake_casify(dictionary: Dict[str, str]) -> Dict[str, str]:
    return {re.sub(r'([A-Z])', r'_\1', k).lower(): v for k, v in dictionary.items()}
