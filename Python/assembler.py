"""https://www.codewars.com/kata/58e24788e24ddee28e000053

This is the first part of this kata series. Second part is here.

We want to create a simple interpreter of assembler which will
support the following instructions:

- mov x y - copies y (either a constant value or the content of
    a register) into register x
- inc x - increases the content of the register x by one
- dec x - decreases the content of the register x by one
- jnz x y - jumps to an instruction y steps away (positive
    means forward, negative means backward, y can be a
    register or a constant), but only if x (a constant or
    a register) is not zero

Register names are alphabetical (letters only). Constants are
always integers (positive or negative).

Note: the jnz instruction moves relative to itself. For example,
an offset of -1 would continue at the previous instruction, while
an offset of 2 would skip over the next instruction.

The function will take an input list with the sequence of the
program instructions and will execute them. The program ends when
there are no more instructions to execute, then it returns a
dictionary (a table in COBOL) with the contents of the registers.

Also, every inc/dec/jnz on a register will always be preceeded by
a mov on the register first, so you don't need to worry about
uninitialized registers.
"""
from typing import Any, Dict, List, NewType, Union
from copy import copy
import re


Register = NewType('Register', str)


class AssemblerInterpreter(object):
    def __init__(self):
        self._registers   = {}
        self._current_idx = 0

    def exec(self, instructions: List[str]) -> Dict[Register, int]:
        while self._current_idx < len(instructions):
            instruction, *args = instructions[self._current_idx].split()

            if   instruction == "mov":
                self._mov(*args)
            elif instruction == "inc":
                self._inc(*args)
            elif instruction == "dec":
                self._dec(*args)
            elif instruction == "jnz":
                self._jmp(*args)
                continue

            self._current_idx += 1

        return copy(self._registers)

    def _isnum(self, val: Any) -> bool:
        return bool(re.match(r"(?:\+|-)?\d+", val))

    def _mov(self, to_register: Register, val: Union[Register, int]) -> None:
        if not self._isnum(val):
            val = self._registers[val]

        self._registers[to_register] = int(val)

    def _inc(self, register: Register) -> None:
        self._registers[register] += 1

    def _dec(self, register: Register) -> None:
        self._registers[register] -= 1

    def _jmp(self, condition: Union[Register, int], steps: Union[Register, int]) -> None:
        if not self._isnum(condition):
            condition = self._registers[condition]

        if int(condition):
            self._current_idx += int(steps if self._isnum(steps) else self._registers[steps])
        else:
            self._current_idx += 1
