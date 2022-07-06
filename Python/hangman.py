"""https://www.codewars.com/kata/602467452b35dd0021cbf46e

In this kata, you will get the following:

- A word(this is a the word that you should use to check for)
- A letter guess from user
- The word that you will receive is guaranteed to be 1 word,
  which can be both lowercase or uppercase.

You will need to create a function that will reveal the
letter guesses, and it should look like this:

Hangman('E', 'everything') ==> 'e_e_______'
Thank you contributors! Also, @iwtaga, I do not know how to fix the idea so if you could help me?
"""
import re


def hangman(guess: str, word: str) -> str:
    return re.sub(fr'[^{guess}]', '_', word, flags=re.I).lower()
